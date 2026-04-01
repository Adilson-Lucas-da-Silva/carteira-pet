
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Veterinario(models.Model):
    id_veterinario = models.AutoField(primary_key=True)
    veterinario = models.CharField(max_length=100)
    email = models.CharField(max_length=100, blank=True, null=True)
    celular = models.CharField(max_length=16, blank=True, null=True)
    telefone = models.CharField(max_length=16, blank=True, null=True)
    logradouro = models.CharField(max_length=50)
    numero_endereco = models.CharField(max_length=10, blank=True, null=True)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    uf = models.CharField(
        max_length=2, db_comment='Unidade da FederaþÒo, exemplo: SP, PE, SC')
    cep = models.CharField(max_length=9, blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.veterinario

    class Meta:
        managed = False
        db_table = 'veterinario'
        verbose_name = 'Veterinário'
        verbose_name_plural = 'Veterinários'


class Especie(models.Model):
    id_especie = models.AutoField(primary_key=True)
    especie = models.CharField(
        max_length=50, db_comment='Descrição da espécie, exemplo: Ave, Canina, Felina')

    def __str__(self):
        return self.especie

    class Meta:
        managed = False
        db_table = 'especie'
        verbose_name = 'Espécie'
        verbose_name_plural = 'Espécies'


class Pet(models.Model):
    id_pet = models.AutoField(primary_key=True)
    pet = models.CharField(max_length=50)
    raca = models.CharField(max_length=50, blank=True, null=True)
    sexo = models.CharField(max_length=1)
    data_nascimento = models.DateField(blank=True, null=True)
    castrado = models.CharField(
        max_length=1, blank=True, null=True, db_comment='Responda apena "S" ou "N"')
    data_castracao = models.DateField(blank=True, null=True)
    tutor = models.ForeignKey('Tutor', models.DO_NOTHING)
    especie = models.ForeignKey(Especie, models.DO_NOTHING)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.pet

    class Meta:
        managed = False
        db_table = 'pet'
        verbose_name = 'Pet'
        verbose_name_plural = 'Pets'


class PetVeterinario(models.Model):
    pet_id_pet = models.ForeignKey(Pet, models.DO_NOTHING)
    veterinario_id_veterinario = models.ForeignKey(
        Veterinario, models.DO_NOTHING)

    def __str__(self):
        return f"{self.pet_id_pet} atendido por {self.veterinario_id_veterinario}"

    class Meta:
        managed = False
        db_table = 'pet_veterinario'
        unique_together = (('pet_id_pet', 'veterinario_id_veterinario'),)


class Tutor(models.Model):
    id_tutor = models.AutoField(primary_key=True)
    tutor = models.CharField(max_length=100, db_comment='Nome do tutor')
    email = models.CharField(max_length=100)
    celular = models.CharField(max_length=20, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    logradouro = models.CharField(max_length=50)
    numero_logradouro = models.CharField(max_length=10, blank=True, null=True)
    complemento = models.CharField(max_length=20, blank=True, null=True)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    uf = models.CharField(
        max_length=2, db_comment='Unidade da FederaþÒo, exemplo: SP, PE, SC')
    cep = models.CharField(max_length=9, blank=True, null=True)
    usuario = models.ForeignKey('Usuario', models.DO_NOTHING)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tutor

    class Meta:
        managed = False
        db_table = 'tutor'
        verbose_name = 'Tutor'
        verbose_name_plural = 'Tutores'


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    login = models.CharField(max_length=50)
    senha = models.CharField(max_length=250)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.login

    class Meta:
        managed = False
        db_table = 'usuario'
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'


class Vacina(models.Model):
    id_vacina = models.AutoField(primary_key=True)
    vacina = models.CharField(max_length=70)
    obs_vacina = models.CharField(max_length=200, blank=True, null=True)
    data_aplicacao = models.DateField()
    pet = models.ForeignKey(Pet, models.DO_NOTHING)
    veterinario = models.ForeignKey('Veterinario', models.DO_NOTHING)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.vacina

    class Meta:
        managed = False
        db_table = 'vacina'
        verbose_name = 'Vacina'
        verbose_name_plural = 'Vacinas'
