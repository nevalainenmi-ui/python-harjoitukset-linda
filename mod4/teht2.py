while True:
    tuumat = float(input("Anna tuumamäärä: "))

    if tuumat < 0:
        break

    print(tuumat * 2.54)