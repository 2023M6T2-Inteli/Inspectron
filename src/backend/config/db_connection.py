from mongoengine import * # Importando o módulo "mongoengine" / "mongoengine" é um módulo que permite a conexão com o banco de dados MongoDB
from dotenv import load_dotenv # Importando o módulo "load_dotenv" / "load_dotenv" é um módulo que permite o acesso às variáveis de ambiente
import os 

load_dotenv() # Carregando as variáveis de ambiente

uri = os.getenv("MONGODB_URI") # Atribuindo o valor da variável de ambiente "MONGODB_URI" à variável "uri"
#Criando uma variavel uri que recebe a string de conexão com o banco de dados MongoDB
