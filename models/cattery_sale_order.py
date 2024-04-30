from odoo import models, fields, api


class CatterySaleOrder(models.Model):
   _inherit = 'sale.order'

   ######################### Fields #########################
   subscription = fields.Boolean(string="Subscription")
   interval = fields.Selection(
        selection=[('weekly', 'Weekly'), ('monthly', 'Monthly')],
        string="Interval",
    )
   frequency = fields.Integer(string="Frequency")
   
   ######################### Onchange Methods #########################
   @api.onchange('subscription')
   def _onchange_subscription(self):
        if self.subscription:
            self.interval = 'weekly'
            self.frequency = 4
        else:
            self.interval = False
            self.frequency = 0
            
