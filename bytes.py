localfile = "Sayonara Fujisan.mp3"

with open(localfile, "rb") as arquivo:
    leiturabytes = arquivo.read()
    bytearrayarquivo = bytearray(leiturabytes)


TOTALLENGHT = len(bytearrayarquivo)

# PROCURA INFORMAÇÕES (TÍTULO, AUTOR, ÁLBUM) PELO TAGv1 ==> info(bytearray[arquivo])
counter = 0
infoplaceholder = ''
info = [] # FUNÇÃO RETORNA ISSO AQUI
titles = ['Título: ', 'Artista: ', 'Álbum: ','Comentário: ', 'Ano: ']
j = 0

# No momento, vê a TAGV1. Atualizar algoritmo para TAGV2. TO DO.

for i in range(125): #Conta os últimos 125 bytes
    if bytearrayarquivo[TOTALLENGHT - 125 + i] != 0: #Caso qualquer um desses bytes seja diferente de 0...
        if counter == 0: #identifica se é o primeiro byte do bloco
            counter += 1 #incrementa o contador em 1 para cada byte encontrado.
        infoplaceholder += chr(bytearrayarquivo[TOTALLENGHT - 125 + i]) #Cria a string de informações com cada byte do bloco de informações.
    else:
        if counter != 0:
            info.append(infoplaceholder) #Adiciona a informação encontrada ao array de controle
            infoplaceholder = '' #Reseta a string
            counter = 0 #reseta a quantidade de bytes encontrados
        
for index, data in enumerate(info): #Printa as informações do array de controle.
    if (index == 4): #Verifica se há um bloco de comentários. Caso não haja, pula o indice 3, que nomeia os comentários.
        print(titles[index], data, "\n")
    else:
        if(index > 2):
            print(titles[index + 1], data, "\n")
        else:
            print(titles[index], data, "\n")




# PROCURANDO OS HEADERS DOS FRAMES: ==> frames(bytearray(arquivo))

last_frame_found = 0
bytes_per_frame = []
frame_indexes = [] #FUNÇÃO RETORNA ISSO AQUI
for i in range(100000):
    if 0xff == bytearrayarquivo[i]:
        if (0xf0 <= bytearrayarquivo[i+1] or 0xe0 <= bytearrayarquivo[i+1]) and 0xff > bytearrayarquivo[i+1]:
            print("\n")
            print(hex(bytearrayarquivo[i-1]), hex(bytearrayarquivo[i]), hex(bytearrayarquivo[i+1]))
            print(f"Começo do Frame: {i}")
            bytes_per_frame.append(i-last_frame_found)
            frame_indexes.append(i)
            print(f"Número de Bytes no último frame: {i-last_frame_found}")
            last_frame_found = i

for i in range(len(frame_indexes) - 1):
    print(f"{frame_indexes[i]}, {bytes_per_frame[i + 1]}") # Melhorar esse cara. No momento o índice I tem a localização do frame em um array e o tamanho do frame anterior no outro array.
            
# for frame_length in bytes_per_frame:
#     print(frame_length)

print(f"Localização do primeiro frame: {frame_indexes[0]}")

# PROCURANDO O "Xing": bitratetype(bytearray(arquivo))
print(f"{frame_indexes[i]}, {bytes_per_frame[i]}")

for i in range(TOTALLENGHT-3):
    if bytearrayarquivo[i:i+4] == bytearray(b'Xing'):
        print(f"Localização do Xing: {i}")
        break
        
print(len(frame_indexes))
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
LÊ AS INFORMAÇÕES PELAS TAGSv2 (TODO)
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





