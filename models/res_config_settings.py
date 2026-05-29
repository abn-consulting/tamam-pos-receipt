from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    pos_till_number = fields.Char(
        related="pos_config_id.till_number",
        readonly=False,
        string="Till Number",
    )
