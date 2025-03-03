q=int(input('Enter q: '))
alpha=int(input('Enter alpha: '))
alpha=alpha%q
Xa=int(input('Enter Xa: '))
Xb=int(input('Enter Xb: '))
Ya=pow(alpha, Xa, q)
Yb=pow(alpha, Xb, q)

print(f"\nPublic Keys - \tYa: {Ya}\tYb: {Yb}")

Ka=pow(Yb, Xa, q)
Kb=pow(Ya, Xb, q)

print(f'\nSecret Session Keys - \tKa: {Ka}\tKb: {Kb}')
