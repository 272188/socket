import socket
host = 'localhost'
port = 8005
addr = ((host, port)) #define a tupla de endereco
serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #cria o socket
serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #realiza o socket
serv_socket.bind(addr)  #define a porta e quais ips podem se conectar com o servidor
serv_socket.listen(10)  #define o limite de conexoes
print ('aguardando conexao...')
con, cliente = serv_socket.accept()   #servidor aguardando conexao
print('conectado')
print('aguardando mensagem...')

enviar = ''
while(enviar != 'sair'):
    recebe = con.recv(1024)  #define que os pacotes recebidos sao de ate 1024 bytes
    print('mensagem recebida: ' + recebe.decode())
    enviar = input('digite uma mensagem para enviar ao cliente: ')
    con.send(enviar.encode())
serv_socket.close() #fecha conexao
