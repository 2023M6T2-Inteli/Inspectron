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
		* [1.2.1. HardWare](#hardware)
		* [1.2.2. FrontEnd e BackEnd](#frontend-e-backend)
* [2. Componestes e Recursos](#componestes-e-recursos)
	* [2.1. Componestes de hardware](#componestes-de-hardware)
	* [2.2. Componestes externos](#componestes-externos)
* [3. Guia de Montagem](#guia-de-montagem)
* [4. Guia de Instalação](#guia-de-instalção)
* [5. Guia de Configuração](#guia-de-configuração)
* [6. Guia de Operação](#guia-de-operação)
* [7. Riscos Operacionaias](#riscos-operacionaias)
* [8. Adequação do Local de Operação do Robô](#adequação-do-local-de-operação-do-robô)
* [9. Guia de Prevenção e Mitigação de Acidentes](#guia-de-prevenção-e-mitigação-de-acidentes)
* [10. Troubleshooting](#troubleshooting)
* [11. Creditos](#creditos) 

# 1. Introdução
## 1.1. Solução
A solução se trata de um sistema de varredura de ambientes confinados, por meio de um robô, com o nome de TurtleBot. O TurtleBot é um Autonomous Guided Vehicle (AGV) que pode ser considerado como um um tipo de robô autônomo que segue uma trajetória pré-definida por meio de software e utiliza sensores, como câmeras e lasers, para navegar no ambiente e evitar obstáculos.

O TurtleBot entra em espaços confinados medindo o nível de oxigênio presente no ambiente a fim de garantir segurança aos operários que necessitem adentrar para fazer reparos. O Robô contará também, com um sensor “lidar”, que será usado para identificar obstáculos à sua frente e contorná-lo e uma câmera a fim de identificar rachaduras ao longo do percurso.

O operador terá disponível um website, que trará informações de varreduras antigas, disponibilizando relatórios e criando novas varreduras.

## 1.2. Arquitetura da Solução

### 1.2.1. HardWare
 
<p align="center"><img src="https://github.com/2023M6T2-Inteli/Inspectron/blob/Manual_branch/docs/media/Arquitetura%20do%20sistema.png?raw=true" width="100%"></img></p>

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



### 1.2.2. FrontEnd e BackEnd

<p align="center"><img src="https://github.com/2023M6T2-Inteli/Inspectron/blob/Manual_branch/docs/media/arquitetura_do_sistema_front_back.png?raw=true" width="100%"></img></p>



 
# 2. Componestes e Recursos 

## 2.1. Componestes de hardware 

* **TurtleBot3Burger**
	* **OpenCr1.0 :**  O OpenCR significa Módulo de Controle de Código Aberto para ROS (Robot Operating System). O OpenCR foi desenvolvido para sistemas embarcados que utilizam o ROS, com o objetivo de fornecer hardware e software completamente de código aberto.
	
	* **Raspberry Pi 3 :** Um microcomputador de baixo custo que pode ser utilizado como o cérebro de robôs e projetos robóticos, permitindo controle e interação com sensores e atuadores.

	* **360 Laser Distance sensor LDS-0 :**  Um dispositivo que utiliza um feixe de laser para medir com precisão a distância entre o sensor e um objeto em sua linha de visão.

	* **Li-Po Battery :**  Um tipo de bateria recarregável que utiliza tecnologia de polímero de íons de lítio.
    
	* **Dynamixel(XL430) :** Um atuador (servo motor).
    

	* **USB2LDS :**  Um adaptador USB para Laser Distance Sensor (LDS). Esse adaptador permite conectar um sensor de distância a laser ao computador por meio de uma porta USB.
	
* **DTH11 :** Um sensor capaz de medir a temperatura e umidade de um ambiente.

*   **MQ135 :** Um sensor capaz de medir os níveis de gases de um ambiente.
    

- **Câmera :** Uma câmera comum para visualização.

<p align="center"><img src="https://github.com/2023M6T2-Inteli/Inspectron/blob/Manual_branch/docs/media/componentes.png?raw=true" width="80%"></img></p>


## 2.2. Componestes externos

* Computador com conexão à internet.
* Uma ou mais redes wifi que juntas cubram todo o ambiente.

# 3. Guia de Montagem

**1.** Seguir a montagem do TurtleBot3 Burger conforme o manual: [Página para download do manual](https://emanual.robotis.com/docs/en/platform/turtlebot3/hardware_setup/), **[Vídeo de montagem](https://youtu.be/5D9S_tcenL4)**.

**2.** Acoplar os sensores MQ135, DTH11 e a câmera em seus devidos suportes.

**3.** Conectar os sensores nas portas(entradas) do Raspberry Pi 3.

**4.** Criar uma conexão estável via wifi com o TurtleBot.

# 4. Guia de Instalção

Caso o operador deseje criar novas funções ao robô, é importante seguir este tutorial abaixo:

 * **1.** O primeiro passo é ter um sistema operacional Linux. Pode ser qualquer distro Linux mas a mais usada é o Ubuntu.
 
 * **2.** Caso seu sistema operacional seja Windows , existem 2 maneiras de resolver:
	 * **a.** Fazer um dualboot(ter 2 sistemas operacionais em um computador)
	 * **b.** Baixar o WSL(o Windows Subsystem for Linux é uma camada de compatibilidade desenvolvida pela Microsoft que permite executar distribuições Linux no sistema operacional Windows.) **Recomendado**
* **3.** Para baixar o wsl, entre neste [link](https://github.com/rmnicola/m6-ec-encontro1/tree/b27ae69c8799c29ce488e7f53bba7b92411eaf7a#instalando-o-wsl) e siga as instruções. Esta é uma versão resumida feita pela instituição de ensino, Inteli, mas caso deseje, aqui está a documentação [original](https://ubuntu.com/tutorials/install-ubuntu-on-wsl2-on-windows-11-with-gui-support#1-overview).

* **4.** Ao completar a instalação do WSL, deve-se baixar o [ROS2 Humble](https://github.com/rmnicola/m6-ec-encontro1/tree/b27ae69c8799c29ce488e7f53bba7b92411eaf7a#instalando-o-ros2-humble). Caso deseje a documentação [oficial](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html).
* **5.** Faça o download do nosso projeto pelo [GitHub](https://github.com/2023M6T2-Inteli/Inspectron)
 	
 

# 5. Guia de Configuração

**1ª:** Fazer o login com um computador no [Site](link do site).

<p align="center"><img src="https://github.com/2023M6T2-Inteli/Inspectron/blob/Manual_branch/docs/media/login_page.png?raw=true" width="80%"></img></p>

**2ª :** Selecionar o botão “+ Nova varredura” para ir até a aba de configuração/criação de um novo robô.

<p align="center"><img src="https://github.com/2023M6T2-Inteli/Inspectron/blob/Manual_branch/docs/media/botoes_laterais.png?raw=true" width="20%"></img></p>

**3ª: ** Após isso é preciso registrar o robô no sistema, preenchendo os seguintes campos. E ao final, clicar em “Iniciar varredura”.

<p align="center"><img src="https://github.com/2023M6T2-Inteli/Inspectron/blob/Manual_branch/docs/media/create_page.png?raw=true" width="80%"></img></p>

**4ª:** Apoios a configuração de um novo robô/varredura, o usuário será redirecionado para a aba onde será possível ver a operação em tempo real.

<p align="center"><img src="https://github.com/2023M6T2-Inteli/Inspectron/blob/Manual_branch/docs/media/visualization_page.png?raw=true" width="80%"></img></p>

# 6. Guia de Operação

**1ª:** Para a visualização a visualização dos dados obtidos em cada varredura ou em um ambiente específico, clique no botão “Varreduras/Locais”

<p align="center"><img src="https://github.com/2023M6T2-Inteli/Inspectron/blob/Manual_branch/docs/media/botoes_laterais.png?raw=true" width="20%"></img></p>

**2ª:** Selecione o ambiente ou a varredura que deseja visualizar.

<p align="center"><img src="https://github.com/2023M6T2-Inteli/Inspectron/blob/Manual_branch/docs/media/historic_page.png?raw=true" width="80%"></img></p>

**3ª:** Ao clicar no ambiente ou varredura desejada, será possível visualizar os dados de oxigênio, dia e horário de cada varredura.

<p align="center"><img src="https://github.com/2023M6T2-Inteli/Inspectron/blob/Manual_branch/docs/media/room_page.png?raw=true" width="80%"></img></p>

# 7. Riscos Operacionais
|   #             |Problema                          |         Descrição                |
|----------------|-------------------------------|-----------------------------|
|1|            |Falhas técnicas            |O robô pode enfrentar falhas técnicas, como mau funcionamento dos componentes, perda de energia, falhas de comunicação ou problemas de software. Essas falhas podem resultar na interrupção da operação do robô, atrasos nas inspeções ou perda de dados. É importante realizar manutenções regulares, testes de funcionalidade e implementar sistemas de backup para lidar com essas situações.|
|2          |            |           |
|3          |  |
# 8. Adequação do Local de Operação do Robô

# 9. Guia de Prevenção e Mitigação de Acidentes

# 10. Troubleshooting

|   #             |Problema                          |         Possível solução                |
|----------------|-------------------------------|-----------------------------|
|1|      Falta de Bateria      |  Parar o que o robô está fazendo e colocar a bateria para carregar. Uma vez que a bateria descarrega, não é possível recarregar novamente.          |
|2          |Falhas no sistema de coleta e análise de dados            |Verifique se há espaço de armanezamento e se os dispositivos de coletos estão funcionando corretamente            |
|3          | Danos físicos |Verifique se o robô sofreu algum dano físico, se os componentes físicos estão em boas condições e se os cabos e conexões estão firmemente conectados |

# 11. Creditos 

* [Antônio Ribeiro Cavalcante](https://www.linkedin.com/in/antonioribeiro893/)
* [Emanuele Lacerda Morais Martins](https://www.linkedin.com/in/emanuele-morais/)
* [Gabriela Barretto Dias](https://www.linkedin.com/in/gabriela-barretto02)
* [Gustavo Francisco Neto Pereira](https://www.linkedin.com/in/gustavo-pereira1/)
* [Luca Sarhan Giberti]()
* [Lyorrei Shono Quintão]()  
* [Vinicios Venâncio Lugli](https://www.linkedin.com/in/vinicioslugli/)
