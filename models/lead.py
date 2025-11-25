# -*- coding: utf-8 -*-
from odoo import models, fields


class AstrahLead(models.Model):
    _name = "astrah.lead"
    _description = "Astrah Test Lead"

    name = fields.Char(required=True)
    customer_name = fields.Char()
    value = fields.Float()
    priority = fields.Selection([
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High"),
    ], default="medium")
    description = fields.Text()