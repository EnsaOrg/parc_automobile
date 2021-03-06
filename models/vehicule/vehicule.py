from odoo import models, fields, api

class ParcAutomobileVehicule(models.Model):
     _name = 'parc_automobile.vehicule'

     matricule = fields.Char('Matricule')
     carte_grise = fields.Char('N° carte grise')
     chassis = fields.Char('Numéro de chassis')
     date_circulation = fields.Date('Date de circulation')
     date_reforme = fields.Date('Date enregistrement')
     kilometrage = fields.Integer('Kilométrage (en km)')
     couleur = fields.Selection([('blanc','Blanc'),('noir','Noir'),('argent','Argent'),('gris','Gris'),('rouge','Rouge'),('jaune','Jaune')])

     marque_id = fields.Many2one(comodel_name='parc_automobile.marque', delegate=True, required=True)
     modele_id = fields.Many2one(comodel_name='parc_automobile.modele', delegate=True, required=True)
     parc_id = fields.Many2one(comodel_name='parc_automobile.parc_automobile', delegate=True, required=True)
     assurance_id = fields.Many2one(comodel_name='parc_automobile.assurance', delegate=True, required=True)
     fournisseur_id = fields.Many2one(comodel_name='parc_automobile.fournisseur', delegate=True, required=True)
     active = fields.Boolean(string='Etat',default=True)

     _sql_constraints = [
          ('matricule', 'unique(matricule)', 'Le matricule existe déjà!'),
          ('carte_grise', 'unique(carte_grise)', 'La carte grise existe déjà!'),
     ]

     @api.multi
     def name_get(self):
          result = []
          for vehicule in self:
               name = '[Matricule: ' + str(vehicule.matricule) + ' - Marque: ' + str(vehicule.marque_id.nom) + ']'
               result.append((vehicule.id, name))

          return result