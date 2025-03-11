# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class NourNdetailspeciale(models.Model):
    _name = 'nour.n_detailspeciale'

    n_speciale_id = fields.Many2one(comodel_name='nour.n_speciale', string='Resident',  ondelete="cascade", required=True )

    s_ds_montant = fields.Float('Montant versée', required=True)
    YY = [('2018', '2018'),('2019', '2019'), ('2020', '2020'), ('2021', '2021'), ('2022', '2022'),
          ('2023', '2023'), ('2024', '2024'), ('2025', '2025'), ('2026', '2026'),('2027', '2027'),('2028', '2028'),('2029', '2029')]
    s_ds_date = fields.Selection(selection=YY, string='Année paiement')





    MONTH_SELECTION1 = [('1', 'JAN'), ('2', 'FEV'), ('3', 'MAR'), ('4', 'AVR'),
                       ('5', 'MAI'), ('6', 'JUN'), ('7', 'JUL'), ('8', 'AUT'),
                       ('9', 'SEP'), ('10', 'OCT'), ('11', 'NOV'), ('12', 'DEC')]
    s_ds_mois = fields.Selection(selection=MONTH_SELECTION1, string="Mois de paiement")

    s_reste = fields.Float('reste', related='n_speciale_id.s_reste')

    @api.onchange('s_ds_montant', 's_ds_mois', 's_ds_date')
    def _check_montant_mois_date(self):
        for record in self:
            if record.s_ds_montant:
                if not record.s_ds_date or not record.s_ds_mois:
                    raise ValidationError(
                        "Les champs 'Date' et 'Mois' sont obligatoires lorsque 'Montant' est renseigné.")
                if not (1 <= int(record.s_ds_mois) <= 12):
                    raise ValidationError("Le champ 'Mois' doit être rempli.")
                if not (2000 <= int(record.s_ds_date) <= 2040):
                    raise ValidationError("Le champ 'Date' doit être rempli.")
                if record.s_ds_montant > record.s_reste:
                    raise ValidationError(
                        "Le champ 'Montant' ne peut pas être supérieur au reste à payer.")
