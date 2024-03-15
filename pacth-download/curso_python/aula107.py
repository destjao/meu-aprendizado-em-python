
l1 = ['Salvador', 'São Paulo', 'Belo Horizonte', 'Rio Branco', 'Maceió', 'Macapá', 'Manaus', 'Fortaleza', 'Brasília', 'Vitória', 'Goiânia', 'São Luís', 'Cuiabá', 'Campo Grande', 'Belém', 'João Pessoa', 'Curitiba', 'Recife', 'Teresina', 'Natal', 'Porto Alegre', 'Porto Velho', 'Boa Vista', 'Florianópolis', 'Aracaju', 'Palmas', 'Rio de Janeiro']
l2 = ['BA', 'SP', 'MG', 'AC', 'AL', 'AP', 'AM', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'PA', 'PB', 'PR', 'PE', 'PI', 'RN', 'RS', 'RO', 'RR', 'SC', 'SE', 'TO', 'RJ']


print(list(zip(l1, l2)))


# def zipper(list1, list2):
#     min_list = (min(len(list1), len(list2)))
#     return [
#         (list1[i], list2[i]) for i in range(min_list)
#     ]

# print(zipper(l1, l2))

list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = [1, 2, 3, 4]

list_sum = [x + y for x, y in zip(list1, list2)]
print(list_sum)

# list_sum = []
# for i in range(len(list2)):
#     list_sum.append(list1[i] + list2[i])

# print(list_sum)

# list_sum = []
# for i, _ in enumerate(list2):
#     list_sum.append(list1[i] + list2[i])

# print(list_sum)