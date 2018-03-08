# This is Homework00 test script!

ime_string = input("Koje je Vase ime: ")
ime_string = str(ime_string)

specijalna_imena = ['Mirza', "Nikola", "Vanja"]


print("Hello " + ime_string)
rekao_je_broj = False

while not rekao_je_broj:

    godine_string = str(input("Koliko imate godina: "))

    if godine_string.isnumeric():
        godine_broj = int(godine_string)
        rekao_je_broj = True
    else:
        print("Izvinite ne razumijemo se!")

ime_malim_slovima = ime_string.lower()
print(ime_malim_slovima)
pozicija_posljednjeg_slova = len(ime_string) - 1
posljednje_slovo = ime_malim_slovima[pozicija_posljednjeg_slova]

if posljednje_slovo == "a":
    pol = "zenski"
else:
    pol = "muski"

if godine_broj >= 18:
    print(ime_string + " ulaz dozvoljen!")
    print("Dobrodosli")
else:
    print(ime_string + " ulaz nije dozvoljen")
    print("Vatite se kad porastete!")

if ime_malim_slovima.title() in specijalna_imena:
    print("Dobrodosli!")
else:
    if pol == "muski":
        print("Bravo brko!")
    else:
        print("Helou, bjuti")