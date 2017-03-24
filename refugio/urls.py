from django.conf.urls import url,include
from django.contrib import admin
from app.usuario.views import RegistroUsuario
from django.contrib.auth.views import login, logout_then_login
urlpatterns = [
    #url(r'^admin/', include('app.mascota.urls',namespace='admin')),
     url(r'^admin/', admin.site.urls),
     url(r'^$', include('app.mascota.urls', namespace='index')), # here inicio de la app
     url(r'^mascota/', include('app.mascota.urls', namespace='mascota')),
     url(r'^usuario/',include('app.usuario.urls', namespace='usuario')),
     url(r'^accounts/login/$', login,{'template_name':'login.html'},name='login'),
     url(r'^logout/', logout_then_login,name='logout'),
    #urls para adopcion
    url(r'^adopcion/', include('app.adopcion.urls', namespace='adopcion')),
    url(r'^adoptante/', include('app.adopcion.urls', namespace='adoptante')),
   
]


