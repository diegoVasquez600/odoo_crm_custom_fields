from odoo import models, fields, _

class MedicalSummary(models.Model):
    _name = 'crm.medical.summary'
    _description = _("Medical Summary")

    lead_id = fields.Many2one('crm.lead', string=_("Lead"), required=True, help=_("The lead this medical summary is associated with."), ondelete='cascade')
    illnesses = fields.Char(string=_("Illnesses"), required=False, translate=True, help=_("The illnesses the lead has, separated by commas."))
    allergies = fields.Char(string=_("Allergies"), required=False, translate=True, help=_("The allergies the lead has, separated by commas."))
    medications = fields.Char(string=_("Medications"), required=False, translate=True, help=_("The medications the lead is taking, separated by commas."))

    # Enforce unique constraint on lead_id
    _sql_constraints = [
        ('lead_id_uniq', 'unique(lead_id)', _("Medical Summary already exists for this lead.")),
    ]