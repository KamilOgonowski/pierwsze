while True:
    dzialanie = input("Jakie dzialanie? ")
    if dzialanie == "q":
        break
    prawidlowe = False
    if dzialanie == "+" or dzialanie == "-" or dzialanie == "/" or dzialanie == "*":
        prawidlowe = True
    if not prawidlowe:
        print("Podano nieprawidlowy operator dzialania:", dzialanie + ".", "Sprobuj jeszcze raz")
        continue

    pierwszaLiczbaTekst = input("Jaka pierwsza liczba? ")
    if pierwszaLiczbaTekst == "q":
        break
    try:
        pierwszaLiczba = int(pierwszaLiczbaTekst)
    except:
        print(pierwszaLiczbaTekst, "to nie liczba!")
        continue

    drugaLiczbaTekst = input("Jaka druga liczba? ")
    if drugaLiczbaTekst == "q":
        break
    try:
        drugaLiczba = int(drugaLiczbaTekst)
    except:
        print(drugaLiczbaTekst, "to nie liczba!")
        continue

    if dzialanie == "+":
        print(pierwszaLiczba, "+", drugaLiczbaTekst, "=", pierwszaLiczba + drugaLiczba)
    if dzialanie == "-":
        print(pierwszaLiczba, "-", drugaLiczbaTekst, "=", pierwszaLiczba - drugaLiczba)
    if dzialanie == "/":
        print(pierwszaLiczba, "/", drugaLiczbaTekst, "=", pierwszaLiczba / drugaLiczba)
    if dzialanie == "*":
        print(pierwszaLiczba, "*", drugaLiczbaTekst, "=", pierwszaLiczba * drugaLiczba)
