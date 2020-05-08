# -*- coding: utf-8 -*-

from odoo import models, fields, api


class TankReference(models.Model):
    _name = 'tank.refrence'

    name = fields.Char('nom')