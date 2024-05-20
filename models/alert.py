from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class RumorAlert(models.Model):
    _name = 'rumor.alert'
    _inherit = 'mail.thread'
    _description = _("Tracking of rumors via RapidPro")
    name = fields.Char(string='Venue', readonly=True, store=True)
    village = fields.Char(string=_("Village"), required=True, tracking=True)
    description = fields.Text(string=_("Description of alert"), required=True, tracking=True)
    cvac_name = fields.Char(string=_("Name of Community Health Actor"), required=True, tracking=True)
    cvac_tel = fields.Char(string=_("Phone Contact of Community Health Actor"), required=True, tracking=True)
    icp_name = fields.Char(string=_("Name of Associated Head Nurse"), required=True, tracking=True)
    icp_tel = fields.Char(string=_("Phone of Associated Head Nurse"), required=True, tracking=True)
    region = fields.Char(string=_("Region"), required=True, tracking=True)
    district = fields.Char(string=_("District"), required=True, tracking=True)
    structure = fields.Char(string=_("Health Facility"), required=True, tracking=True)
    ref = fields.Char(string="Référence",
                      default=lambda self: self.env['ir.sequence'].sudo().next_by_code('rumor.alert') or _("Nouveau"))


    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['ref'] = self.env['ir.sequence'].sudo().next_by_code('rumor.alert')
            vals['region'] = vals['region'].upper()
            vals['district'] = vals['district'].upper()
            vals['name'] = vals['village'].upper() + '_' + vals['structure']
        return super(RumorAlert, self).create(vals_list)

    @api.model
    def create(self, vals):
        vals['ref'] = self.env['ir.sequence'].sudo().next_by_code('rumor.alert')
        vals['name'] = vals['village'].upper() + '_' + vals['structure']
        record = super(RumorAlert, self).create(vals)
        # Insérez ici votre code personnalisé à exécuter lors de la création d'un seul enregistrement
        return record
