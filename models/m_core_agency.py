# -*- coding: utf-8 -*-
from odoo import models, fields, api

class MCoreAgency(models.Model):
    _inherit = 'res.partner'

    type_id = fields.Many2one('m.core.agency.type', string='Agency Type')
    fax = fields.Char('Fax')
    ein = fields.Char('EIN')
    partner_type = fields.Selection([('agency','Agency')], string='Type')
    npi = fields.Char('Agency NPI')
    region_id = fields.Many2one('m.core.region',string='Region')
    taxonomy_ids = fields.One2many('m.core.agency.taxonomy','agent_id', string='Taxonomy')

class MCoreAgencyTaxonomy(models.Model):
    _name = 'm.core.agency.taxonomy'
    _rec_name = 'selected_taxonomy'
    _description = "Agency Taxonomy"

    agent_id = fields.Many2one('res.partner')
    primary_taxonomy = fields.Selection([('yes','Yes'),('no','No')], string='Primary Taxonomy')
    selected_taxonomy = fields.Char('Selected Taxonomy')
    state = fields.Char('State')
    license_number = fields.Char('License Number')
