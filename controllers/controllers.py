# -*- coding: utf-8 -*-
from odoo import http, _
from odoo.http import request
import json


class Rumors(http.Controller):
    @http.route('/rumor/alert/add', type='http', auth='none', methods=['GET'], csrf=False)

    def add_alert(self, village=None, description=None, cvac_name=None, cvac_tel=None, icp_name=None, icp_tel=None,
                  region=None, district=None, structure=None ** kw):
        # Valider les paramètres
        if not village or not description or not cvac_name or not cvac_tel or not icp_name or not icp_tel or not region or not district or not structure:
            return _("Paramètres manquants")

        # Créer l'enregistrement
        alert = request.env['rumor.alert'].sudo().create({
            'name': village.upper() + '_' + ref,
            'village': village,
            'description': description,
            'cvac_name': cvac_name,
            'cvac_tel': cvac_tel,
            'icp_name': icp_name,
            'icp_tel': icp_tel,
            'region': region,
            'district': district,
            'structure': structure
        })

        if alert:
            # return "Enregistrement de l'alerte ajouté avec succès"
            return json.dumps({'success': True, 'alert_id': alert.id})
        else:
            return _("Une erreur s'est produite lors de l'ajout de l'alerte")
