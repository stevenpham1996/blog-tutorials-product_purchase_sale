from odoo import models, fields, api

class CatteryPurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    ######################### Fields #########################
    date_required = fields.Date(string="Date Required")