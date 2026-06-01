from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    pos_till_number = fields.Char(
        string="Till Number",
        compute="_compute_pos_till_number",
        inverse="_inverse_pos_till_number",
        readonly=False,
    )

    @api.depends("pos_config_id", "pos_config_id.till_number")
    def _compute_pos_till_number(self):
        for settings in self:
            settings.pos_till_number = settings.pos_config_id.till_number

    def _inverse_pos_till_number(self):
        for settings in self:
            if settings.pos_config_id:
                settings.pos_config_id.till_number = settings.pos_till_number
