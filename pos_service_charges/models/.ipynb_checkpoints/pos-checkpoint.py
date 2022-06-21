# -*- coding: utf-8 -*-

from odoo import fields, models,tools,api


class pos_config(models.Model):
    _inherit = 'pos.config' 
    
    allow_service_charge = fields.Boolean(string="Allow Service Charges", default=True)
    charges_type = fields.Selection([('percent', '%'),('amount','Amount')],default='percent', string="Charges Type")
    default_charge = fields.Float(string='Default Charge', default=10)
    service_product_id = fields.Many2one('product.product', string='Service Product', domain="[('available_in_pos', '=', True),('type', '=', 'service')]")

