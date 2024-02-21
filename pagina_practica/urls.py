from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    # Destinos
    path('bonampak/', views.bonampak, name='bonampak'),
    path('cañon/', views.cañon, name='cañon'),
    path('casa/', views.casa, name='casa'),
    path('ciapa/', views.ciapa, name='ciapa'),
    path('san/', views.san, name='san'),
    # promociones
    path('dos/', views.dos, name='dos'),
    path('promo/', views.promo, name='promo'),
    path('avion/', views.avion, name='avion'),
    path('tematicos/', views.tematicos, name='tematicos'),
    # tips
    path('sol/', views.sol, name='sol'),
    path('tours/', views.tours, name='tours'),
    path('top/', views.top, name='top'),
    path('guia/', views.guia, name='guia'),
    path('cafe/', views.cafe, name='cafe'),
    path('mapas/', views.mapas, name='mapas'),
    # Contactanos
    path('direccion/', views.direccion, name='direccion'),
    path('contform/', views.contform, name='contform'),
    path('mapa/', views.mapa, name='mapa'),
    # Empezar
    path('regisform/', views.regisform, name='regisform'),
    # Iniciar sesión
    path('sesionform/', views.sesionform, name='sesionform'),
    # Footer
    path('terminos/', views.terminos, name='terminos'),
    path('aviso/', views.aviso, name='aviso'),
    #formularios
    path('goal/', views.goal, name='goal'),
    path('goal1/', views.goal1, name='goal1'),
    path('goal2/', views.goal2, name='goal2'),
    path('goal2/', views.goal2, name='goal2'),
    path('post/form', views.postform, name='postform'),
    path('post/goal/', views.postgoal, name='postgoal'),

]
