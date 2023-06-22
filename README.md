<table>
<tr>
<td>
<a href= "https://www2.gerdau.com.br/"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Gerdau_logo_%282011%29.svg/1200px-Gerdau_logo_%282011%29.svg.png" alt="Gerdau" border="0" width="20%"></a>
</td>
<td><a href= "https://www.inteli.edu.br/"><img src="https://www.inteli.edu.br/wp-content/uploads/2021/08/20172028/marca_1-2.png" alt="Inteli - Instituto de Tecnologia e Liderança" border="0" width="30%"></a>
</td>
</tr>
</table>

# Grupo 1 - Inspectron

## Parceiro de projeto: Gerdau

## Integrantes: 
<a href="https://www.linkedin.com/in/victorbarq/">Antonio Ribeiro</a>, <a href="https://www.linkedin.com/in/victorbarq/">Emanuele Morais</a>, <a href="https://www.linkedin.com/in/gabriela-barretto02/">Gabriela Barretto</a>, <a href="https://www.linkedin.com/in/victorbarq/">Gustavo Pereira</a>, <a href="https://www.linkedin.com/in/luca-giberti-63a4ab231/">Luca Sarhan Giberti</a>, <a href="https://www.linkedin.com/in/victorbarq/">Lyorrei Quintão</a>, <a href="https://www.linkedin.com/in/victorbarq/">Vinicius Lugli</a>

## Descrição

📜  O projeto desenvolvido consiste em um robô AGV autônomo projetado para operar em espaços confinados. Ele possui a capacidade de se locomover nesses ambientes, coletando dados por meio de sensores que medem a concentração de dióxido de carbono e compostos orgânicos voláteis presentes no ar. Além disso, o robô é equipado com tecnologia de transmissão de vídeo ao vivo e possui um sistema de detecção de rachaduras, tornando-o uma ferramenta valiosa para inspeções prévias de estruturas e execução de tarefas.


💡 Ao coletar dados sobre a concentração de dióxido de carbono e compostos orgânicos voláteis, o robô é capaz de fornecer informações importantes sobre a qualidade do ar em espaços confinados. Isso é especialmente relevante em ambientes onde a ventilação pode ser limitada ou onde a presença dessas substâncias químicas pode representar riscos à saúde.

A transmissão de vídeo ao vivo permite que os operadores visualizem as imagens capturadas pelo robô em tempo real, o que facilita a detecção de rachaduras ou danos nas estruturas. Essa funcionalidade auxilia tanto na avaliação prévia de locais de difícil acesso quanto na execução de atividades que requerem inspeção visual, fornecendo uma visão detalhada e em tempo real do ambiente.

Além das funcionalidades descritas anteriormente, o projeto inclui uma plataforma frontend integrada que permite a criação de relatórios sobre as vistorias realizadas. Essa plataforma oferece diversas opções para acessar e analisar os dados coletados pelos sensores durante as inspeções, bem como os vídeos armazenados.

### Principais features implementadas no projeto:

![image](https://github.com/2023M6T2-Inteli/Inspectron/assets/99221221/1d42e919-e5b2-4743-a699-68bf15d8b10d)


## 🛠 Estrutura de pastas
```
├── LICENSE
├── README.md
├── docs
│   ├── dev
│   ├── media
│   ├── README.md
│   ├── _config.yml
│   ├── manual_do_usuario.md
│   └── index.md
├── media
│   └── README.md
├── src
│   ├── backend
│   ├── frontend
│   ├── model
│   ├── robot
    └── README.md
```

A estrutura da pasta raiz consiste nos seguintes diretórios:

- docs: Esta pasta contém o arquivo index.md, que serve como ponto central da documentação do projeto. É aqui que os usuários podem encontrar informações detalhadas e instruções sobre o sistema.

- media: Nesta pasta estão armazenadas algumas imagens relacionadas ao sistema que são utilizadas no projeto. Essas imagens podem ser recursos visuais para ilustrar conceitos ou elementos do sistema.

- src: Essa pasta contém todo o código-fonte do sistema, pronto para ser baixado e utilizado. Ao entrar na pasta src, você encontrará quatro diretórios principais:

  - backend: Este diretório contém o código relacionado à lógica de implementação da solução. Aqui estão os arquivos e componentes responsáveis pelo processamento dos dados, gerenciamento de banco de dados, regras de negócio e qualquer outra funcionalidade relacionada ao backend.

  - frontend: Neste diretório, você encontrará a parte visual do projeto. Aqui estão os arquivos responsáveis pela interface do usuário, design, componentes de interface e interações do sistema. É aqui que os usuários podem interagir com o sistema de forma intuitiva e amigável.

  - model: Este diretório contém o código utilizado para treinar o modelo de inteligência artificial que detecta rachaduras. Aqui estão os scripts, dados de treinamento e quaisquer outros recursos relacionados ao processo de criação e treinamento do modelo.

  - robot: Este diretório contém o código que foi implementado no Turtlebot3, o robô utilizado para o MVP (Minimum Viable Product). Aqui estão os arquivos relacionados à integração do sistema com o robô, como controle de movimento, comunicação e qualquer outra funcionalidade específica do robô.

## 🛠 Instalação e configuração para Desenvolvimento

É possível encontrar informações relativas a instalação e execução do projeto no manual de usuário disponível em `doc/manual_do_usuario.md`. Demais informações relativas a desenvolvimento do projeto são encontradas em `doc/index.md`


## 📋 Licença/License

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/Spidus/Teste_Final_1">MODELO GIT INTELI</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://www.yggbrasil.com.br/vr">INTELI, VICTOR BRUNO ALEXANDER ROSETTI DE QUIROZ</a> is licensed under <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"></a></p>

