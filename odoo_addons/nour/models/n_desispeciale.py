# -*- coding: utf-8 -*-
from odoo import models, fields

class NourNdesispeciale(models.Model):
    _name = 'nour.n_desispeciale'
    _rec_name = 's_designation'

    n_speciale_ids = fields.One2many(comodel_name='nour.n_speciale', inverse_name='n_desispeciale_id')
    s_designation = fields.Char('Désignation')
    s_observation = fields.Char('Observation')

