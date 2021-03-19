# -*- coding: utf-8 -*-

from odoo import models, fields, api




# class esirecommandation(models.Model):
#     _name = 'esirecommandation.esirecommandation'

#     name = fields.Char()
class Demande(models.Model):
    _name = 'esirecommandation.demande'
    _description = "Demande de lettre de recommandation"

    """  @api.model
    def create(self, values):
        self.is_created = True
        return super(Demande, self).create(values) """

    title = fields.Char(string="Titre de la demande", required=True )
    name_student = fields.Char(string="Nom Etudiant", required=True)
    start_date = fields.Date(required=True)
    end_date = fields.Date()
    is_archived =fields.Boolean(default =False)
   # is_created = fields.Boolean(default =False)
    formation = fields.Text(required=True)
    is_done = fields.Boolean(default=False)
    done = fields.Char(string="Note de realisation")
    competance_ids = fields.Many2many('esirecommandation.competance',string="Competances a valoriser",required=True)
    lettre_ids = fields.One2many(
        'esirecommandation.lettre', 'demande_id', string="Lettres de recommandation")
    
    @api.depends('lettre_ids')
    def _compute_len_lettres(self): 
        if self.lettre_ids:
            self.len_lettres = len(self.lettre_ids)
        else:
            self.len_lettres =  0
    len_lettres = fields.Integer("Nombre de lettre recommandation",compute='_compute_len_lettres',store=True)


class Lettre(models.Model):
    _name = 'esirecommandation.lettre'
    _description = "Lettre de Recommandation"


    name_teacher = fields.Char(string="Nom Enseigant", required=True)
    lettre_date = fields.Date(required=True)
    description = fields.Text(required=True)
    demande_id = fields.Many2one('esirecommandation.demande',
        ondelete='cascade', string="Demande de recommandation", required=True)

class competance(models.Model):
    _name = 'esirecommandation.competance'
    _description = "Competance d'un etudiant"

    name_competance = fields.Char(string="Competance", required=True)