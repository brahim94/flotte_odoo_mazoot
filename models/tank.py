# -*- coding: utf-8 -*-

import itertools
import psycopg2

from odoo.addons import decimal_precision as dp

from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError, RedirectWarning, except_orm
from odoo.tools import pycompat


class Fleet(models.Model):

    _name = 'tank'
    #name = fields.Char(compute="_compute_reservoir_name", store=True, readonly=False)
    name = fields.Char(compute="_compute_reservoir_name",string='ID Table' ,store=True, readonly=False)
    _sql_constraints = [
        ('name_uniq',
         'UNIQUE (name)',
         'ID TABLE must be unique.')
    ]
    #reference_id = fields.Many2one('tank.refrence', string='Reference reservoir')
    #name = fields.Char('Ref')
    lang=fields.Char('L')
    larg=fields.Char('l')
    haut=fields.Char('H')
    diemnsion_unit=fields.Selection([('cm','cm'),('mm','mm')],'Unité de Mesure', default='cm')
    dim=fields.Char('Dimension')
    id = fields.Integer
    truck_id = fields.Many2one('fleet.list.marque', 'Truck Ref')
    size=fields.Char("Size")
    notes=fields.Text("Commentaire")
    type=fields.Selection([('p','P'),('s','S')], default='p')
    truck_ref=fields.Char("Truck Ref")
    Ref_Res=fields.Char('Ref Reservoir')
    sensor_type=fields.Char("Sensor Type",default='JT606X')
    client_id = fields.Many2one('res.partner', 'Client', track_visibility="onchange", help='Client de barémage de réservoir ',
                                copy=False, auto_join=True)
    sensor_length=fields.Char("Sensor Length")
    sensor_max=fields.Char('Sensor Max' ,default="4095")
    image = fields.Binary(attachment=True,
              help="This field holds the image used as logo for the brand, limited to 1024x1024px.")



    @api.model
    def create(self, vals):
        tools.image_resize_images(vals)
        return super(Fleet, self).create(vals)

    @api.multi
    def write(self, vals):
        tools.image_resize_images(vals)
        return super(Fleet, self).write(vals)

