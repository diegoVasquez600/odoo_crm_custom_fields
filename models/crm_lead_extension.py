from odoo import models, fields, _

class CrmLead(models.Model):
    _inherit = 'crm.lead'
    x_has_chatted = fields.Boolean(string=_("Has chatted"), required=False, translate=True, 
                                   help=_("Has the lead chatted with a sales representative?, or has the lead been contacted by a sales representative?"))
    x_gender = fields.Selection([
    ('female', _("Female")),
    ('male', _("Male")),
    ('other', _("Other"))
    ], string=_("Gender"), required=False, translate=True, help=_("The genre of the lead."))
    # Service of interest
    x_service_of_interest = fields.Selection([
        ('hair_transplant', _("Hair Transplant")),
        ('beard_transplant', _("Beard Transplant")),
        ('eyebrow_transplant', _("Eyebrow Transplant")),
        ('african_american_hair', _("African American Hair")),
        ('women_hair_transplant', _("Women Hair Transplant")),
        ('stem_cell', _("Stem Cell")),
        ('eye_care', _("Eye Care")),
        ('dental_care', _("Dental Care")),
        ('biomedicine_services', _("Biomedicine Services")),
        ('other', _("Other"))], string=_("Service of Interest"), required=False, translate=True, 
        help=_("The service the lead is interested in."))
    # has been operated in Colombia Care?
    x_has_been_operated = fields.Boolean(string=_("Has been operated?"), required=False, translate=True, help=_("Has the lead been operated by Colombia Care?"))
    # if the lead has been operated, this field will be filled with the operation details else not shown
    x_operation_details = fields.Text(string=_("Operation Details"), required=False, translate=True, 
                                      help=_("Details of the operation the lead had in Colombia Care, if any, separated by commas."))
    x_medical_summary = fields.Many2one('crm.medical.summary', string=_("Medical Summary"), required=False, 
                                        help=_("The medical summary of the lead, if any."))
    x_has_appointment = fields.Boolean(string=_("Has appointment?"), required=False, translate=True, help=_("Does the lead have an appointment with Colombia Care?"))
    # if the lead has an appointment, this field will be filled with the date of the appointment else not shown
    x_appointment_date = fields.Date(string=_("Appointment Date"), required=False, translate=True, help=_("The date of the appointment with Colombia Care."))
    x_preferred_language = fields.Selection([
        ('en', _("English")),
        ('es', _("Spanish")),
        ('pt', _("Portuguese")),
        ('fr', _("French")),
        ('de', _("German"))], string=_("Preferred Language"), required=False, translate=True, help=_("The language the lead prefers to communicate in."))
    x_next_follow_up = fields.Date(string=_("Next Follow Up"), required=False, translate=True, help=_("The date of the next follow up with the lead."))
    x_first_contact_date = fields.Date(string=_("First Contact Date"), required=False, translate=True, help=_("The date of the first contact with the lead."))
    x_last_contact_date = fields.Date(string=_("Last Contact Date"), required=False, translate=True, help=_("The date of the last contact with the lead."))
    x_messages_count_from_lead = fields.Integer(string=_("Messages Count from Lead"), required=False, translate=True, help=_("The number of messages sent by the lead."))
