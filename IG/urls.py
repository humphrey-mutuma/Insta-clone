from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    url(r'^$',views.welcome,name = 'welcome'),
    url(r'^accounts/profile/$',views.profile,name = 'profile'),
    url(r'^profile/(\d+)',views.other_profile,name = 'viewprofile'),
    url(r'^search/profile$', views.search, name='results'),
    url(r'^timeline$', views.timeline, name='timeline'),
    url(r'^edit_profile$', views.edit_profile, name='editprofile'),
    url(r'registration_complete$', views.registration_complete, name='registration_complete'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)