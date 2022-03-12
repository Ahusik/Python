#Przykład 1
#Wersja z pentlą
# a = []
# for x in range(10):
#     a.append(x**2)
# print(a)
# b = []
# for y in range(6):
#     b.append(3**y)
# print(b)
# c = []
# for z in a:
#     if z % 2 == 1:
#         c.append(z)
# print(c)

#Wersja z comprehension
# a = [x ** 2 for x in range(10)]
# b = [3 ** i for i in range(6)]
# c = [x for x in a if x % 2 == 1]
# print(a)
# print(b)
# print(c)
#
#Przykład 2
# Wersja z petlą
# liczby = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# lista = []
# for i in liczby:
#     if i % 2 == 0:
#         lista.append(i)
# print("Liczby parzyste uzyskane z wykorzystaniem pętli")
# print(lista)
# print()

# Wersja z comprehension
# lista2 = [i for i in liczby if i % 2 == 0]
# print(lista2)

# Przykład 3
#Wersja z zangieżdżeniem pętlami
# lista = []
# for i in [1, 2, 3]:
#     for j in [4, 5, 6]:
#         lista.append((i, j))
# print(lista)

#Wersja z comprehension
# lista2 = [(i, j) for i in [1, 2, 3] for j in [4, 5, 6]]
# print(lista2)

#Przykład 4
#Wersja z pętlą
# skroty = {"PZU":"Państwowy zakład ubezpieczeń",
#           "ZUS":"Zakład ubezpieczeń społęczności",
#           "PKO":"Państwowa kasa oszczędności"}
# odwrocone= {}
# for key,value in skroty.items():
#     odwrocone[value] = key
# print(odwrocone)
#Wersja z comprehension
# odwrocone2 = {value: key for key, value in skroty.items()}
# print(odwrocone2)

#Funkcje podprogramy matlaby
# import math
# def row_kwadratowe(a,b,c):
#     delta = b** 2 - 4 * a * c
#     if delta < 0:
#         print("Brak pierwiastków")
#         return -1
#     elif delta == 0:
#         print("jeden pierwiastek")
#         x = (-b) / (2 * a)
#         return x
#     else:
#         print("dwa pierwiastki")
#         x1 = (-b - math.sqrt(delta))/(2*a)
#         x2 = (-b + math.sqrt(delta))/(2*a)
#         return x1,x2
# print(row_kwadratowe(6,1,3))
# print(row_kwadratowe(1,2,1))
# print(row_kwadratowe(1,4,1))
#Przykład drugi
# import math
#
# def dlugosc_odcinka(x1=0, y1=0, x2=0,y2=0):
#     return math.sqrt((x2-x1)**2+(y2-y1)**2)
#Funcka dla wartosci domyślnych
# print(dlugosc_odcinka())
#Dla Własnych podanych wartości
# print(dlugosc_odcinka(1,2,3,4))
#Intepretowane są jako x1 i y1 jako podane w definicji
# print(dlugosc_odcinka(2,2,y2=2,x2=1))

#Przykład trzeci
# def ciag(* liczby):
    # jeżeli nie ma argumentów to
    # if len(liczby) == 0:
    #     return 0
    # else:
    #     suma= 0
        #sumujemy elementy ciągu
        # for i in liczby:
        #     suma += i
        #zwracamy wartość sumy
        # return suma
# print(ciag())
# print(ciag(1,2,3.5,4,5,6,7,8))

#Przykład czwarty
# def to_lubie(** rzeczy):
#     for cos in rzeczy:
#         print("To jest")
#         print(cos)
#         print("co lubie")
#         print(rzeczy[cos])
#
# to_lubie(slodycze="czekolada", rozrywka=['gry','filmy'])
#
# #Moduły i pakiety


#Zad 1
import random

# a = [1-x for x in range(1,10)]
# b = [4 ** i for i in range(8)]
# c = [x for x in b if x % 2 == 0]
# print(a)
# print(b)
# print(c)

#Zad 2
# lista = []
# print("Losowe liczby")
# for i in range(10):
#     lista.append(random.randint(0,100))
# print(lista)
# print()
# lista2 = [i for i in lista  if i % 2 == 0]
# print(lista2)

#Zad 3
# slownik = {"ziemniak":"kg",
#            "banan":"kg",
#            "pomidor":"szt",
#            "kalafior":"szt",
#            "sałata":"szt",
#            "cebula":"kg"}
# lista1= {}
# for value,key in slownik.items():
#     lista1[value] = key
# print(lista1)
# lista2= {key: value for key, value in slownik.items()}
# print(lista2)
#DOKONCZYC
