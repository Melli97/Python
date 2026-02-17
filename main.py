print("Welcome")
print("missione")
scelta1=input("destra or sinistra? ").lower()

if scelta1 == "sinistra":
         scelta2= input('"sei arrivato al lago "wait" o "nuoti""').lower()

         if scelta2 == "wait":
                 print("sei arrivato dall'altra parte")

else:
        print("game over")