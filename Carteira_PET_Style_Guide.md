# Carteira PET — Guia de Design (Style Guide)

> Documento de referência visual extraído diretamente da aplicação em produção.
> URL: https://carteira-pet-bf25460a.base44.app/style-guide
> Plataforma: Base44 | Framework CSS: Tailwind CSS v3.4.17

---

## 1. Visão Geral

A Carteira PET é um sistema web para gerenciamento de saúde e vacinação de pets. O design adota uma estética **minimalista, limpa e moderna**, utilizando uma paleta de cores baseada na escala **Slate** do Tailwind CSS. A identidade visual transmite profissionalismo, confiança e simplicidade, com cards de vidro (glassmorphism sutil), gradientes suaves e tipografia system-ui.

A aplicação é construída como um SPA (Single Page Application) com autenticação integrada (email/senha e Google OAuth), e utiliza componentes visuais consistentes em todas as telas.

---

## 2. Paleta de Cores

A paleta é baseada na escala **Slate** do Tailwind CSS, que oferece tons de cinza-azulado elegantes e neutros. Não há cores de destaque vibrantes — a hierarquia visual é criada pela variação de opacidade e peso tipográfico.

### 2.1 Cores Principais

| Token             | HEX        | RGB                   | Uso principal                                      |
|-------------------|------------|-----------------------|----------------------------------------------------|
| `slate-50`        | `#F8FAFC`  | `rgb(248, 250, 252)`  | Fundo da página (gradiente), background de inputs    |
| `slate-100`       | `#F1F5F9`  | `rgb(241, 245, 249)`  | Fundo da página (gradiente), fundo alternativo      |
| `slate-200`       | `#E2E8F0`  | `rgb(226, 232, 240)`  | Bordas de inputs, bordas de botões secundários      |
| `slate-300`       | `#CBD5E1`  | `rgb(203, 213, 225)`  | Gradiente decorativo, separador "OR"               |
| `slate-400`       | `#94A3B8`  | `rgb(148, 163, 184)`  | Placeholder de inputs                              |
| `slate-500`       | `#64748B`  | `rgb(100, 116, 139)`  | Texto secundário, links, botões ghost              |
| `slate-700`       | `#334155`  | `rgb(51, 65, 85)`    | Texto de botões secundários                         |
| `slate-900`       | `#0F172A`  | `rgb(15, 23, 42)`    | **Cor primária** — fundo de botões CTA, headings   |
| `zinc-950`        | `#09090B`  | `rgb(9, 9, 11)`      | Cor de texto principal (body)                      |
| `white`           | `#FFFFFF`  | `rgb(255, 255, 255)` | Fundo de cards, texto sobre fundo escuro           |

### 2.2 Cores Semânticas

| Função       | Cor utilizada                                        | Contexto                          |
|--------------|------------------------------------------------------|-----------------------------------|
| Fundo página | `bg-gradient-to-br from-slate-50 to-slate-100`       | Gradiente linear diagonal         |
| Card         | `bg-white/95` + `backdrop-blur-sm`                   | Glassmorphism sutil               |
| Input        | `bg-slate-50/50` + `border-slate-200`                | Campos de formulário              |
| Botão primário| `bg-slate-900` + `text-white`                       | Ação principal (Sign in, Create)  |
| Botão secundário| `bg-white` + `border-slate-200` + `text-slate-700` | Google login, ações alternativas |
| Link/ghost   | `text-slate-500`                                     | Forgot password, Sign up          |
| Erro         | A ser definido pelo sistema Base44 (toast/sonner)    | Validação de formulário           |
| Sucesso      | A ser definido pelo sistema Base44 (toast/sonner)    | Feedback positivo                 |

### 2.3 Gradientes

| Elemento         | Classes Tailwind                                              | Efeito visual                          |
|------------------|---------------------------------------------------------------|----------------------------------------|
| Fundo da página  | `bg-gradient-to-br from-slate-50 to-slate-100`                 | Gradiente suave diagonal (canto superior esquerdo → inferior direito) |
| Barra do card    | `bg-gradient-to-r from-slate-200 via-slate-300 to-slate-200`  | Faixa decorativa no topo do card        |
| Blur decorativo  | `bg-gradient-to-br from-slate-200 to-slate-300 blur-xl opacity-30` | Círculo desfocado atrás do logo   |

---

## 3. Tipografia

### 3.1 Font Family

```
font-family: ui-sans-serif, system-ui, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";
```

A aplicação utiliza a **fonte system-ui nativa do dispositivo**, sem importação de fontes externas. Isso garante carregamento instantâneo e aparência nativa em cada plataforma.

### 3.2 Hierarquia Tipográfica

| Elemento          | Tamanho     | Peso    | Cor                   | Line Height | Uso                              |
|-------------------|-------------|---------|-----------------------|-------------|----------------------------------|
| H1 (Título página)| `30px`      | `700`   | `slate-900`           | —           | "Welcome to Carteira Pet"        |
| H2 (Subtítulo)    | `24px`      | `700`   | `slate-900`           | —           | "Create your account"            |
| Parágrafo         | `16px`      | `400`   | `slate-500`           | —           | "Sign in to continue"            |
| Label             | `14px`      | `400`   | `slate-700` (input)   | —           | Rótulos dos campos de formulário |
| Input text        | `14px`      | `400`   | `zinc-950`            | —           | Texto digitado nos campos        |
| Placeholder       | `14px`      | `400`   | `slate-400`           | —           | Texto hint dos inputs            |
| Botão primário    | `14px`      | `500`   | `white`               | —           | "Sign in", "Create account"      |
| Botão secundário  | `16px`      | `500`   | `slate-700`           | —           | "Continue with Google"           |
| Botão ghost/link  | `14px`      | `500`/`400` | `slate-500`        | —           | "Forgot password?", "Sign up"    |
| Small/Caption     | `12px` (xs) | `400`   | `slate-500`           | —           | Textos auxiliares                 |

---

## 4. Componentes

### 4.1 Card (Container Principal)

O card é o elemento central do layout, usado para agrupar formulários e conteúdo.

| Propriedade       | Valor                                                     |
|-------------------|-----------------------------------------------------------|
| Fundo             | `bg-white/95` (branco 95% opacidade)                     |
| Border radius     | `16px` (`rounded-2xl`)                                   |
| Sombra            | `shadow-2xl` — `0 25px 50px -12px rgba(0,0,0,0.25)`     |
| Backdrop blur     | `backdrop-blur-sm` (4px blur)                            |
| Borda             | `border-0` (sem borda visível)                           |
| Overflow          | `overflow-hidden`                                         |
| Largura           | `max-w-md` (28rem = 448px)                               |
| Padding interno   | `p-8` (mobile) / `p-10` (tablet `sm:`)                   |

**Barra decorativa superior do card:**

| Propriedade       | Valor                                                        |
|-------------------|--------------------------------------------------------------|
| Posição           | `absolute top-0 left-0 right-0 h-1`                         |
| Gradiente         | `from-slate-200 via-slate-300 to-slate-200` (horizontal)    |
| Altura            | `4px` (`h-1`)                                               |

**Elemento decorativo (blur circle) atrás do logo:**

| Propriedade       | Valor                                                        |
|-------------------|--------------------------------------------------------------|
| Posição           | `absolute inset-0` (preenche o card)                         |
| Gradiente         | `from-slate-200 to-slate-300` (diagonal)                    |
| Blur              | `blur-xl` (24px)                                             |
| Border radius     | `rounded-full` (círculo)                                    |
| Opacidade         | `opacity-30` (30%)                                          |
| Hover             | `group-hover:opacity-40` (40%)                              |
| Transição         | `transition-opacity duration-300`                            |

### 4.2 Logo

| Propriedade       | Valor                                                          |
|-------------------|----------------------------------------------------------------|
| Imagem            | `https://media.base44.com/images/public/69d05d6832b317d3bf25460a/85908382c_logo.png` |
| Alt text          | "Carteira Pet logo"                                           |
| Tamanho           | `80x80px` (mobile) / `96x96px` (tablet `sm:`)                 |
| Border radius     | `rounded-full` (círculo)                                     |
| Object fit        | `object-cover`                                                |
| Sombra            | `shadow-lg` (`0 10px 15px -3px rgba(0,0,0,0.1)`)             |
| Ring              | `ring-4 ring-white/50` (anel branco 50% opacidade, 4px)       |
| Hover             | `group-hover:shadow-xl`                                       |
| Transição         | `transition-all duration-300`                                 |
| Flex              | `shrink-0`                                                    |

### 4.3 Campos de Input (Formulário)

| Propriedade         | Valor                                                          |
|---------------------|----------------------------------------------------------------|
| Tipo                | Text, email, password                                          |
| Background          | `bg-slate-50/50` (slate-50 a 50% opacidade)                   |
| Border              | `1px solid slate-200` (`border-slate-200`)                     |
| Border radius       | `12px` (`rounded-xl`)                                          |
| Padding             | `8px 12px 8px 40px` (40px à esquerda para ícone)             |
| Height              | `48px` (login) / `44px` (signup)                              |
| Font size           | `14px`                                                        |
| Cor do texto        | `zinc-950`                                                    |
| Cor do placeholder  | `slate-400`                                                   |
| Focus               | `border-slate-400` + `ring-slate-400`                         |
| Focus ring          | `focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-offset-2` |
| Transição           | `transition-colors duration-200`                              |
| Ícone               | Posicionado com `absolute left-3 top-1/2 -translate-y-1/2`     |

### 4.4 Botões

#### Botão Primário (CTA)

| Propriedade     | Valor                                              |
|-----------------|----------------------------------------------------|
| Background      | `bg-slate-900` (`rgb(15, 23, 42)`)                |
| Cor do texto    | `text-white`                                       |
| Border radius   | `12px` (`rounded-xl`)                              |
| Padding         | `8px 12px`                                         |
| Font size       | `14px`                                            |
| Font weight     | `500` (`font-medium`)                              |
| Sombra          | `shadow-sm` (`0 1px 2px rgba(0,0,0,0.05)`)       |
| Hover           | `hover:bg-slate-800`                               |
| Focus           | `focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-offset-2` |
| Estado disabled | `disabled:pointer-events-none disabled:cursor-not-allowed disabled:opacity-50` |

#### Botão Secundário (Google / Borda)

| Propriedade     | Valor                                              |
|-----------------|----------------------------------------------------|
| Background      | `bg-white`                                         |
| Cor do texto    | `slate-700`                                        |
| Border          | `1px solid slate-200`                              |
| Border radius   | `12px` (`rounded-xl`)                              |
| Padding         | `14px 20px`                                        |
| Font size       | `16px`                                            |
| Font weight     | `500` (`font-medium`)                              |
| Hover           | `hover:bg-slate-50` + `hover:border-slate-300`     |

#### Botão Ghost / Link

| Propriedade     | Valor                                              |
|-----------------|----------------------------------------------------|
| Background      | `transparent`                                      |
| Cor do texto    | `slate-500`                                        |
| Border          | nenhum                                             |
| Padding         | nenhum (herda do layout)                           |
| Font size       | `14px`                                            |
| Font weight     | `500` ou `400`                                     |
| Hover           | `hover:text-slate-700`                             |
| Cursor          | `pointer`                                          |

### 4.5 Separador "OR"

| Propriedade     | Valor                                              |
|-----------------|----------------------------------------------------|
| Layout          | Flexbox com `gap-3`                                |
| Linha           | `h-px bg-slate-200 flex-1`                         |
| Texto           | `text-xs uppercase tracking-wider text-slate-400`  |
| Font size       | `12px`                                            |
| Transform       | `uppercase`                                        |
| Letter spacing  | `0.05em` (`tracking-wider`)                       |

### 4.6 Toast / Notificações

O sistema utiliza a biblioteca **Sonner** para notificações toast.

| Propriedade       | Valor padrão Sonner                                  |
|-------------------|------------------------------------------------------|
| Posição           | Bottom-right                                         |
| Border radius     | `8px`                                                |
| Fundo             | Variável (normal-bg via CSS custom properties)       |
| Fonte             | `ui-sans-serif, system-ui, ...`                      |
| Animação          | Slide-up com fade                                     |
| Z-index           | `999999999`                                          |

---

## 5. Layout e Espaçamento

### 5.1 Container da Página

| Propriedade       | Valor                                                          |
|-------------------|----------------------------------------------------------------|
| Min-height        | `min-h-screen` (100vh)                                        |
| Display           | `flex items-center justify-center` (centralizado)             |
| Background        | `bg-gradient-to-br from-slate-50 to-slate-100 p-4`           |
| Padding           | `16px` (mobile `p-4`)                                         |

### 5.2 Card Interno

| Propriedade       | Valor                                                          |
|-------------------|----------------------------------------------------------------|
| Largura           | `max-w-md` (448px)                                            |
| Padding           | `32px` (mobile `p-8`) / `40px` (tablet `sm:p-10`)            |
| Gap entre campos  | `space-y-3` (12px) ou `space-y-4` (16px)                    |

### 5.3 Logo + Título

| Propriedade       | Valor                                                          |
|-------------------|----------------------------------------------------------------|
| Espaçamento logo  | `my-6` (24px vertical)                                        |
| Gap (título → subtitle) | `space-y-1.5` (6px)                                      |
| Gap (subtitle → botão Google) | `space-y-6` (24px)                                     |

### 5.4 Formulário

| Propriedade           | Valor                                              |
|-----------------------|----------------------------------------------------|
| Gap entre campos      | `space-y-2` (8px) ou `space-y-3` (12px)           |
| Largura dos inputs    | `w-full` (100%)                                   |
| Gap entre input group | `gap-2` (8px) — entre ícone e input              |
| Gap label → input     | Integrado no componente (label embutido)           |

---

## 6. Sombras

| Token        | Valor                                                  | Uso                          |
|--------------|--------------------------------------------------------|------------------------------|
| `shadow-sm`  | `0 1px 2px 0 rgba(0,0,0,0.05)`                        | Botão primário               |
| `shadow-lg`  | `0 10px 15px -3px rgba(0,0,0,0.1), 0 4px 6px -4px rgba(0,0,0,0.1)` | Logo                       |
| `shadow-xl`  | `0 20px 25px -5px rgba(0,0,0,0.1), 0 8px 10px -6px rgba(0,0,0,0.1)` | Logo (hover)              |
| `shadow-2xl` | `0 25px 50px -12px rgba(0,0,0,0.25)`                   | Card principal               |

---

## 7. Bordas e Border Radius

| Elemento            | Border Radius | Borda                                   |
|---------------------|---------------|-----------------------------------------|
| Card                | `16px`        | `none` (border-0)                       |
| Input               | `12px`        | `1px solid slate-200`                   |
| Botão primário      | `12px`        | `none`                                  |
| Botão secundário    | `12px`        | `1px solid slate-200`                   |
| Logo                | `9999px`      | `ring-4 ring-white/50`                  |
| Blur decorativo     | `9999px`      | `none`                                  |
| Separador OR (linha)| `0`           | `1px solid slate-200` (via h-px + bg)  |

---

## 8. Animações e Transições

| Elemento            | Transição                                       | Duração  |
|---------------------|-------------------------------------------------|----------|
| Botão hover         | `transition-colors`                             | `150ms`  |
| Input focus         | `transition-colors`                             | `200ms`  |
| Logo (hover)        | `transition-all` (sombra + escala)              | `300ms`  |
| Blur decorativo     | `transition-opacity`                            | `300ms`  |
| Card appearance     | Renderização nativa do SPA                     | —        |

---

## 9. Responsividade

### 9.1 Breakpoints

| Breakpoint | Largura     | Adaptações                                          |
|------------|-------------|-----------------------------------------------------|
| Mobile     | `< 640px`   | Logo `80x80px`, padding `32px`, 1 coluna           |
| Tablet (sm)| `>= 640px`  | Logo `96x96px`, padding `40px`, `space-y-4/5`      |
| Desktop (md)| `>= 768px` | Padding horizontal `40px`, padding top `48px`      |

### 9.2 Classes Responsivas Observadas

| Elemento       | Mobile                   | Tablet (`sm:`)             | Desktop (`md:`)            |
|----------------|--------------------------|----------------------------|----------------------------|
| Logo tamanho   | `h-20 w-20` (80px)      | `sm:h-24 sm:w-24` (96px)   | —                          |
| Card padding   | `p-8` (32px)            | `sm:p-10` (40px)           | —                          |
| Spacing        | `space-y-3` (12px)      | `sm:space-y-4` (16px)      | —                          |
| Card gap       | `gap-2` (8px)           | `sm:gap-0` (0px)           | —                          |
| Body padding   | `p-4` (16px)            | —                          | `md:px-10` (40px)          |
| Section padding| —                        | —                          | `md:pt-12 md:pb-10`       |
| Fonte subtitle | `text-sm` (14px)        | `sm:text-base` (16px)      | `md:text-sm` (14px)        |

---

## 10. Tokens CSS (Custom Properties)

O Tailwind CSS injeta automaticamente variáveis CSS no elemento raiz:

```css
:root {
  --tw-border-spacing-x: 0;
  --tw-border-spacing-y: 0;
  --tw-translate-x: 0;
  --tw-translate-y: 0;
  --tw-rotate: 0;
  --tw-skew-x: 0;
  --tw-skew-y: 0;
  --tw-scale-x: 1;
  --tw-scale-y: 1;
  --tw-ring-offset-width: 0px;
  --tw-ring-offset-color: #fff;
  --tw-ring-color: rgb(59 130 246 / 0.5);  /* Blue padrão Tailwind */
  --tw-ring-offset-shadow: 0 0 #0000;
  --tw-ring-shadow: 0 0 #0000;
  --tw-shadow: 0 0 #0000;
  --tw-shadow-colored: 0 0 #0000;
}
```

**Dark Mode:** Configurado como `darkMode: 'class'`, permitindo alternância manual via classe `.dark` no elemento `<html>`.

---

## 11. Estrutura das Telas

### 11.1 Tela de Login

```
min-h-screen (gradient: slate-50 → slate-100)
└── Card (max-w-md, rounded-2xl, shadow-2xl, bg-white/95, backdrop-blur)
    ├── Barra decorativa (h-1, gradient horizontal, absolute top-0)
    ├── Blur decorativo (gradient circle, opacity-30)
    ├── Logo (80-96px, rounded-full, shadow-lg, ring-4 ring-white/50)
    ├── H1: "Welcome to Carteira Pet"
    ├── P: "Sign in to continue"
    ├── Botão: "Continue with Google" (secundário, com ícone Google)
    ├── Separador: "OR"
    ├── Formulário:
    │   ├── Input: Email (com ícone)
    │   └── Input: Password (com ícone)
    ├── Botão: "Sign in" (primário)
    ├── Botão: "Forgot password?" (ghost/link)
    └── Botão: "Need an account? Sign up" (ghost/link)
```

### 11.2 Tela de Cadastro

```
min-h-screen (gradient: slate-50 → slate-100)
└── Card (max-w-md, rounded-2xl, shadow-2xl, bg-white/95, backdrop-blur)
    ├── Barra decorativa (h-1, gradient horizontal, absolute top-0)
    ├── Blur decorativo (gradient circle, opacity-30)
    ├── Logo (80-96px, rounded-full, shadow-lg, ring-4 ring-white/50)
    ├── H2: "Create your account"
    ├── Formulário:
    │   ├── Input: Email (placeholder: "you@example.com")
    │   ├── Input: Password (placeholder: "Min. 8 characters")
    │   └── Input: Confirm Password (placeholder: "Re-enter password")
    ├── Botão: "Create account" (primário)
    └── Botão: "Back to sign in" (ghost/link)
```

### 11.3 Tela de Verificação de Email

```
min-h-screen (gradient: slate-50 → slate-100)
└── Card (max-w-md, rounded-2xl, shadow-2xl, bg-white/95, backdrop-blur)
    ├── Barra decorativa (h-1, gradient horizontal, absolute top-0)
    ├── Blur decorativo (gradient circle, opacity-30)
    ├── H2: "Verify your email"
    ├── P: "We've sent a 6-digit code to {email}"
    ├── 6 inputs de código (pin, individuais)
    ├── Botão: "Verify email" (primário)
    └── Botão: "Resend" (ghost/link)
```

---

## 12. Metadados da Aplicação

| Propriedade              | Valor                                                                                                  |
|--------------------------|--------------------------------------------------------------------------------------------------------|
| Nome do app              | Carteira Pet                                                                                           |
| Logo                     | [Logo PNG](https://media.base44.com/images/public/69d05d6832b317d3bf25460a/85908382c_logo.png) |
| Descrição                | "A digital hub to manage your pet's health records, medical history, and vaccination schedules in one accessible place." |
| Tema (theme-color)       | `#000000`                                                                                              |
| Apple Mobile Web App     | `yes`                                                                                                  |
| Status Bar Style         | `black`                                                                                                |
| Framework CSS            | Tailwind CSS v3.4.17 (via CDN)                                                                         |
| Dark Mode                | `class` (ativável via classe `.dark` no `<html>`)                                                     |
| Auth provider            | Google OAuth + Email/Password                                                                          |
| Toast library            | Sonner                                                                                                  |
| Viewport                 | `width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover`    |
| Robots                   | `noindex, nofollow`                                                                                    |

---

## 13. Referência Rápida — Classes Tailwind Utilizadas

### Layout

```html
<!-- Página -->
<div class="min-h-screen flex items-center justify-center bg-gradient-to-br from-slate-50 to-slate-100 p-4">

<!-- Card -->
<div class="text-card-foreground relative overflow-hidden border-0 shadow-2xl bg-white/95 backdrop-blur-sm rounded-2xl max-w-md w-full">

<!-- Conteúdo interno do card -->
<div class="p-8 sm:p-10">
```

### Inputs

```html
<!-- Input com ícone -->
<div class="relative">
  <svg class="absolute left-3 top-1/2 -translate-y-1/2 h-4 w-4 text-slate-400 pointer-events-none">
    <!-- ícone SVG -->
  </svg>
  <input type="email" placeholder="you@example.com"
    class="w-full h-12 bg-slate-50/50 border border-slate-200 rounded-xl pl-10 pr-4 text-sm
           focus:border-slate-400 focus:ring-slate-400 transition-colors duration-200
           placeholder:text-slate-400" />
</div>
```

### Botões

```html
<!-- Primário -->
<button class="w-full bg-slate-900 text-white rounded-xl py-2 text-sm font-medium
               hover:bg-slate-800 shadow-sm transition-colors duration-150
               focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-offset-2">
  Sign in
</button>

<!-- Secundário -->
<button class="w-full bg-white border border-slate-200 rounded-xl px-5 py-3.5
               text-base font-medium text-slate-700 hover:bg-slate-50 hover:border-slate-300
               transition-all duration-200">
  Continue with Google
</button>

<!-- Ghost -->
<button class="text-sm font-medium text-slate-500 hover:text-slate-700 transition-colors">
  Forgot password?
</button>
```

### Logo

```html
<div class="flex justify-center my-6 group">
  <div class="relative">
    <div class="absolute inset-0 bg-gradient-to-br from-slate-200 to-slate-300
                rounded-full blur-xl opacity-30 group-hover:opacity-40
                transition-opacity duration-300"></div>
    <img src="logo.png" alt="Carteira Pet logo"
         class="relative h-20 w-20 sm:h-24 sm:w-24 rounded-full object-cover
                shadow-lg ring-4 ring-white/50 group-hover:shadow-xl
                transition-all duration-300" />
  </div>
</div>
```

---

*Documento gerado automaticamente a partir da análise da aplicação Carteira PET em produção.*
*Última atualização: Abril 2026*
