import socket

HOST = "127.0.0.1"  # localhost padrão
PORT = 65432  # Porta a ser utilizada

#iniciando o socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #Associa um endereço a um socket. O primeiro parâmetro é o endereço IP e o segundo é o número da porta.
    s.bind((HOST, PORT))
    #O método listen() coloca o socket em modo servidor e aceita conexões.
    s.listen()
    #Aceita uma conexão de entrada e retorna um novo objeto de socket e o endereço do cliente.
    conn, addr = s.accept()

    with conn:
        print(f"Connected by {addr}")
        while True:
            #recebe dados do socket
            data = conn.recv(1024)
            if not data:
                break
            #semelhante à função send(), mas garante que todos os dados sejam enviados através do socket. A função continua tentando enviar os dados até que todos tenham sido enviados ou ocorra um erro.
            conn.sendall(data)