# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class NourNspeciale(models.Model):

    _name = 'nour.n_speciale'
    _rec_name = 'n_nom'
    _order = "n_desispeciale_id asc, n_code asc"

    n_an_id = fields.Many2one(comodel_name='nour.n_an',  ondelete="cascade")
    n_code = fields.Char('Code App', related='n_resident_id.n_code')
    n_nom = fields.Char('Nom', related='n_resident_id.n_nom')
    n_annee = fields.Integer('Année', related='n_an_id.n_annee')

    n_desispeciale_id = fields.Many2one(comodel_name='nour.n_desispeciale')
    n_detailspeciale_ids = fields.One2many(comodel_name='nour.n_detailspeciale',inverse_name='n_speciale_id', string='Détails des versements')

    n_resident_id = fields.Many2one(comodel_name='nour.n_resident')

    s_designation = fields.Char('Désigntion', related='n_desispeciale_id.s_designation')
    s_apayer = fields.Float('A verser')
    # s_recu = fields.Integer('M_Reçu')
    s_reste = fields.Float('Reste speciale', compute='_copmute_reste_speciale')

    n_obs_speciale = fields.Char('observation')
    s_totalverse = fields.Float(string='Total des Montants', compute='_compute_total_montant', store=True)
    _sql_constraints = [
                           ('unique_speciale_annee', 'unique(n_an_id, n_resident_id, n_desispeciale_id)',
                            "IL Y A UNE REPETITION !"),
                        ]



    @api.depends('n_detailspeciale_ids.s_ds_montant')
    def _compute_total_montant(self):
        for record in self:
            record.s_totalverse = sum(record.n_detailspeciale_ids.mapped('s_ds_montant'))

    @api.depends('s_apayer', 's_totalverse')
    def _copmute_reste_speciale(self):
         for record in self:
          record.s_reste = (record.s_apayer - record.s_totalverse)


    @api.constrains('n_an_id', 'n_resident_id', 'n_desispeciale_id')
    def _check_unique_speciale_annee(self):
        for record in self:
            existing_record = self.search([
                ('n_an_id', '=', record.n_an_id.id),
                ('n_resident_id', '=', record.n_resident_id.id),
                ('n_desispeciale_id', '=', record.n_desispeciale_id.id),
                ('id', '!=', record.id)  # Exclure l'enregistrement en cours de modification
            ])
            if existing_record:
                raise ValidationError("IL Y A UNE RÉPÉTITION !")