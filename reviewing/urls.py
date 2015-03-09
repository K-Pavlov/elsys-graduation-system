from django.conf.urls import patterns, url

from views import referals, referees

urlpatterns = patterns('', 
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
)