from odoo import models, fields, api


class Services(models.Model):

    _name = 'fleet.services'
    _description = 'Services for vehicles'

    notes = fields.Text()
    date_intevention = fields.Date('Date D'/'intervention')