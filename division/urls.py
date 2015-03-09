from django.conf.urls import patterns, url

from views import class_letters, mentors, specializations, students, topics

urlpatterns = patterns('',
    # Students
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
    # Mentors
    url(r'^mentors/$', mentors.all, name='all_mentors'),
    url(r'^mentors/create/$', mentors.create, name='create_mentor'),
    url(r'^mentors/edit/(?P<id>[-\w]+)/$', mentors.edit, name='edit_mentor'),
    url(r'^mentors/page/(?P<page_num>[-\w]+)/$', mentors.get_page, name='get_mentor_page'),
    url(r'^mentors/delete/(?P<id>[-\w]+)/$', mentors.delete, name='delete_mentor'),
    url(r'^mentors/preview/$', mentors.preview_csv, name='preview_mentors'),
    url(r'^mentors/upload/$', mentors.upload_csv, name='upload_mentors'),
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
)