def cria_arvore_0_8(prefixo):
  cont = prefixo 
  x = prefixo 
  y = 0
  tupla = []
  
  lista_pre = []
  if cont == 0:
    x += 1
    lista_pre.append(0)
    cont += 1
    h = 256/(2**x)
    while y < 256:
      y += h
      if y != 256:
        lista_pre.append(int(y))
    
    prefixo +=1 
    #print ("Seus possíveis IPs:")
    tupla.append(("0" ,"/0"))
    for i in range(len(lista_pre)):
      tupla.append((lista_pre[i],prefixo))
  
  
  while cont < 8:
    c = cont + 1
    y = 0
    lista_cont = []
    lista_cont.append(0)  
    while y < 256:
      h = 256/(2**c)
      y += h
      if y != 256:
        lista_cont.append(int(y))
    cont += 1
    for i in range(len(lista_cont)):
      tupla.append((lista_cont[i],cont))
  return tupla      

########################################################################

def cria_arvore_8_16(prefixo, ipx):
  cont = prefixo
  x = prefixo - 7
  y = 0
  cont2 = 0
  tupla = []
  
  while cont2 <= 0:
    for j in range(len(ipx)):
      if ipx[j] == ".":
        fim = j
        cont2 += 1
  
  lista_pre = []
  if cont == 8:
    lista_pre.append(0)
    cont += 1
    h = 256/(2**x)
    while y < 256:
      y += h
      if y != 256:
        lista_pre.append(int(y))


    prefixo +=1 
    #print ("Seus possíveis IPs:")
    tupla.append(("0" ,"/8"))
    for i in range(len(lista_pre)):
      tupla.append((lista_pre[i],prefixo))
  
  
  while cont < 15:
    c = cont - 7
    y = 0
    lista_cont = []
    lista_cont.append(0)  
    while y < 256:
      h = 256/(2**c)
      y += h
      if y != 256:
        lista_cont.append(int(y))
    cont += 1
    for i in range(len(lista_cont)):
      tupla.append((lista_cont[i],cont))
  return tupla
  

########################################################################

def cria_arvore_16_24(prefixo,ipx):
  cont = prefixo
  x = prefixo - 15
  y = 0
  cont2 = 0
  tupla = []
  
  while cont2 <= 1:
    for j in range(len(ipx)):
      if ipx[j] == ".":
        fim = j
        cont2 += 1

  lista_pre = []
  if cont == 16:  
    lista_pre.append(0)
    cont += 1
    h = 256/(2**x)
    while y < 256:
      y += h
      if y != 256:
        lista_pre.append(int(y))

    prefixo +=1 
    #print ("Seus possíveis IPs:")
    tupla.append(("0" ,"/16"))
    for i in range(len(lista_pre)):
      tupla.append((lista_pre[i],prefixo))
  
  
  while cont < 23:
    c = cont - 15
    y = 0
    lista_cont = []
    lista_cont.append(0)  
    while y < 256:
      h = 256/(2**c)
      y += h
      if y != 256:
        lista_cont.append(int(y))
    cont += 1
    for i in range(len(lista_cont)):
      tupla.append((lista_cont[i],cont))
 
  return tupla


########################################################################

def cria_arvore_24_low(prefixo,ipx):
  cont = prefixo
  x = prefixo - 23
  y = 0
  tupla = []
  
  for j in range(len(ipx)):
    if ipx[j] == ".":
        fim = j
  
  lista_pre = []
  if cont == 24:
    lista_pre.append(0)
    cont += 1
    h = 256/(2**x)
    while y < 256:
      y += h
      if y != 256:
        lista_pre.append(int(y))
    prefixo +=1 
    #print ("Seus possíveis IPs:")
    tupla.append(("0","/24"))
    for i in range(len(lista_pre)):
      tupla.append((lista_pre[i],prefixo))
  
  
  while cont < 30:
    c = cont - 23
    y = 0
    lista_cont = []
    lista_cont.append(0)
    while y < 256:
      h = 256/(2**c)
      y += h
      if y != 256:
        lista_cont.append(int(y))
    cont += 1
    for i in range(len(lista_cont)):
      tupla.append((lista_cont[i],cont))
      
  return tupla
  

  
#######################################################################



def arvore2(pre,ip):
	
	while pre >= 30:
		print("Prefixo inválido!")
		pre = int(input("Digite o prefixo: "))
	conti = 0
	for E in range(len(ip)):
		if ip[E] == ".":
			conti += 1
	while conti < 3:
		print("Ip inválido!")
		ip = input("Digite o IP:")
		conti = 0
		for  E in range(len(ip)):
			if ip[E] == ".":
				conti += 1

	if pre >= 24:
		arvore = cria_arvore_24_low(pre,ip)
		return arvore 
	elif pre >=16:
		arvore2 = cria_arvore_16_24(pre,ip)
		pre = 24
		arvore = cria_arvore_24_low(pre,ip)
		return arvore2,arvore 
	elif pre >= 8:
		arvore3 = cria_arvore_8_16(pre,ip)
		pre = 16
		arvore2 = cria_arvore_16_24(pre,ip)
		pre = 24
		arvore = cria_arvore_24_low(pre,ip) 
		return arvore3,arvore2,arvore
	else:
		arvore4 = cria_arvore_0_8(pre)
		pre = 8
		arvore3 = cria_arvore_8_16(pre,ip)
		pre =16
		arvore2 = cria_arvore_16_24(pre,ip)
		pre = 24
		arvore = cria_arvore_24_low(pre,ip)
		return arvore4,arvore3,arvore2,arvore

