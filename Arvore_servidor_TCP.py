import socket
from arvore  import arvore2

HOST = "127.0.0.1"     # Endereco IP do Servidor
PORT = 80         # Porta que o Servidor está

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP
orig = (HOST, PORT)
servidor.bind(orig)
servidor.listen(5)

while True:	
	conexao, cliente = servidor.accept()
	print("Servidor conectado a", str(cliente))
	data = conexao.recv(1024)
	datadec = data.decode()
	print(datadec)
	print(len(datadec))
	if len(datadec) < 3 :
		prefixo = int(datadec)
		conexao.send(b"Informe o IP: ")
		ip = conexao.recv(1024)
		ipdec = ip.decode()
		arvore = arvore2(prefixo, ipdec)
		arvore = str(arvore)
		#print(arvore)
		conexao.send(arvore.encode())

servidor.close()
