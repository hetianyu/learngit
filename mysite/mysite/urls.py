from django.conf.urls.defaults import *
from books.views import *
urlpatterns = patterns('',
('^home/$', index),
('^add/$', addbook),
('^addbook/$',add),
('^search/$', search),
('^information/$',information),
('^delete/$', delete),                   
)
