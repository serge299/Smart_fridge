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

if milk and cereals or eggs:
    if eggs:
        if milk:
           breakfast="омлет"
        else:
            breakfast="яиxница"

    else:
        breakfast="молоко с хлопьями"
else:
    if milk:
        breakfast="стакан молока"
    elif cereals:
        breakfast="погрызу хлопья"
    else:
        breakfast="ничего"
print("Сегодня на завтрак",breakfast)
