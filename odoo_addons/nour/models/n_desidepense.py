# -*- coding: utf-8 -*-
from odoo import models, fields

class NourNdesidepense(models.Model):
    _name = 'nour.n_desidepense'
    _rec_name = 'd_desidepense'

    n_depense_ids = fields.One2many(comodel_name='nour.n_depense', inverse_name='n_desidepense_id') #pas obligatoire
    d_desidepense = fields.Char('Désignation', required='True')
    dp_desiobservation = fields.Char('Observation')
    d_ordre = fields.Integer(string='Ordre', default=100)

