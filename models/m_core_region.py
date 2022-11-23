# -*- coding: utf-8 -*-
from odoo import models, fields, api

class MCoreRegion(models.Model):
    _name = 'm.core.region'
    _description = "Region"

    name = fields.Char('Region')