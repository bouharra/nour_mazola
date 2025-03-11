# -*- coding: utf-8 -*-
from odoo import models, fields, api

class NourResidence(models.Model):
    _name = 'nour.n_residence'
    _rec_name = 'n_designation'

    n_designation = fields.Char('Désignation')  # Ajout d'une majuscule pour l'étiquette
    n_adresse = fields.Char('Adresse')  # Ajout d'une majuscule pour l'étiquette
    n_initial = fields.Float('Solde Initial')
    n_observation=fields.Char('Observation')
    n_an_ids = fields.One2many(comodel_name='nour.n_an', inverse_name='n_residence_id')
    n_logo = fields.Binary("Logo")
    s_cotisations = fields.Float(string='Total Cotisations', compute='_compute_total_s_coti')
    s_depenses = fields.Float(string='Total Dépenses', compute='_compute_total_s_dp')
    s_reste = fields.Float(string='Total Reste', compute='_compute_total_s_reste')
    s_solde = fields.Float(string='Solde Cotisations', compute='_compute_total_s_solde')

    s_speciale = fields.Float(string='Total cotisations', compute='_compute_total_s_speciale')
    s_r_speciale = fields.Float(string='Reste Coti spéciale', compute='_compute_total_s_restespeciale')



    @api.depends('n_an_ids.somme_cotisation')
    def _compute_total_s_coti(self):
        for record in self:
            record.s_cotisations = sum(record.n_an_ids.mapped('somme_cotisation'))

    @api.depends('n_an_ids.somme_reste')
    def _compute_total_s_reste(self):
        for record in self:
            record.s_reste = sum(record.n_an_ids.mapped('somme_reste'))

    @api.depends('n_an_ids.somme_depense')
    def _compute_total_s_dp(self):
        for record in self:
            record.s_depenses = sum(record.n_an_ids.mapped('somme_depense'))

    @api.depends('n_an_ids.somme_restespeciale')
    def _compute_total_s_restespeciale(self):
        for record in self:
            record.s_r_speciale = sum(record.n_an_ids.mapped('somme_restespeciale'))

    @api.depends('n_an_ids.somme_speciale')
    def _compute_total_s_speciale(self):
        for record in self:
            record.s_speciale = sum(record.n_an_ids.mapped('somme_speciale'))

    @api.depends('n_an_ids.solde','n_initial')
    def _compute_total_s_solde(self):
        for record in self:
            record.s_solde = (sum(record.n_an_ids.mapped('solde')) + record.n_initial)

