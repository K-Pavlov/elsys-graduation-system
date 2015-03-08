# -*- coding: utf-8 -*-
 
from datetime import datetime
 
from django.contrib import admin
from django.conf import settings
from django.conf.urls import patterns, url, include
from django.conf.urls.static import static

from shared.forms import BootstrapAuthenticationForm
from shared.views import home, teachers, firms, seasons
from reviewing.views import referals, referees
from division.views import class_letters, mentors, specializations, students, topics
from defences import views as comissions
 
admin.autodiscover()

urlpatterns = patterns('',
    # Students
    url(r'^$', home.index, name='home'),
    url(r'^students/$', students.all, name='all_students'),
    url(r'^students/create/$', students.create, name='create_student'),
    url(r'^students/edit/(?P<id>[-\w]+)/$', students.edit, name='edit_student'),
    url(r'^students/page/(?P<page_num>[-\w]+)/$', students.get_page, name='get_student_page'),
    url(r'^students/delete/(?P<id>[-\w]+)/$', students.delete, name='delete_student'),
    url(r'^students/upload/$', students.upload_csv, name='upload_students'),
    url(r'^students/preview/$', students.preview_csv, name='preview_students'),
    # Topics
    url(r'^topics/$', topics.all, name='all_topics'),
    url(r'^topics/create/$', topics.create, name='create_topic'),
    url(r'^topics/edit/(?P<id>[-\w]+)/$', topics.edit, name='edit_topic'),
    url(r'^topics/page/(?P<page_num>[-\w]+)/$', topics.get_page, name='get_topic_page'),
    url(r'^topics/delete/(?P<id>[-\w]+)/$', topics.delete, name='delete_topic'),
    url(r'^topics/preview/$', topics.preview_csv, name='preview_topics'),
    url(r'^topics/upload/$', topics.upload_csv, name='upload_topics'),
    # Seasons
    url(r'^seasons/$', seasons.all, name='all_seasons'),
    url(r'^seasons/create/$', seasons.create, name='create_season'),
    url(r'^seasons/edit/(?P<id>[-\w]+)/$', seasons.edit, name='edit_season'),
    url(r'^seasons/page/(?P<page_num>[-\w]+)/$', seasons.get_page, name='get_season_page'),
    url(r'^seasons/delete/(?P<id>[-\w]+)/$', seasons.delete, name='delete_season'),
    url(r'^seasons/change/$', seasons.change, name='change_season'),
    # Mentors
    url(r'^mentors/$', mentors.all, name='all_mentors'),
    url(r'^mentors/create/$', mentors.create, name='create_mentor'),
    url(r'^mentors/edit/(?P<id>[-\w]+)/$', mentors.edit, name='edit_mentor'),
    url(r'^mentors/page/(?P<page_num>[-\w]+)/$', mentors.get_page, name='get_mentor_page'),
    url(r'^mentors/delete/(?P<id>[-\w]+)/$', mentors.delete, name='delete_mentor'),
    url(r'^mentors/preview/$', mentors.preview_csv, name='preview_mentors'),
    url(r'^mentors/upload/$', mentors.upload_csv, name='upload_mentors'),
    # Referees
    url(r'^referees/$', referees.all, name='all_referees'),
    url(r'^referees/create/$', referees.create, name='create_referee'),
    url(r'^referees/edit/(?P<id>[-\w]+)/$', referees.edit, name='edit_referee'),
    url(r'^referees/page/(?P<page_num>[-\w]+)/$', referees.get_page, name='get_referee_page'),
    url(r'^referees/delete/(?P<id>[-\w]+)/$', referees.delete, name='delete_referee'),
    url(r'^referees/upload/$', referees.upload_csv, name='upload_referees'),
    url(r'^referees/preview/$', referees.preview_csv, name='preview_referees'),
    url(r'^referees/refereal_upload/$', referees.upload_referal, name='upload_referal'),
    # Referals
    url(r'^referals/$', referals.all, name='all_referals'),
    url(r'^referals/create/$', referals.create, name='create_referal'),
    url(r'^referals/edit/(?P<id>[-\w]+)/$', referals.edit, name='edit_referal'),
    url(r'^referals/page/(?P<page_num>[-\w]+)/$', referals.get_page, name='get_referal_page'),
    url(r'^referals/delete/(?P<id>[-\w]+)/$', referals.delete, name='delete_referal'),
    # Class letters
    url(r'^class_letters/$', class_letters.all, name='all_class_letters'),
    url(r'^class_letters/create/$', class_letters.create, name='create_class_letter'),
    url(r'^class_letters/edit/(?P<id>[-\w]+)/$', class_letters.edit, name='edit_class_letter'),
    url(r'^class_letters/page/(?P<page_num>[-\w]+)/$', class_letters.get_page, name='get_class_letter_page'),
    url(r'^class_letters/delete/(?P<id>[-\w]+)/$', class_letters.delete, name='delete_class_letter'),
    # Specializations
    url(r'^specializations/$', specializations.all, name='all_specializations'),
    url(r'^specializations/create/$', specializations.create, name='create_specialization'),
    url(r'^specializations/edit/(?P<id>[-\w]+)/$', specializations.edit, name='edit_specialization'),
    url(r'^specializations/page/(?P<page_num>[-\w]+)/$', specializations.get_page, name='get_specialization_page'),
    url(r'^specializations/delete/(?P<id>[-\w]+)/$', specializations.delete, name='delete_specialization'),
    # Firms
    url(r'^firms/$', firms.all, name='all_firms'),
    url(r'^firms/create/$', firms.create, name='create_firm'),
    url(r'^firms/edit/(?P<id>[-\w]+)/$', firms.edit, name='edit_firm'),
    url(r'^firms/page/(?P<page_num>[-\w]+)/$', firms.get_page, name='get_firm_page'),
    url(r'^firms/delete/(?P<id>[-\w]+)/$', firms.delete, name='delete_firm'),
    # Teachers
    url(r'^teachers/$', teachers.all, name='all_teachers'),
    url(r'^teachers/create/$', teachers.create, name='create_teacher'),
    url(r'^teachers/edit/(?P<id>[-\w]+)/$', teachers.edit, name='edit_teacher'),
    url(r'^teachers/page/(?P<page_num>[-\w]+)/$', teachers.get_page, name='get_teacher_page'),
    url(r'^teachers/delete/(?P<id>[-\w]+)/$', teachers.delete, name='delete_teacher'),
    # Comissions
    url(r'^comissions/$', comissions.all, name='all_comissions'),
    url(r'^comissions/create/$', comissions.create, name='create_comission'),
    url(r'^comissions/edit/(?P<id>[-\w]+)/$', comissions.edit, name='edit_comission'),
    url(r'^comissions/page/(?P<page_num>[-\w]+)/$', comissions.get_page, name='get_comission_page'),
    url(r'^comissions/delete/(?P<id>[-\w]+)/$', comissions.delete, name='delete_comission'),
    # Protocols
    url(r'^comissions/protocol/all_students/$', comissions.all_students, name='all_students_protocol'),
    url(r'^comissions/protocol/comission_with_students/(?P<id>[-\w]+)/$', comissions.comission_with_students, name='comission_with_students_protocol'),
    url(r'^comissions/comission_students_indepth/(?P<id>[-\w]+)/$', comissions.comission_students_indepth, name='comission_students_indepth_protocol'),
    # Google auth and normal login
    url(r'^login/$',
        'django.contrib.auth.views.login',
        {
            'template_name': 'login.html',
            'authentication_form': BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': u'Влизане в системата',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        'django.contrib.auth.views.logout',
        {
            'next_page': '/',
        },
        name='logout'),
    # Django auth urls
    url('', include('django.contrib.auth.urls', namespace='auth')),
    # Python social app django urls
    url('', include('social.apps.django_app.urls', namespace='social')),
    # Django admin urls 
    url(r'^admin/', admin.site.urls),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
