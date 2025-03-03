q=int(input('Enter q: '))
alpha=int(input('Enter alpha: '))
alpha=alpha%q
Xa=int(input('Enter Xa: '))
Xb=int(input('Enter Xb: '))
Ya=pow(alpha, Xa, q)
Yb=pow(alpha, Xb, q)

print(f"\nPublic Keys - \tYa: {Ya}\tYb: {Yb}\n")

Xda=int(input("Enter Xda: "))
Xdb=int(input("Enter Xdb: "))
Yda=pow(alpha, Xda, q)
Ydb=pow(alpha, Xdb, q)

print(f'\nAttackers Public Keys - \tYda: {Yda}\tYdb: {Ydb}\n')

Ka=pow(Yda, Xa, q)
Kb=pow(Ydb, Xb, q)

print(f'Attackers Shared Secret Keys - \tKa: {Ka}\tKb: {Kb}\n')

Kda=pow(Ya, Xda, q)
Kdb=pow(Yb, Xdb, q)

print(f'Shared Session Keys - \tKda: {Kda}\tKdb: {Kdb}')
