# -*- coding: utf-8 -*-

from odoo import models, fields, api

class vit_asset_received(models.Model):
	_inherit = 'vit.transfer'


	@api.multi 
	def action_open(self):
		self.validity_check()
		self.state = 'open'

	@api.multi
	def action_received(self):
		if not self.is_interco or not sum(line.asset_id.value_residual for line in self.asset_line) :
			self.action_approve()