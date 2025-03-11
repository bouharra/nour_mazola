# -*- coding: utf-8 -*-
from odoo import models, fields, api

class NourAn(models.Model):
    _name = 'nour.n_an'
    _rec_name = 'n_annee'

    n_annee = fields.Integer('Année', required=True)

    n_obs_an = fields.Char('Observation')  # Ajout d'une majuscule pour l'étiquette
    n_cotisation_ids = fields.One2many(comodel_name='nour.n_cotisation', inverse_name='n_an_id')
    n_mois_ids = fields.One2many(comodel_name='nour.n_mois', inverse_name='n_an_id')
    n_depense_ids = fields.One2many(comodel_name='nour.n_depense', inverse_name='n_an_id')
    n_speciale_ids = fields.One2many(comodel_name='nour.n_speciale', inverse_name='n_an_id')
    n_residence_id = fields.Many2one(comodel_name='nour.n_residence')
    n_desi_speciale = fields.Char('speciale')
    MONTH_FILTRE = [('1', 'JAN'), ('2', 'FEV'), ('3', 'MAR'), ('4', 'AVR'),
                       ('5', 'MAI'), ('6', 'JUN'), ('7', 'JUL'), ('8', 'AUT'),
                       ('9', 'SEP'), ('10', 'OCT'), ('11', 'NOV'), ('12', 'DEC'), ('13', 'Reliquat')]
    x = fields.Selection(selection=MONTH_FILTRE, string="Filtre")
    # n_annee = fields.Many2one('n_residence'comodel_name='nour.n_residence')
    somme_cotisation = fields.Float(string='Cotisations', compute='_compute_total_coti')
    somme_speciale = fields.Float(string='Speciale', compute='_compute_total_speciale')
    somme_restespeciale = fields.Float(string='Reste speciale', compute='_compute_total_restespeciale')
    somme_depense = fields.Float(string='Dépenses', compute='_compute_total_dp')
    somme_reste = fields.Float(string='Reste', compute='_compute_total_reste')
    solde = fields.Float(string='Solde', compute='_compute_solde')
    compte_cotisation = fields.Integer(string='nombre', compute='fonction_compte')

    _sql_constraints = [('n_annee_unique','unique(n_annee)', 'L\'année doit etre unique.')]

    _sql_constraints = [('n_annee_range', 'CHECK(n_annee >= 2000 AND n_annee <= 2040)', 'La valeur de l\'année est éronnée.')]


    sp1 = fields.Float(string="Montant Mois 1", compute='_compute_montants', store=True)
    sp2 = fields.Float(string="Montant Mois 2", compute='_compute_montants', store=True)
    sp3 = fields.Float(string="Montant Mois 3", compute='_compute_montants', store=True)
    sp4 = fields.Float(string="Montant Mois 4", compute='_compute_montants', store=True)
    sp5 = fields.Float(string="Montant Mois 5", compute='_compute_montants', store=True)
    sp6 = fields.Float(string="Montant Mois 6", compute='_compute_montants', store=True)
    sp7 = fields.Float(string="Montant Mois 7", compute='_compute_montants', store=True)
    sp8 = fields.Float(string="Montant Mois 8", compute='_compute_montants', store=True)
    sp9 = fields.Float(string="Montant Mois 9", compute='_compute_montants', store=True)
    sp10 = fields.Float(string="Montant Mois 10", compute='_compute_montants', store=True)
    sp11 = fields.Float(string="Montant Mois 11", compute='_compute_montants', store=True)
    sp12 = fields.Float(string="Montant Mois 12", compute='_compute_montants', store=True)
    sp13 = fields.Float(string="Montant Mois 13", compute='_compute_montants', store=True)



    for i in range(1, 14):
        locals()[f'sv{i}'] = fields.Integer(string=f'S_{i:02d}', compute='_compute_values')
        locals()[f'sdp{i}'] = fields.Integer(string=f'D_{i:02d}', compute='_compute_values')
        locals()[f's_diff{i}'] = fields.Integer(string=f'Diff_{i:02d}', compute='_compute_values')
        # locals()[f's_sp{i}'] = fields.Integer(string=f'sp_{i:02d}', compute='_compute_values')

    @api.depends('n_cotisation_ids.v1', 'n_cotisation_ids.v2', 'n_cotisation_ids.v3',
                 'n_cotisation_ids.v4', 'n_cotisation_ids.v5', 'n_cotisation_ids.v6',
                 'n_cotisation_ids.v7', 'n_cotisation_ids.v8', 'n_cotisation_ids.v9',
                 'n_cotisation_ids.v10', 'n_cotisation_ids.v11', 'n_cotisation_ids.v12', 'n_cotisation_ids.v13',
                 'n_depense_ids.dp1', 'n_depense_ids.dp2', 'n_depense_ids.dp3',
                 'n_depense_ids.dp4', 'n_depense_ids.dp5', 'n_depense_ids.dp6',
                 'n_depense_ids.dp7', 'n_depense_ids.dp8', 'n_depense_ids.dp9',
                 'n_depense_ids.dp10', 'n_depense_ids.dp11', 'n_depense_ids.dp12', 'n_depense_ids.dp13')


    def _compute_values(self):
        for record in self:
            for i in range(1, 14):
                # Calculer la somme des cotisations (sv), des dépenses (sdp) et inclure sp{i}
                sv = sum(record.n_cotisation_ids.mapped(f'v{i}'))
                sdp = sum(record.n_depense_ids.mapped(f'dp{i}'))
                sp = getattr(record, f'sp{i}', 0)  # Obtenir la valeur sp{i}, par défaut à 0 si elle n'existe pas

                # Affecter les valeurs calculées
                record[f'sv{i}'] = sv
                record[f'sdp{i}'] = sdp

                # Calculer la différence sv - sdp + sp
                record[f's_diff{i}'] = sv - sdp + sp


                # sv1 = fields.Integer(string='S_JAN', compute='_compute_sv1')
    # sv2 = fields.Integer(string='S_FEV', compute='_compute_sv2')

    @api.depends('n_speciale_ids.n_detailspeciale_ids.s_ds_montant',
                 'n_speciale_ids.n_detailspeciale_ids.s_ds_date',
                 'n_speciale_ids.n_detailspeciale_ids.s_ds_mois')
    def _compute_montants(self):
        all_year_records = self.search([])

        for year_record in all_year_records:
            # Initialiser les montants à zéro pour chaque mois (1 à 12)
            montants = {i: 0.0 for i in range(1, 13)}

            # Parcourir tous les détails de n_detailspeciale
            all_details = self.env['nour.n_detailspeciale'].search([])

            for detail in all_details:
                try:
                    # S'assurer que l'année de paiement correspond à l'année de l'enregistrement 'n_annee'
                    if int(detail.s_ds_date) == int(year_record.n_annee):
                        mois = int(detail.s_ds_mois)  # Conversion de s_ds_mois en entier

                        # Vérifier si le mois est entre 1 et 12 (inclus)
                        if 1 <= mois <= 12:
                            montants[mois] += float(detail.s_ds_montant)  # Ajouter le montant au mois correspondant
                except ValueError:
                    continue  # Ignorer si l'année ou le mois ne peuvent être convertis en entier

            # Assigner les montants calculés aux champs correspondants sp1 à sp12
            for i in range(1, 13):
                setattr(year_record, f'sp{i}', montants[i])

            # # Assigner les montants calculés aux champs correspondants
            # record.sp1 = montants[1]
            # record.sp2 = montants[2]
            # record.sp3 = montants[3]
            # record.sp4 = montants[4]
            # record.sp5 = montants[5]
            # record.sp6 = montants[6]
            # record.sp7 = montants[7]
            # record.sp8 = montants[8]
            # record.sp9 = montants[9]
            # record.sp10 = montants[10]
            # record.sp11 = montants[11]
            # record.sp12 = montants[12]
            # record.sp13 = montants[13]

    @api.depends('n_cotisation_ids.total_coti')
    def _compute_total_coti(self):
        for record in self:
            record.somme_cotisation = sum(record.n_cotisation_ids.mapped('total_coti'))

    @api.depends('n_speciale_ids.s_totalverse')
    def _compute_total_speciale(self):
        for record in self:
            record.somme_speciale = sum(record.n_speciale_ids.mapped('s_totalverse'))

    @api.depends('n_speciale_ids.s_reste')
    def _compute_total_restespeciale(self):
        for record in self:
            record.somme_restespeciale = sum(record.n_speciale_ids.mapped('s_reste'))

    @api.depends('n_depense_ids.total_dp')
    def _compute_total_dp(self):
        for record in self:
            record.somme_depense = sum(record.n_depense_ids.mapped('total_dp'))


    @api.depends('n_cotisation_ids.reste_coti')
    def _compute_total_reste(self):
        for record in self:
            record.somme_reste = sum(record.n_cotisation_ids.mapped('reste_coti'))


    @api.depends('somme_cotisation', 'somme_depense')
    def _compute_solde(self):
        for record in self:
            record.solde = (record.somme_cotisation + record.somme_speciale - record.somme_depense)

    def fonction_compte(self):
        self.compte_cotisation = len(self.n_cotisation_ids)

