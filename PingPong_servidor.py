import socket
HOST = "127.0.0.1"     # Endereco IP do Servidor
PORT = 5000         # Porta que o Servidor está

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

orig = (HOST, PORT)
udp.bind(orig)

while True:	
	data, cliente = udp.recvfrom(1024)
	#print(data)
	print("Servidor recebeu de", str(cliente),":",data.decode())
	if data.decode() == "ping":   #verifica mensagem do cliente		
		udp.sendto(b"pong", cliente)	#responde pong
	elif data.decode() != "ping":
		udp.sendto(data, cliente)
	  
	
    
udp.close()
