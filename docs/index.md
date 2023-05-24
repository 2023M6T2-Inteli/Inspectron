<table>
<tr>
<td>
<a href= "https://www2.gerdau.com.br/"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Gerdau_logo_%282011%29.svg/1200px-Gerdau_logo_%282011%29.svg.png" alt="Gerdau" border="0" width="70%"></a>
</td>
<td><a href= "https://www.inteli.edu.br/"><img src="https://www.inteli.edu.br/wp-content/uploads/2021/08/20172028/marca_1-2.png" alt="Inteli - Instituto de Tecnologia e Liderança" border="0" width="30%"></a>
</td>
</tr>
</table>

# Sumário

- [1 - Entendimento de negócio](#1-entendimento-de-negócio)
  - [1.1 - Canvas Proposta de Valor](#11-canvas-proposta-de-valor)
  - [1.2 - Matriz de Riscos](#12-matriz-de-riscos)
  - [1.3 - Oceano Azul](#13-oceano-azul)
  - [1.4 - Análise financeira](#14-análise-financeira)
- [2 - Entendimento do metadesign](#2-entendimento-do-metadesign)
  - [2.1 - Fatores mercadológicos](#21-fatores-mercadológicos)
  - [2.2 - Sistema produto/design](#22-sistema-produto/design)
  - [2.3 - Sustentabilidade ambiental](#23-sustentabilidade-ambiental)
  - [2.4 - Influências socioculturais](#24-influências-socioculturais)
  - [2.5 - Tipológico-formais e ergonômicos](#25-tipológico-formais-e-ergonômicos)
  - [2.6 - Tecnologia produtiva e materiais empregados](#26-tecnologia-produtiva-e-materiais-empregados)
- [3 - Descrição da arquitetura do sistema](#3-descrição-da-arquitetura-do-sistema)
- [4 - Sistema de locomoção e otimização de rota](#4-sistema-de-locomoção-e-otimização-de-rota)
- [5 - Interface de usuário](#5-interface-de-usuário)
- [6 - Sistema de visão computacional](#6-sistema-de-visão-computacional)
- [7 - Sistemas de segurança](#7-sistemas-de-segurança)
- [8 - Backend](#8-backend)
- [9 - Integração de sistemas](#9-integração-de-sistemas)
- [10 - Validação da eficácia do sistema](#10-validação-da-eficácia-do-sistema)
- [11 - Referências](#11-referências)

---

# 1. Entendimento de negócio.

## 1.1. Canvas Proposta de Valor

O Canvas de Proposta de Valor é uma forma de ajudar criadores de solução a focar naquilo que é importante para o consumidor da solução, priorizando aquilo que gera valor ao produto final. A principal vantagem da proposta de valor apresentada é aumentar a segurança dos colaboradores da Gerdau, melhorar as vistorias realizadas e monitorar em tempo real.

<p align="center"><img src="https://user-images.githubusercontent.com/99221221/235381624-3a66133d-8ee4-43b3-a694-97aa20c38639.png" width=100%></img></p>

## 1.2. Matriz de Riscos

Matriz de riscos é uma ferramenta utilizada para identificar, avaliar e priorizar os riscos que podem afetar um projeto, uma empresa ou uma organização. Na matriz os riscos podem ser classificados como baixo, médio ou alto em termos de probabilidade e impacto. A partir da análise é possível identificar quais riscos devem receber mais atenção e quais medidas devem ser tomadas para mitigá-los ou eliminá-los.

<p align="center"><img src="https://user-images.githubusercontent.com/99221221/235231848-dffbb591-547e-476b-bc44-37f2dcd9c1d0.png" width=80%></img></p>

### Ameaças e plano de mitigação

1. Queima de componentes eletrônicos

Para evitar a queima de componentes eletrônicos, é crucial observar e seguir as boas práticas da eletrônica. O primeiro passo é fazer as ligações em um simulador para evitar desperdícios. Em seguida, faz-se a montagem de acordo com a simulação e, antes de ligar o sistema, realiza-se o teste de continuidade. Dessa forma, as chances de queimar qualquer componente são praticamente nulas.

2. Custos elevados para aquisição e manutenção dos equipamentos tecnológicos

Para amenizar os gastos imediatos do projeto, é possível que a Gerdau solicite financiamento a investidores ou instituições financeiras. Dessa forma, a empresa compartilha os potenciais riscos com aqueles que fornecerão o financiamento, de modo a diminuir, consequentemente, a exposição a condições financeiras perigosas.

3. O dispositivo ser frágil para determinados ambientes

Para capacitar o robô a operar em ambientes com condições adversas, pode-se adicionar módulos externos que permitam a operação com segurança. Por exemplo, em espaços confinados de alta temperatura, como fornalhas, fornos ou caldeiras, é possível utilizar um escudo térmico no robô.

4. Divergência nas informações captadas pelos sensores e o estado atual

Para garantir a qualidade das informações dos sensores, deve-se escolher sensores precisos e calibrá-los regularmente. Além disso, é possível utilizar sensores redundantes, para comparar as informações captadas por ele e identificar possíveis incongruências.

### Oportunidades

1. Maior conforto para empresa, ao não arriscar a vida de um funcionário (Automação de uma atividade perigosa)
2. Aumento da precisão na inspeção dos espaços confinados
3. Manutenção preventiva dos locais confinados com maior facilidade
4. Robô realizar com praticidade sua função em locais impossíveis de locomoção humana
5. Demonstrar o compromisso da Gerdau com a segurança de seus colaboradores.
6. Redução dos custos com equipamentos de proteção individual e pessoal treinado para exercer atividades em locais confinados
7. Adaptação dessa tecnologia para outros cenários, desastres naturais, etc

## 1.3. Oceano Azul

O conceito de Oceano Azul é uma abordagem estratégica que pode ajudar a criar novos mercados e a alcançar o sucesso em meio à concorrência acirrada de uma solução. Para realizar a análise foi feita a comparação entre o método atual utilizada pela parceira e a solução que está sendo desenvolvida.

<p align="center"><img src="https://user-images.githubusercontent.com/99221221/235233152-7ea9aae8-9fae-4492-af04-e381366007a7.png" width=60%></img></p>

**Variáveis análisadas:**

1. Custo
2. Qualidade
3. Tecnologia
4. Conforto
5. Intervenção humana
6. Precisão da análise
7. Segurança
8. Praticidade

### Aumentar

- A Qualidade da inspeção irá aumentar pois o robô irá entrar dentro do espaço confinado, diferente do processo atual que é apenas superficial;
- A precisão da análise será elevada pois a inspeção será no interior do espaço que necessita de manutenção;
- Irá melhorar a praticidade pois os colaboradores da Gerdau terão apenas que controlar a dashboard de dados coletador pelo robô;

### Diminuir

- De acordo com dados da análise financeira é perceptivel que o custo da solução irá baratear o processo depois de um certo periodo;
- Realiza a inspeção e coleta de dados em espaços confinados de maneira mais rápida, reduzindo o tempo necessário para realizar essas atividades

### Criar

- Tecnologia será criada pois o processo atual é feito de forma manual;
- Irá criar segurança, uma vez que, os colaboradores não serão expostos ao risco;
- Monitoramento remoto em tempo real, permitindo a análise de dados coletados e a tomada de decisões de forma mais rápida e eficiente.
- Flexibilidade, pois a tecnologia é adaptável às necessidades dos clientes, permitindo a personalização dos recursos para cada cenário.

### Eliminar

- A intervenção humana no processo de vistoria será eliminada pois o robô fara o trabalho de entrada no espaço confinado;
- Erros humanos durante a inspeção e coleta de dados em espaços confinados.

## 1.4. Análise financeira

A análise financeira informa o quanto o parceiro tem projetado para investir no projeto e quais são as projeções de custos e de receitas que o parceiro projeta ter relacionadas ao projeto. Ressalta-se que é uma estimativa feita baseada nos materiais disposibilizados para realizar o MVP, para um processo de real implementação é necessário reavaliar os dispositivos de hardware utilizados.

<p align="center"><img src="https://user-images.githubusercontent.com/99221221/235224067-2c36aa92-0bc3-4073-a9b2-650df9a09703.png" width=120%></img></p>

** ICMS é a sigla para Imposto sobre Circulação de Mercadorias e Prestação de Serviços de Transporte Interestadual e Intermunicipal e de Comunicação. Regulamentado pela Lei Kandir (Lei complementar 87/1996), é um tributo estadual e seus valores são definidos pelos estados e Distrito Federal.

Ao realizar a análise financeira da solução, constatou-se que o custo total de compra e implementação é de **R$ 10.030,00 no primeiro ano**. Após a compra da solução, os gastos necessários seriam apenas com manutenção e treinamento de novos funcionários, conforme a demanda. Assim, **o retorno sobre o investimento (ROI) seria alcançado em um ano**.

Considerando o salário anual de um funcionário que realiza inspeção em espaço confinado é de R$ 71.500,00 (13 x R$ 5.500,00 - Página da Gerdau no Glassdoor), com esse valor, seria possível implementar 7 robôs e realocar os colaboradores para outras atividades, mediante o treinamento necessário para controlar a solução.

# 2. Entendimento do metadesign

## 2.1. Fatores mercadológicos

### Produto, orientação de mercado e precificação

Um AGV é um tipo de robô autônomo que segue uma trajetória pré-definida por meio de software e utiliza sensores, como câmeras e lasers, para navegar no ambiente e evitar obstáculos. Esses robôs são altamente precisos e seguros, permitindo que se movimentem por espaços apertados com habilidade superior à das mãos humanas. Por essas razões, eles são amplamente utilizados para transportar materiais em ambientes industriais ou logísticos. Além de seu uso para transporte, os AGVs podem ser equipados com sensores e câmeras para realizar a inspeção de áreas de difícil acesso ou perigosas para os humanos. Isso garante mais segurança e precisão na realização da manutenção preventiva.

Durante uma entrevista com um parceiro, foi levantada a questão de que a vistoria de locais confinados é feita apenas pelo lado de fora, o que não permite entender verdadeiramente a condição do espaço. Apesar dos riscos envolvidos, tarefas como limpeza, manutenção e inspeção precisam ser realizadas em espaços confinados. No entanto, devido à dificuldade de acesso, essas atividades podem resultar em várias situações perigosas.

Felizmente, a indústria 4.0 está trazendo soluções para esse problema através da automatização desses processos perigosos. Essa tecnologia aumenta a segurança dos trabalhadores e otimiza os processos, tornando as atividades em espaços confinados mais eficientes e menos perigosas. O projeto criado se orienta para o mercado de segurança e otimização de processos na indústria 4.0. Tal informação pode ser aferida pois o protótipo desenvolvido utiliza recursos avançados, como câmeras, lasers, sensores de proximidade, sensores de gases e outros, para automatizar trabalhos considerados perigosos para os humanos. Além disso, fornece dados em tempo real para uma melhor análise das informações obtidas.

No que se refere à precificação do produto, é importante destacar que os AGVs apresentam uma ampla variação de preços ("How much does an AGV cost?", [s.d.], que podem variar dependendo do tipo de veículo, tamanho, sensores instalados, função e outras possíveis variações. Além disso, é preciso levar em consideração os custos envolvidos na implantação do AGV, tais como o treinamento dos funcionários, a instalação de trilhos ou outras referências de movimento e a integração com outros sistemas de softwares. Para precificar o MVP, será utilizado o TurtleBot3 com os sensores necessários e os investimentos necessários para implementar a solução na empresa parceira.

### Cenário do mercado

Com as mudanças globais em constante evolução, as expectativas dos consumidores e investidores estão se tornando cada vez mais exigentes. Nesse contexto, a Indústria 4.0 surge como um grande integrador de toda a cadeia da indústria, levantando debates importantes sobre o seu desenvolvimento ("Indústria 4.0 no Brasil: cenário e perspectivas", [s.d.]). No Brasil, a implementação da Indústria 4.0 apresenta desafios que vão desde o investimento em equipamentos que incorporem essas tecnologias até a adaptação de processos e formas de relacionamento entre as empresas ao longo da cadeia produtiva, além da criação de novas especialidades e desenvolvimento de competências ("Indústria 4.0", [s.d]).

No entanto, de acordo com a McKinsey, estima-se que até 2025, os processos relacionados à Indústria 4.0 poderão reduzir os custos de manutenção de equipamentos em 10% a 40%, reduzir o consumo de energia entre 10% e 20%, e aumentar a eficiência do trabalho em 10% a 25%. Com isso, é possível concluir que, apesar dos desafios de implementação, a Indústria 4.0 oferece grandes benefícios.

Em ambientes confinados a utilização de robôs tem se mostrado uma alternativa favorável para facilitar vistórias em ambientes restritos e perigosos para seres humanos. De acordo com um relatório da BCC Research, o mercado global de veículos guiados automatizados (AGVs) deve atingir US$ 4 bilhões até 2025. Isso indica que os AGVs estão sendo amplamente adotados pelas indústrias para aumentar a eficiência de suas operações, uma vez que essa tecnologia oferece diversos benefícios, como o diminuição da exposição de trabalhadores a tarefas perigodas e otimização na coleta de dados.

### Visão do projeto proposto

O setor siderúrgico, onde a Gerdau atua, envolve a manipulação de equipamentos e materiais pesados, altas temperaturas e exposição dos trabalhadores a materiais e gases químicos tóxicos, o que o torna um setor de alto risco em termos de segurança do trabalho.

A segurança dos colaboradores é um dos valores primordiais da Gerdau ("Sobre nós", [s.d.]) e, como tal, a empresa busca continuamente formas de garantir maior segurança em suas operações. Neste contexto, um dos principais riscos que causa grande preocupação na Gerdau são os espaços confinados.

O trabalho em espaços confinados é considerado uma das modalidades mais perigosas, já que os colaboradores estão expostos a diversos riscos e o ambiente favorece a ocorrência de acidentes graves e frequentes ("CONECT, E. O que preciso saber sobre trabalho em espaço confinado?", [s.d.]). Em uma conversa com o parceiro, foi constatado que o processo atual é realizado externamente ao espaço e antes da manutenção, o que torna impossível ter uma visão real da situação dentro do espaço confinado.

Nesse cenário, o projeto apresenta uma grande importância para a Gerdau pois tem ação direta em um valor apontado como ideal pela empresa. Ao implementar inspeções sem necessidade de humanos atuando inseguramente dentro dos espaços para vistorias preventivas de manutenção, será possível elevar ainda mais a segurança no trabalho, padrões de qualidade em vistorias e proporcionar maior satisfação e segurança aos colaboradores.

## 2.2. Sistema produto/design

### Missão do projeto

O setor siderúrgico é conhecido por envolver o manuseio de equipamentos e materiais pesados, altas temperaturas e exposição a materiais químicos tóxicos, tornando-o de alto risco em termos de segurança do trabalho. A Gerdau, valorizando a segurança de seus colaboradores ("Sobre nós", [s.d.]), traça objetivos para tornar o desenvolvimento de segurança mais palpável e busca alcançar o objetivo de acidente zero por meio da adoção de rigorosos padrões de operação e manutenção, além de seguir normas nacionais e internacionais de segurança.

A empresa realizou um mapeamento das possíveis ameaças à segurança e identificou que os espaços confinados são um dos riscos mais relevantes em suas operações. Esses espaços não foram projetados para ocupação humana contínua, e a falta de uma rotina de inspeção no interior desses locais pode sujeitar a empresa e seus trabalhadores a eventualidades prejudiciais.

Para solucionar esse problema e estar em linha com sua política de segurança, a Gerdau pretende realizar inspeções em espaços confinados por meio de um AGV (Automated Guided Vehicle), um veículo guiado automaticamente que permitirá que a empresa tenha acesso a informações e imagens do ambiente em tempo real através de um software de integração. Dessa forma, a empresa poderá identificar possíveis vazamentos, problemas na infraestrutura e outros riscos relacionados a espaços confinados e preparar-se corretamente para realizar intervenções seguras.

### Unidade formal entre o design do produto, as formas de divulgação e venda

A solução desenvolvida para a Gerdau é personalizada e não será comercializada em larga escala. Nesse sentido, a abordagem de divulgação e venda deve ser adaptada à visão interna da empresa. É importante manter a coerência em todos os aspectos do projeto, desde a apresentação visual até os requisitos técnicos do produto, para manter uma unidade formal entre o design, a forma de divulgação e a venda. Esses elementos têm um grande impacto na imagem do projeto e da empresa.

Para atingir a excelência nesse objetivo, a criação de um manual de uso do produto é essencial para otimizar a experiência do usuário. Um manual bem elaborado traz diversas vantagens para o projeto, como facilitar a compreensão do sistema e da ideia, tornar a manutenção possível e reduzir possíveis erros de uso, esperados e inesperados.

Além disso, a capacitação dos funcionários, principalmente nos setores que terão contato direto com a solução, é fundamental para o sucesso do projeto. Um teste em ambiente controlado com um técnico especialista pode ser realizado para que os usuários da solução entendam o funcionamento do sistema e observem o sucesso do projeto naquilo que é esperado. Isso aumentará a confiança e o conforto dos trabalhadores na utilização do produto.

## 2.3. Sustentabilidade ambiental

### Ecoeficiente do projeto

O projeto visa uma automatização do processo de varredura de gases em espaços confinados que possibilita análises em diferentes áreas destes. Com o escopo em mente, assume-se que o projeto poderá trazer uma quantidade menor de recursos, onde um único robô poderá fazer varreduras em diversos segmentos, seja em meio a leitura de gases ou gravação do atual estado estrutural do ambiente, sem a necessidade de um operador ser exposto ao risco. `<br>`

Os principais pontos que justificam o uso de uma nova tecnologia são: `<br>`

- A identificação dos riscos ambientais relacionados às manutenções que, com o uso da nova solução, pode-se reduzir a liberação de gases tóxicos derivados de um mal fechamento ou falha nas válvulas. `<br>`
- A adoção de tecnologias ecoeficientes pode contribuir para reduzir os riscos ambientais e promover a segurança do trabalho pois não expõe as equipes de manutenção a um contado de gases tóxicos e situações adiversas. `<br>`
- O monitoramento em tempo real provido por sensores é fundamental para avaliar a efetividade das medidas de prevenção e controle de riscos ambientais. A análise dos resultados pode contribuir para a implementação de novas medidas preventivas e para a melhoria contínua da segurança do trabalho e da ecoeficiência na empresa.

## 2.4. Influências socioculturais

## 2.5. Tipológico-formais e ergonômicos

## 2.6. Tecnologia produtiva e materiais empregados

# 3. Descrição da arquitetura do sistema.

A arquitetura de solução nossa contém três áreas de atuação:

- `Embarcado`: Parte do embarcado/robô, onde contém todo controle de movimento e sensores do turtlebot, por exemplo: _IMU_, _LIDAR_ e _Camera_.
- `Backend`: Sistema de servidor em núvem que fornece dados sobre o `embarcado` para o `frontend`, e armazena as varreduras feitas, junto ao código de execução do trajeto necessário para o funcionamento autônomo do robô.
- `Frontend`: Dashboard principal do usuário, apresentando dados sobre as rotinas, e enviando solicitações/comandos indiretamenta ao robô utilizando do `Backend` em requisições _HTTP_ ou _Sockets_.

Todos os componentes estão ligados pela internet rede _WI-FI_ para terem uma forma de comunicação contínua, principalmente utilizando o `ROS2`, que facilita todo o sistema de comunicação e comandos entre o `Backend` e o `Embarcado`.

![Arquitetura-do-sistema](./media/Arquitetura%20do%20sistema.png)

# 4. Sistema de locomoção e otimização de rota.

Diante do contexto de nossa aplicação, optamos por utilizar do robô e seus sensores para realizar sua movimentação. Assim, o robô diante da "entrada" ao espaço deverá seguir um caminho desobstruído diante de uma analise que ela realizará sobre o valor dos sensores, pensamos em utilizar principalmente seu sensor LIDAR para aumentar a precisão dos pontos entre robô e a estrutura/obstruções do local. Detalhando a implementação, foi desenvolvido um Script no qual a principal lógica é caso um objeto em linha reta seja identificado eplo sensor (podemos configurar uma medida) ele deverá desviar sua rota, podendo ser ela a continuação do percurso ou até mesmo uma meia volta diante de uma obstrução.

Para a realização de testes, iniciamos no simulador Gazebo do ROS, que dispõem do sensor LIDAR. Com o MVP desenvolvido,

# 5. Interface de usuário.

# 6. Sistema de visão computacional.

A partir da necessidade de realizar um serviço de streaming entre o robô e a plataforma diante das decisões tomadas para o projeto e a implementação de um modelo pré treinado para a avaliação de rachaduras nas imagens captadas ao longo do percurso, tivemos de contruir nosso sistema de visão computacional pensando em cumprir tais objetivos.

A fim de analisar o desempenho de nosso modelo preditivo disponível pela YoLo para análise de imagens, utilizamos da câmera de um notebook para testarmos a detecção de rachaduras. Colocamos em frente à camera imagens que poderiam ser detectadas e na maioria dos casos ele apresentou corretamente suas dimensões e posições na tela, logo pudemos observar que o modelo havia sido treinado corretamente e que poderiamos utilizar de seu arquivo .pt gerado em nosso backend, para que fosse possivel realizar essa inspeção em imagens que chegam do nodo ROS e sua apresentação no frontend de maneira imediata.

Para o serviço de streaming, contamos com tecnologias como Socketio e a capacidade de subscrever e publicar em topicos da rede local. Devemos então, converter as imgaens obtidas em um formato que seja facil para transmitir entre a rede, para tal utilizamos da função tobytes(), que permite que os frames sejam transmitidos via tópicos, neste caso 'streaming'. Seguindo a lógica da aplicação, 

# 7. Sistemas de segurança.

# 8. Backend.

## Modelagem do Banco de Dados

O banco de dados é uma ferramenta utilizada para o armazenamento e gerenciamento de informações do sistema. O projeto baseia-se na automação de inspeção de espaços confinados por meio de um AGV, ou seja, deve-se pensar na necessidade de salvamento de espaços, rotas e informações de ambiente captadas pelos sensores do robô. `<br>`
Neste sentido, é necessário que o banco de dados seja capaz de relacionar duas coleções, *space* (que representa o espaço confinado em si) e *route* (que representa as leituras feitas nos determinados espaços).

<p align="center"><img src="https://github.com/2023M6T2-Inteli/Inspectron/blob/docs/add-simple-describes-and-format/media/Inspectron%20DB.jpg"></img></p>
A entidade *space* é composta pelos documentos *id*, *name* e *coordinates*. O id é a primary key da coleção, ou seja, ele é responsável por fornecer um registro exclusivo a ela. Dessa forma, ele garante que não haja duplicatas na coleção e também possibilita a relação entre as coleções do banco de dados. O *name* é utilizado para facilitar a identificação e pesquisa de registros do espaço. E por fim, o documento *coordinates* é utilizado para localizar físicamente o espaço salvo. Ele é do tipo *object*, isso significa que ele precisa de mais de uma informação na sua composição. Para cumprir sua função corretamente no projeto, ele precisa receber uma coordenada x e uma coordenada y. <br>
Já a entidade *route* é composta pelos documentos *id*, *directions*, *oxygen* e *space*. O *id* exerce a mesma função comentada anteriormente. O documento *directions* é utilizado para salvar a movimentação que o robô faz dentro do espaço. Ele é uma array do tipo *object* que recebe o enum *direction*, utilizado para dar um valor inteiro para constantes nomeadas e *value* que metrifica essa movimentação. <br>
A estrutura do enum *direction* pode ser representada como: <br>
{ <br>
Frente: 0 <br>
Trás: 1 <br>
Esquerda: 2 <br>
Direita: 3 <br>
} <br>
O documento *oxygen* representa a deficiência ou enriquecimento de oxigênio medidos em porcentagem captados pelo sensor do robô. <br>
Além disso, essa coleção possui a *Foreign Key* *space*, que a relaciona com a coleção *space*. A *Foreign Key* garante a integridade dos dados das duas coleções, tornando possível estabelecer a relação com segurança.

# 9. Integração de sistemas.

# 10. Validação da eficácia do sistema.

# 11. Referências

Página da Gerdau no Glassdorr. Disponível em [https://www.glassdoor.com.br/Vis%C3%A3o-geral/Trabalhar-na-Gerdau-EI_IE7569.13,19.htm](https://www.glassdoor.com.br/Vis%C3%A3o-geral/Trabalhar-na-Gerdau-EI_IE7569.13,19.htm).

A Indústria 4.0 e o futuro da manufatura com a utilização de AGVs – Sinova AGV – Sistema AGV e Solução. Disponível em: [https://www.sinova.com.br/2021/10/22/a-industria-4-0-e-o-futuro-da-manufatura-com-a-utilizacao-de-agvs/](https://www.sinova.com.br/2021/10/22/a-industria-4-0-e-o-futuro-da-manufatura-com-a-utilizacao-de-agvs/).

‌How much does an AGV cost? Disponível em: [https://www.flexqube.com/news/how-much-does-an-agv-cost/#:~:text=AGV%20Forklifts%20have%20an%20estimated](https://www.flexqube.com/news/how-much-does-an-agv-cost/#:~:text=AGV%20Forklifts%20have%20an%20estimated).

‌EDGE-ADMIN. AGV ou AMR? Qual a melhor tecnologia para robôs móveis? - EDGE. Disponível em: [https://edgeglobal.com.br/blog/agv-ou-amr/](https://edgeglobal.com.br/blog/agv-ou-amr/).

‌Veículo autoguiado e os benefícios na indústria 4.0 – Sinova AGV – Sistema AGV e Solução. Disponível em: [https://www.sinova.com.br/2021/03/11/veiculo-autoguiado-e-os-beneficios-na-industria-4-0/](https://www.sinova.com.br/2021/03/11/veiculo-autoguiado-e-os-beneficios-na-industria-4-0/).

‌CONECT, E. O que preciso saber sobre trabalho em espaço confinado? Disponível em: [https://conect.online/blog/o-que-preciso-saber-sobre-trabalho-em-espaco-confinado/](https://conect.online/blog/o-que-preciso-saber-sobre-trabalho-em-espaco-confinado/).

Indústria 4.0 no Brasil: cenário e perspectivas - KPMG Brasil. Disponível em: [https://kpmg.com/br/pt/home/insights/2021/07/industria-4-0.html](https://kpmg.com/br/pt/home/insights/2021/07/industria-4-0.html).

‌Indústria 4.0. Disponível em: [https://www.portaldaindustria.com.br/industria-de-a-z/industria-4-0/](https://www.portaldaindustria.com.br/industria-de-a-z/industria-4-0/).

Veículos Autoguiados: estimativa de mercado da automação industrial – Sinova AGV – Sistema AGV e Solução. Disponível em: [https://www.sinova.com.br/2020/12/22/veiculos-autoguiados-estimativa-de-mercado-da-automacao-industrial/](https://www.sinova.com.br/2020/12/22/veiculos-autoguiados-estimativa-de-mercado-da-automacao-industrial/).

Sobre nós. Disponível em: [https://www2.gerdau.com.br/sobre-nos/](https://www2.gerdau.com.br/sobre-nos/).
