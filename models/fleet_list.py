# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
from odoo import models, fields, api, _
from odoo.exceptions import Warning, UserError, ValidationError
from odoo.tools.misc import formatLang
from odoo.osv import expression
from odoo.tools import float_is_zero, float_compare
# from odoo.addons import decimal_precision as dp
from dateutil.relativedelta import relativedelta
from odoo.http import request
import qrcode
import base64
from io import BytesIO
from odoo.http import request

def generate_qr_code(url):
    qr = qrcode.QRCode(
             version=1,
             error_correction=qrcode.constants.ERROR_CORRECT_L,
             box_size=20,
             border=4,
             )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image()
    temp = BytesIO()
    img.save(temp, format="PNG")
    qr_img = base64.b64encode(temp.getvalue())
    return qr_img


class FleetList(models.Model):

    _name = 'fleet.list'
    name = fields.Char('Immatriculation')
    #type_vehicule = fields.Selection([('utiliaire','Utilitaire'),('mini-bus','Mini-Bus'),('bus','Bus'),
                                    #('camion','Camion'),('engin','Engin')],'Type', default='Utilitaire')
    type_ve_id = fields.Many2one('fleet.list.type', string='Type Vehicule')
    marque_id = fields.Many2one('fleet.list.marque', string='Truck Ref')
    reference_id = fields.Many2one('tank', 'ID Table #1')
    reference_tank_id = fields.Many2one('tank.refrence', 'ID Table #1')
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
    color_full = fields.Integer(string='color')
    date_birth = fields.Date(string="Date de naissance")
    date_plu_mounth = fields.Datetime(string="Date plus mois", compute='_add_mounth')
    qr_image = fields.Binary("QR Code", compute='_generate_qr_code')
    #age = fields.Char(compute="_cal_age", string="Age")
    
    def action_fitch(self):
        # res = super(FleetList, self).action_fitch()
        
        # if not self.reference_id:
        #     raise ValidationError(_('Données incomplétes.'))
        
        # tank_id_find = self.env['tank'].search([('reference_id', '=', self.reference_tank_id.id)], limit=1)
        # if not tank_id_find:
        #     raise ValidationError(_("ba9i ma kaynch chi correspendance !"))
        
        # tank_log = self.env['tank.refrence'].create({
        #     'name': self.lieu_install,
        #     'SIM_N_ref': self.SIM_N,
        #     'SIM_SE_ref': self.SIM_N,
        #     'lieu_install_ref': self.SIM_N,
        # })
        tank_log = self.env['fleet.list'].search_count([])
        print('tank_log', tank_log)    
        
        # return res
    
    def _generate_qr_code(self):
        base_url = request.env['ir.config_parameter'].get_param('web.base.url')
        base_url += '/web#id=%d&view_type=form&model=%s' % (self.id, self._name)
        self.qr_image = generate_qr_code(base_url)
    
    def _add_mounth(self):
        for order in self:
            duree_mois = 1
            if self.date_instal:
                date_start_dt = fields.Datetime.from_string(self.date_instal)
                dt = date_start_dt + relativedelta(months=duree_mois)
                date_plu_mounth = fields.Datetime.to_string(dt)
        order.update({'date_plu_mounth': date_plu_mounth})

    
                # self.date_plu_mounth = (fields.Datetime.from_string(self.date_instal,'%Y-%m-%d') + relativedelta(months=self.duree_mois)).strftime('%Y-%m-%d')
                # order.update({'date_plu_mounth': date_plu_mounth}) 

#@api.depends('date_birth')
    #def _cal_age(self):
        #if self.date_birth:
            #years = relativedelta(date.today(), self.date_birth).years
            #months = relativedelta(date.today(), self.date_birth).months
            #day = relativedelta(date.today(), self.date_birth).days
            #self.age = str(int(years)) + ' An(s) ' + str(int(months)) + ' Mois ' + str(day) + ' Jour(s)'

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

class Buildings(models.Model):
    _name = 'my_module.buildings'    
    name = fields.Char()
    rooms = fields.One2many('my_module.rooms', 'building_id')

class Rooms(models.Model):
    _name = 'my_module.rooms'    
    name = fields.Char()
    building_id = fields.Many2one('my_module.buildings', required=True)
    
    # this method should open a form for the clicked room
    def open_one2many_line(self, context=None):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Open Line',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': self._name,
            'res_id': context('active_id'),
            'target': 'current',
        }





#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
