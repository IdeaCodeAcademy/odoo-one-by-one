from odoo import api, fields, models


class ICACourse(models.Model):
    _name = "ica.course"
    _description = "ICA Course"

    name = fields.Char(required=True)
    description = fields.Text()

    partner_id = fields.Many2one('res.partner', required=True, string='Instructor')
    phone = fields.Char(related='partner_id.phone')
    email = fields.Char(related='partner_id.email')
    # category_ids =fields.Many2many('res.partner.category',related='partner_id.category_id')

    company_id = fields.Many2one('res.company', default=lambda self: self.env.company, readonly=True)
    currency_id = fields.Many2one('res.currency', related='company_id.currency_id')
    fees = fields.Monetary(currency_field='currency_id')
    notes = fields.Html()
    state = fields.Selection([
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('cancel', 'Cancelled')], default='draft')
    lesson_ids = fields.One2many('ica.lesson', 'course_id', string='Lessons')

    _sql_constraints = [('name_uniq', "unique(name)",
                         "Course Name Should be unique.")]

    def action_draft(self):
        self.state = 'draft'

    def action_publish(self):
        self.state = 'published'

    def action_cancel(self):
        self.state = 'cancel'

# table
#       id,cloumns 1, col 2, col3 ,state
# self # 1,abc,20,099999,draft
# self # 2,abc,20,099999,draft

# sample
# def abc(self):
#     return self.env.company
# lambda self:self.env.company
