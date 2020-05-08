# -*- coding: utf-8 -*-

from odoo import models, fields, api


class FleetList(models.Model):

    _name = 'fleet.list'
    name = fields.Char('Immatriculation')
    #type_vehicule = fields.Selection([('utiliaire','Utilitaire'),('mini-bus','Mini-Bus'),('bus','Bus'),
                                    #('camion','Camion'),('engin','Engin')],'Type', default='Utilitaire')
    type_ve_id = fields.Many2one('fleet.list.type', string='Type Vehicule')
    marque_id = fields.Many2one('fleet.list.marque', string='Truck Ref')
    reference_id = fields.Many2one('tank', 'ID Table #1')
    ref_reservoir_pr = fields.Char('Réf Rés pri', related='reference_id.Ref_Res', store=True)
    Table_id = fields.Many2one('tank', 'ID Table #2')
    ref_reservoir_sec = fields.Char('Réf Rés Sec', related='Table_id.Ref_Res', store=True)
    iemi_id = fields.Many2one('imei.list', 'IEMI', required=True)
    date_instal = fields.Date(string="Date d\'installation", default=fields.Date.today)
    SIM_N = fields.Char ('SIM N°')
    SIM_SE = fields.Char('SIM Serie')
    #ref_reservoir_pr = fields.Integer('Réf Rés Pr')
    #ref_reservoir_sec = fields.Integer('Réf Rés Sec')
    lieu_install = fields.Char('Lieu d\'installation')
    #ref_res_pr_id = fields.Many2one('tank.refrence', 'Réf Rés Pr', track_visibility="onchange", help=" Reference Reservoire Principale", copy=False, auto_join=True)
    #ref_res_Sec_id = fields.Many2one('tank.refrence', 'Réf Rés Sec', track_visibility="onchange", help=" Reference Reservoire Secondaire", copy=False, auto_join=True)
    client_id = fields.Many2one('res.partner', 'Client', track_visibility="onchange", help='Client Bénéficiare', copy=False, auto_join=True)
   # clt = fields.Many2many('res.partner', string='Client')
    boitier_gps = fields.Boolean('Boitier GPS/GPRS', default=False)
    relais_moteur_marche = fields.Boolean('Relais Moteur Marche', default = False)
    relais_immobilisation = fields.Boolean('Relais Immob', default = False)
    jauge_crb_prin = fields.Boolean('Jauge carburant Pr', default = False)
    jauge_crb_sec = fields.Boolean('Jauge carburant Sec', default = False)
    sonde = fields.Boolean('Sonde Température', default=False)
    color = fields.Integer()

    #@api.multi
    #def return_action_to_open(self):
        #""" This opens the xml view specified in xml_id for the current vehicle """
        #self.ensure_one()
        #xml_id = self.env.context.get('xml_id')
        #if xml_id:
            #res = self.env['ir.actions.act_window'].for_xml_id('fleet', xml_id)
            #res.update(
                #context=dict(self.env.context, default_vehicle_id=self.id, group_by=False),
                #domain=[('vehicle_id', '=', self.id)]
            #)
            #return res
        #return False



class FleetListTypes(models.Model):

    _name = 'fleet.list.type'

    name = fields.Char('nom')


class FleetServices(models.Model):

    _name = 'fleet.list.service'


    name = fields.Char('nom')
    note = fields.Text('Commentaire')
    client_id = fields.Many2one('res.partner', 'Client', track_visibility="onchange",
                                help='Client de barémage de réservoir ',
                                copy=False, auto_join=True)


    @api.model
    def create(self, vals):
        res = super(FleetServices, self).create(vals)
        if 'client_id' in vals and vals['client_id']:
            res.create_imei_history(vals['client_id'])
        return res

    def create_imei_history(self, client_id):
        for imei in self:
            self.env['imei.assignation.log'].create({
                'imei_id': imei.id,
                'client_id': client_id,
                'date_start': fields.Date.today(),
            })

    def open_assignation_logs(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Assignation Logs',
            'view_mode': 'tree',
            'res_model': 'imei.assignation.log',
            'domain': [('imei_id', '=', self.id)],
            'context': {'default_client_id': self.client_id.id, 'default_imei_id': self.id}
        }


class IMEIListAssignationLog(models.Model):
    _name = "imei.assignation.log"
    _description = "Drivers history on a vehicle"
    _order = "date_start"

    imei_id = fields.Many2one('imei.list', string="IMEI List", required=True)
    client_id = fields.Many2one('res.partner', string="Client", required=True)
    date_start = fields.Date(string="Date d'installation")
    date_end = fields.Date(string="Date de résiliation")

class FleetListMARQUE(models.Model):

    _name = 'fleet.list.marque'

    name = fields.Char('nom')





#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
