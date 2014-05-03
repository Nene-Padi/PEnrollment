from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

#from enrollment import views as enrollviews

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'PEnrollment.views.intro', name='intro'),
    # url(r'^blog/', include('blog.urls')),

    #Django Admin site
    url(r'^admin/', include(admin.site.urls)),

    #Django-registration
    #url(r'^accounts/', include('registration.backends.default.urls')),

    #Accounts app 
    url(r'^accounts/', include('accounts.urls')),
    url(r'^home/$', 'PEnrollment.views.home', name='home'),

    #Enrollment
    url(r'^enroll/', include('enrollment.urls')),
    #url(r'^provider/$', enrollviews.ProviderCreateView.as_view(), name='create_provider'),
    #url(r'^professional_liability_insurance/$', enrollviews.ProfessionalLiabilityInsuranceView.as_view(), name='professional_liability_insurance'),

    #Thanks
    url(r'^thanks/$', login_required(TemplateView.as_view(template_name='thanks.html')), ),
)
