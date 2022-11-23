# -*- coding: utf-8 -*-
from odoo import models, fields, api

# class Module(models.Model):
#     _inherit = 'ir.module.module'

#     def write(self,vals):
#         res = super(Module,self).write(vals)
#         for module in self:
#             if module.name == 'myzc_u_c_configuration_agency':
#                 agency = self.env['m.core.configuration'].search([('name', '=', 'Agency')])
#                 if vals.get('state') == 'installed' and not agency :
#                     self.env['m.core.configuration'].create({'name':'Agency',
#                                                               'icon': module.icon})
#                 if vals.get('state') == 'uninstalled':
#                     agency.unlink()
#         return res