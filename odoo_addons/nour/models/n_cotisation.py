# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class NourNcotisation(models.Model):
    _name = 'nour.n_cotisation'

    n_resident_id = fields.Many2one(comodel_name='nour.n_resident', ondelete="cascade")
    n_an_id = fields.Many2one(comodel_name='nour.n_an', ondelete="cascade")
    MONTH_FILTRE = [('1', 'JAN'), ('2', 'FEV'), ('3', 'MAR'), ('4', 'AVR'),
                    ('5', 'MAI'), ('6', 'JUN'), ('7', 'JUL'), ('8', 'AUT'),
                    ('9', 'SEP'), ('10', 'OCT'), ('11', 'NOV'), ('12', 'DEC'), ('13', 'Reliquat')]
    n_annee = fields.Integer('Année', related='n_an_id.n_annee')
    x = fields.Selection(selection=MONTH_FILTRE, related='n_an_id.x')
    n_code = fields.Char('Code App', related='n_resident_id.n_code')
    n_nom = fields.Char('Nom', related='n_resident_id.n_nom')
    n_coti_an = fields.Float('Cotian', related='n_resident_id.n_coti_an')
    # n_cloture = fields.boolean('Année Cloturée', related='n_an_id.n_cloture')
    reste_coti = fields.Float(string='Reste_app', compute='_compute_reste')
    total_coti = fields.Float(string='Total_app', compute='_compute_total')
    n_observation = fields.Char('Observation')

    _sql_constraints = [('unique_resident_annee', 'unique(n_resident_id, n_an_id)',
                         "Le nom du résident doit être unique pour chaque année !"), ]

    n1 = fields.Integer('JAN')  # Ajout d'une étiquette et champ requis
    n2 = fields.Integer('FEV')
    n3 = fields.Integer('MAR')
    n4 = fields.Integer('AVR')
    n5 = fields.Integer('MAI')
    n6 = fields.Integer('JUN')
    n7 = fields.Integer('JUL')
    n8 = fields.Integer('AUT')
    n9 = fields.Integer('SEP')
    n10 = fields.Integer('OCT')
    n11 = fields.Integer('NOV')
    n12 = fields.Integer('DEC')
    n13 = fields.Integer('REL')
    n0 = fields.Integer('REL')

    COLOR_MAP = {
        '1': '#FFFFFF', '2': '#FFFFFF', '3': '#FFFFFF4',
        '4': '#FFFFFF', '5': '#FFFFFFE', '6': '#FFFFFFF',
        '7': '#FFFFFF', '8': '#FFFFFFE', '9': '#FFFFFF',
        '10': '#FFFFFF', '11': '#FFFFFF', '12': '#FFFFFF', '13': '#FFFFFF'
    }
    n1_color = fields.Html(string="JAN", compute="_compute_n_color", sanitize="false")
    n2_color = fields.Html(string="FEV", compute="_compute_n_color", sanitize="false")
    n3_color = fields.Html(string="MAR", compute="_compute_n_color", sanitize="false")
    n4_color = fields.Html(string="AVR", compute="_compute_n_color", sanitize="false")
    n5_color = fields.Html(string="MAI", compute="_compute_n_color", sanitize="false")
    n6_color = fields.Html(string="JUN", compute="_compute_n_color", sanitize="false")
    n7_color = fields.Html(string="JUL", compute="_compute_n_color", sanitize="false")
    n8_color = fields.Html(string="AUT", compute="_compute_n_color", sanitize="false")
    n9_color = fields.Html(string="SEP", compute="_compute_n_color", sanitize="false")
    n10_color = fields.Html(string="OCT", compute="_compute_n_color", sanitize="false")
    n11_color = fields.Html(string="NOV", compute="_compute_n_color", sanitize="false")
    n12_color = fields.Html(string="DEC", compute="_compute_n_color", sanitize="false")
    MONTH_SELECTION = [('1', 'JAN'), ('2', 'FEV'), ('3', 'MAR'), ('4', 'AVR'),
                       ('5', 'MAI'), ('6', 'JUN'), ('7', 'JUL'), ('8', 'AUT'),
                       ('9', 'SEP'), ('10', 'OCT'), ('11', 'NOV'), ('12', 'DEC')]
    
    dd1 = fields.Selection(selection=MONTH_SELECTION, string="Mois1")
    dd2 = fields.Selection(selection=MONTH_SELECTION, string="Mois2")
    dd3 = fields.Selection(selection=MONTH_SELECTION, string="Mois3")
    dd4 = fields.Selection(selection=MONTH_SELECTION, string="Mois4")
    dd5 = fields.Selection(selection=MONTH_SELECTION, string="Mois5")
    dd6 = fields.Selection(selection=MONTH_SELECTION, string="Mois6")
    dd7 = fields.Selection(selection=MONTH_SELECTION, string="Mois7")
    dd8 = fields.Selection(selection=MONTH_SELECTION, string="Mois8")
    dd9 = fields.Selection(selection=MONTH_SELECTION, string="Mois9")
    dd10 = fields.Selection(selection=MONTH_SELECTION, string="Mois10")
    dd11 = fields.Selection(selection=MONTH_SELECTION, string="Mois11")
    dd12 = fields.Selection(selection=MONTH_SELECTION, string="Mois12")
    dd13 = fields.Selection(selection=MONTH_SELECTION, string="Mois13")
    selected_value = fields.Selection(selection=MONTH_SELECTION, string="Valeur à Filtrer")

    XXX = [('2018', '2018'),('2019', '2019'), ('2020', '2020'), ('2021', '2021'), ('2022', '2022'),
                       ('2023', '2023'), ('2024', '2024'), ('2025', '2025'), ('2026', '2026')]

    da1 = fields.Selection(selection=XXX, string='annee1')
    da2 = fields.Selection(selection=XXX, string='annee2')
    da3 = fields.Selection(selection=XXX, string='annee3')
    da4 = fields.Selection(selection=XXX, string='annee4')
    da5 = fields.Selection(selection=XXX, string='annee5')
    da6 = fields.Selection(selection=XXX, string='annee6')
    da7 = fields.Selection(selection=XXX, string='annee7')
    da8 = fields.Selection(selection=XXX, string='annee8')
    da9 = fields.Selection(selection=XXX, string='annee9')
    da10 = fields.Selection(selection=XXX, string='annee10')
    da11 = fields.Selection(selection=XXX, string='annee11')
    da12 = fields.Selection(selection=XXX, string='annee12')

    v1 = fields.Integer(string="V1", compute="_compute_values", store=True)
    v2 = fields.Integer(string="V2", compute="_compute_values", store=True)
    v3 = fields.Integer(string="V3", compute="_compute_values", store=True)
    v4 = fields.Integer(string="V4", compute="_compute_values", store=True)
    v5 = fields.Integer(string="V5", compute="_compute_values", store=True)
    v6 = fields.Integer(string="V6", compute="_compute_values", store=True)
    v7 = fields.Integer(string="V7", compute="_compute_values", store=True)
    v8 = fields.Integer(string="V8", compute="_compute_values", store=True)
    v9 = fields.Integer(string="V9", compute="_compute_values", store=True)
    v10 = fields.Integer(string="V10", compute="_compute_values", store=True)
    v11 = fields.Integer(string="V11", compute="_compute_values", store=True)
    v12 = fields.Integer(string="V12", compute="_compute_values", store=True)
    v13 = fields.Integer(string="V13", compute="_compute_values", store=True)

    @api.depends('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7', 'n8', 'n9', 'n10', 'n11', 'n12')
    def _compute_total(self):
        for record in self:
            record.total_coti = (record.n1 + record.n2 + record.n3 + record.n4 + record.n5 + record.n6
                                 + record.n7 + record.n8 + record.n9 + record.n10 + record.n11 + record.n12)

    @api.depends('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7', 'n8', 'n9', 'n10', 'n11', 'n12', 'n_coti_an', 'x')
    def _compute_reste(self):
        for record in self:
            try:
                x_value = float(record.x)
            except (ValueError, TypeError):
                x_value = 0
            total_paid = sum(getattr(record, f'n{i}') for i in range(1, 13))
            record.reste_coti = (record.n_coti_an * (x_value)) - total_paid - record.n0


    @api.depends("n1", "n2", "n3", "n4", "n5", "n6",
                 "n7", "n8", "n9", "n10", "n11", "n12",
                 "dd1", "dd2", "dd3", "dd4", "dd5", "dd6",
                 "dd7", "dd8", "dd9", "dd10", "dd11", "dd12", 'n_annee')
    def _compute_n_color(self):
        """Change la couleur du fond en fonction de la valeur des mois et des seuils."""

        for record in self:
           # ici injecter code pour extraire xx de date en fonction nannee et mois xx=11

            xx = int(record.x)
            for i in range(1, 13):
                n_field = f'n{i}'
                dd_field = f'dd{i}'
                n_color_field = f'n{i}_color'
                dd_value = getattr(record, dd_field, None)
                n_value = getattr(record, n_field, "")

                # Si ni est égal à 0, appliquer la couleur rouge
                if n_value == 0:
                    color = "#FDCFC7"  # Rouge
                # Si dd_value est strictement inférieur à XX, appliquer la couleur gris
                elif dd_value and dd_value.isdigit() and int(dd_value) < xx:
                    color = "#E0F878"  # vert
                # Si dd_value est égal à XX, appliquer la couleur vert
                elif dd_value and dd_value.isdigit() and int(dd_value) == xx:
                    color = "#E0F878"  # Bleu
                else:
                    color = "transparent"  # Pas de background

                # Appliquer la couleur avec le champ HTML
                setattr(record, n_color_field,
                        f'<span style="background-color: {color}; padding: 5px;">{n_value}</span>')

    @api.depends('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7', 'n8', 'n9', 'n10', 'n11', 'n12',
                 'dd1', 'dd2', 'dd3', 'dd4', 'dd5', 'dd6', 'dd7', 'dd8', 'dd9', 'dd10', 'dd11', 'dd12',
                 'da1', 'da2', 'da3', 'da4', 'da5', 'da6', 'da7', 'da8', 'da9', 'da10', 'da11', 'da12',
                 'n_annee', 'n_resident_id')
    def _compute_values(self):
        for record in self:
            values = {i: 0.0 for i in range(1, 13)}
            n_annee = int(getattr(record, 'n_annee', 0))
            n_resident_id = record.n_resident_id.id

            for i in range(1, 13):
                da_value = int(getattr(record, f'da{i}', 0))

                if da_value == n_annee:
                    n_value = getattr(record, f'n{i}', 0.0)
                    dd_value = getattr(record, f'dd{i}', 0)

                    if isinstance(dd_value, str) and dd_value.isdigit():
                        dd_value = int(dd_value)

                    if isinstance(dd_value, int) and 1 <= dd_value <= 12:
                        values[dd_value] += n_value

                else:
                    da_field = f'da{i}'
                    other_records = self.search([
                        (da_field, '=', n_annee),
                        ('n_resident_id', '=', n_resident_id),
                        ('id', '!=', record.id)
                    ])
                    for other_record in other_records:
                        other_da_value = int(getattr(other_record, da_field, 0))

                        if other_da_value == n_annee:
                            n_value = getattr(other_record, f'n{i}', 0.0)
                            dd_value = getattr(other_record, f'dd{i}', 0)

                            if isinstance(dd_value, str) and dd_value.isdigit():
                                dd_value = int(dd_value)

                            if isinstance(dd_value, int) and 1 <= dd_value <= 12:
                                values[dd_value] += n_value
                            break

            for i in range(1, 13):
                setattr(record, f'v{i}', values[i])


    @api.onchange('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7', 'n8', 'n9', 'n10', 'n11', 'n12', 'n13',
                 'dd1', 'dd2', 'dd3', 'dd4', 'dd5', 'dd6', 'dd7', 'dd8', 'dd9', 'dd10', 'dd11', 'dd12', 'dd13',
                 'da1', 'da2', 'da3', 'da4', 'da5', 'da6', 'da7', 'da8', 'da9', 'da10', 'da11', 'da12', 'n_annee')
    def update_values(self):
        """Vide le cache et recalcule les valeurs."""
        self._compute_values()  # Recalcule les valeurs

    @api.onchange('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7', 'n8', 'n9', 'n10', 'n11', 'n12', 'n13',
                 'dd1', 'dd2', 'dd3', 'dd4', 'dd5', 'dd6', 'dd7', 'dd8', 'dd9', 'dd10', 'dd11', 'dd12', 'dd13',
                 'da1', 'da2', 'da3', 'da4', 'da5', 'da6', 'da7', 'da8', 'da9', 'da10', 'da11', 'da12')  # Ajoutez tous les champs concernés
    def _check_cotisation_fields(self):
        for record in self:
            for i in range(1, 13):  # Boucle de 1 à 12
                da = getattr(record, f'da{i}')
                dd = getattr(record, f'dd{i}')
                n = getattr(record, f'n{i}')

                # Vérification de la logique : si dd{i} est rempli, alors da{i} doit l'être aussi
                if dd and not da:
                    raise ValidationError(f"Le champ Année doit être rempli avant le mois de paiyement.")

                # Si n{i} est rempli, les champs da{i} et dd{i} doivent l'être aussi
                if n and (not dd or not da):
                    raise ValidationError(f"Les champs Année et mois doivent être remplis.")
