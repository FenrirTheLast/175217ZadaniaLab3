# # Zad.1
#
# A = {1 - x for x in range(1, 11)}
# B = {4 ** i for i in range(1,8)}
# C = {x for x in B if x % 2 == 0}
#
# print(A)
# print(B)
# print(C)


# Zad.2
#
# import random
#
# list1 = [random.randint(1, 60) for _ in range(10)]
# parzyste_elementy = [x for x in list1 if x % 2 == 0]
#
# print('Losowe elementy:', list1)
# print("Parzyste elementy", parzyste_elementy)

# Zad.3

produkty_sporzywcze = {"mandarynka": "kg", "cukierki": "kg", "masło": "sztuki", "sałatka umyta": "sztuki", "jajak": "sztuki"}
produkty_sztuki = [produkt for produkt jednostka in produ ]