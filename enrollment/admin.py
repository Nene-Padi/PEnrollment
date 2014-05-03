from django.contrib import admin

from .models import (
	Provider,
	Business,
	IndividualSigningApplication,
	ContactInfo,
	LiabilityInsurance,
	ProfessionalLiabilityInsurance
)

admin.site.register(Provider)
admin.site.register(Business)
admin.site.register(IndividualSigningApplication)
admin.site.register(ContactInfo)
admin.site.register(LiabilityInsurance)
admin.site.register(ProfessionalLiabilityInsurance)