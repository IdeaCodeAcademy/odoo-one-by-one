from odoo import api, fields, models

class IcaLesson(models.Model):
    _name = 'ica.lesson'
    _description = 'IcaLesson'

    name = fields.Char()
    course_id = fields.Many2one('ica.course', string='Course')
    sequence = fields.Integer()


