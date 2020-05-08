# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


class IMEIList(models.Model):
    #_inherit = ['mail.thread', 'mail.activity.mixin']
    _name = 'imei.list'
    name = fields.Char(string='IEMI' ,store=True, readonly=False)
    _sql_constraints = [
        ('name_uniq',
         'UNIQUE (name)',
         'iemi must be unique.')
    ]
    #imei=fields.Integer('IMEI',  digit=(15,0))
    type_id = fields.Many2one('balise.type', string='Type')
    #type_imei = fields.Selection([('s', 'S'),('d', 'D'),('v', 'V')],string ='Type',default='s')
    description = fields.Text(string='Commentaire')
    client_id = fields.Many2one('res.partner', 'Client', track_visibility="onchange",
                                #help='Client de barémage de réservoir ',
                                copy=False, auto_join=True)

    @api.constrains('name')
    @api.one
    def _check_my_field(self):

        if len(self.name) != 15:
            raise ValidationError('le nombre de chiffre composant une série IEMI doit être composé de 15 chiffres')

    #@api.model
    #def create(self, vals):
        #res = super(IMEIList, self).create(vals)
        #if 'client_id' in vals and vals['client_id']:
            #res.create_imei_history(vals['client_id'])
        #return res

    #def create_imei_history(self, client_id):
        #for imei in self:
            #self.env['imei.assignation.log'].create({
                #'imei_id': imei.id,
                #'client_id': client_id,
                #'date_start': fields.Date.today(),
            #})

    #def open_assignation_logs(self):
        #self.ensure_one()
        #return {
            #'type': 'ir.actions.act_window',
            #'name': 'Assignation Logs',
            #'view_mode': 'tree',
            #'res_model': 'imei.assignation.log',
            #'domain': [('imei_id', '=', self.id)],
            #'context': {'default_client_id': self.client_id.id, 'default_imei_id': self.id}
        #}


class BaliseType(models.Model):
    _name = 'balise.type'

    name = fields.Char('Type')
    #_name = "imei.assignation.log"
    #_description = "Drivers history on a vehicle"
    #_order = "date_start"

    #imei_id = fields.Many2one('imei.list', string="IMEI List", required=True)
    #client_id = fields.Many2one('res.partner', string="Client", required=True)
    #date_start = fields.Date(string="Date d'installation")
   # date_end = fields.Date(string="Date de résiliation")



#class EMIListinhit(models.Model):
 #   _name = 'emi.cms'
  #  _inherit = 'mail.thread'
