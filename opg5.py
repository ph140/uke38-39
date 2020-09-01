x = int(input("Tall: "))


for i in range(2, x):
    if x % i == 0:
        print("Ikke primtall")
        break
    elif x == i+1:
        print("Primtall")
        break
