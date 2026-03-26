from django.contrib import admin
from .models import Especie, Pet, Tutor, Usuario, Veterinario, Vacina

# Configuração para Veterinário


@admin.register(Veterinario)
class VeterinarioAdmin(admin.ModelAdmin):
    list_display = ('veterinario', 'cidade', 'celular', 'criado_em')
    readonly_fields = ('criado_em', 'atualizado_em')
    search_fields = ('veterinario', 'cidade')

# Configuração para Espécie


@admin.register(Especie)
class EspecieAdmin(admin.ModelAdmin):
    list_display = ('especie',)
    search_fields = ('especie',)

# Configuração para Tutor


@admin.register(Tutor)
class TutorAdmin(admin.ModelAdmin):
    list_display = ('tutor', 'email', 'celular', 'cidade')
    readonly_fields = ('criado_em', 'atualizado_em')
    search_fields = ('tutor', 'email')

# Configuração para Pet


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('pet', 'raca', 'especie', 'tutor', 'criado_em')
    readonly_fields = ('criado_em', 'atualizado_em')
    list_filter = ('especie', 'sexo', 'castrado')
    search_fields = ('pet', 'raca')

# Configuração para Usuário


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('login', 'criado_em')
    readonly_fields = ('criado_em', 'atualizado_em')
    # Ocultamos a senha da listagem por segurança
    search_fields = ('login',)

# Configuração para Vacina


@admin.register(Vacina)
class VacinaAdmin(admin.ModelAdmin):
    list_display = ('vacina', 'pet', 'data_aplicacao', 'veterinario')
    readonly_fields = ('criado_em', 'atualizado_em')
    list_filter = ('vacina', 'data_aplicacao')
    # Busca pelo nome do Pet relacionado
    search_fields = ('vacina', 'pet__pet')
