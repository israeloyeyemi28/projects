ct = input("Your city: ")
pop = int(input("Your population:"))
text = input("your name:")

with open("s.s.txt", "at") as cut_f:
    print(f"{ct},{pop},{text}",file=cut_f)