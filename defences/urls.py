from django.conf.urls import patterns, url

import views as comissions

urlpatterns = patterns('',
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
)