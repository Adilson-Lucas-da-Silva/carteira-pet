from django.shortcuts import render, redirect
from .models import Usuario, Tutor, Pet, Especie, Vacina, Veterinario


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

    return render(request, 'tela_inicial.html')


def login_view(request):
    if request.method == 'POST':
        login = request.POST.get('login')
        senha = request.POST.get('senha')

        try:
            usuario = Usuario.objects.get(login=login, senha=senha)

            # GUARDA NA SESSÃO
            request.session['usuario_id'] = usuario.id_usuario

            return redirect('tela_inicial')

        except Usuario.DoesNotExist:
            return render(request, 'login.html', {'erro': 'Login inválido'})

    return render(request, 'login.html')


def cadastro_view(request):
    if request.method == 'POST':
        nome = request.POST.get('tutor')
        email = request.POST.get('email')
        celular = request.POST.get('celular')
        telefone = request.POST.get('telefone')
        logradouro = request.POST.get('logradouro')
        numero_logradouro = request.POST.get('numero_logradouro')
        complemento = request.POST.get('complemento')
        bairro = request.POST.get('bairro')
        cidade = request.POST.get('cidade')
        uf = request.POST.get('uf')
        cep = request.POST.get('cep')

        login = request.POST.get('login')
        senha = request.POST.get('senha')

        # cria usuário
        usuario = Usuario.objects.create(
            login=login,
            senha=senha
        )

        # cria tutor
        Tutor.objects.create(
            tutor=nome,
            email=email,
            celular=celular,
            telefone=telefone,
            logradouro=logradouro,
            numero_logradouro=numero_logradouro,
            complemento=complemento,
            bairro=bairro,
            cidade=cidade,
            uf=uf,
            cep=cep,
            usuario=usuario
        )

        return redirect('login')

    return render(request, 'cadastro.html')


def cadastro_pet(request):
    if not usuario_esta_logado(request):
        return redirect('login')
    tutor = get_tutor_logado(request)
    if not tutor:
        return redirect('login')

    especies = Especie.objects.all()

    if request.method == 'POST':
        nome = request.POST.get('pet')
        raca = request.POST.get('raca')
        sexo = request.POST.get('sexo')
        data_nascimento = request.POST.get('data_nascimento')
        castrado = request.POST.get('castrado')
        data_castracao = request.POST.get('data_castracao')
        especie_id = request.POST.get('especie')

        especie = Especie.objects.get(id_especie=especie_id)

        Pet.objects.create(
            pet=nome,
            raca=raca,
            sexo=sexo,
            data_nascimento=data_nascimento or None,
            castrado=castrado,
            data_castracao=data_castracao or None,
            especie=especie,
            tutor=tutor
        )

        return redirect('tela_inicial')

    return render(request, 'cadastro_pet.html', {'especies': especies})


def cadastro_vacina(request):
    if not usuario_esta_logado(request):
        return redirect('login')
    tutor = get_tutor_logado(request)
    if not tutor:
        return redirect('login')

    if not tutor:
        return redirect('login')

    pets = Pet.objects.filter(tutor=tutor)
    veterinarios = Veterinario.objects.all()

    if request.method == 'POST':
        nome_vacina = request.POST.get('vacina')
        obs = request.POST.get('obs_vacina')
        data = request.POST.get('data_aplicacao')
        pet_id = request.POST.get('pet')
        veterinario_id = request.POST.get('veterinario')

        pet = Pet.objects.get(id_pet=pet_id)
        veterinario = Veterinario.objects.get(id_veterinario=veterinario_id)

        Vacina.objects.create(
            vacina=nome_vacina,
            obs_vacina=obs,
            data_aplicacao=data,
            pet=pet,
            veterinario=veterinario
        )

        return redirect('tela_inicial')

    return render(request, 'cadastro_vacina.html', {
        'pets': pets,
        'veterinarios': veterinarios
    })


def cadastro_veterinario(request):
    if not usuario_esta_logado(request):
        return redirect('login')

    if request.method == 'POST':
        nome = request.POST.get('veterinario')
        email = request.POST.get('email')
        celular = request.POST.get('celular')
        telefone = request.POST.get('telefone')
        logradouro = request.POST.get('logradouro')
        numero = request.POST.get('numero_endereco')
        bairro = request.POST.get('bairro')
        cidade = request.POST.get('cidade')
        uf = request.POST.get('uf')
        cep = request.POST.get('cep')

        Veterinario.objects.create(
            veterinario=nome,
            email=email,
            celular=celular,
            telefone=telefone,
            logradouro=logradouro,
            numero_endereco=numero,
            bairro=bairro,
            cidade=cidade,
            uf=uf,
            cep=cep
        )

        return redirect('tela_inicial')

    return render(request, 'cadastro_veterinario.html')


def logout_view(request):
    request.session.flush()
    return redirect('login')
