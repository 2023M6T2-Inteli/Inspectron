<table>
<tr>
<td>
<a href= "https://www2.gerdau.com.br/"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Gerdau_logo_%282011%29.svg/1200px-Gerdau_logo_%282011%29.svg.png" alt="Gerdau" border="0" width="20%"></a>
</td>
<td><a href= "https://www.inteli.edu.br/"><img src="[https://www.inteli.edu.br/wp-content/uploads/2022/04/28103439/Logo-Container.png](https://github.com/2023M6T2-Inteli/Inspectron/blob/Manual_branch/docs/media/Logo-Container.png?raw=true)" alt="Inteli - Instituto de Tecnologia e Liderança" border="0" width="300%"></a>
</td>
</tr>
</table>

<h1> Manual de Instruções 
	
# Índice

* [1. Introdução](#introdução)
	* [1.1. Solução](#solução) 
	* [1.2. Arquitetura da Solução](#arquitetura-da-solução)
		* [1.2.1. Hardware](#hardware)
		* [1.2.2. Frontend e Backend](#frontend-e-backend)
* [2. Componestes e Recursos](#componestes-e-recursos)
	* [2.1. Componentes de hardware](#componentes-de-hardware)
	* [2.2. Componentes externos](#componentes-externos)
* [3. Guia de Montagem](#guia-de-montagem)
* [4. Guia de Instalação](#guia-de-instalção)
	* [4.1. TurtleBot3](#turtlebot3)
	* [4.2. Site](#site)
		* [4.2.1. Backend](#backend)
		* [4.2.2. Frontend](#frontend)

* [5. Guia de Configuração](#guia-de-configuração)
* [6. Guia de Operação](#guia-de-operação)
* [7. Riscos Operacionaias](#riscos-operacionaias)
* [8. Adequação do Local de Operação do Robô](#adequação-do-local-de-operação-do-robô)
* [9. Guia de Prevenção e Mitigação de Acidentes](#guia-de-prevenção-e-mitigação-de-acidentes)
* [10. Troubleshooting](#troubleshooting)
* [11. Créditos](#creditos) 

# 1. Introdução
## 1.1. Solução
A solução trata-se de um sistema de varredura de ambientes confinados, por meio de um robô, com o nome de TurtleBot. O TurtleBot é um Autonomous Guided Vehicle (AGV) que pode ser considerado como um um tipo de robô autônomo que segue uma trajetória pré-definida por meio de software e utiliza sensores, como câmeras e lasers, para navegar no ambiente e evitar obstáculos.

O TurtleBot entra em espaços confinados medindo o nível de oxigênio presente no ambiente a fim de garantir segurança aos operários que necessitem adentrar para fazer reparos. O robô também conta com um sensor “lidar”, que é usado para identificar obstáculos à sua frente e contorná-lo, e com uma câmera para identificar rachaduras ao longo do percurso.

O operador terá disponível um website, que trará informações de varreduras antigas, disponibilizando relatórios e criando novas varreduras.

## 1.2. Arquitetura da Solução

### 1.2.1. Hardware
 
<p align="center"><img src="https://github.com/2023M6T2-Inteli/Inspectron/blob/LucaSarhan-patch-1/docs/media/Arquitetura%20do%20sistema.png?raw=true" width="100%"></img></p>

<p align="center"><img src="" width="100%"></img></p>

<table>  
<tr>  
<th>1º Node</th>  
<th>2º Node</th>   
</tr>  
<tr>  
<td><p align="center"><img src="https://github.com/2023M6T2-Inteli/Inspectron/blob/Manual_branch/docs/media/priemiro_node_hardware.png?raw=true" width="90%"></img></p></td>  
<td><p align="center"><img src="https://github.com/2023M6T2-Inteli/Inspectron/blob/Manual_branch/docs/media/segundo_node_backend.png?raw=true" width="90%"></img></p></td>    
</tr>  
 
</table>



### 1.2.2. Frontend e Backend

<p align="center"><img src="https://github.com/2023M6T2-Inteli/Inspectron/blob/LucaSarhan-patch-1/docs/media/arquitetura_do_sistema_front_back.png?raw=true" width="100%"></img></p>



 
# 2. Componentes e Recursos 

## 2.1. Componentes de hardware 

* **TurtleBot3Burger**
	* **OpenCr1.0 :**  O OpenCR significa Módulo de Controle de Código Aberto para ROS (Robot Operating System). O OpenCR foi desenvolvido para sistemas embarcados que utilizam o ROS, com o objetivo de fornecer hardware e software completamente de código aberto.
	
	* **Raspberry Pi 3 :** Um microcomputador de baixo custo que pode ser utilizado como o cérebro de robôs e projetos robóticos, permitindo controle e interação com sensores e atuadores.

	* **360 Laser Distance sensor LDS-0 :**  Um dispositivo que utiliza um feixe de laser para medir com precisão a distância entre o sensor e um objeto em sua linha de visão.

	* **Li-Po Battery :**  Um tipo de bateria recarregável que utiliza tecnologia de polímero de íons de lítio.
    
	* **Dynamixel(XL430) :** Um atuador (servo motor).
    

	* **USB2LDS :**  Um adaptador USB para Laser Distance Sensor (LDS). Esse adaptador permite conectar um sensor de distância a laser ao computador por meio de uma porta USB.

* ** CJMCU-811 :** Um sensor de qualidade do ar, projetado para medir e detectar a concentração de dióxido de carbono (CO2) e compostos orgânicos voláteis (COV) no ambiente.


* ** GPS NEO-6M V2 :** É um módulo GPS (Global Positioning System) compacto e altamente preciso. Ele utiliza o sistema de posicionamento por satélite para determinar a localização geográfica com base em coordenadas de latitude e longitude. O módulo NEO-6M V2 é conhecido por sua eficiência em termos de consumo de energia e sua capacidade de aquisição rápida de sinais de satélite, mesmo em condições desafiadoras.


- **Câmera :** Uma câmera comum para visualização.

<p align="center"><img src="https://github.com/2023M6T2-Inteli/Inspectron/blob/LucaSarhan-patch-1/docs/media/componentes.png?raw=true" style="background-color: #f2f2f2;" width="80%" ></img></p>

## 2.2. Componentes externos

* Computador com conexão à internet.
* Uma ou mais redes wifi que, juntas, cubram todo o ambiente.

# 3. Guia de Montagem

**1.** Seguir a montagem do TurtleBot3 Burger conforme o manual: [Página para download do manual](https://emanual.robotis.com/docs/en/platform/turtlebot3/hardware_setup/), **[Vídeo de montagem](https://youtu.be/5D9S_tcenL4)**.

**2.** Acoplar os sensores MQ135, DTH11 e a câmera em seus devidos suportes.

**3.** Conectar os sensores nas portas(entradas) do Raspberry Pi 3.

**4.** Criar uma conexão estável via wifi com o TurtleBot.

# 4. Guia de Instalação

## 4.1. TurtleBot3 Burger
Caso o operador queira criar novas funções ao robô, é importante seguir este tutorial abaixo:

 * **1.** O primeiro passo é ter um sistema operacional Linux. Pode ser qualquer distro Linux mas a mais usada é o Ubuntu. 
 
 * **2.** Caso seu sistema operacional seja Windows , existem 2 maneiras de resolver:
	 * **a.** Fazer um dualboot(ter 2 sistemas operacionais em um computador)
	 * **b.** Baixar o WSL(o Windows Subsystem for Linux é uma camada de compatibilidade desenvolvida pela Microsoft que permite executar distribuições Linux no sistema operacional Windows.) **Recomendado**
* **3.** Para baixar o wsl, entre neste [link](https://github.com/rmnicola/m6-ec-encontro1/tree/b27ae69c8799c29ce488e7f53bba7b92411eaf7a#instalando-o-wsl) e siga as instruções. Esta é uma versão resumida feita pela instituição de ensino Inteli. Porém, mas caso queira, aqui está a documentação [original](https://ubuntu.com/tutorials/install-ubuntu-on-wsl2-on-windows-11-with-gui-support#1-overview).

* **4.** Ao completar a instalação do WSL, deve-se baixar o [ROS2 Humble](https://github.com/rmnicola/m6-ec-encontro1/tree/b27ae69c8799c29ce488e7f53bba7b92411eaf7a#instalando-o-ros2-humble). Caso queira, a documentação [oficial](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html).
* **5.** Faça o download do nosso projeto pelo [GitHub](https://github.com/2023M6T2-Inteli/Inspectron).
* **6.** Após ter o nosso projeto em sua máquina de escolha é necesário colocar os arquivos de código em seus respectivos lugares. Por exemplo, colocar o código do robô no robô em si.
 	
 ## 4.2. Site

 ### 4.2.1 BackEnd

 * **1.** O primeiro passo é fazer o download do projeto pelo [GitHub](https://github.com/2023M6T2-Inteli/Inspectron). Isso pode ser feito utilizando o comando ```git clone https://github.com/2023M6T2-Inteli/Inspectron/blob/main```.
 * **2.** Após baixar o projeto, é necessário localizar os arquivos relevantes do código do backend. Esses arquivos estão na pasta "Backend" dentro da pasta "Src"
 * **3.** Para instalar o Python, você pode seguir as instruções de instalação disponíveis no site oficial do Python (python.org). Dependendo do sistema operacional, pode ser necessário utilizar um gerenciador de pacotes, como o pip, para instalar o Python. No terminal, você pode executar o comando ```pip install python``` para instalar o Python.
 * **4.** Para instalar o MongoDB, você pode seguir um tutorial [oficial](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-windows/) fornecido pela equipe do MongoDB. O tutorial geralmente inclui instruções específicas para diferentes sistemas operacionais e ambientes. É recomendável seguir o tutorial oficial para garantir uma instalação correta e atualizada. 
 * **5.** Ao trabalhar com bibliotecas e dependências específicas do projeto, podem ocorrer erros relacionados à falta de instalação das bibliotecas necessárias. Nesses casos, você pode utilizar o pip para instalar as bibliotecas faltantes. No terminal, você pode executar o comando ```pip3 install fastapi uvicorn eventlet ultralytics python-socketio mongoengine python-dotenv pydantic passlib python-jose[cryptography]``` para instalar as bibliotecas específicas. Se o comando pip não funcionar, você pode consultar a documentação oficial da biblioteca para obter instruções de instalação específicas.
 * **6.** Se você precisar colocar o backend em produção, é necessário realizar o processo de implantação em um servidor ou plataforma de hospedagem. Por exemplo, se você estiver usando a AWS (Amazon Web Services), precisará configurar um ambiente de hospedagem (como uma instância EC2) e implantar seu projeto no servidor.
 * **7.** Caso você queira executar o backend localmente, você pode abrir um terminal e navegar até o diretório onde está localizado o arquivo do backend. Em seguida, execute o comando ```python3 <nome_do_arquivo>``` para iniciar o servidor localmente. Certifique-se de ter o Python corretamente instalado e configurado em seu sistema antes de executar esse comando.

 ### 4.2.2 FrontEnd

 * **1.** O primeiro passo é fazer o download do projeto pelo [GitHub](https://github.com/2023M6T2-Inteli/Inspectron). Isso pode ser feito utilizando o comando ```git clone git clone https://github.com/2023M6T2-Inteli/Inspectron/blob/main```.
 * **2.** Após baixar o projeto, é necessário localizar os arquivos relevantes do código do frontend. O framework utilizado é o React, que é uma biblioteca JavaScript para construção de interfaces de usuário. Os arquivos do frontend estão localizados na pasta "frontend" que está dentro da pasta "src".
 * **3.** Ao trabalhar com bibliotecas e dependências no projeto React, podem ocorrer erros relacionados à falta de instalação das bibliotecas necessárias. Para solucionar esses erros, você pode utilizar o npm (gerenciador de pacotes do Node.js) para instalar as dependências. No terminal, dentro da pasta do projeto, execute o comando ```npm install``` para instalar as dependências do projeto. Caso ocorra algum erro, é recomendado verificar a documentação oficial da biblioteca ou pacote específico para obter instruções de instalação corretas.
 * **4.** Se você precisa disponibilizar o site online, é necessário realizar o processo de hospedagem. Um exemplo mencionado é utilizar a AWS (Amazon Web Services), onde você precisará configurar um ambiente de hospedagem (como uma instância EC2) e implantar seu projeto. Existem também outras opções de hospedagem, como serviços de hospedagem compartilhada, plataformas de hospedagem específicas para React, entre outras. Cada opção tem suas próprias etapas específicas para implantação.
 * **5.** Caso você deseje rodar o projeto localmente no Visual Studio Code, você pode utilizar ferramentas como o Live Server, que é uma extensão do VS Code que permite iniciar um servidor local para executar o frontend do projeto. Basta abrir o projeto no VS Code, clicar com o botão direito no arquivo HTML principal do projeto e selecionar a opção "Open with Live Server" para iniciar o servidor local e visualizar o site no navegador.

## 4.3. Tecnologias utilizados
* **1.** Js React é um framework JavaScript amplamente utilizado para o desenvolvimento de interfaces de usuário interativas e responsivas. Ele permite a criação de componentes reutilizáveis que representam diferentes partes da interface do usuário e atualizam dinamicamente conforme os dados mudam. O React utiliza uma abordagem baseada em componentes, onde cada componente possui seu próprio estado e é capaz de renderizar uma visualização atualizada com base nesse estado. Ele é utilizado principalmente para criar aplicativos web de página única (SPA) e aplicativos móveis nativos utilizando o React Native. O React oferece uma maneira eficiente de criar interfaces complexas e de alto desempenho, além de ter uma comunidade ativa e uma vasta quantidade de bibliotecas e ferramentas disponíveis.
* **2.** Python é uma linguagem de programação de alto nível, orientada a objetos e de propósito geral. Ela é conhecida por sua sintaxe clara e legível, o que a torna muito fácil de aprender e usar. Python é usado em uma ampla variedade de aplicações, desde desenvolvimento web até análise de dados, inteligência artificial e automação de tarefas. A linguagem possui uma grande biblioteca padrão que fornece funcionalidades para várias tarefas, além de uma extensa coleção de pacotes de terceiros mantidos pela comunidade. Python é valorizado por sua produtividade, simplicidade e facilidade de integração com outras linguagens e sistemas.
* **3.** MongoDB é um banco de dados orientado a documentos, classificado como NoSQL (Não Somente SQL). Ao contrário dos bancos de dados relacionais tradicionais, que armazenam dados em tabelas e linhas, o MongoDB armazena dados em documentos flexíveis do tipo JSON (BSON). Ele oferece uma abordagem escalável e de alto desempenho para armazenamento e recuperação de dados. O MongoDB é amplamente utilizado em aplicativos web modernos, especialmente em cenários onde a flexibilidade de esquema é necessária, pois não exige uma estrutura rígida de dados. Ele suporta consultas avançadas, índices, replicação para alta disponibilidade e recursos de escalabilidade horizontal. O MongoDB é usado em conjunto com várias linguagens de programação, incluindo Python, para armazenar e acessar dados de forma eficiente.
* **4.** Tailwind CSS é um framework de CSS utilitário que permite a construção rápida e eficiente de interfaces de usuário responsivas. Ao contrário de outros frameworks de CSS, como Bootstrap ou Foundation, que fornecem estilos predefinidos, o Tailwind CSS adota uma abordagem diferente, fornecendo classes utilitárias de baixo nível que podem ser combinadas para criar estilos personalizados.
* **5.** Next.js é um framework de desenvolvimento web React que permite a criação de aplicativos web rápidos e escaláveis. Ele combina as poderosas funcionalidades do React com recursos avançados de servidor e renderização do lado do servidor (SSR) e renderização do lado do cliente (CSR).
* **6.** Há um arquivo chamado requirements.txt na pasta do backend com as libs do back instaladas
* **7.** Há um arquivo chamado package.json na pasta do frontend com as libs do front instaladas

# 5. Guia de Configuração

**1ª:** Fazer o login com um computador no [Site](link do site).

<p align="center"><img src="https://github.com/2023M6T2-Inteli/Inspectron/blob/Manual_branch/docs/media/login_page.png?raw=true" width="80%"></img></p>

**2ª:** Selecionar o botão “+ Nova varredura” para ir até a aba de configuração/criação de um novo robô.

<p align="center"><img src="https://github.com/2023M6T2-Inteli/Inspectron/blob/Manual_branch/docs/media/botoes_laterais.png?raw=true" width="20%"></img></p>

**3ª:** Após isso é preciso registrar o robô no sistema, preenchendo os campos abaixo. E ao final, clicar em “Iniciar varredura”.

<p align="center"><img src="https://github.com/2023M6T2-Inteli/Inspectron/blob/Manual_branch/docs/media/create_page.png?raw=true" width="80%"></img></p>

**4ª:** Apoios a configuração de um novo robô/varredura, o usuário será redirecionado para a aba onde será possível ver a operação em tempo real.

<p align="center"><img src="https://github.com/2023M6T2-Inteli/Inspectron/blob/Manual_branch/docs/media/visualization_page.png?raw=true" width="80%"></img></p>

# 6. Guia de Operação

**1ª:** Para a visualização dos dados obtidos em cada varredura ou em um ambiente específico, clique no botão “Varreduras/Locais”

<p align="center"><img src="https://github.com/2023M6T2-Inteli/Inspectron/blob/Manual_branch/docs/media/botoes_laterais.png?raw=true" width="20%"></img></p>

**2ª:** Selecione o ambiente ou a varredura que deseja visualizar.

<p align="center"><img src="https://github.com/2023M6T2-Inteli/Inspectron/blob/Manual_branch/docs/media/historic_page.png?raw=true" width="80%"></img></p>

**3ª:** Ao clicar no ambiente ou varredura desejada, será possível visualizar os dados de oxigênio, dia e horário de cada varredura.

<p align="center"><img src="https://github.com/2023M6T2-Inteli/Inspectron/blob/Manual_branch/docs/media/room_page.png?raw=true" width="80%"></img></p>

# 7. Riscos Operacionais
|   #             |Problema                          |         Descrição                |
|----------------|-------------------------------|-----------------------------|
|1|Falhas técnicas            |O robô pode enfrentar falhas técnicas como: mau funcionamento dos componentes, perda de energia, falhas de comunicação ou problemas de software. Essas falhas podem resultar na interrupção da operação do robô, atrasos nas inspeções ou perda de dados. É importante realizar manutenções regulares, testes de funcionalidade e implementar sistemas de backup para lidar com essas situações.            |
|2|Riscos de cibersegurança          |O robô pode estar conectado a uma rede ou sistema central, o que pode torná-lo vulnerável a ataques cibernéticos. Isso pode resultar em acesso não autorizado, manipulação de dados, interrupção das operações ou danos aos sistemas conectados.            |           
|3|Danos às estruturas          |O robô pode acidentalmente danificar as estruturas durante a inspeção, especialmente se tiver movimentos descontrolados ou se houver componentes rígidos que entrem em contato com as estruturas.|
# 8. Adequação do Local de Operação do Robô
|   #             |Item                          |         Descrição                |
|----------------|-------------------------------|-----------------------------|
|1|Segurança do local|Considere a segurança geral do local de operação. Evite a presença de pessoas não autorizadas ou animais que possam interferir no funcionamento do robô. Se possível, implemente medidas de segurança adicionais, como cercas, portões ou sistemas de segurança, para proteger a área de operação do robô.|
|2|Iluminação adequada|Verifique se há iluminação adequada no local, especialmente se o robô realizar inspeções em áreas com pouca luz. A iluminação inadequada pode afetar a qualidade das imagens capturadas ou a capacidade do robô de detectar obstáculos.|
|3|Acessibilidade|Certifique-se de que o local seja acessível para o robô. Considere a largura de passagem, portas estreitas, escadas ou outros obstáculos que possam limitar ou impedir a entrada e movimentação do robô. Se possível, faça as adaptações ou modificações adequadas no ambiente.|
|4|Sinalização e advertências|Se o robô estiver operando em áreas onde outras pessoas possam estar presentes, coloque sinalizações e advertências adequadas para alertar sobre a presença do robô em operação. Isso ajudará a evitar acidentes e garantir a segurança de todos.|
# 9. Guia de Prevenção e Mitigação de Acidentes
Segue uma tabela com possiveis passos que podem sererm tomados para a mitigação e prevenção de acidentes:
|   #             |Item                          |         Descrição                |
|----------------|-------------------------------|-----------------------------|
|1|Treinamento adequado| Forneça treinamento adequado aos operadores do robô para garantir que eles compreendam as precauções de segurança, os procedimentos de operação corretos e a resposta a emergências. Isso inclui familiarizá-los com as características do robô, seus controles, limitações e possíveis riscos operacionais.|
|2|Manutenção regular|Estabeleça um plano de manutenção regular para o robô, seguindo as diretrizes do fabricante. Isso inclui a verificação e substituição de peças desgastadas, a limpeza adequada dos componentes e a realização de inspeções preventivas para detectar problemas antes que eles se tornem críticos.|
|3|Avaliação contínua|Realize avaliações regulares do desempenho do robô, incluindo sua segurança operacional. Identifique áreas de melhoria e faça ajustes nos procedimentos ou no equipamento, conforme necessário.|
|4|Atualizações de segurança|Mantenha-se atualizado sobre as atualizações de segurança do robô, incluindo atualizações de software e firmware. Essas atualizações podem incluir correções de segurança, melhorias de desempenho e novos recursos de segurança. Garanta que todas as atualizações sejam aplicadas regularmente para manter o robô protegido contra ameaças potenciais.|
# 10. Troubleshooting

|   #             |Problema                          |         Possível solução                |
|----------------|-------------------------------|-----------------------------|
|1|      Falta de Bateria      |  Parar o que o robô está fazendo e colocar a bateria para carregar. Uma vez que a bateria descarrega, não é possível recarregar novamente.          |
|2          |Falhas no sistema de coleta e análise de dados            |Verifique se há espaço de armanezamento e se os dispositivos de coletas estão funcionando corretamente.            |
|3          | Danos físicos |Verifique se o robô sofreu algum dano físico, se os componentes físicos estão em boas condições e se os cabos e conexões estão firmemente conectados. |
|4|Conexão de rede perdida|Verifique se o robô está dentro da faixa de alcance do roteador Wi-Fi, reinicie o roteador e verifique se outras conexões de rede estão funcionando corretamente e verifique se as configurações de rede do robô estão corretas e atualizadas.|
|5|Perda de sinal de GPS|Certifique-se de que o módulo GPS esteja corretamente conectado e funcionando adequadamente; reinicie o módulo GPS e verifique se os cabos de conexão estão firmemente conectados.|
|6|Falha no sistema de mapeamento e navegação|Reinicie o sistema de mapeamento e navegação; verifique se todas as configurações estão corretas e verifique se há interferências magnéticas ou outras fontes de perturbação que possam afetar a precisão do sistema.|

# 11. Créditos 

* [Antônio Ribeiro Cavalcante](https://www.linkedin.com/in/antonioribeiro893/)
* [Emanuele Lacerda Morais Martins](https://www.linkedin.com/in/emanuele-morais/)
* [Gabriela Barretto Dias](https://www.linkedin.com/in/gabriela-barretto02)
* [Gustavo Francisco Neto Pereira](https://www.linkedin.com/in/gustavo-pereira1/)
* [Luca Sarhan Giberti]()
* [Lyorrei Shono Quintão]()  
* [Vinicios Venâncio Lugli](https://www.linkedin.com/in/vinicioslugli/)
