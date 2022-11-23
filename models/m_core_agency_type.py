# -*- coding: utf-8 -*-
from odoo import models, fields, api

class MCoreAgencyType(models.Model):
    _name = 'm.core.agency.type'
    _description = "Agency Type"

    name = fields.Char('Type')