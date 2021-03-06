from odoo import models, fields, api

class ParcAutomobileEntretien(models.Model):
     _name = 'parc_automobile.entretien'
     # _inherit = "parc_automobile.intervention"
     # _description = "Hérite de la classe intervention"

     date = fields.Date('Date d\'entretien')
     montant_frais = fields.Float('Frais (en DH)')
     prestataire = fields.Char()
     duree = fields.Integer('Durée (en jours)')

     type = fields.Selection([('entretien courant', 'Entretien courant'), ('révision', 'Révision'), ('réparation', 'Réparation'),])

     vehicule_id = fields.Many2one(comodel_name='parc_automobile.vehicule', delegate=True, required=True)

     @api.multi
     def name_get(self):
          result = []
          for entretien in self:
               name = '[Matricule: ' + entretien.vehicule_id.matricule + ' - Type: ' + entretien.type+']'
               result.append((entretien.id,name))
          return result