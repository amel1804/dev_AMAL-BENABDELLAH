from odoo import api,fields, models, Command

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    training_date = fields.Date(string="Training Date")
    employee_id = fields.Many2one('hr.employee', string="Employee")

    # @api.onchange('employee_id', 'training_date')
    # def create_event(self):
    #     calendar_event_obj = self.env['calendar.event']
    #     for record in self:
    #         if record.employee_id and record.training_date:
    #             event_name = 'Formation for employee ' + record.employee_id.name
    #             calendar_event_obj.create({
    #                 'name': event_name,
    #                 'start_datetime': record.training_date,
    #                 'stop_datetime': record.training_date,
    #                 'partner_ids': [(4, record.employee_id.user_id.partner_id.id)],
    #             })