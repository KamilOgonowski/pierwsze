import ast


pierwsza_liczba_check = False
zakonczyc_dzialanie = False
brak_pliku_do_wczytania = False

dodawanie = {}
mnozenie = {}
odejmowanie = {}
dzielenie = {}

                                            #  TO DO:
# • dodac funkcje do eksportowania poszczegolnych slowników do pliku, pozniej zlozyc wszystko w funkcje main,
# • tak aby na poczatku bylo pytanie, czy zaimportowac cache, oraz dac mozliwosc np po wpisaniu eksport do wywolania
# • funkcji eksporujacej poszegolne slowniki - na podstawie argumentu
#   zaimplementowac graficzne przedstawienie dla japonskiego mnozenia przy pomocy turtle


def eksportuj_cache(rodzaj_dzialania):
    global dodawanie, odejmowanie, mnozenie, dzielenie
    sciazka_pliku = "cache/" + rodzaj_dzialania + "_cache.txt"
    if rodzaj_dzialania == "dodawanie":
        eksport = str(dodawanie)
    elif rodzaj_dzialania == "odejmowanie":
        eksport = str(odejmowanie)
    elif rodzaj_dzialania == "mnozenie":
        eksport = str(mnozenie)
    elif rodzaj_dzialania == "dzielenie":
        eksport = str(dzielenie)
    plik = open(sciazka_pliku, "w")
    plik.write(eksport)
    print("Wyeksportowano baze obliczen dla", rodzaj_dzialania, "do pliku.")
    plik.close()


def eskportowanie():
    mozliwe_operacje = ["dodawanie", "odejmowanie", "mnozenie", "dzielenie"]
    check = input("Czy chciałbyś wyeksportować wyniki obliczeń do pliku [Tak/ Nie]?: ")
    check = check.lower()
    if check == "tak":
        co_eksportowac = input("Czy chcesz wyeksportowac wszystkie obliczenia [Tak/ Nie]?: ")
        co_eksportowac = co_eksportowac.lower()
        if co_eksportowac == "tak":
            for dzialanie in mozliwe_operacje:
                eksportuj_cache(dzialanie)
            print("Wszystkie słowniki zostaly zaktualizowane!")
            return " "
        elif co_eksportowac == "nie":
            while True:
                wybor = input("Wprowadz rodzaj obliczen do wyeksportowania [dodawanie, odejmowanie, mnozenie, "
                              "dzielenie]: ")
                wybor = wybor.lower()
                if wybor in mozliwe_operacje:
                    eksportuj_cache(wybor)
                    break
                else:
                    print("Wprowadzono nieprawidlowa wartosc dla rodzaju obliczen. Sprobuj jeszcze raz.")
    else:
        return" "


def zaimportuj_cache_konwersja(nazwa_pliku):
    global brak_pliku_do_wczytania
    try:
        with open(nazwa_pliku, "r") as plik:
            zawartosc = plik.read()
    except FileNotFoundError:
        print("Niestety plik", nazwa_pliku, "nie istnieje. Wczytywanie pliku nie powidoło się.")
        brak_pliku_do_wczytania = True
    else:
        slownik_jako_str = zawartosc
        return slownik_jako_str


def zaimportuj_cache(rodzaj_dzialania):
    global dodawanie, mnozenie, odejmowanie, dzielenie, brak_pliku_do_wczytania

    nazwa_pliku = "cache/" + rodzaj_dzialania + "_cache.txt"  # niezależnie od systemu operacyjnego (windows, linux,
    # mac) w pythonie jako separator pomiedzy folderami zawsze uzywam prawego ukosnika (mimo, że scięzki w windowsie
    # zapisaen sa w systemie z uzyciem lewego ukosnika \  ). Python sobie jakos to zamienia, a znak lewego ukosnika
    # jest znakiem specjalnym i powoduje problemy
    dzialanie = rodzaj_dzialania
    rodzaj_dzialania = zaimportuj_cache_konwersja(nazwa_pliku)
    if not brak_pliku_do_wczytania:
        original_String = rodzaj_dzialania
        # using ast.literal_eval() method
        result = ast.literal_eval(original_String)  # to jakos magicznie zamienia str z pliku spowrotem w slownik
        # orginalny kod znalazłem na str: https://favtutor.com/blogs/string-to-dict-python

        print("Zaimportowano bazę danych dla:", dzialanie + ", która ma następujące wyniki:", str(result)) # moge pozbyc
        # sie str =, zastepujac str(result) przez result

        if dzialanie == "odejmowanie":
            odejmowanie = result
        elif dzialanie == "dodawanie":
            dodawanie = result
        elif dzialanie == "mnozenie":
            dodawanie = result
        elif dzialanie == "dzielenie":
            dzielenie = result

        print("Slownik dla", dzialanie, "wyglada teraz tak:", result)
        return result
    else:
        print("Podano niepoprawną nazwe pliku:", str(dzialanie) + "_cache")
        brak_pliku_do_wczytania = False


def importowanie():
    global zakonczyc_dzialanie
    importuj = input("Czy chcesz zaimportować bazę wyników dla obliczeń? [Tak/ Nie/ q]: ")
    check = czy_q(importuj)
    if check:
        zakonczyc_dzialanie = True
        return " "
    importuj = importuj.lower()
    if importuj == "tak":
        rodzaj_dzialania = input("Wprowadz rodzaj działania [dodawanie/ odejmowanie/ dzielenie/ mnozenie]: ")
        rodzaj_dzialania = rodzaj_dzialania.lower()
        while True:
            if rodzaj_dzialania in ["dodawanie", "odejmowanie", "dzielenie", "mnozenie"]:
                zaimportuj_cache(rodzaj_dzialania)
                break
            else:
                print("Podano nieprawidłowe działanie do zaimportowania. Spróbuj jeszcze raz")
                rodzaj_dzialania = input("Wprowadz rodzaj działania [dodawanie/ odejmowanie/ dzielenie/ mnozenie]: ")
                rodzaj_dzialania = rodzaj_dzialania.lower()
                check = czy_q(rodzaj_dzialania)
                if check:
                    zakonczyc_dzialanie = True
                    return " "
                continue
    elif importuj == "nie":
        print("Użytkownik nie chec zaimportować obliczeń z pliku")
        return ""


def czy_q(tekst):
    if tekst in "Qq":
        print("Użytkownik zakończył działanie kalkulatora.")
        return True
    else:
        return False


def dzialanie():
    global zakonczyc_dzialanie
    while True:
        dzialanie = input("Jakie dzialanie mam obliczyć?: ")
        if czy_q(dzialanie):
            zakonczyc_dzialanie = True
            #  chyba dodac jeszcze cos zeby zamknac caly program
            break
        prawidlowe = False
        if dzialanie == "+" or dzialanie == "-" or dzialanie == "/" or dzialanie == "*":
            return dzialanie
        if not prawidlowe:
            print("Podano nieprawidlowy operator dzialania:", '"'+dzialanie + '".', "Sprobuj jeszcze raz ->")
            continue


def liczba_obliczenia():
    global pierwsza_liczba_check
    global zakonczyc_dzialanie
    while True:
        if not pierwsza_liczba_check:
            liczba = input("Wprowadź pierwszą liczbę dla wykonywanych obliczeń: ")
        else:
            liczba = input("Wprowadź drugą liczbę dla wykonywanych obliczeń: ")
        if czy_q(liczba):
            zakonczyc_dzialanie = True
            break
        try:
            pierwsza_liczba = int(liczba)  # wydaje mi sie, że w obu przypadkach mógłbym zastąpic pierwsza_liczba przez liczba
            pierwsza_liczba_check = True
            return pierwsza_liczba
        except ValueError:
            print(liczba, "to nie liczba!")
            continue


def dodawanie_liczb(a,b):
    return a + b


def mnozenie_liczb(a, b):
    return a * b


def odejmowanie_liczba(a, b):
    return a - b


def dzielenie_liczba(a, b):
    return a/b


def wykonaj_obliczenia(znak, pierwsza_liczba, druga_liczba):
    if znak == "+":
        wynik = dodawanie_liczb(pierwsza_liczba, druga_liczba)
    elif znak == "*":
        wynik = mnozenie_liczb(pierwsza_liczba, druga_liczba)
    elif znak == "/":
        wynik = dzielenie_liczba(pierwsza_liczba, druga_liczba)
    elif znak == "-":
        wynik = odejmowanie_liczba(pierwsza_liczba, druga_liczba)
    return wynik


def obliczenia(znak, pierwsza_liczba, druga_liczba):
    global dodawanie, mnozenie, odejmowanie, dzielenie
    if znak == "+":
        rodzaj_dzialania = dodawanie
    elif znak == "-":
        rodzaj_dzialania = odejmowanie
    elif znak == "*":
        rodzaj_dzialania = mnozenie
    elif znak == "/":
        rodzaj_dzialania = dzielenie
    if pierwsza_liczba in rodzaj_dzialania:
        if druga_liczba in rodzaj_dzialania[pierwsza_liczba]:
            print("Pobieram wynik z bazy:", pierwsza_liczba, znak, druga_liczba, "=",
                  rodzaj_dzialania[pierwsza_liczba][druga_liczba])
        else:
            wynik = wykonaj_obliczenia(znak, pierwsza_liczba, druga_liczba)
            rodzaj_dzialania[pierwsza_liczba][druga_liczba] = wynik
            if druga_liczba in rodzaj_dzialania:
                rodzaj_dzialania[druga_liczba][pierwsza_liczba] = wynik
            else:
                rodzaj_dzialania[druga_liczba] = {}
                rodzaj_dzialania[druga_liczba][pierwsza_liczba] = wynik  # dodane - moze nie dzialac
                print(rodzaj_dzialania)  # testowo - do usunięcia

    else:
        wynik = wykonaj_obliczenia(znak, pierwsza_liczba, druga_liczba)
        print(pierwsza_liczba, znak, druga_liczba, "=", wynik)
        rodzaj_dzialania[pierwsza_liczba] = {}
        rodzaj_dzialania[pierwsza_liczba][druga_liczba]= wynik
        if znak == "*" or znak == "+":
            if druga_liczba in rodzaj_dzialania:
                rodzaj_dzialania[druga_liczba][pierwsza_liczba] = wynik
            else:
                rodzaj_dzialania[druga_liczba] = {}
                rodzaj_dzialania[druga_liczba][pierwsza_liczba] = wynik
        print(rodzaj_dzialania)


def main():
    global zakonczyc_dzialanie, pierwsza_liczba_check

    importowanie()
    if zakonczyc_dzialanie:
        return " "

    while not zakonczyc_dzialanie:
        pierwsza_liczba_check = False
        operacja = dzialanie()

        if zakonczyc_dzialanie:
            eskportowanie()
            break
        pierwsza_liczba = liczba_obliczenia()
        if zakonczyc_dzialanie:
            eskportowanie()
            break
        druga_liczba = liczba_obliczenia()
        if zakonczyc_dzialanie:
            eskportowanie()
            break
        obliczenia(operacja, pierwsza_liczba, druga_liczba)


main()