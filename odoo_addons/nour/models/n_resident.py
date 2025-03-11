#"-*- coding: utf-8 -*-
from odoo import models, fields, api

class NourNresident(models.Model):
    _name = 'nour.n_resident'
    _rec_name = 'n_nom'  # ce que vous voyez zn haut formulaire

    n_code = fields.Char('Code Résidence')
    n_nom = fields.Char('Nom & Prénom')
    n_coti_an = fields.Float('Cotisation')  # Ajout d'une étiquette
    n_telephone = fields.Char('Téléphone')
    n_email = fields.Char('Mail')
    n_cotisation_ids = fields.One2many(comodel_name='nour.n_cotisation', inverse_name='n_resident_id')
    n_speciale_ids = fields.One2many(comodel_name='nour.n_speciale', inverse_name='n_resident_id')
    somme_cotisation2 = fields.Float(string='Cotisations', compute='_compute_total_coti2')
    somme_reste2 = fields.Float(string='Reste', compute='_compute_total_reste2')
    somme_s_reste = fields.Float(string='Speciale Reste', compute='_compute_total_sreste')
    somme_s_recu = fields.Float(string='Speciale Reçu', compute='_compute_total_srecu')
    somme_s_RR = fields.Float(string='Total du', compute='_compute_total_sRR')

    @api.depends('n_cotisation_ids.total_coti')
    def _compute_total_coti2(self):
        for record in self:
            record.somme_cotisation2 = sum(record.n_cotisation_ids.mapped('total_coti'))

    @api.depends('n_cotisation_ids.reste_coti')
    def _compute_total_reste2(self):
        for record in self:
            record.somme_reste2 = sum(record.n_cotisation_ids.mapped('reste_coti'))

    @api.depends('n_speciale_ids.s_reste')
    def _compute_total_sreste(self):
        for record in self:
            record.somme_s_reste = sum(record.n_speciale_ids.mapped('s_reste'))

    @api.depends('n_speciale_ids.s_totalverse')
    def _compute_total_srecu(self):
        for record in self:
            record.somme_s_recu = sum(record.n_speciale_ids.mapped('s_totalverse'))

    @api.depends('somme_s_reste', 'somme_reste2')
    def _compute_total_sRR(self):
        for record in self:
            record.somme_s_RR = (record.somme_reste2+ record.somme_s_reste)

