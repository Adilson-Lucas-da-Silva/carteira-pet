

from django.shortcuts import render, redirect
from .models import Usuario, Tutor, Pet, Especie, Vacina, Veterinario
from django.db.models import Count
from django.db.models.functions import ExtractYear
from datetime import date  # Adicionado para o cálculo de idade

# ================================
# FUNÇÕES AUXILIARES
# ================================


def get_usuario_logado(request):
    usuario_id = request.session.get('usuario_id')
    if usuario_id:
        return Usuario.objects.get(id_usuario=usuario_id)
    return None


def get_tutor_logado(request):
    usuario = get_usuario_logado(request)
    if not usuario:
        return None
    return Tutor.objects.filter(usuario=usuario).first()


def usuario_esta_logado(request):
    return 'usuario_id' in request.session

# ================================
# VIEWS
# ================================


def tela_inicial(request):
    if not usuario_esta_logado(request):
        return redirect('login')
    return render(request, 'tela_inicial_apos_login.html')


def login_view(request):
    if request.method == 'POST':
        login = request.POST.get('login')
        senha = request.POST.get('senha')
        try:
            usuario = Usuario.objects.get(login=login, senha=senha)
            request.session['usuario_id'] = usuario.id_usuario
            return redirect('tela_inicial_apos_login')
        except Usuario.DoesNotExist:
            return render(request, 'login.html', {'erro': 'Login inválido'})
    return render(request, 'login.html')


def cadastro_view(request):
    if request.method == 'POST':
        # ... (lógica de cadastro mantida)
        usuario = Usuario.objects.create(login=request.POST.get(
            'login'), senha=request.POST.get('senha'))
        Tutor.objects.create(
            tutor=request.POST.get('tutor'),
            email=request.POST.get('email'),
            celular=request.POST.get('celular'),
            usuario=usuario,
            # adicione os demais campos conforme seu formulário
        )
        return redirect('login')
    return render(request, 'cadastro.html')


def cadastro_pet(request):
    if not usuario_esta_logado(request):
        return redirect('login')
    tutor = get_tutor_logado(request)
    especies = Especie.objects.all()
    if request.method == 'POST':
        especie = Especie.objects.get(id_especie=request.POST.get('especie'))
        Pet.objects.create(
            pet=request.POST.get('pet'),
            raca=request.POST.get('raca'),
            sexo=request.POST.get('sexo'),
            data_nascimento=request.POST.get('data_nascimento') or None,
            castrado=request.POST.get('castrado'),
            especie=especie,
            tutor=tutor
        )
        return redirect('tela_inicial_apos_login')
    return render(request, 'cadastro_pet.html', {'especies': especies})


def cadastro_vacina(request):
    if not usuario_esta_logado(request):
        return redirect('login')
    tutor = get_tutor_logado(request)
    pets = Pet.objects.filter(tutor=tutor)
    veterinarios = Veterinario.objects.all()
    if request.method == 'POST':
        pet = Pet.objects.get(id_pet=request.POST.get('pet'))
        vet = Veterinario.objects.get(
            id_veterinario=request.POST.get('veterinario'))
        Vacina.objects.create(
            vacina=request.POST.get('vacina'),
            data_aplicacao=request.POST.get('data_aplicacao'),
            pet=pet,
            veterinario=vet
        )
        return redirect('tela_inicial_apos_login')
    return render(request, 'cadastro_vacina.html', {'pets': pets, 'veterinarios': veterinarios})


def cadastro_veterinario(request):
    if not usuario_esta_logado(request):
        return redirect('login')
    if request.method == 'POST':
        Veterinario.objects.create(veterinario=request.POST.get(
            'veterinario'), email=request.POST.get('email'))
        return redirect('tela_inicial_apos_login')
    return render(request, 'cadastro_veterinario.html')


def tela_inicial_apos_login(request):
    if not usuario_esta_logado(request):
        return redirect('login')
    return render(request, 'tela_inicial_apos_login.html')


def listar_vacinas(request):
    if not usuario_esta_logado(request):
        return redirect('login')
    tutor = get_tutor_logado(request)
    vacinas = Vacina.objects.filter(pet__tutor=tutor)
    return render(request, 'vacinas.html', {'vacinas': vacinas})


def detalhes_tutor(request):
    if not usuario_esta_logado(request):
        return redirect('login')
    return render(request, 'detalhes_tutor.html', {'tutor': get_tutor_logado(request)})


def editar_tutor(request):
    if not usuario_esta_logado(request):
        return redirect('login')
    tutor = get_tutor_logado(request)
    if request.method == 'POST':
        tutor.tutor = request.POST.get('tutor')
        tutor.save()
        return redirect('detalhes_tutor')
    return render(request, 'editar_tutor.html', {'tutor': tutor})


def detalhes_pet(request, pet_id):
    if not usuario_esta_logado(request):
        return redirect('login')
    pet = Pet.objects.get(id_pet=pet_id, tutor=get_tutor_logado(request))
    vacinas = Vacina.objects.filter(pet=pet)
    return render(request, 'detalhes_pet.html', {'pet': pet, 'vacinas': vacinas})


def meus_pets(request):
    if not usuario_esta_logado(request):
        return redirect('login')
    pets = Pet.objects.filter(tutor=get_tutor_logado(request))
    return render(request, 'meus_pets.html', {'pets': pets})


def dashboard(request):
    if not usuario_esta_logado(request):
        return redirect('login')

    tutor = get_tutor_logado(request)
    pets = Pet.objects.filter(tutor=tutor)

    total_pets = pets.count()
    total_vacinas = Vacina.objects.filter(pet__tutor=tutor).count()

    ultima = Vacina.objects.filter(
        pet__tutor=tutor).order_by('-data_aplicacao').first()

    # Vacinas por ano
    vacinas_por_ano = (
        Vacina.objects
        .filter(pet__tutor=tutor)
        .annotate(ano=ExtractYear('data_aplicacao'))
        .values('ano')
        .annotate(total=Count('id_vacina'))
        .order_by('ano')
    )

    anos = [v['ano'] for v in vacinas_por_ano if v['ano'] is not None]
    totais = [v['total'] for v in vacinas_por_ano if v['ano'] is not None]

    pets_nomes = []
    pets_idades = []

    for pet in pets:
        if pet.data_nascimento:
            idade = date.today().year - pet.data_nascimento.year
            pets_nomes.append(pet.pet)
            pets_idades.append(idade)

    return render(request, 'dashboard.html', {
        'pets': pets,
        'total_pets': total_pets,
        'total_vacinas': total_vacinas,
        'ultima_vacina': ultima.vacina if ultima else '-',
        'pet_ultima_vacina': ultima.pet.pet if ultima else '-',
        'anos': anos,
        'totais': totais,
        'pets_nomes': pets_nomes,
        'pets_idades': pets_idades,
    })


def logout_view(request):
    request.session.flush()
    return redirect('login')
