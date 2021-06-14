# -*- coding: utf-8 -*-

from odoo import models, fields, api


class TankReference(models.Model):
    _name = 'tank.refrence'

    name = fields.Char('nom')
    SIM_N_ref = fields.Char ('SIM N°')
    SIM_SE_ref = fields.Char('SIM Serie')
    #ref_reservoir_pr = fields.Integer('Réf Rés Pr')
    #ref_reservoir_sec = fields.Integer('Réf Rés Sec')
    lieu_install_ref = fields.Char('Lieu d\'installation')
    reference_ref_id = fields.Many2one('tank', 'ID Table #1')
    
