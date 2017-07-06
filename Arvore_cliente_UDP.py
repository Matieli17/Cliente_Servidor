import socket
import timeit
import time

HOST = "127.0.0.1"  # Endereco IP do Cliente
PORT = 5001           # Porta que o Cliente está

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)
server = ('127.0.0.1', 65000)

print ("Digite S para sair")
udp.bind(dest)
resp = input("Prefixo > ")
while True:
	'''ti = round((time.clock())*1000) também serve no windows para medir o tempo em milisegundos, 
	porém, em qualquer plataforma o módulo timeit.default_timer() mede o tempo real.'''
	#ti = round((timeit.default_timer())*1000) 
	resp = str(resp)
	udp.sendto(resp.encode(), server)
	data, cliente = udp.recvfrom(1000000) #len(resp.decode())
	#tf = round((timeit.default_timer())*1000)
	resp = data.decode()
	print(resp)
	#print("Tempo: ",tf-ti,"ms")
	resp = input("Ip > ")
	
	

		
    
udp.close()
