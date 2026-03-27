from django.urls import path
from . import views

urlpatterns = [
    path('', views.tela_inicial, name='tela_inicial'),
    path('login/', views.login_view, name='login'),
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('pet/cadastro/', views.cadastro_pet, name='cadastro_pet'),
    path('vacina/cadastro/', views.cadastro_vacina, name='cadastro_vacina'),
    path('logout/', views.logout_view, name='logout'),
    path('veterinario/cadastro/', views.cadastro_veterinario,
         name='cadastro_veterinario'),

]
