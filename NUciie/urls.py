
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from django.conf.urls import include


from accounts.views import register, login_view, logout_view
from gallery import views as g
from events import views as e
from team import views as t
from home import views as h
from joinus import views as j
from startup import views as su
from authentication import views as au
from mailing import views as ml
from nustartup import views as nu
from robotics import views as ro
from idea_join import views as i
from bigstartup import views as bs

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register/$', register,name="register"),
    url(r'^login/$', login_view, name="login"),
    url(r'^logout/$', logout_view, name="logout"),
    url(r'^gallery/$', g.gallery, name="gallery"),
    url(r'^events/$', e.events, name="events"),
    url(r'^event_details/$',e.event_details, name="event_details"),
    url(r'^team/$', t.team, name="team"),
    url(r'^wedo/$', t.wedo, name="wedo"),
    url(r'^joinus/$', j.join, name="joinus"),
    url(r'^startupform/$', bs.incub, name="startup"),
    url(r'^$', h.home, name="home"),
    path('events/submit', e.submit, name="eventSubmit"),
    path('<int:pk>/gen_pdf_preview/', su.serve_pdf_preview),
    url(r'^auth/', include('social_django.urls', namespace='social')),
    url(r'^test/', au.auth),
    url(r'^mail/', ml.email),
   url(r'^startups/$', nu.startups, name='startups'),
    url(r'^startup/$', nu.startup),
    url(r'^robotics/$', ro.robotics,name='robotics'),
    url(r'^idea/$',i.idea,name='idea')

]

urlpatterns += staticfiles_urlpatterns();

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header="NU CIIE Admin"
admin.site.site_title="NU CIIE"
admin.site.index_title="Welcome to NU CIIE"

LOGIN_REDIRECT_URL = 'home'
