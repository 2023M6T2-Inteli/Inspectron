# Importando o módulo "mongoengine" / "mongoengine" é um módulo que permite a conexão com o banco de dados MongoDB
from mongoengine import connect

# Importando o módulo "load_dotenv" / "load_dotenv" é um módulo que permite o acesso às variáveis de ambiente
from dotenv import load_dotenv

import os
import logging
import sys

load_dotenv()  # Carregando as variáveis de ambiente

def connect_to_database():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    logger = logging.getLogger("uvicorn")
    
    console_handler = logging.StreamHandler(sys.stdout)
    logger.addHandler(console_handler)
    
    try:
        # Atribuindo o valor da variável de ambiente "MONGODB_URI" à variável "uri"
        #Para Funcionar, crie um file chamado ".evn" e passe a senha do banco de dados como uma variavel.
        uri = os.getenv("MONGODB_URI")

        connect(host=uri)
        logger.info("Conexão com o banco de dados estabelecida com sucesso")
    except:
        logger.info("Não foi possível conectar-se ao banco de dados")
        exit(1)
