# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class NourNMois(models.Model):
    _name = 'nour.n_mois'
    _description = 'Table N Mois'

    n_an_id = fields.Many2one(comodel_name='nour.n_an', ondelete="cascade")
    n_annee = fields.Integer('Année', related='n_an_id.n_annee')
    MONTH_FIL = [
        ('1', 'JANVIER'), ('2', 'FEVRIER'), ('3', 'MARS'), ('4', 'AVRIL'),
        ('5', 'MAI'), ('6', 'JUIN'), ('7', 'JUILLET'), ('8', 'AOUT'),
        ('9', 'SEPTEMPRE'), ('10', 'OCTOBRE'), ('11', 'NOVEMBRE'), ('12', 'DECEMBRE'), ('13', 'Reliquat')
    ]
    d_mois = fields.Selection(selection=MONTH_FIL)

    # Contrainte SQL pour garantir l'unicité de d_mois pour chaque n_an_id
    _sql_constraints = [
        ('unique_d_mois_per_n_an_id', 'UNIQUE(n_an_id, d_mois)', 'Le mois doit être unique pour chaque année !'),
    ]

