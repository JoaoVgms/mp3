localfile = "Tokyo Reggie.mp3"

with open(localfile, "rb") as arquivo:
    leiturabytes = arquivo.read()
    bytearrayarquivo = bytearray(leiturabytes)


FRAMESTART = 0xff
TOTALLENGHT = len(bytearrayarquivo)

  
counter = 0
infoplaceholder = ''
info = []
titles = ['Título: ', 'Artista: ', 'Álbum: ','Comentário: ', 'Ano: ']
j = 0

for i in range(125): #Conta os últimos 128 bytes
    if bytearrayarquivo[TOTALLENGHT - 125 + i] != 0: #Caso qualquer um desses bytes seja diferente de 0...
        if counter == 0: #identifica se é o primeiro byte do bloco
            counter += 1 #incrementa o contador em 1 para cada byte encontrado.
        infoplaceholder += chr(bytearrayarquivo[TOTALLENGHT - 125 + i]) #Cria a string de informações com cada byte do bloco de informações.
    else:
        if counter != 0:
            info.append(infoplaceholder) #Adiciona a informação encontrada ao array de controle
            infoplaceholder = '' #Resete a string
            counter = 0 #reseta a quantidade de bytes encontrados
        
for index, data in enumerate(info): #Printa as informações do array de controle.
    if (index == 4): #Verifica se há um bloco de comentários. Caso não haja, pula o indice 3, que nomeia os comentários.
        print(titles[index], data, "\n")
    else:
        if(index > 2):
            print(titles[index + 1], data, "\n")
        else:
            print(titles[index], data, "\n")
   
# PROCURANDO OS HEADERS DOS FRAMES: 
last_i = 0
bytes_per_frame = []
for i in range(TOTALLENGHT - 1):
    if 0xff == bytearrayarquivo[i]:
        if 0xf0 <= bytearrayarquivo[i+1] or 0xe0 <= bytearrayarquivo[i+1]:
            # print("\n")
            # print(hex(bytearrayarquivo[i-1]), hex(bytearrayarquivo[i]), hex(bytearrayarquivo[i+1]))
            # print(f"Começo do Frame: {i}")
            bytes_per_frame.append(i-last_i)
            # print(f"Número de Bytes nesse frame: {i-last_i}")
            last_i = i
            
# for coordenada in bytes_per_frame:
#     print(coordenada)


# PROCURANDO O "XING":
for i in range(TOTALLENGHT-3):
    # print(i,bytearrayarquivo[i:i+4], sep=" - ")
    if bytearrayarquivo[i] == 0x58:
        if bytearrayarquivo[i+1] == 0x69:
            if bytearrayarquivo[i+2] == 0x6E:
                if bytearrayarquivo[i+3] == 0x67:
                    print(i)
        
'''
print(f"Primeiros 100 bytes: {bytearrayarquivo[::]}")
'''
# counter = 0

# for i in range(len(bytearrayarquivo[:10000])):
#     if bytearrayarquivo[i] == FRAMESTART:
#         counter += 1
#         print(i, end=", ")

# print(counter)


# print(bytearrayarquivo[10:])

# titulo = ''
# counter = 0
# for i in range (0, 128):
#     if bytearrayarquivo[i:i+4] == b'TIT2':
#         j = i + 5
#         while bytearrayarquivo[j: j+4] != b'TPE1':
#             if bytearrayarquivo[j:j+3] == bytearray(3):
#                 counter += 1
#             if counter == 1:
#                 titulo += chr(bytearrayarquivo[j])
#             j += 1
# print(f"Titulo: {titulo}")
# counter2 = 0

####################################################
'''
LÊ AS INFORMAÇÕES PELO HEADER DE CIMA (TRABALHAR NISSO)
DATACOORD = []
BIT = 0
while bytearrayarquivo[BIT] != FRAMESTART: #procura as coordenadas começo e fim dos bytes b'0x0'b'0x0'b'0x0', usados para delimitar informações, até encontrar um bit b'0xFF'.
    if bytearrayarquivo[BIT:BIT+3] == bytearray(3):
        DATACOORD.append(BIT) 
        DATACOORD.append(BIT + 3)
    
    BIT += 1

print(BIT)
LENDATACOORD = len(DATACOORD)
print(DATACOORD)


for n in range(LENDATACOORD): 
    print(bytearrayarquivo[DATACOORD[n - 1]:DATACOORD[n]])
'''
###################################################





