from odoo import models, fields, api

class CatteryProductAttribute(models.Model):
    _inherit = 'product.attribute'

    ######################### Fields #########################
    flavor = fields.Selection(
        selection=[
            ('chicken', 'Chicken'),
            ('beef', 'Beef'),
            ('fish', 'Fish'),
            ('pork', 'Pork'),
        ],
        string = "Flavor"
    )
    kibble_size = fields.Selection(
        selection=[
            ('small', 'Small'),
            ('medium', 'Medium'),
            ('large', 'Large'),
        ],
        string = "Kibble Size"
    )
    grain_free = fields.Boolean(string="Grain-Free?")