from django.shortcuts import render
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib.formtools.wizard.views import SessionWizardView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from .models import (
	Provider,
	Business,
	IndividualSigningApplication,
	ContactInfo,
	LiabilityInsurance,
	ProfessionalLiabilityInsurance
)

from .forms import (
	ProviderForm,
	BusinessForm,
	IndividualSigningApplicationForm,
	ContactInfoForm,
	LiabilityInsuranceForm,
	ProfessionalLiabilityInsuranceForm
)
import os

class ProviderCreateView(CreateView):
	"""docstring for ProviderCreateView"""
	model = Provider
	form_class = ProviderForm
	template_name = 'provider_form.html'
	success_url = '/thanks/'

	def form_valid(self, form):
		#save current user into "created_by" field in models.
		form.instance.created_by = self.request.user
		return super(ProviderCreateView, self).form_valid(form)

	@method_decorator(login_required)
	def dispatch(self, * args, ** kwargs):
		return super(ProviderCreateView, self).dispatch(* args, ** kwargs)

class BusinessView(CreateView):
	"""docstring for BusinessView"""
	model = Business
	form_class = BusinessForm
	template_name = 'provider_form.html'

	def form_valid(self, form):
		return super(BusinessView, self).form_valid(form)

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(BusinessView, self).dispatch(*args, **kwargs)	

class IndividualSigningApplicationView(CreateView):
    model = IndividualSigningApplication
    form_class = IndividualSigningApplicationForm
    template_name = 'provider_form.html'

    def form_valid(self, form):
    	return super(IndividualSigningApplicationView, self).form_valid(form)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(IndividualSigningApplicationView, self).dispatch(*args, **kwargs)

class ContactInfoView(CreateView):
    model = ContactInfo
    template_name = 'provider_form.html'
    form_class = ContactInfoForm

    def form_valid(self, form):
    	return super(ContactInfoView, self).form_valid(form)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ContactInfoView, self).dispatch(*args, **kwargs)

class LiabilityInsuranceView(CreateView):
    model = LiabilityInsurance
    template_name = 'provider_form.html'
    form_class = LiabilityInsuranceForm

    def form_valid(self, form):
    	return super(LiabilityInsuranceView, self).form_valid(form)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LiabilityInsuranceView, self).dispatch(*args, **kwargs)

class ProfessionalLiabilityInsuranceView(CreateView):
	model = ProfessionalLiabilityInsurance
	form_class = ProfessionalLiabilityInsuranceForm
	template_name = 'provider_form.html'
	success_url = '/thanks/'

	def form_valid(self, form):
		return super(ProfessionalLiabilityInsuranceView, self).form_valid(form)

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
	    return super(ProfessionalLiabilityInsuranceView, self).dispatch(*args, **kwargs)


class EnrollmentWizard(SessionWizardView):
	template_name = "enrollment_form.html"

	def done(self, form_list, **kwargs):
		form_data = process_form_data(form_list)
		return HttpResponseRedirect('/thanks/')
	file_storage = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'files'))

def process_form_data(form_list):
	form_data = [form.cleaned_data for form in form_list]

	if form_data.is_valid():
		form_data.save()