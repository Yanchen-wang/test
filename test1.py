from random import randint
random = randint(1,10)
print("benvenuto nel socializzatore")
nome = input("come ti chiami?(nome e cognome)")
print("piacere di conoscerti",nome)
età = input("quanti anni hai?")
print("anchio, e dove abiti tu?")
abitazione = input() 
hobby = input("qual'è la tua attivita preferita nelle ore libere?")
print("bello da sapere , invece qual'è la tua occupazione?")
occupazione = input()
altezza = input("quanto sei alto in cm?")
print("profilo nuovo creato:")
print("nome e cognome:",nome,"  età:",età,"  altezza:",altezza,"cm")
print("abitazione:",abitazione,"  occupazione:",occupazione)
print("hobby preferito:",hobby,"  ID :",int(età)*random-randint(1,10)+int(altezza))