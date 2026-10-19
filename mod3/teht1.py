pituus = float(input("Anna kuhan pituus (cm): "))

if pituus < 37:
    puuttuu = 37 - pituus
    print(f"Kuha on alamittainen, laske se takaisin järveen. Pituudesta puuttuu {puuttuu:.1f} cm.")
else:
    print("Kuha on sallitun pyyntimitan mukainen.")
