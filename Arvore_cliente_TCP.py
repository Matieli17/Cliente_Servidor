import socket

HOST = "127.0.0.1"  # Endereco IP do Servidor
PORT = 80           # Porta do servidor

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((HOST, PORT))

resp = input("Prefixo > ")
while True:
	resp = str(resp)
	cliente.send(resp.encode())
	data = cliente.recv(1000000) 
	resp = data.decode()
	print(resp)
	resp = input("Ip > ")

cliente.close()
	
