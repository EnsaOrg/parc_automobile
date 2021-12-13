from odoo import models, fields, api

class ParcAutomobileConducteur(models.Model):
     _name = 'parc_automobile.conducteur'

     matricule = fields.Char('Matricule')
     nom = fields.Char('Nom')
     prenom = fields.Char('Prénom')
     num_permis = fields.Integer()
     service = fields.Char('Service')
     departement = fields.Char('Département')
     type_permis = fields.Selection([('A','A'),('A1','A1'),('A2','A2'),
                                     ('B','B'),('B1','B1'),('BE','BE'),('C1E','C1E'),
                                     ('C','C'),('C1','C1'),('C1E','C1E'),
                                     ('D','D'),('D1','D1'),('D1E','D1E'),('DE','DE')])
     ordre = fields.Selection([('principal','Principal'),('secondaire','Secondaire')])
     validite_permis = fields.Date('Date d\'expiration')

     # conducteur_ids = fields.Many2many(comodel_name='university.conducteur',
     #                                    relation='conducteur_affectation_rel',
     #                                    column1='matricule',
     #                                    column2='date_debut')