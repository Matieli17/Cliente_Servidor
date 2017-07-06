import socket
import timeit
import time

HOST = "127.0.0.1"  # Endereco IP do Cliente
PORT = 5001           # Porta que o Cliente está

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)
server = ('127.0.0.1', 5000)

print ("Digite S para sair")
udp.bind(dest)
msg = input("> ")
while True:
	'''ti = round((time.clock())*1000) também serve no windows para medir o tempo em milisegundos, 
	porém, em qualquer plataforma o módulo timeit.default_timer() mede o tempo real.'''
	ti = ((timeit.default_timer())*1000) 
	udp.sendto(msg.encode(), server)
	data, cliente = udp.recvfrom(1024)
	tf = ((timeit.default_timer())*1000)
	if msg == "ping":
		print("Servidor",str(cliente),"responde: ",data.decode())
		print("Tempo: ",tf-ti,"ms")
		msg = input("> ")
	elif msg == "S":
		break
	else:
		msg = input("> ")
		
    
udp.close()
