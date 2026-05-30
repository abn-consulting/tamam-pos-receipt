from odoo import api, fields, models


class PosConfig(models.Model):
    _inherit = "pos.config"

    till_number = fields.Char(
        string="Till Number",
        help="Till number printed on this POS receipt.",
    )

    @api.model
    def _load_pos_data_read(self, records, config):
        read_records = super()._load_pos_data_read(records, config)
        till_numbers = {record.id: record.till_number or False for record in records}
        for read_record in read_records:
            read_record["till_number"] = till_numbers.get(read_record["id"], False)
        return read_records
