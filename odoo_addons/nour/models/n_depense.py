# -*- coding: utf-8 -*-
from odoo import models, fields, api

class NourNdepense(models.Model):
    _name = 'nour.n_depense'

    n_desidepense_id = fields.Many2one(comodel_name='nour.n_desidepense', string="Désignation", ondelete='cascade')
    d_desidepense = fields.Char('Designation', related='n_desidepense_id.d_desidepense')
    d_ordre = fields.Integer('ordre', related='n_desidepense_id.d_ordre')

    dp1 = fields.Float('JAN')  # Ajout d'une étiquette et champ requis
    dp2 = fields.Float('FEV')
    dp3 = fields.Float('MAR')
    dp4 = fields.Float('AVR')
    dp5 = fields.Float('MAI')
    dp6 = fields.Float('JUN')
    dp7 = fields.Float('JUL')
    dp8 = fields.Float('AUT')
    dp9 = fields.Float('SEP')
    dp10 = fields.Float('OCT')
    dp11 = fields.Float('NOV')
    dp12 = fields.Float('DEC')
    dp13 = fields.Float('RLQ')
    dp_observation = fields.Char('Observation')
    total_dp = fields.Float(string='Total_depense', compute='_compute_total_dp', store=True)
    n_an_id = fields.Many2one(comodel_name='nour.n_an',  ondelete="cascade")

    _sql_constraints = [
        ('unique_depense_annee', 'unique(n_desidepense_id, n_an_id)',
         "Cette désignation de dépense existe déja !"),
    ]

    # Champs HTML associés à chaque dpX
    dp1_html = fields.Html(compute='_compute_dp_html', string='JAN', sanitize=False)
    dp2_html = fields.Html(compute='_compute_dp_html', string='FEV', sanitize=False)
    dp3_html = fields.Html(compute='_compute_dp_html', string='MAR', sanitize=False)
    dp4_html = fields.Html(compute='_compute_dp_html', string='AVR', sanitize=False)
    dp5_html = fields.Html(compute='_compute_dp_html', string='MAI', sanitize=False)
    dp6_html = fields.Html(compute='_compute_dp_html', string='JUN', sanitize=False)
    dp7_html = fields.Html(compute='_compute_dp_html', string='JUL', sanitize=False)
    dp8_html = fields.Html(compute='_compute_dp_html', string='AUT', sanitize=False)
    dp9_html = fields.Html(compute='_compute_dp_html', string='SEP', sanitize=False)
    dp10_html = fields.Html(compute='_compute_dp_html', string='OCT', sanitize=False)
    dp11_html = fields.Html(compute='_compute_dp_html', string='NOV', sanitize=False)
    dp12_html = fields.Html(compute='_compute_dp_html', string='DEC', sanitize=False)
    dp13_html = fields.Html(compute='_compute_dp_html', string='DEC', sanitize=False)


    @api.depends('dp1', 'dp2', 'dp3', 'dp4', 'dp5', 'dp6', 'dp7', 'dp8', 'dp9', 'dp10', 'dp11', 'dp12')
    def _compute_dp_html(self):
        for record in self:
            for i in range(1, 14):
                dp_value = getattr(record, f'dp{i}', 0)  # Obtenir la valeur de dpX
                # Formatage de la valeur pour qu'elle ait deux décimales
                formatted_value = '{:,.2f}'.format(dp_value)
                if dp_value != 0:
                    # Si la valeur n'est pas zéro, appliquer un fond jaune
                    setattr(record, f'dp{i}_html',
                            f'<div style="background-color:#FEDADD;padding:5px;">{formatted_value}</div>')
                else:
                    # Si la valeur est zéro, ne pas appliquer de fond
                    setattr(record, f'dp{i}_html', f'<div>{formatted_value}</div>')


    # somme_total = fields.Integer(string='somme Total', compute='_compute_total_somme', store=True)
    @api.depends('dp1', 'dp2', 'dp3', 'dp4', 'dp5', 'dp6', 'dp7', 'dp8', 'dp9', 'dp10', 'dp11', 'dp12')
    def _compute_total_dp(self):
        for record in self:
            record.total_dp = (record.dp1 + record.dp2 + record.dp3 + record.dp4 + record.dp5 + record.dp6
                                 + record.dp7 + record.dp8 + record.dp9 + record.dp10 + record.dp11 + record.dp12)

