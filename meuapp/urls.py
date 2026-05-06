

from django.urls import path
from . import views

urlpatterns = [
    path('', views.tela_inicial, name='tela_inicial'),
    path('login/', views.login_view, name='login'),
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.tela_inicial_apos_login,
         name='tela_inicial_apos_login'),

    # Tutor
    path('tutor/', views.detalhes_tutor, name='detalhes_tutor'),
    path('tutor/editar/', views.editar_tutor, name='editar_tutor'),

    # Pets
    path('meus_pets/', views.meus_pets, name='meus_pets'),
    path('pet/cadastro/', views.cadastro_pet, name='cadastro_pet'),
    path('pet/<int:pet_id>/', views.detalhes_pet, name='detalhes_pet'),

    # Vacinas e Veterinários
    path('vacinas/', views.listar_vacinas, name='listar_vacinas'),
    path('vacina/cadastro/', views.cadastro_vacina, name='cadastro_vacina'),
    path('veterinario/cadastro/', views.cadastro_veterinario,
         name='cadastro_veterinario'),

    # Dashboard (Corrigido para apontar para views.dashboard)
    path('dashboard/', views.dashboard, name='dashboard'),
]
