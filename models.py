# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class esirecommandation(models.Model):
#     _name = 'esirecommandation.esirecommandation'

#     name = fields.Char()
class Demande(models.Model):
    _name = 'esirecommandation.demande'
    _description = "Demande de lettre de recommandation"

    title = fields.Char(string="Titre de la demande", required=True)
    name_student = fields.Char(string="Nom Etudiant", required=True)
    start_date = fields.Date()
    end_date = fields.Date()
    is_archived =fields.Boolean(default =False)
    formation = fields.Text()
    competance_ids = fields.Many2many('esirecommandation.competance',string="Competances a valoriser")
    #realisation 
    lettre_ids = fields.One2many(
        'esirecommandation.lettre', 'demande_id', string="Lettres de recommandation")

class Lettre(models.Model):
    _name = 'esirecommandation.lettre'
    _description = "Lettre de Recommandation"


    name_teacher = fields.Char(string="Nom Enseigant", required=True)
    lettre_date = fields.Date()
    description = fields.Text()
    demande_id = fields.Many2one('esirecommandation.demande',
        ondelete='cascade', string="Demande de recommandation", required=True)

class competance(models.Model):
    _name = 'esirecommandation.competance'
    _description = "Competance d'un etudiant"

    name_competance = fields.Char(string="Competance", required=True)