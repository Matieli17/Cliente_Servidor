import socket
from arvore  import arvore2

HOST = "127.0.0.1"     # Endereco IP do Servidor
PORT = 65000         # Porta que o Servidor está

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

orig = (HOST, PORT)
udp.bind(orig)
#print(arvore2(24,"0.0.0.0"))
while True:	
	data, cliente = udp.recvfrom(1024)
	#print(data)
	print("Servidor recebeu de", str(cliente),":", data.decode())
	#resp = int(data.decode())
	#print(resp)
	if len(data.decode()) <= 2  :
		prefixo = int(data.decode())
		udp.sendto(b"Informe o IP: ", cliente)
	else: #data.decode() >= "0.0.0.0" and data.decode() <= "255.255.255.255":
		ip = data.decode()
		arvore = arvore2(prefixo, ip)
		arvore = str(arvore)
		udp.sendto(arvore.encode(), cliente)
