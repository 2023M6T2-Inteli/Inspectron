<table>
<tr>
<td>
<a href= "https://www2.gerdau.com.br/"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Gerdau_logo_%282011%29.svg/1200px-Gerdau_logo_%282011%29.svg.png" alt="Gerdau" border="0" width="70%"></a>
</td>
<td><a href= "https://www.inteli.edu.br/"><img src="https://www.inteli.edu.br/wp-content/uploads/2021/08/20172028/marca_1-2.png" alt="Inteli - Instituto de Tecnologia e Liderança" border="0" width="30%"></a>
</td>
</tr>
</table>

<font size="+12"><center>

</center></font>

# 1. Entendimento de negócio.
## 1.1. Matriz de Riscos
### Plano de resposta aos riscos
1. <b>Risco:</b> Custos elevados para aquisição e manutenção dos equipamentos tecnológicos<br>
<b>Resposta (transferência):</b> Para amenizar os gastos imediatos do projeto, é possível que a Gerdau solicite financiamento a investidores ou instituições financeiras. Dessa forma, a empresa passa a compartilhar os riscos com aqueles que forneceram o financiamento e, assim, diminui-se o risco.

2. <b>Risco:</b> Solução inapta para situações específicas (com água, fogo, altas temperaturas, etc.)<br>
<b>Resposta (mitigação):</b> Para capacitar o robô a operar em ambientes com condições adversas, pode-se adicionar módulos externos que permitam a operação com segurança. Por exemplo, em espaços confinados de alta temperatura, como fornalhas, fornos ou caldeiras, é possível utilizar um escudo térmico no robô.

3. <b>Risco:</b> Queima de componentes eletrônicos <br>
<b>Resposta (mitigação):</b> Para evitar a queima de componentes eletrônicos, é crucial observar e seguir as boas práticas da eletrônica. O primeiro passo é fazer as ligações em um simulador para evitar desperdícios. Em seguida, faz-se a montagem de acordo com a simulação e, antes de ligar o sistema, realiza-se o teste de continuidade. Dessa forma, as chances de queimar qualquer componente são praticamente nulas.

4. <b>Risco: O dispositivo é frágil para determinados ambientes</b> <br>
<b>Resposta ():</b>

5. <b>Risco: Divergência nas informações captadas pelos sensores e o estado atual</b> <br>
<b>Resposta ():</b>

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
