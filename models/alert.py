from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class RumorAlert(models.Model):
    _name = 'rumor.alert'
    _inherit = 'mail.thread'
    _description = _("Tracking of rumors via RapidPro")
    village = fields.Char(string=_("Village"), required=True, tracking=True)
    description = fields.Text(string=_("Description de l'alerte"), tracking=True)
    cvac_name = fields.Char(string=_("Name of Community Health Actor"), required=True, tracking=True)
    cvac_tel = fields.Char(string=_("Phone Contact of Community Health Actor"), required=True, tracking=True)
    icp_name = fields.Char(string=_("Name of Associated Head Nurse"), required=True, tracking=True)
    icp_tel = fields.Char(string=_("Phone of Associated Head Nurse"), required=True, tracking=True)
    region = fields.Char(string=_("Region"), compute="_compute_capitalized_name", tracking=True)
    district = fields.Char(string=_("District"), compute="_compute_capitalized_name", tracking=True)
    structure = fields.Char(string=_("Health Facility"), required=True, tracking=True)
    ref = fields.Char(string="Référence",
                      default=lambda self: self.env['ir.sequence'].next_by_code('rumor.alert') or _("Nouveau"))

    @api.depends('name')
    def _compute_capitalized_name(self):
        for rec in self:
            if rec.region:
                rec.region = rec.region.upper()
            else:
                rec.region = ''
            if rec.district:
                rec.district = rec.district.upper()
            else:
                rec.district = ''

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['ref'] = self.env['ir.sequence'].next_by_code('rumor.alert')
        return super(RumorAlert, self).create(vals_list)
