from django.forms import ModelForm
from django.utils.translation import ugettext as _
from .models import (
	Provider,
	Business,
	IndividualSigningApplication,
	ContactInfo,
	LiabilityInsurance,
	ProfessionalLiabilityInsurance
)

class ProviderForm(ModelForm):
	"""docstring for ProviderForm"""
	class Meta:
		model = Provider
		exclude = ['created_by']
		labels = {
			'npi' : _('Provider number (NPI or Denti-Cal number as applicable)'),
			'provider_or_applicant_name' : _('Legal name of applicant or provider (as listed with the IRS)'),
			'license_number' : _('License number (attach legible copy)'),
			'license_effective_date' : _('License effective date'),
			'license_expiration_date' : _('License expiration date'),
			'provider_type' : _('Provider type'),
			'medicare_or_other_npi' : _('Medicare/Other NPI (see instructions)'),
			'primary_taxonomy_code' : _('Primary Taxonomy Code'),
			'taxonomy_code1' : _('Taxonomy Code'),
			'taxonomy_code2' : _('Taxonomy Code'),
			'taxpayer_indentification_number' : _('Taxpayer Identification Number (TIN) issued by the IRS, attach a legible copy of the IRS form'),
			'social_security_number' : _('Social security number. If sole proprietor not using a TIN, you must disclose this number.'),
			'duration_of_training' : _('(Nurse Practitioner only) Duration of training program and school'),
			'clinical_and_didatic_training' : _('(Nurse Practitioner only) Clinical and didactic training or equivalent experience completed'),
			'clinical_laboratory_improvement_amendment_certificate_number' : _('Clinical Laboratory Improvement Amendment (CLIA) Certificate number (attach a legible copy)'),
			'state_laboratory_license_or_registration_number' : _('State Laboratory License/Registration number (attach a legible copy)'),
			'drivers_license_or_state_issued_identification_number' : _('Driver’s license or state-issued identification number and state of issuance (attach a legible copy)'),
		}

class BusinessForm(ModelForm):
    class Meta:
    	model = Business
    	exclude = ['provider']
    	labels = {}

class IndividualSigningApplicationForm(ModelForm):
    class Meta:
    	model = IndividualSigningApplication
    	exclude = ['provider']
    	labels = {}

class ContactInfoForm(ModelForm):
    class Meta:
    	model = ContactInfo
    	exclude = ['provider']
    	labels = {}

class LiabilityInsuranceForm(ModelForm):
    class Meta:
    	model = LiabilityInsurance
    	exclude = ['provider']
    	labels = {}

class ProfessionalLiabilityInsuranceForm(ModelForm):
	class Meta:
		model = ProfessionalLiabilityInsurance
		exclude = ['provider']
		labels = {
			'insurance_company' : _('Name of insurance company'),
			'insurance_policy_number' : _('Insurance policy number'),
			'issued_date' : _('Date policy issued'),
			'expiration_date' : _('Expiration date of policy'),
			'insurance_agent' : _('Insurance agent’s name'),
			'telephone_number' : _('Telephone number')
		}