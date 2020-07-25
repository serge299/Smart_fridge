cereals = False
milk = False
eggs = False

print("у тебя есть молоко?")
q = input()
if q.lower() == "да":
    milk = True

print("у тебя есть хлопья?")
q = input()
if q.lower() == "да":
    cereals = True

print("у тебя есть яйца")
q = input()
if q.lower() == "да":
    eggs = True
