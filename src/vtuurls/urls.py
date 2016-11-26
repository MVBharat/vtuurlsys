
from django.conf.urls import url
from django.contrib import admin

from shortener.views import HomeView, URLRedirectView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view()),
    url(r'^(?P<shortcode>[\w-]+)/$', URLRedirectView.as_view(), name='scode'),  #  python regurlar expresion and $ indicates end of patern matching at the url
 

]
