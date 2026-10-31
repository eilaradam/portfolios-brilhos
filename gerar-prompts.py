# Gera modelos.js e prompts.js a partir das descrições abaixo.
# Rode com: python3 gerar-prompts.py
import json

MODELOS = [
  # pasta, nome, emoji, familia, genero (a = textos no feminino | o = no masculino)
  ("brilho-01-clara",     "Brilho clara",      "✦",  "brilhos",   "a"),
  ("brilho-03-docinho",   "Docinho",           "🍒", "brilhos",   "a"),
  ("brilho-04-it-girl",   "It girl",           "📸", "brilhos",   "a"),
  ("brilho-05-studio",    "Studio",            "🕊️", "brilhos",   "a"),
  ("brilho-06-colagem",   "Colagem",           "🎞️", "brilhos",   "a"),
  ("brilho-07-basico",    "Básico",            "🤍", "brilhos",   "a"),
  ("brilho-08-street", "Street",            "🧢", "brilhos",   "o"),
  ("brilho-09-papel",  "Papel rasgado",     "✸",  "brilhos",   "o"),
  ("brilho-10-marca",  "Marca",             "👁️", "brilhos",   "o"),
]

def base(nome_modelo, g):
    ela = "aluna" if g == "a" else "aluno"
    formada = "Formada" if g == "a" else "Formado"
    return f"""Você vai criar o MEU PORTFÓLIO de UGC Creator no modelo "{nome_modelo}". Crie a primeira versão completa sem me fazer perguntas antes: quando terminar, eu peço os ajustes.

== COMO ENTREGAR ==
- Tudo em UM ÚNICO arquivo chamado index.html, com o CSS dentro de uma tag style e o JavaScript dentro de uma tag script, no mesmo arquivo.
- Sem bibliotecas e sem build: só as fontes do Google Fonts podem vir de fora.
- Precisa abrir com dois cliques no navegador e poder ser publicado no GitHub Pages ou na Vercel sem nenhum ajuste.
- No head: title com o meu nome e "portfólio UGC", meta description curta e meta viewport.
- Quando terminar, me diga em uma linha como abrir o arquivo e me pergunte o que eu quero ajustar primeiro.

== ESTRUTURA: O FUNIL DO PORTFÓLIO (exatamente nesta ordem, não mude e não acrescente seções) ==
A capa filtra, o meio convence, o fim fecha. A marca precisa chegar ao contato sem desvio.
1. CAPA: menu no topo com o meu nome e links que rolam suave até cada seção (Sobre mim, Destaques, Nichos, O que as marcas falam, Contato), virando menu enxuto no celular. No computador, a capa tem DUAS COLUNAS: o MEU NOME bem grande À ESQUERDA e a MINHA FOTO À DIREITA. Nunca capa centralizada. No celular empilha com o nome primeiro. Na coluna do nome: uma linha "UGC creator de [meus nichos]", uma frase curta do que eu faço pela marca, três números curtos (vídeos gravados, marcas atendidas, prazo de entrega) e dois botões: "Ver meus melhores vídeos" (rola até os destaques) e "Falar comigo" (rola até o contato).
2. SOBRE MIM: texto curto em primeira pessoa (quem eu sou, onde moro, minha rotina e por que as marcas do meu nicho combinam comigo), uma segunda foto minha no dia a dia, três diferenciais (estudo a dor do cliente da marca; roteiro meu, aprovado pela marca antes de gravar; edição pronta pra anúncio, com gancho forte e som tratado) e um selo "{formada} no Método Profissão do Futuro · {ela} da Rafa Chagas".
3. DESTAQUES: os meus 5 MELHORES vídeos (não os mais recentes), com o mais forte em evidência (maior ou no centro). Se o vídeo tiver resultado real (ex.: 116 vendas), ele ganha um selo com o resultado. Cada card mostra título curto, nicho e formato (ADS, review, unboxing, tutorial, nativo).
4. CONTEÚDO POR NICHOS: abas, uma por nicho, e ao clicar aparecem só os vídeos daquele nicho, sem recarregar a página. Cada nicho precisa de pelo menos 3 vídeos: se tiver menos, mostre um aviso discreto "mínimo 3 vídeos: com menos, tire o nicho". Se a página abrir com ?c=nome-do-nicho no link, ela já abre na aba desse nicho e rola até a seção (é o link que eu mando nas plataformas).
5. O QUE AS MARCAS FALAM: três depoimentos de marcas, com o nome da marca e o contexto, e embaixo a lista das marcas que eu já atendi. NUNCA invente depoimento: onde eu ainda não tiver, mostre o espaço vazio com a dica "cole aqui a frase ou o print real da marca".
6. CONTATO: um chamado curto ("bora trabalhar juntos/juntas?"), botão principal de WhatsApp que já abre com a mensagem pronta "Oi, [meu nome]! Vi seu portfólio e quero conversar sobre vídeos pra minha marca." (se eu não tiver WhatsApp, o botão vira e-mail com assunto pronto), botão do Instagram e quatro dúvidas curtas logo ali: onde posso usar o conteúdo, por quanto tempo, tem exclusividade, qual o prazo. Depois um rodapé simples com meu nome e "UGC creator · {ela} da Rafa Chagas".

== VÍDEOS ==
- Todo vídeo é vertical 9:16. Ao passar o mouse, o vídeo começa a tocar sem som dentro do card. Ao clicar, abre um player grande por cima da página, com som e controles, que fecha no X, clicando fora ou com Esc.
- Enquanto eu não colocar o link de um vídeo ou de uma foto, o espaço aparece listrado, com um ícone e uma dica curta do que colocar ali (ex.: na foto de capa "Retrato com rosto, luz natural e ambiente real. Sem selfie: a capa mostra o seu nível"; nos destaques "Os melhores na frente, não os mais recentes").

== DADOS FÁCEIS DE TROCAR ==
- Coloque TODOS os meus dados num objeto JavaScript chamado DADOS, no fim do arquivo, com comentários em português explicando cada campo: nome, instagram, whatsapp, email, nichosResumo, frase, provas (3 números), fotoCapa, fotoSobre, sobreTexto, diferenciais, destaques (5 vídeos com titulo, nicho, formato, video, capa e res), nichos (cada um com nome e lista de vídeos), elogios (texto, marca, detalhe), marcas e duvidas.
- A página inteira é montada a partir desse objeto, então eu só mexo nele pra trocar tudo.

== TAMANHO E LEITURA ==
- Tamanho contido, pra caber bem na tela sem parecer com zoom: títulos de seção até uns 44px, o nome da capa grande mas sem estourar, texto entre 14 e 16px e NADA abaixo de 12px.
- Contraste bom: texto claro só sobre fundo escuro e vice-versa.
- Respeite prefers-reduced-motion (sem animação pra quem pediu).
- No celular (até 520px): uma coluna, margens de 16px, sem rolagem lateral, destaques num carrossel que desliza pro lado.
"""

VISUAIS = {
"brilho-01-clara": """== IDENTIDADE VISUAL: BRILHO CLARA ==
Estética de SaaS moderno com cara de rede social, clara e brilhante.
- Fonte: Poppins (Google Fonts) em tudo, pesos 400 a 800. Títulos com espaçamento entre letras apertado (-3%).
- Cores: fundo off-white quente #F1F0EA e #F7F6F2, preto quente #141414, roxo elétrico #6B3BF8 (botão principal e destaques de texto), verde-limão #D7FF00 (só em blocos e números, NUNCA como texto em fundo claro), rosa #E84CA7 só como tempero, lavanda #EFEAFF nos fundos de ícone, cinzas quentes #55534E e #8D8B84 nos textos de apoio.
- Tudo arredondado: botões, chips e selos em pílula (999px), cards com 16 a 28px de canto.
- Capa: fundo com grade de pontinhos roxos discretos e estrelinhas ✦ roxas e rosa piscando. Selo em pílula com borda preta e fundo holográfico animado (degradê lavanda, rosa, limão e azul claro correndo devagar) escrito "✦ Brilho · formada pela Rafa Chagas". Nome com uma estrelinha roxa ✦ no fim. Os três números em pílulas brancas. Foto num quadro com borda branca de 6px, levemente girado, com dois adesivos: um limão com o primeiro número e um roxo "✦ Brilho / aluna do Método".
- Sobre mim: fundo #F7F6F2, diferenciais em cards brancos com ícone em quadradinho lavanda, e o selo do método num card com borda holográfica.
- Destaques: 5 cards de vídeo com o primeiro mais largo; selo de resultado em pílula limão.
- Nichos: uma fileira por nicho com título grande e os vídeos deslizando pro lado.
- O que as marcas falam: seção escura grafite #2A2928 com cards #3A3836, aspas e inicial da marca num quadradinho limão.
- Contato: "Seu produto merece um vídeo que brilha." com "um vídeo que brilha" em roxo, estrelinhas piscando, botão roxo e dúvidas em 4 cards brancos.
""",
"brilho-02-noite": """== IDENTIDADE VISUAL: BRILHO NOITE ==
Modo noite tipo "baile de brilho".
- Fonte: Poppins (Google Fonts), pesos 400 a 900, títulos bem pesados com letras apertadas.
- Cores: fundo noite #0D0A17 e #16112A, texto #F4F1FF, apoio #B8B2CC, roxo #6B3BF8, lilás #B9A4FF, limão #D7FF00, rosa #E84CA7 e #FF9AD5. Brilhos suaves de roxo e rosa no fundo.
- Efeito holográfico: um degradê furta-cor (lilás, rosa, amarelo claro, limão, azul claro) que corre devagar, usado no nome da capa (texto com o degradê dentro), nas palavras de destaque dos títulos, no botão principal e na aba selecionada.
- Fundo inteiro com PURPURINA: um canvas fixo atrás da página com pontinhos em branco, lilás, rosa, limão e azul que piscam e flutuam devagar; os maiores viram estrelinhas em cruz.
- Rastro de estrelinhas ✦ coloridas seguindo o mouse (só no computador).
- Capa em duas colunas: à esquerda selo com borda holográfica girando "✦ Brilho · formada pela Rafa Chagas", nome gigante holográfico com brilho em volta, "UGC Creator de...", frase e botões (holográfico e de vidro fosco). À direita, a foto numa moldura em ARCO (topo redondo) com borda furta-cor que gira, um selo circular com o texto "brilho ✦ ugc creator" girando em volta de uma estrela limão, e os três números em cartões de vidro fosco flutuando em volta da foto.
- Sobre mim: foto com borda holográfica girando ao lado de um cartão de vidro fosco (borda branca fina, fundo translúcido, desfoque).
- Destaques: o vídeo mais forte fica no CENTRO, maior, com brilho limão em volta. Ao passar o mouse, os cards inclinam em 3D e um reflexo de luz atravessa.
- Nichos: abas em pílula de vidro, a selecionada holográfica.
- O que as marcas falam: cartinhas levemente tortas com borda holográfica, que também inclinam no mouse.
- Contato: globo de discoteca 🪩 girando, título grande com "um vídeo que brilha" holográfico, dúvidas em cartões de vidro e um letreiro enorme no fim alternando o meu nome com "vídeo que brilha".
""",
"brilho-03-docinho": """== IDENTIDADE VISUAL: DOCINHO ==
Vibe de doceria fofa e caprichada.
- Fontes (Google Fonts): Fraunces nos títulos (serifa suave, peso 500), DM Sans no texto, Caveat pra anotações escritas à mão.
- Cores: creme #FDF6EE e papel #FFFBF6, vinho #7A1430 (texto e títulos), vermelho #D2283A, rosa #F9C9D6 e #F48FB1, lilás #C9C6FF, pêssego #F9A27C, linhas rosadas #F2D3D9.
- Fundo de papel quadriculado (linhas rosadas de 26px) na capa e no feedback.
- Menu rosa com BORDA ONDULADA embaixo (meias-luas), meu nome no centro como logo em serifa com uma estrelinha vermelha, links dos dois lados em caixa alta pequena.
- Capa em duas colunas: à esquerda "(UGC CREATOR · BRILHO DA RAFA CHAGAS)" em caixa alta pequena, nome grande em serifa vinho, "UGC creator de..." em itálico vermelho, frase, os três números em SELOS ONDULADOS (forma de flor/carimbo feita em SVG) em pêssego, vinho e rosa, botões lilás e branco, e uma seta desenhada à mão apontando pra foto. À direita, a foto numa POLAROID branca levemente girada, presa com duas fitas adesivas (vermelha e rosa translúcidas), um bilhete escrito à mão "me chama pra brilhar ✦" e uma etiqueta de papel "Vídeos feitos por: [meu nome]". Adesivos de batom, brilho, cereja e estrela balançando em volta (escondidos no celular).
- Sobre mim: faixa vermelha com uma FOLHA DE CADERNO creme por cima, com furinhos redondos no topo; foto em polaroid com fita; os três diferenciais numa tabelinha de 3 colunas com borda vinho, a primeira coluna com fundo vinho; selo do método numa pílula rosa.
- Destaques: metade da tela creme com o título "Meus melhores vídeos" e um botão vermelho "Ver conteúdo por nichos"; a outra metade com LISTRAS VERTICAIS rosa e branco e os 5 vídeos como polaroids tortinhas com fita e legenda escrita à mão. O mais forte é maior e, com resultado, ganha um selo ondulado vermelho.
- Uma faixa XADREZ vinho e rosa separando destaques de nichos.
- Nichos (nesta versão NÃO use abas, isto substitui as abas da estrutura): fundo lilás com a etiqueta rosa "Conteúdo por nichos", o título "Ache o vídeo do seu nicho" e atalhos em pílula com borda vinho que rolam até cada nicho. Embaixo, UMA PÁGINA POR NICHO: cada nicho é um cartão creme com borda toda ondulada, etiqueta "página 01", nome do nicho grande em serifa, a quantidade de vídeos escrita à mão e duas setas redondas vinho. Dentro, um CARROSSEL que mostra 4 vídeos por vez (2 no tablet, 1 e um pedaço no celular) em polaroids tortinhas com fita; as setas andam uma tela de vídeos e dá pra arrastar. Cabe quantos vídeos eu quiser por nicho (ideal 4 ou mais). O link com ?c=nicho rola direto até a página do nicho.
- O que as marcas falam: bilhetes de papel coloridos levemente tortos presos com fita rosa, frase em serifa e nome da marca escrito à mão.
- Contato: outra folha de caderno sobre listras rosa, título "Seu produto merece um vídeo que brilha ✦", dúvidas numa tabelinha 2x2 com borda vinho. Rodapé vinho com borda ondulada em cima e "feito com brilho ✦" escrito à mão.
""",
"brilho-04-it-girl": """== IDENTIDADE VISUAL: IT GIRL ==
Estética "it girl" de agência de conteúdo jovem.
- Fontes (Google Fonts): Instrument Serif nos títulos (serifa fina), Mrs Saint Delafield pra letra cursiva, DM Sans no texto e nas etiquetas em caixa alta espaçada.
- Cores: creme #FFFCF4, vinho #5E1A2F, rosa bebê #FBC8EE, azul lavanda #B9C9F2, limão #DDF06A, coral #F26B4A, tinta #2B1219.
- Topo: barra limão fina "✦ Agenda aberta pra novas marcas ✦" e menu rosa com o meu nome em letra cursiva como logo, links em serifa e botão limão com contorno "Falar comigo".
- Botões retangulares com contorno de 1,5px, fundo limão ou vazio, caixa alta espaçada, sombra dura no hover.
- Adesivos de emoji com borda branca grossa (raio, drinque, câmera, globo de discoteca, dado), balançando devagar.
- Capa em duas colunas: à esquerda o NOME ENORME em letra cursiva vinho, levemente inclinado, "UGC creator · Brilho da Rafa Chagas" em caixa alta, frase, três números em caixinhas rosa e os botões. À direita, uma CÂMERA DIGITAL prateada desenhada em CSS com a minha foto na tela, uma polaroid atrás, uma TIRINHA DE CABINE DE FOTO preta com 3 fotos em preto e branco, e um selo redondo coral girando com "brilho ✦ ugc creator".
- Faixa lilás com borda preta e meus formatos e nichos rolando em serifa: "UGC pra ADS / Unboxing / Review / ...".
- Sobre mim: fundo vinho com o título "Sou creator com um olho pra conteúdo e uma paixão por vender", com "olho" em cursiva rosa e "paixão" em cursiva limão. Abaixo, um cartão creme com BORDA ONDULADA em cima e embaixo, com a minha foto dentro de um CELULAR desenhado (girado, com ilha no topo) e uma etiqueta limão "eu mesma" em cursiva; do lado, uma ficha com linhas pontilhadas: "Prazer!" numa etiqueta rosa, meu nome em cursiva, quem eu sou, nichos em cursiva e diferenciais.
- Destaques: título "meus melhores vídeos" em cursiva grande; 5 cards coloridos com contorno preto (rosa, azul com cantos bem redondos, limão no centro e maior, azul, rosa), cada um com um adesivo de emoji em cima.
- Nichos (nesta versão NÃO use abas, isto substitui as abas da estrutura): cabeçalho centralizado com "escolha o seu" em cursiva coral, o título "Conteúdo por nichos" e atalhos em serifa com bolinha (○ vira ● no hover) que rolam até cada nicho. Embaixo, UMA PÁGINA POR NICHO: cada nicho é uma faixa de largura total com borda preta em cima, alternando fundo cinza claro #E9E6E1, rosa e azul lavanda, com etiqueta "página 01" de contorno preto, nome do nicho em serifa, a quantidade de vídeos em cursiva e duas setas quadradas limão com contorno. Dentro, um CARROSSEL que mostra 4 vídeos por vez (2 no tablet, 1 e um pedaço no celular) em polaroids brancas tortas com legenda em cursiva; as setas andam uma tela de vídeos e dá pra arrastar. Cabe quantos vídeos eu quiser por nicho (ideal 4 ou mais). O link com ?c=nicho rola direto até a página do nicho.
- O que as marcas falam: faixa vinho com as marcas rolando em serifa e um bloco coral com os depoimentos em CARROSSEL (setas e pontinhos), frase grande em serifa e nome da marca em cursiva.
- Contato: "bora trabalhar juntas?" em cursiva grande, botões e as dúvidas em 4 cards com contorno (rosa, azul, limão e branco). Rodapé rosa com meu nome em cursiva.
""",
"brilho-05-studio": """== IDENTIDADE VISUAL: STUDIO ==
Estética de estúdio criativo, editorial e descontraída.
- Fontes (Google Fonts): Instrument Serif em CAIXA ALTA e esticada na vertical (transform: scaleY(1.12)) nos títulos, Yellowtail pra palavras em cursiva, Patrick Hand SC pras etiquetas e botões, Josefin Sans no texto.
- Cores: verde-oliva #4A5E1A, limão pastel #D4EBA0, lilás #DCCDF6, azul #A9C6FF, creme #F8F6F0, preto #111, uva #4B1E4F.
- Menu: uma barra branca com borda preta por cima do fundo oliva, logo "PRIMEIRO ✦ SOBRENOME" em serifa e um botão em pílula limão "fale comigo".
- Botões retangulares lilás com borda preta e sombra dura de 3px.
- Capa verde-oliva em duas colunas: à esquerda um pombinho 🕊️ com "me chama!" em cursiva limão, a linha "A UGC CREATOR por trás de" (com "por trás de" em cursiva) em limão e o meu NOME grande em caixa alta branca; frase, dois botões lilás e os três números com um filete limão do lado. À direita, duas fotos sobrepostas e giradas: a da frente com moldura lilás grossa, a de trás com moldura limão. A capa termina num DIVISOR ONDULADO que entra no creme.
- Sobre mim: "PRAZER, [MEU NOME]" gigante centralizado, uma linha de apresentação em letra de mão; abaixo, a foto numa MOLDURA AZUL DE BORDA ONDULADA (tipo selo postal) com "que bom que você veio!" escrito na vertical em cursiva, uma seta rabiscada, o título "CONTEÚDO QUE PARECE conversa E VENDE COMO ANÚNCIO" com "conversa" em cursiva e a segunda linha com marca-texto limão, o texto justificado, os diferenciais e o selo do método.
- Faixa preta com texto em itálico serifado rolando: "agenda aberta ✿ vídeo que vende ✿ brilho da rafa ✿ ...".
- Destaques: fundo lilás, título "MEUS DESTAQUES (os melhores)" e os 5 vídeos LADO A LADO numa fileira, alinhados embaixo, com o primeiro mais largo. Cada vídeo fica num cartão branco com borda preta e sombra dura preta de 4px (o primeiro com fundo limão), e embaixo do vídeo vem o número em serifa (01 a 05), um rótulo em cursiva ("o mais forte", "queridinho", "viralizou", "favorito", "bônus") e o nicho · formato em letra de mão. Sem linha do tempo. No celular vira um carrossel que desliza pro lado.
- Nichos: título em caixa alta serifada, abas retangulares com borda preta (a selecionada lilás com sombra), vídeos em grade.
- O que as marcas falam: fundo oliva, título com "falam" em cursiva limão, depoimentos em cartões creme com borda preta e sombra limão, o do meio levemente girado.
- Contato: "BORA TRABALHAR juntas?" grande, botões limão e branco, dúvidas em 4 caixas com borda preta alternando lilás e branco. Rodapé oliva com meu nome em cursiva limão.
""",
"brilho-06-colagem": """== IDENTIDADE VISUAL: COLAGEM ==
Colagem fofa de blocos arredondados, estilo perfil de app.
- Fontes (Google Fonts): Fredoka nos títulos (arredondada, 600/700), Quicksand no texto (500 a 700), Gluten pra pequenos avisos.
- Cores: creme #F8F3EC, rosa #F48A9A e #FBC3CB, azul #8FAEE8, azul-acinzentado #E3E9F3, limão #D6E06A e #E8EE9E, branco, texto azulado #5A6B8C e #3F4F70.
- Tudo em blocos com cantos bem redondos (30 a 40px), etiquetas em pílula com borda azul e fundo azul-acinzentado, textos pequenos em caixa alta bem espaçada.
- Menu: pílula branca flutuante com o meu nome em rosa, links em caixa alta pequena e botão rosa "Falar comigo 💬".
- Capa em duas colunas: à esquerda um balão branco em pílula "UGC CREATOR · BRILHO DA RAFA CHAGAS / agenda aberta pra marcas ✦", o NOME grande em rosa (minúsculas), um card azul de perfil com "oi, que bom que você veio!" e a frase sublinhada, etiquetas em pílula com os nichos e formatos, botão limão e botão branco. Rabisquinhos limão (elipse e bolinha). À direita, uma TIRA DE FILME rosa (furos brancos em cima) com 3 fotos em quadros arredondados (capa, bastidor, com produto) e os três números em pílulas brancas presas no canto da tira.
- Sobre mim: card azul grande com a foto à esquerda e, à direita, "SOBRE MIM", meu nome, o texto, a etiqueta "informação pessoal", meus nichos e o selo do método numa pílula limão. Do lado, um painel azul "meus diferenciais" com os 3 diferenciais em BOLINHAS DE STORY (círculo branco com emoji e anel rosa). Uma seta curva limão grossa saindo do card.
- Destaques: painel branco grande com "🎞️ SETOR DE VÍDEOS EM DESTAQUE" em caixa alta limão escuro e "meus melhores vídeos" em rosa; os 5 vídeos em quadros arredondados lado a lado, o primeiro maior.
- Nichos: um bloco rosa com cantinho inferior esquerdo bem arredondado ("CONTEÚDO POR NICHOS", "escolha o nicho da sua marca" e os nichos em pílulas brancas translúcidas, a selecionada branca), ao lado de uma grade de vídeos num bloco rosa claro.
- O que as marcas falam: os depoimentos viram CARDS DE NOTIFICAÇÃO azul-acinzentados ("🔔 NOTIFICAÇÃO", frase em azul, marca em rosa), ao lado de um bloco limão com "o que as marcas falam" em branco, a lista de marcas em caixa alta e um botãozinho de música ♫.
- Contato: uma barra limão longa em pílula "CONTATO · bora conversar?" com o miolo "seu produto merece um vídeo que brilha ✦", um bloco rosa "me chama!" com os botões e as dúvidas em cards brancos. Rodapé com o meu primeiro número em rosa e pílulas azul e rosa.
""",
"brilho-07-basico": """== IDENTIDADE VISUAL: BÁSICO ==
Limpo, direto e profissional. Sem efeitos, sem textura, sem animação de enfeite: o que aparece são os vídeos.
- Fonte: Poppins (Google Fonts) em tudo, pesos 400 a 700; títulos com letras apertadas (-3% a -4,5%).
- Cores: fundo branco, seções alternadas em cinza muito claro #F6F6F4, linhas #E2E2DD, títulos #141414, texto #2B2B2B, apoio #6B6B66. Um único toque de cor: roxo #6B3BF8 (com fundo lavanda #F0EBFF) só nas etiquetas pequenas, no destaque mais forte e no selo do método.
- Cantos arredondados: fotos 24px, vídeos 16px, cards 20px, botões e etiquetas em pílula.
- Botões: principal preto com texto branco; secundário branco com borda fina cinza.
- Cada seção começa com uma etiqueta pequena em pílula lavanda com texto roxo (ex.: "Sobre mim", "Destaques") e o título em Poppins 600.
- Menu branco fixo com borda fina embaixo: meu nome com um ponto roxo no fim, links em cinza e botão preto "Falar comigo".
- Capa em duas colunas: à esquerda a etiqueta "✦ UGC creator · Brilho da Rafa Chagas", o NOME grande em Poppins 700, "UGC creator de [nichos]" em cinza, a frase, os três números lado a lado separados por linhas verticais finas e os dois botões. À direita, a foto com cantos arredondados.
- Sobre mim: fundo cinza claro, foto arredondada à esquerda e, à direita, o título "Prazer, eu sou a [nome].", o texto, os 3 diferenciais com um check branco dentro de uma bolinha preta e o selo em pílula branca "✦ Formada no Método Profissão do Futuro · aluna da Rafa Chagas" (o nome do método em roxo).
- Destaques: título "Meus melhores vídeos" e os 5 vídeos em fileira de mesmo tamanho; o mais forte tem um contorno roxo e a legenda "✦ o mais forte". Embaixo de cada vídeo, título e formato.
- Nichos (nesta versão NÃO use abas, isto substitui as abas da estrutura): título "Ache o vídeo do seu nicho" com atalhos em pílula de borda fina que rolam até cada nicho. UMA PÁGINA POR NICHO: nome do nicho, quantidade de vídeos em cinza, linha fina embaixo e duas setas redondas de borda fina; embaixo um CARROSSEL com 4 vídeos por vez (2 no tablet, 1 e um pedaço no celular) que anda com as setas e dá pra arrastar. Se tiver menos de 3 vídeos, uma etiqueta lavanda "mínimo 3 vídeos". O link com ?c=nicho rola até a página do nicho.
- O que as marcas falam: fundo cinza claro, 3 cards brancos com borda fina (o vazio com borda tracejada) e as marcas atendidas em pílulas brancas.
- Contato: centralizado, "Bora fazer o vídeo da sua marca?", o texto, botão preto e botão de borda, e as 4 dúvidas em colunas com linha fina em cima. Rodapé simples com meu nome.
""",
"brilho-08-street": """== IDENTIDADE VISUAL: STREET ==
Estética streetwear editorial, limpa e forte.
- Fontes (Google Fonts): Anton em CAIXA ALTA nos títulos (condensada alta), Herr Von Muellerhoff pra uma assinatura cursiva, Inter no texto e nas etiquetas em caixa alta bem espaçada.
- Cores: off-white #F4F1EA, branco, azul cobalto #1430E0, preto #111, cinza #6B6B6B, linhas #D9D5CC.
- Botões retangulares em caixa alta espaçada: preto, contorno preto e azul.
- Topo: barra preta fina e menu off-white com o meu primeiro nome no centro em Anton, links dos dois lados.
- Capa em duas colunas: atrás de tudo, o meu nome GIGANTE só no contorno, em cinza bem claro. À esquerda, "UGC CREATOR / VÍDEO QUE VENDE / PRA SUA MARCA" em caixa alta espaçada com um tracinho embaixo, o NOME enorme em Anton (primeiro nome em azul cobalto, sobrenome em preto), a minha assinatura em cursiva preta inclinada por cima, a frase e os botões. À direita, a minha foto em PRETO E BRANCO, alta, encostada embaixo.
- Faixas finas com borda preta em cima e embaixo, com os nichos e formatos rolando em azul: "/ TECH / FITNESS / UGC PRA ADS /". Uma versão preta com "/ CONTEÚDO POR NICHOS" rolando antes dos nichos.
- Sobre mim: dois painéis lado a lado. Um cinza claro com "SOBRE MIM" em azul, o texto, os três números grandes em azul com rótulo em caixa alta e a foto com cantos arredondados. Outro AZUL com "EU CRIO" em branco e os diferenciais em pílulas translúcidas ligadas por uma linha vertical (tipo diagrama), e o selo "✦ Formado no Método Profissão do Futuro · aluno da Rafa Chagas" com contorno branco.
- Destaques: fundo azul cobalto com uma GRADE de cards off-white com borda preta, cada um com rótulo em Anton "/ O MAIS FORTE", "/ DESTAQUE 02"..., o vídeo e o nicho · formato; no fim um painel vertical com o meu primeiro nome em Anton azul escrito na vertical e "ugc" em cursiva.
- Nichos: título "CONTEÚDO POR NICHOS" com "prova" em cursiva azul, abas retas em bloco com borda preta (a selecionada preta), vídeos em grade com legenda "/ NICHO" e número.
- O que as marcas falam: fundo preto, título em Anton branco com "feedback" em cursiva azul claro, depoimentos em 3 colunas separadas por linhas finas e as marcas em Anton cinza.
- Contato: "BORA TRABALHAR?" enorme em azul com "contato" em cursiva por cima, botões e as dúvidas em lista com linha preta em cima de cada uma.
""",
"brilho-09-papel": """== IDENTIDADE VISUAL: PAPEL RASGADO ==
Estética de portfólio de designer: papel, recorte e anotação à mão.
- Fontes (Google Fonts): Archivo Black em CAIXA ALTA nos títulos (extra pesada), Caveat pras anotações à mão, Inter no texto.
- Cores: papel #EFEFEC com linhas #DADAD5, preto #121212, vermelho #E5322D, branco, cinza #5F5F5A.
- Fundo inteiro de PAPEL QUADRICULADO (linhas de 24px) com manchas claras e escuras bem suaves, como papel amassado.
- Botões retangulares em Archivo Black: preto, branco com borda e vermelho; no hover, sombra dura vermelha.
- Capa em duas colunas: à esquerda, em cima, "UGC CREATOR / [MEUS NICHOS]" e o ano; o NOME ENORME em Archivo Black (cada palavra numa linha); uma ANOTAÇÃO À MÃO com setinha desenhada: "esse sou eu, prazer!"; os símbolos ✸✦♣; frase e botões. À direita, a minha foto dentro de uma CAIXA DE SELEÇÃO VERMELHA estilo Figma (borda fina vermelha com quadradinhos nos cantos e no meio) e uma etiqueta vermelha "foto_capa.jpg" embaixo.
- Sobre mim: "OLÁ" gigante, "Prazer, eu sou o [meu nome].", o texto e os três números; do lado, "NICHOS" com cada nicho como ícone em quadradinho preto arredondado (emoji branco) com o nome embaixo, e "DIFERENCIAIS" em formato de currículo (número vermelho, título e descrição), incluindo o selo do método.
- Uma FAIXA PRETA DE PAPEL RASGADO (bordas irregulares em cima e embaixo, feitas com clip-path) com "UGC CREATOR" em branco gigante, inclinado, e a minha segunda foto no meio recortada em arco com CONTORNO VERMELHO grosso.
- Destaques: título "DESTAQUES" com "os melhores vêm primeiro ↓" à mão em vermelho; os 5 vídeos como POLAROIDS brancas tortas presas com CLIPE DE PAPEL (desenhado em CSS) e legenda à mão; o primeiro maior.
- Nichos: "CONTEÚDO POR NICHOS", abas que parecem etiquetas de papel levemente tortas (a selecionada preta), vídeos em polaroids com clipe e um aviso à mão em vermelho quando o nicho tem menos de 3 vídeos.
- O que as marcas falam: bilhetes brancos com clipe, frase em vermelho, marca em Archivo Black, e as marcas atendidas em Archivo Black cinza sobre uma linha preta.
- Contato: outra faixa preta com borda rasgada em cima, "BORA TRABALHAR?" enorme em branco com o ponto de interrogação vermelho, botões e as dúvidas em 4 colunas com linha branca em cima.
""",
"brilho-10-marca": """== IDENTIDADE VISUAL: MARCA ==
Estética de brand designer: forte, quente e com rabiscos.
- Fontes (Google Fonts): Big Shoulders Display 900 em CAIXA ALTA pro nome e logos (pesada condensada), Fraunces nos títulos (serifa), Caveat pras palavras à mão, Inter no texto.
- Cores: creme #F6EEDC e #FBF6EA, amarelo #F2B416, laranja-vermelho #E5482A, preto #151515, cinza #5D574C.
- Botões em pílula: amarelo, preto e com contorno, em caixa alta com seta →.
- Menu creme com o meu nome em Big Shoulders e uma estrela ✸ vermelha, links em caixa alta e botão amarelo "Bora trabalhar →".
- Capa em duas colunas: à esquerda "UGC CREATOR" em vermelho pequeno, o NOME ENORME em Big Shoulders (cada palavra numa linha), uma PINCELADA vermelha embaixo, a frase, botões e um SELO REDONDO vermelho girando com "estratégia ✸ roteiro ✸ edição". À direita, a minha foto sobre um BORRÃO AMARELO irregular (forma de pincelada), com um OLHO vermelho desenhado com cílios, um risco de pincel preto e uma grade de pontinhos pretos.
- Sobre mim: duas metades. À esquerda a foto de mim trabalhando, com uma faixa vermelha na lateral e uma coroa rabiscada. À direita, "SOBRE MIM" em vermelho, o título "Conteúdo com estratégia. Vídeo com alma." (com "alma." à mão em vermelho e sublinhado rabiscado), o texto, minha assinatura à mão e um círculo amarelo girado "aluno da Rafa Chagas · formado no método ✸". Logo abaixo, uma FAIXA PRETA com "O que eu faço pela sua marca" e os 3 diferenciais em colunas separadas por linhas (ícone, título em serifa, descrição) e os três números em amarelo.
- Destaques: à esquerda "DESTAQUES", "Meus melhores vídeos" em serifa, um rabisco ondulado vermelho e botão amarelo; à direita os 5 vídeos em molduras grossas alternando vermelho, preto e amarelo, com legenda em caixa alta e seta →; o primeiro maior.
- Nichos: "CONTEÚDO POR NICHOS" em vermelho, título "Ache o vídeo do seu nicho" com "seu nicho" à mão sublinhado, abas em pílula com contorno (a selecionada amarela).
- O que as marcas falam: faixa laranja-vermelha com "O que as marcas falam" em serifa branca e aspas grandes, depoimentos em 3 colunas separadas por linhas, nome da marca em amarelo, marcas atendidas em Big Shoulders e um selo branco girando "feedback ✸ real".
- Contato: as dúvidas em 4 colunas com linha preta em cima e, depois, uma FAIXA AMARELA com "Bora fazer um vídeo que vende?" (sublinhado rabiscado), botão preto e uma EXPLOSÃO vermelha desenhada. Rodapé preto com o meu nome e ✸ vermelha.
""",
}


# selo "Brilho · aluna/aluno Rafa Chagas" que vai na capa, junto da foto
SELOS = {
"brilho-01-clara":   'redondo preto (120px), girando devagar, com "BRILHO ✦ ALUNA RAFA CHAGAS ✦" em limão #D7FF00 escrito em volta e uma bolinha roxa #6B3BF8 com estrela limão no meio. Fica no canto de baixo à direita da foto.',
"brilho-03-docinho": 'selo ONDULADO (forma de carimbo de flor feita em SVG) vinho #7A1430, girando bem devagar, com "BRILHO ♥ ALUNA RAFA CHAGAS ♥" em rosa #F9C9D6 em volta e uma cereja 🍒 no meio. Fica no lado esquerdo da polaroid.',
"brilho-04-it-girl": 'o selo redondo coral #F26B4A com borda preta que gira na capa traz escrito em volta "BRILHO ✦ ALUNA RAFA CHAGAS ✦" e um ✨ no meio.',
"brilho-05-studio":  'carimbo redondo lilás #DCCDF6 com borda preta fina, girando devagar, com "BRILHO ✿ ALUNA RAFA CHAGAS ✿" em letra de mão preta em volta e um "b" em cursiva Yellowtail verde-oliva no meio. Fica no canto de baixo à esquerda da foto da frente.',
"brilho-06-colagem": 'bolinha de STORY: círculo branco com anel grosso em degradê rosa, azul e limão, girando devagar, com "BRILHO ♡ ALUNA RAFA CHAGAS ♡" em azul #8FAEE8 em volta e uma bolinha rosa com estrela no meio. Fica no lado esquerdo da tira de filme.',
"brilho-07-basico":  'redondo branco discreto com borda fina #E2E2DD, girando devagar, com "BRILHO · ALUNA RAFA CHAGAS ·" em preto em volta e uma bolinha lavanda com estrela roxa no meio. Fica no canto de baixo à esquerda da foto.',
"brilho-08-street":  'ETIQUETA DE ROUPA azul cobalto #1430E0, levemente girada, com costura tracejada branca por dentro, um furinho no topo, "BRILHO" em Anton branca grande e "ALUNO · RAFA CHAGAS" pequeno embaixo. Fica no canto de cima à esquerda da foto.',
"brilho-09-papel":   'CARIMBO DE BORRACHA vermelho #E5322D, torto (-14°), com dois círculos, "BRILHO ✸ ALUNO RAFA CHAGAS ✸" em Archivo Black em volta e ✸ no meio, meio transparente como tinta de carimbo. Fica carimbado no canto de cima à esquerda da foto.',
"brilho-10-marca":   'o selo redondo vermelho que gira ao lado do nome traz escrito em volta "BRILHO ✸ ALUNO RAFA CHAGAS ✸" e uma ✸ vermelha no meio.',
}

FIM = """
Depois da identidade visual, siga à risca a ESTRUTURA DO FUNIL acima: o visual muda, a ordem das seções e as regras não mudam."""

modelos_js = [dict(pasta=p, nome=n, emoji=e, familia=f, genero=g) for p, n, e, f, g in MODELOS]
prompts = {p: base(n, g) + "\n" + VISUAIS[p].strip() + "\n- SELO BRILHO NA CAPA (obrigatório, mostra que eu sou da turma da Rafa): " + SELOS[p] + "\n" + FIM for p, n, e, f, g in MODELOS}

with open("modelos.js", "w", encoding="utf-8") as f:
    f.write("window.MODELOS = " + json.dumps(modelos_js, ensure_ascii=False, indent=1) + ";\n")
with open("prompts.js", "w", encoding="utf-8") as f:
    f.write("window.PROMPTS = " + json.dumps(prompts, ensure_ascii=False, indent=1) + ";\n")
print("ok:", len(prompts), "prompts,", sum(len(v) for v in prompts.values()), "caracteres")
