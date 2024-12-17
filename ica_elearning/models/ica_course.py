from odoo import api, fields, models

class ICACourse(models.Model):
    _name = "ica.course"
    _description = "ICA Course"

    name = fields.Char(required=True)
    description = fields.Text()
    partner_id = fields.Many2one('res.partner',required=True,string='Instructor')
    company_id = fields.Many2one('res.company',default=lambda self:self.env.company,readonly=True)
    currency_id = fields.Many2one('res.currency',related='company_id.currency_id')
    fees = fields.Monetary(currency_field='currency_id')
    notes = fields.Html()
    state = fields.Selection([('draft','Draft'),('published','Published'),('cancel','Cancelled')],default='draft')
    lesson_ids =fields.One2many('ica.lesson','course_id',string='Lessons')

# sample
# def abc(self):
#     return self.env.company
# lambda self:self.env.company