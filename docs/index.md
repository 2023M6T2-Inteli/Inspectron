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

-   [1 - Entendimento de negócio](#1-entendimento-de-negócio)
    -   [1.1 - Canvas Proposta de Valor](#11-canvas-proposta-de-valor)
    -   [1.2 - Matriz de Riscos](#12-matriz-de-riscos)
    -   [1.3 - Oceano Azul](#13-oceano-azul)
    -   [1.4 - Análise financeira](#14-análise-financeira)
-   [2 - Entendimento do metadesign](#2-entendimento-do-metadesign)
    -   [2.1 - Fatores mercadológicos](#21-fatores-mercadológicos)
    -   [2.2 - Sistema produto/design](#22-sistema-produto/design)
    -   [2.3 - Sustentabilidade ambiental](#23-sustentabilidade-ambiental)
    -   [2.4 - Influências socioculturais](#24-influências-socioculturais)
    -   [2.5 - Tipológico-formais e ergonômicos](#25-tipológico-formais-e-ergonômicos)
    -   [2.6 - Tecnologia produtiva e materiais empregados](#26-tecnologia-produtiva-e-materiais-empregados)
-   [3 - Descrição da arquitetura do sistema](#3-descrição-da-arquitetura-do-sistema)
-   [4 - Sistema de locomoção e otimização de rota](#4-sistema-de-locomoção-e-otimização-de-rota)
-   [5 - Interface de usuário](#5-interface-de-usuário)
-   [6 - Sistema de visão computacional](#6-sistema-de-visão-computacional)
-   [7 - Sistemas de segurança](#7-sistemas-de-segurança)
-   [8 - Backend](#8-backend)
-   [9 - Integração de sistemas](#9-integração-de-sistemas)
-   [10 - Validação da eficácia do sistema](#10-validação-da-eficácia-do-sistema)

---

# 1. Entendimento de negócio.

## 1.1. Canvas Proposta de Valor

## 1.2. Matriz de Riscos

<p align="center"><img src="https://github.com/2023M6T2-Inteli/Inspectron/blob/main/docs/media/Matriz%20de%20Risco.png?raw=true" width=80%></img></p>

### Plano de resposta aos riscos

1. <b>Risco:</b> Custos elevados para aquisição e manutenção dos equipamentos tecnológicos<br>
   <b>Resposta (transferência):</b> Para amenizar os gastos imediatos do projeto, é possível que a Gerdau solicite financiamento a investidores ou instituições financeiras. Dessa forma, a empresa compartilha os potenciais riscos com aqueles que fornecerão o financiamento, de modo a diminuir, consequentemente, a exposição a condições financeiras perigosas.

2. <b>Riscos:</b> Solução inapta para situações específicas (com água, fogo, altas temperaturas, etc.) e O dispositivo é frágil para determinados ambientes<br>
   <b>Resposta (mitigação):</b> Para capacitar o robô a operar em ambientes com condições adversas, pode-se adicionar módulos externos que permitam a operação com segurança. Por exemplo, em espaços confinados de alta temperatura, como fornalhas, fornos ou caldeiras, é possível utilizar um escudo térmico no robô.

3. <b>Risco:</b> Queima de componentes eletrônicos <br>
   <b>Resposta (mitigação):</b> Para evitar a queima de componentes eletrônicos, é crucial observar e seguir as boas práticas da eletrônica. O primeiro passo é fazer as ligações em um simulador para evitar desperdícios. Em seguida, faz-se a montagem de acordo com a simulação e, antes de ligar o sistema, realiza-se o teste de continuidade. Dessa forma, as chances de queimar qualquer componente são praticamente nulas.

4. <b>Risco:</b> Divergência nas informações captadas pelos sensores e o estado atual<br>
   <b>Resposta (mitigação):</b> Para garantir a qualidade das informações dos sensores, deve-se escolher sensores precisos e calibrá-los regularmente. Além disso, é possível utilizar sensores redundantes, para comparar as informações captadas por ele e identificar possíveis incongruências.

## 1.3. Oceano Azul

<b>Reduzir:</b>

- A inspeção e coleta de dados em espaços confinados de maneira mais rápida, reduz o tempo  para realizar essas atividades e aumenta a produtividade.

- Riscos à saúde dos colaboradores durante a realização de atividades em espaços confinados.

<b>Aumentar:</b>

- Pode aumentar a precisão dos dados coletados em espaços confinados, permitindo uma melhor identificação de possíveis problemas ou riscos nas estruturas.

- A segurança dos colaboradores durante a realização de atividades em espaços confinados, reduzindo o risco de acidentes.

<b>Eliminar:</b>

- Erros humanos durante a inspeção e coleta de dados em espaços confinados, garantindo a precisão dos resultados.

- A exposição de colaboradores a gases tóxicos ou falta de oxigênio.

<b>Criar:</b>

- Flexível e adaptável às necessidades dos clientes, permitindo a personalização dos recursos de acordo com a demanda. 

- Monitoramento remoto em tempo real, permitindo a análise de dados coletados e a tomada de decisões de forma mais rápida e eficiente.

## 1.4. Análise financeira

 O robô tem custo fixo, portanto quanto mais robôs a Gerdau decidir usar mais caro vai ficar. O custo de implementação do nosso código foi calculado usando o salário médio de um técnico de robótica no Brasil que equivale a  $ 4779.18, depois foi calculado o custo presumindo 15 minutos de trabalho para completar seria R$ 7.47. Por ter componentes elétricos, o robô tem uma bateria e o custo da sua carga também tem que ser levado em consideração, que equivale a 12 centavos por carga completa, presumindo que seja carregado em uma tomada de 110 volts. Achei que cabia colocar manutenção preventiva como um custo relevante para prevenir outros custos que podem ser maiores. Isso foi calculado também pelo salário do técnico de robótica mencionado anteriormente pelo mesmo período de tempo, portanto tendo o mesmo valor. O nosso trabalho é gratuito portanto não tem custo associado. Também não existe nenhum imposto associado ao projeto a ser pago.

# 2. Entendimento do metadesign

## 2.1. Fatores mercadológicos

### Produto, orientação de mercado e precificação

Um AGV é um tipo de robô autônomo que segue uma trajetória pré-definida por meio de software e utiliza sensores, como câmeras e lasers, para navegar no ambiente e evitar obstáculos. Esses robôs são altamente precisos e seguros, permitindo que se movimentem por espaços apertados com habilidade superior à das mãos humanas. Por essas razões, eles são amplamente utilizados para transportar materiais em ambientes industriais ou logísticos. Além de seu uso para transporte, os AGVs podem ser equipados com sensores e câmeras para realizar a inspeção de áreas de difícil acesso ou perigosas para os humanos. Isso garante mais segurança e precisão na realização da manutenção preventiva.

Durante uma entrevista com um parceiro, foi levantada a questão de que a vistoria de locais confinados é feita apenas pelo lado de fora, o que não permite entender verdadeiramente a condição do espaço. Apesar dos riscos envolvidos, tarefas como limpeza, manutenção e inspeção precisam ser realizadas em espaços confinados. No entanto, devido à dificuldade de acesso, essas atividades podem resultar em várias situações perigosas.

Felizmente, a indústria 4.0 está trazendo soluções para esse problema através da automatização desses processos perigosos. Essa tecnologia aumenta a segurança dos trabalhadores e otimiza os processos, tornando as atividades em espaços confinados mais eficientes e menos perigosas. O projeto criado se orienta para o mercado de segurança e otimização de processos na indústria 4.0. Tal informação pode ser aferida pois o protótipo desenvolvido utiliza recursos avançados, como câmeras, lasers, sensores de proximidade, sensores de gases e outros, para automatizar trabalhos considerados perigosos para os humanos. Além disso, fornece dados em tempo real para uma melhor análise das informações obtidas.

No que se refere à precificação do produto, é importante destacar que os AGVs apresentam uma ampla variação de preços, que podem variar de $40.000 a $200.000, dependendo do tipo de veículo, tamanho, sensores instalados, função e outras possíveis variações. Além disso, é preciso levar em consideração os custos envolvidos na implantação do AGV, tais como o treinamento dos funcionários, a instalação de trilhos ou outras referências de movimento e a integração com outros sistemas de softwares. Para precificar o MVP, será utilizado o TurtleBot3 com os sensores necessários e os investimentos necessários para implementar a solução na empresa parceira.

### Cenário do mercado

Com as mudanças globais em constante evolução, as expectativas dos consumidores e investidores estão se tornando cada vez mais exigentes. Nesse contexto, a Indústria 4.0 surge como um grande integrador de toda a cadeia da indústria, levantando debates importantes sobre o seu desenvolvimento. No Brasil, a implementação da Indústria 4.0 apresenta desafios que vão desde o investimento em equipamentos que incorporem essas tecnologias até a adaptação de processos e formas de relacionamento entre as empresas ao longo da cadeia produtiva, além da criação de novas especialidades e desenvolvimento de competências.

No entanto, de acordo com a McKinsey, estima-se que até 2025, os processos relacionados à Indústria 4.0 poderão reduzir os custos de manutenção de equipamentos em 10% a 40%, reduzir o consumo de energia entre 10% e 20%, e aumentar a eficiência do trabalho em 10% a 25%. Com isso, é possível concluir que, apesar dos desafios de implementação, a Indústria 4.0 oferece grandes benefícios.

Em ambientes confinados a utilização de robôs tem se mostrado uma alternativa favorável para facilitar vistórias em ambientes restritos e perigosos para seres humanos. De acordo com um relatório da BCC Research, o mercado global de veículos guiados automatizados (AGVs) deve atingir US$ 4 bilhões até 2025. Isso indica que os AGVs estão sendo amplamente adotados pelas indústrias para aumentar a eficiência de suas operações, uma vez que essa tecnologia oferece diversos benefícios, como o diminuição da exposição de trabalhadores a tarefas perigodas e otimização na coleta de dados.

### Visão do projeto proposto

O setor siderúrgico, onde a Gerdau atua, envolve a manipulação de equipamentos e materiais pesados, altas temperaturas e exposição dos trabalhadores a materiais químicos tóxicos, o que o torna um setor de alto risco em termos de segurança do trabalho.

A segurança dos colaboradores é um dos valores primordiais da Gerdau e, como tal, a empresa busca continuamente formas de garantir maior segurança em suas operações. Neste contexto, um dos principais riscos que causa grande preocupação na Gerdau são os espaços confinados.

O trabalho em espaços confinados é considerado uma das modalidades mais perigosas, já que os colaboradores estão expostos a diversos riscos e o ambiente favorece a ocorrência de acidentes graves e frequentes. Em uma conversa com o parceiro, foi constatado que o processo atual é realizado externamente ao espaço e antes da manutenção, o que torna impossível ter uma visão real da situação dentro do espaço confinado.

Nesse cenário, o projeto apresenta uma grande importância para a Gerdau. Ao implementar inspeções automatizadas para vistorias preventivas de manutenção, será possível elevar ainda mais a segurança no trabalho, padrões de qualidade em vistorias e proporcionar maior satisfação aos colaboradores.

## 2.2. Sistema produto/design

### Qual a missão do projeto proposto?

Um dos príncipais valores da Gerdau é a segurança de seus colaboradores. O setor siderúrgico envolve o manuseio de equipamentos e materiais pesados, altas temperaturas, além de sujeitar os trabalhadores a exposição de materiais químicos que podem ser tóxicos para o ser humano. Portanto, podemos considerar esse setor como de alto risco quando se fala de segurança do trabalho. Neste sentido, a Gerdau traça objetivos para que o desenvolvimento de segurança da empresa seja mais palpável, um deles é o acidente zero e para alcança-lo a empresa segue rígidos padrões de operação e manutenção, além de seguir normas nacionais e internacionais de segurança. Por isso, um dos riscos mais relevantes que foi identificado nas operações da Gerdau é o Espaço Confinado. Espaço Confinado são lugares que não foram feitos para intervenção humana em período contínuo. Hoje, a rotina de inspeção desses espaços é realizada externamente ao espaço e previamente a manutenção, para que possa ser observada a situação do ambiente e da infraestrutura do local.

## 2.3. Sustentabilidade ambiental

## 2.4. Influências socioculturais

## 2.5. Tipológico-formais e ergonômicos

## 2.6. Tecnologia produtiva e materiais empregados

# 3. Descrição da arquitetura do sistema.

# 4. Sistema de locomoção e otimização de rota.

# 5. Interface de usuário.

# 6. Sistema de visão computacional.

# 7. Sistemas de segurança.

# 8. Backend.

# 9. Integração de sistemas.

# 10. Validação da eficácia do sistema.
