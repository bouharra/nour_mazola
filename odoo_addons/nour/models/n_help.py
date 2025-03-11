# -*- coding: utf-8 -*-
from odoo import models, fields

class NourNhelp(models.Model):
    _name = 'nour.n_help'
    _description = 'Description de l\'application'

    h_name = fields.Char('Titre', default="Aide - Description")
    h_description = fields.Text('Description complète')

