from odoo import models, fields, api

class CatteryProductAttribute(models.Model):
    _inherit = 'product.attribute'

    ######################### Fields #########################
    description = fields.Text(string="Description")