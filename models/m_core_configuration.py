# -*- coding: utf-8 -*-
from odoo import models, _

# class MCoreConfiguration(models.Model):
# 	_inherit = 'm.core.configuration'

# 	def button_create_view(self):
# 		if self.name == 'Agency':
# 			return {
# 				'name': _('Agency'),
# 				'type': 'ir.actions.act_window',
# 				'view_mode': 'form',
# 				'res_model': 'res.partner',
# 				'view_id': self.env.ref('myzc_u_c_configuration_agency.m_core_agency_form_view').id,
# 				'context': {'default_partner_type': 'agency'},
# 			}
# 		else:
# 			super(MCoreConfiguration,self).button_create_view()

# 	def button_list_view(self):
# 		if self.name == 'Agency':
# 			return {
# 				'name': _('Agency'),
# 				'view_mode': 'tree,form',
# 				'domain': [('partner_type','=', 'agency')],
# 				'res_model': 'res.partner',
# 				'type': 'ir.actions.act_window',
# 				'context': {'default_partner_type': 'agency',
# 				            'tree_view_ref': 'myzc_u_c_configuration_agency.m_core_agency_tree_view',
# 							'form_view_ref': 'myzc_u_c_configuration_agency.m_core_agency_form_view'},
# 			}
# 		else:
# 			super(MCoreConfiguration, self).button_list_view()

# class MCoreConfig(models.Model):
