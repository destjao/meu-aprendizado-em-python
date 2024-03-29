numeros = [3, 13, 24, 76, 70, 101, 130, 152, 176, 200, 1,
            53, 7, 134, 173, 171, 158, 27, 51, 22, 5, 95,
              103, 194, 72, 170, 122, 141, 197, 45, 2, 192,
                107, 155, 84, 128, 36, 99, 125, 189, 63, 47,
                  109, 127, 14, 73, 33, 157, 50, 146, 23, 4,
                    6, 19, 15, 20, 28, 187, 9, 26, 46, 34, 126,
                      164, 168, 196, 43, 59, 105, 15, 86, 60, 61,
                        62, 64, 65, 66, 67, 68, 69, 71, 12, 8, 199,
                          40, 10, 25, 41, 89, 123, 198, 21, 11, 49, 74,
                            16, 37, 57, 29, 75, 18, 133, 104, 80, 100,
                              102, 17, 31, 32, 19, 42, 44, 92, 35, 38,
                                39, 48, 52, 54, 55, 56, 58, 77, 78, 79,
                                  81, 88, 111, 120, 124, 139, 140, 144,
                                    150, 160, 166, 169, 178, 180, 188, 190,
                                      191, 215, 93, 85, 87, 30, 82, 83, 149,
                                        96, 156, 154, 163, 220, 112, 113, 114,
                                          115, 116, 117, 118, 119, 121, 131, 153,
                                            98, 137, 97, 147, 161, 162, 94, 148, 129,
                                              135, 165, 151, 177, 132, 106, 108, 172,
                                                174, 179, 181, 182, 184, 185, 183, 195,
                                                  193, 142, 143, 145, 90, 175, 159, 167,
                                                    175, 186, 138, 91, 233, 250, 214, 301,
                                                      305, 400, 222, 201, 211, 202, 203, 204,
                                                        205, 206, 207, 208, 302, 303, 314, 348,
                                                          373, 364, 304, 392, 390, 281, 271, 395,
                                                            399, 244, 245, 246, 247, 371, 280, 210,
                                                              336, 315, 243, 351, 352, 353, 354, 355,
                                                                356, 357, 358, 359, 360, 209, 315, 213,
                                                                  254, 227, 318, 324, 334, 212, 322, 221, 
                                                            242, 316, 298, 300, 386, 307, 223, 224, 
                                                        299, 277, 310, 230, 297, 219, 337, 323, 340,
                                                    241, 344, 253, 275, 282, 225, 226, 288, 218,
                                            311, 262, 377, 285, 216, 217, 228, 240, 279,
                                    397, 285, 398, 266, 231, 232, 229, 248, 249,
                            265, 239, 252, 313, 234, 296, 286, 273, 274, 238, 
                       236, 333, 261, 263, 264, 265, 267, 268, 269, 270, 
           235, 239, 251, 391, 394, 335, 320, 284, 372, 283,
    255, 290, 257,  258,  259, 260, 256, 136,339,110,367,389]  # Substitua [...] pela sua lista de números

numeros_faltantes = sorted(set(range(1, 401)) - set(numeros))

print("Os números faltantes na sequência de 1 a 400 são:")
for num in numeros_faltantes:
    print(num, 'LIVRE')
print("\nO total de números faltantes é:", len(numeros_faltantes))


# from random import randint

# pessoas_numeros = {
#     "Zé": [3, 13, 24, 76, 70, 101, 130, 152, 176, 200, 90, 175, 159, 167, 175, 186, 138, 91],
#     "Dedé": [1, 53, 7, 134, 173, 171, 158, 27, 51, 22],
#     "Carol": [5, 95, 103, 194, 72, 170, 122, 141, 197, 45],
#     "Meire": [2, 192, 107, 155, 84, 128, 36, 99, 125, 189, 324, 334, 212, 322, 221, 242, 316, 298, 300, 386],
#     "Rosângela": [63, 47, 109, 127],
#     "Ciene": [14, 73, 33, 157, 50, 146],
#     "Loriene": [23],
#     "Karen": [4],
#     "Leninha amiga": [6, 19],
#     "Josy": [15, 20],
#     "Leila": [28, 187],
#     "Selma": [9, 26, 46],
#     "Neinha": [34, 126, 164, 168, 196, 43, 59, 105, 15, 86],
#     "Félix": [60, 61, 62, 64, 65, 66, 67, 68, 69, 71],
#     "Mara": [12, 8],
#     "Cleide": [199, 40],
#     "Graciele Daher": [10, 25, 41, 89, 123, 198],
#     "Katia": [21, 11],
#     "Lidiane": [49, 74],
#     "Lucilene (irmã de Arlete)": [16, 37, 57],
#     "Sandra Silva": [29, 75, 18, 133],
#     "Wesley": [104, 80],
#     "Larissa Silvano": [100, 102],
#     "Picida": [17, 31, 32, 19, 42, 44, 92, 35, 38, 39, 48, 52, 54, 55, 56, 58, 77, 78, 79, 81],
#     "Ivete/Gean": [88, 111, 120, 124, 139, 140, 144, 150, 160, 166, 169, 178, 180, 188, 190, 191, 215, 93, 85, 87],
#     "Ana Paula": [30, 82],
#     "Letícia": [83],
#     "Luana": [149, 96],
#     "Amarílis": [156, 154, 163, 220],
#     "Getúlio": [112, 113, 114, 115, 116, 117, 118, 119, 121, 131],
#     "Rita": [153, 98, 137, 209, 315],
#     "Tati": [97, 147, 279, 397],
#     "Gustavo": [161, 162, 94],
#     "Diego": [148, 129, 135],
#     "Eliane zé": [165, 151],
#     "Cissa": [177, 132],
#     "Mateus": [106, 108],
#     "Edson": [172, 174, 179, 181, 182, 184, 185, 183, 195, 193],
#     "Vivian": [142, 143, 145],
#     "Jú": [233, 250],
#     "Cadu": [214, 301, 305, 400],
#     "Jaqueline(Jú)": [222],
#     "Paloma Gabriela": [201, 211],
#     "Leonardo Barros": [202, 203, 204, 205, 206, 207, 208, 302, 303, 314, 348, 373, 364, 304, 392, 390, 281, 271, 395, 399],
#     "Amiga de Picida": [244, 245, 246, 247],
#     "Vinícius Xavier": [371, 280, 210, 336],
#     "José Baracho": [315, 243],
#     "João": [351, 352, 353, 354, 355, 356, 357, 358, 359, 360],
#     "Arlete": [213, 254, 227, 318],
#     "Jusciele": [307],
#     "Karina": [223, 224],
#     "Igor": [299, 277],
#     "Marcela": [310],
#     "Antônio": [230],
#     "Juliana": [297],
#     "Guilherme": [219, 337, 323],
#     "Alexandre": [340, 241],
#     "Adelson": [344, 253, 275, 282],
#     "Marreta": [225, 226],
#     "Vitor": [288],
#     "Fernando": [218, 311],
#     "André": [262, 377],
#     "Joyce": [285],
#     "Guilu": [216, 217],
#     "Irene": [228, 240],
#     "Gilmar": [285],
#     "Naty (amiga de Rosangela)": [398, 266],
#     "Paulo": [231, 232],
#     "Otávio": [229, 248, 249, 296, 286],
#     "Sérgio": [265, 239],
#     "Tiago": [252, 313],
#     "Marrom": [234],
#     "Gleice": [273, 274],
#     "Rafael vazada": [238, 236, 333],
#     "Angelo": [261, 263, 264, 265, 267, 268, 269, 270],
#     "Papai": [235, 239, 251, 391, 394, 335, 320, 284, 372, 283],
#     "Thais": [256, 367, 243],
#     "Andréia Letícia": [325, 389, 292, 339],
#     "Giliard": [255, 290, 257, 258, 259, 260]
# }


# def encontrar_dono(numero):
#     for pessoa, numeros in pessoas_numeros.items():
#         if numero in numeros:
#             return pessoa
#     return None

# numero = randint(1,400)
# dono = encontrar_dono(numero)


# if dono is not None:
#     print(f"O número sorteado foi {numero} é o ganhador e {dono}!! Obrigado por participar <3")
# else:
#     print(f"Desculpe, o número {numero} não foi encontrado.")
