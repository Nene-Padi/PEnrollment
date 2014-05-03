from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views
from .forms import (
	ProviderForm,
	BusinessForm,
	IndividualSigningApplicationForm,
	ContactInfoForm,
	LiabilityInsuranceForm,
	ProfessionalLiabilityInsuranceForm
)
from .views import EnrollmentWizard

urlpatterns = patterns('',
	url(r'^provider/$', views.ProviderCreateView.as_view(), name='create_provider'),
	url(r'^professional_liability_insurance/$', views.ProfessionalLiabilityInsuranceView.as_view(), name='professional_liability_insurance'),
	url(r'^business/$', views.BusinessView.as_view()),
	url(r'^contact_info/$', views.ContactInfoView.as_view()),
	url(r'^liability_insurance/$', views.LiabilityInsuranceView.as_view()),
	url(r'^signing/$', views.IndividualSigningApplicationView.as_view()),
	url(r'^enrollment/$', EnrollmentWizard.as_view([ProviderForm,BusinessForm, IndividualSigningApplicationForm, ContactInfoForm, LiabilityInsuranceForm, ProfessionalLiabilityInsuranceForm]))
)