# Importando o módulo "mongoengine" / "mongoengine" é um módulo que permite a conexão com o banco de dados MongoDB
from mongoengine import connect

# Importando o módulo "load_dotenv" / "load_dotenv" é um módulo que permite o acesso às variáveis de ambiente
from dotenv import load_dotenv
from .logger import Console

import os

load_dotenv()  # Carregando as variáveis de ambiente

def connect_to_database():
    try:
        # Atribuindo o valor da variável de ambiente "MONGODB_URI" à variável "uri"
        uri = os.getenv("MONGODB_URI")

        connect(host=uri)
        Console.log("Conexão com o banco de dados estabelecida com sucesso")
    except:
        Console.log("Não foi possível conectar-se ao banco de dados")
        exit(1)
