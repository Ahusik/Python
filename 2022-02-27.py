import sys
import math

print(sys.version)
#if waruenk1:
#-instrukcja lub blok instrukcji dla warunek1
#elif warunek2:
#-instrukcja lub blok instrukcji
#elif warunekn:
#-instrukcja lub blok instrukcji
#else:
#-instrukcje gdy warunki niespełnione
# x == y , x-y, x>y, x<y, x>=y, x<=y
#a = 7
#b = 5

#if a > b:
    #print('liczba a jest wiekszą od b')
#elif a < b:
    #print('Liczba a jest mniejszą od b')
#else:
    #print('liczby sa równe')
#a = input("podaj liczbę a: ")
#b = input("podaj liczbę b: ")
#c = input("podaj liczbę c: ")
#d = input("podaj liczbe d: ")
#print(a)
#print(type(a))
#a = int(a)
#b = int(b)
#c = int(c)
#d = int(d)
#print(type(a))
#if  (a > b) & (c > d):
    #print('liczba a jest większa od liczby b i liczba c jest większa od liczby d')
#else:
    #print('liczba a jest mniejsza niż liczba b lub liczba c jest mniejsza od d')

#for: licznik in sekwencja
#-instrukcja lub blok instrukcji
#else:
#-instrukcja po zakończeniu działania pętli
# range(start,stop,step)
# for (int i=0, i<10, i++)

#for i in range(0, 7, 1):
    #print(i)

# lista = ['cos', 3, 4, 5.6]
# for element in lista:
#     print(element)
# else:
#     print('wyświetlono wszystkie elementy listy')
#pętrla while
#while warunek:
#   instrukcja lub blok instrukcji
#else:
#   instrukcja po zakończeniu działania pętli

# z = 0
# while z != 11:
#     print(z)
#     z += 1
# else:
#     print('wyświetlono ' + str(z) + ' liczb')

# lista = [4, 6, 2, 3, 5, 9, 1]
# liczba = input('podaj liczbe: ')
# licznik = 0
# while licznik != len(lista):
#     if int(liczba) - lista[licznik] == 0:
#         print(liczba + '- ' + str(lista[licznik]) + ' - 0')
#         break
#     else:
#         licznik += 1
#
# lista1 = [4, 6, 2, 3, 5, 9, 1]
# lista2 = [7, 3, 4, 6]
# suma = []
# for a in lista1:
#     for b in lista2:
#         wynik = a + b
#         suma.append(wynik)
#     print(suma)

#try:
#   blok instrukcji
#except: nazwa błedu
#   blok instrukkcji po napotkaniu błędu
#else:
#   instukcje bez błedu
#
# liczba1 = input("podaj pierwszą liczbę: ")
# liczba2 = input("Podaj drugą liczbe: ")
#
# try:
#     liczba1 = int(liczba1)
#     liczba2 = int(liczba2)
#     wynik = liczba1 / liczba2
#     print("wynik działania = " + str(wynik))
# except ZeroDivisionError:
#     print('nie można dzielić przez 0')
# except ValueError:
#     print('Nie wczytano liczby całkowitej')
#
#lista =[]
#słownik = {}
#klucz wartość -- 1 element słownika
#słownik ={1, 10},'klucz','wartość'{1 20}

kontakty = {"Łukasz" : 843993292, "Tomek" : 574939024, "Mateusz" : 536294849}
del kontakty["Tomek"]
for imie in kontakty:
    print("%s ma numer telefonu: %d" % (imie, kontakty[imie]))
