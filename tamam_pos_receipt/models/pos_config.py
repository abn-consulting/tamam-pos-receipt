from odoo import fields, models


class PosConfig(models.Model):
    _inherit = "pos.config"

    till_number = fields.Char(
        string="Till Number",
        help="Till number printed on this POS receipt.",
    )
