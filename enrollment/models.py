from django.db import models

from django.contrib.auth.models import User

from .choices import *

#NOTES
#ImageFields requires PIL/Pillow http://python-imaging.github.io/Pillow/

class Provider(models.Model):
	npi = models.CharField(max_length=10)
	provider_or_applicant_name = models.CharField(max_length=100)
	license_number = models.CharField(max_length=50)
	license_attachment = models.FileField(upload_to='files')
	license_effective_date = models.DateField()
	license_expiration_date = models.DateField()
	provider_type = models.CharField(max_length=2, choices=PROVIDER_TYPE_CHOICES)
	medicare_or_other_npi = models.CharField(max_length=50)
	primary_taxonomy_code = models.CharField(max_length=20)
	taxonomy_code1 = models.CharField(max_length=20, blank=True, null=True)
	taxonomy_code2 = models.CharField(max_length=20, blank=True, null=True)
	taxpayer_indentification_number = models.CharField(max_length=50)#tin_attachment = ..... #taxpayer_identification_number attachment
	social_security_number = models.CharField(max_length=50, blank=True, null=True) #if not tin for sole proprietor fill this # for Nurse practitioner only
	duration_of_training = models.PositiveIntegerField(max_length=2, blank=True, null=True) #In years only 
	clinical_and_didatic_training = models.CharField(max_length=100, blank=True, null=True)
	#end for
	clinical_laboratory_improvement_amendment_certificate_number = models.PositiveIntegerField(max_length=25) #CLIA
	clia_attachment = models.FileField(upload_to='files') # clinical_laboratory_improvement_amendment --> clia

	state_laboratory_license_or_registration_number = models.CharField(max_length=50)
	sll_or_reg_num_attachment = models.FileField(upload_to='files') # state_laboratory_license_or_registration_number attachment

	drivers_license_or_state_issued_identification_number = models.CharField(max_length=50)
	dl_sin_attachment = models.FileField(upload_to='files') # drivers_license_or_state_issued_identification_number attachment

	created_by = models.ForeignKey(User)

	def __str__(self):
		return '%s, %s' % (self.provider_or_applicant_name, self.npi)


class Business(models.Model):
	
	name = models.CharField(max_length=100, blank=True)
	is_this_a_fiticious_name = models.CharField(max_length=1, choices=BUSINESS_NAME_CHOICES)
	telephone_number = models.IntegerField(max_length=11)
	fiticious_statement_or_permit_number = models.CharField(max_length=100)
	attached_statement_or_permit = models.FileField(upload_to='files')
	effective_date = models.DateField()
	business_address = models.TextField()
	bussiness_address_city = models.CharField(max_length=20)
	business_address_country = models.CharField(max_length=50)#choices=COUNTRY_CHOICES)
	business_address_state = models.CharField(max_length=2, choices=STATE_CHOICES)
	business_address_zip_code = models.CharField(max_length=9)

	pay_to_address = models.TextField()
	pay_to_city = models.CharField(max_length=20)
	pay_to_state = models.CharField(max_length=2, choices=STATE_CHOICES)
	pay_to_zip_code = models.PositiveIntegerField(max_length=9)

	mailing_address = models.TextField()
	mailing_address_city = models.CharField(max_length=20)
	mailing_address_state = models.CharField(max_length=2, choices=STATE_CHOICES)
	mailing_address_zip_code = models.CharField(max_length=9)

	#for change of address
	previous_business_address = models.TextField(blank=True)
	previous_bussiness_address_city = models.CharField(max_length=20, blank=True)
	previous_business_address_state = models.CharField(max_length=2, choices=STATE_CHOICES, blank=True)
	previous_business_address_zip_code = models.PositiveIntegerField(max_length=9, blank=True)
    # end Provider


class IndividualSigningApplication(models.Model):
	
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	middle_name = models.CharField(max_length=20, blank=True)
	drivers_license = models.CharField(max_length=20)
	date_of_birth = models.DateField()
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
	license_attachment = models.FileField(upload_to='files') 
	social_security_number = models.CharField(max_length=50, blank=True, null=True)
	declaration = models.BooleanField(default=True)
	signature = models.FileField(upload_to='files')
	title = models.CharField(max_length=20)
	#Executed at
	city = models.CharField(max_length=20)
	state = models.CharField(max_length=2, choices=STATE_CHOICES)
	date = models.DateField(auto_now=True)
	notary_public = models.TextField()

class ContactInfo(models.Model):
	
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	middle_name = models.CharField(max_length=20, blank=True)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
	title_or_position = models.CharField(max_length=20)
	email = models.EmailField()
	telephone_number = models.IntegerField(max_length=11)

class LiabilityInsurance(models.Model):
	
	insurance_company = models.CharField(max_length=50)
	insurance_policy_number = models.CharField(max_length=25)
	issued_date = models.DateField()
	expiration_date = models.DateField()
	insurance_agent = models.CharField(max_length=50)
	telephone_number = models.IntegerField(max_length=11)
	attachment = models.FileField(upload_to='files')

class ProfessionalLiabilityInsurance(models.Model):
	
	insurance_company = models.CharField(max_length=50)
	insurance_policy_number = models.CharField(max_length=25)
	issued_date = models.DateField()
	expiration_date = models.DateField()
	insurance_agent = models.CharField(max_length=50)
	telephone_number = models.CharField(max_length=11)
	attachment = models.FileField(upload_to='files')

#class WorkersCompensationLicense(models.Model):
