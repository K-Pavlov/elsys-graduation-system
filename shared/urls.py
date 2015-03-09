from django.conf.urls import patterns, url

from views import home, teachers, firms, seasons

urlpatterns = patterns('',
    # Main page
    url(r'^$', home.index, name='home'), 
    # Seasons
    url(r'^seasons/$', seasons.all, name='all_seasons'),
    url(r'^seasons/create/$', seasons.create, name='create_season'),
    url(r'^seasons/edit/(?P<id>[-\w]+)/$', seasons.edit, name='edit_season'),
    url(r'^seasons/page/(?P<page_num>[-\w]+)/$', seasons.get_page, name='get_season_page'),
    url(r'^seasons/delete/(?P<id>[-\w]+)/$', seasons.delete, name='delete_season'),
    url(r'^seasons/change/$', seasons.change, name='change_season'),
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
)