localfile = "C:\\Users\\User\\Desktop\\teste\\Tokyo Reggie.mp3"

with open(localfile, "rb") as arquivo:
    leiturabytes = arquivo.read()
    bytearrayarquivo = bytearray(leiturabytes)


FRAMESTART = 0xff
TOTALLENGHT = len(bytearrayarquivo)

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

counter = 0

for i in range(128):
    if bytearrayarquivo[TOTALLENGHT - 128 + i] == 0:
        if counter == 0:
            print("\n")
        counter += 1
    else:
        counter = 0
        print(chr(bytearrayarquivo[TOTALLENGHT - 128 + i]), end="")







