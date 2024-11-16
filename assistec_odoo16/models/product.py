from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    brand = fields.Char(string='Marca')
    model = fields.Char(string='Modelo')
    serial_number = fields.Char(string='Número de Série')
    color = fields.Char(string='Cor')
    accessories = fields.Text(string='Acessórios')
