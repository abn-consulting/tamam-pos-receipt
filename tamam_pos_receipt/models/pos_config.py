from odoo import fields, models


class PosConfig(models.Model):
    _inherit = "pos.config"

    till_number = fields.Char(
        string="Till Number",
        help="Till number printed on this POS receipt.",
    )

    def _load_pos_data_fields(self, config):
        fields = super()._load_pos_data_fields(config)
        if "till_number" not in fields:
            fields.append("till_number")
        return fields
