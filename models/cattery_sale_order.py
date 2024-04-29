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
       for record in self:
           if record.subscription:
               record.interval = 'weekly'
               record.frequency = 4
           else:
               record.interval = False
               record.frequency = 0
            
