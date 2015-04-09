from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from mysite.view import hello, home_page, current_datetime, display_meta, hours_ahead
from books import views  # the path to books  - not mysite.books
# for url mapping, we need to import the correspond view model
# for view.py, no import these pages

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    ('^$', home_page),
    url(r'^hello/$', hello),
    ('^time/$', current_datetime),
    ('^display/$',display_meta),
    (r'^time/plus/(\d{1,2})/$', hours_ahead),
    (r'^contact/$',views.contact),
    (r'^search/$', views.search),
    (r'^admin/', include(admin.site.urls)),
)
