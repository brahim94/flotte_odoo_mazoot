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
    seniority = fields.Float(string='Ancienneté', readonly=True, track_visibility='always')
    frais_voiture_a_m = fields.Float(string='Frais de voiture A.M')
    frais_voiture_employe = fields.Float(string='Frais de voiture employé')
    frais_voiture_direction = fields.Float(string='Frais voiture direction')
    frais_voiture_imp = fields.Float(string='Frais voiture imp.')
    prime_exep_one = fields.Float(string='Prime exceptionnelle 1')
    prime_fete = fields.Float(string='Prime fête')
    prime_fin_carriere = fields.Float(string='Prime fin de carrière')
    prime_intressement = fields.Float(string='Prime intressement')
    prime_key_user = fields.Float(string='Prime key user')
    prime_logement = fields.Float(string='Prime logement')
    prime_pelerinage = fields.Float(string='Prime pelerinage')
    prime_s_a_p = fields.Float(string='Prime s a p')
    prime_bonus = fields.Float(string='Prime bonus')
    prime_com_lub = fields.Float(string='Prime com lub')
    ind_caisse = fields.Float(string='Ind. Caisse')
    ind_voiture_cadre = fields.Float(string='Ind. De voiture cadre')
    ind_demenagement = fields.Float(string='Ind. Déménagement')
    ind_depart_imposable = fields.Float(string='Ind. Départ imposable')
    ind_encaissement = fields.Float(string='Ind. Encaissement')
    ind_fonction = fields.Float(string='Ind. Fonction')
    ind_preavis = fields.Float(string='Ind. Preavis')
    ind_velomoteur = fields.Float(string='Ind. Vélomoteur')
    ind_zone_sud = fields.Float(string='Ind. Zone Sud')
    achoura_aid_scolaire = fields.Float(string='Achoura & aid scolaire')
    allocation_achoura = fields.Float(string='Allocation achoura')
    allocation_scolaire = fields.Float(string='Allocation scolaire')
    unite_base = fields.Selection([ ('Jour', 'Jour'), ('Heure', 'Heure')], string='Unité de base', default='Jour', readonly=False) 
    mode_pymnt = fields.Selection([ ('Virement', 'Virement'), ('Cheque', 'Cheque'), ('Espece', 'Espéce')], string='Mode de paiement', default='Virement', required=True) 
    hsnorm = fields.Float(string="Montant_H_Normal" ,default=0)
    hs25 = fields.Float(string="Montant_H_sup25" ,default=0)
    hs50 = fields.Float(string="Montant_H_sup50",default=0)
    hs100 = fields.Float(string="Montant_H_sup100",default=0)
    av_sal = fields.Float(string="Avance_sur_Salaire",default=0)   
    nb_days = fields.Float(string="Nbr.Jours_de_travail") 
    nb_heurs = fields.Float(string="Nbr.Heurs_de_travail") 
    prime_annuel = fields.Float(string="Montant_Prime_annuel")
    indm_licenciement = fields.Float(string="Indemnité_de_licenciement")
    indm_transport = fields.Float(string="Indemnité_de_Transport")
    indm_kilometrique = fields.Float(string="Indemnité_kilometrique")
    prime_rendement = fields.Float(string="Prime_rendement")
    prime_representation = fields.Float(string="Prime_Représentation")
    prime_panier = fields.Float(string="Prime_de_panier(Fixe)")
    prime_panier_imposable = fields.Float(string="Prime panier Imposable")
    prime_panier_net = fields.Float(string="Prime de panier NET")
    prime_autre1 = fields.Float(string="Prime_D_Encouragement")
    prime_autre2 = fields.Float(string="Indeminité Salissure")
    prime_tournee = fields.Float(string="Credit_Tournee")
    credit_Logement = fields.Float(string="Prime_Logement")
    cot_sal_mass = fields.Float(string="Cot Sal M.ASS")
    retenu_petrom_card = fields.Float(string="Retenu PETROM CARD")
    frais_medicau = fields.Float(string="Frais médicaux ")
    indemnite_mutation = fields.Float(string="Indemnité de mutation") 
    cot_conjoint_cmin = fields.Float(string="Cot. conjoint CMIN") 
    prime_fete = fields.Float(string="Prime fête") 
    panier_verif = fields.Boolean(string='Prime du panier?')
    panier_journalise = fields.Float(string='Montant/J du panier journalisé')
    panier_net_cnss = fields.Float(string='Montant/J du panier net')
    conge_annuel_mois = fields.Float(string='Congé annuel par mois (Jours)',default=1.5)
    conge_annuel = fields.Float(string='Congé annuel (Jours/An)',default=18)
    condition_augmentation_an = fields.Float(string='Condition d\'augmentation (An)',default=5.0)
    augmentation_mois = fields.Float(string='Augmentation (Jours/An)',default=1.5)
    reliquat_conge = fields.Float(string='N-1')
    advantages = fields.Text('Avantage')
    wage = fields.Float(string='salaire')

    #@api.constrains('name')
    #@api.one
    #def _check_my_field(self):

        #if len(self.name) != 15:
            #raise ValidationError('le nombre de chiffre composant une série IEMI doit être composé de 15 chiffres')

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
