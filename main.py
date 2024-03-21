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
# produkty_spozywcze = {
#     "jabłka": "kg",
#     "chleb": "sztuki",
#     "jajka": "sztuki",
#     "pomarańcze": "kg",
#     "ziemniaki": "kg",
#     "cukier": "kg",
#     "ryż": "kg",
# }
#
# produkty_sztuki = {produkt: jednostka for produkt, jednostka in produkty_spozywcze.items() if jednostka == "sztuki"}
#
# print("Produkty spożywcze, których jednostką są sztuki:")
# print(produkty_sztuki)

# Zad. 4
# def czy_trojkat_prostokatny(a, b, c):
#     if a < b:
#         a, b = b, a
#     if a < c:
#         a, c = c, a
#
#     if a ** 2 == b ** 2 + c ** 2:
#         return True
#     else:
#         return False
#
# a = float(input("Podaj długość pierwszego boku trójkąta: "))
# b = float(input("Podaj długość drugiego boku trójkąta: "))
# c = float(input("Podaj długość trzeciego boku trójkąta: "))
#
#
# if czy_trojkat_prostokatny(a, b, c):
#     print("Trójkąt o podanych bokach jest trójkątem prostokątnym.")
# else:
#     print("Trójkąt o podanych bokach nie jest trójkątem prostokątnym.")

# Zad. 5
# def pole_trapezu(a=5, b=7, h=4):
#
#     pole = 0.5 * (a + b) * h
#     return pole
#
# print("Pole trapezu:", pole_trapezu())
# print("Pole trapezu:", pole_trapezu(3, 6, 5))

# Zad. 6
# def iloczyn_ciagu(a=1, b=4, ile=10):
#
#     wynik = a
#     for _ in range(1, ile):
#         wynik *= b
#     return wynik
#
# print("Iloczyn ciągu:", iloczyn_ciagu())
# print("Iloczyn ciągu:", iloczyn_ciagu(2, 3, 5))

# Zad. 7
import math

try:
    liczba = float(input("Podaj liczbę: "))
    if liczba < 0:
        raise ValueError("Podano liczbę ujemną.")
    pierwiastek = math.sqrt(liczba)
    print("Pierwiastek z", liczba, "to:", pierwiastek)
except ValueError as e:
    print("Błąd:", e)
