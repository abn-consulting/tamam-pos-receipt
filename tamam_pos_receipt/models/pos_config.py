from odoo import api, fields, models


class PosConfig(models.Model):
    _inherit = "pos.config"

    till_number = fields.Char(
        string="Till Number",
        help="Till number printed on this POS receipt.",
    )

    @api.model
    def _load_pos_data_fields(self, config):
        fields_list = super()._load_pos_data_fields(config)
        if "till_number" not in fields_list:
            fields_list.append("till_number")
        return fields_list
