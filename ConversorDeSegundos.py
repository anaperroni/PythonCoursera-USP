entradaSeg = int(input("Digite o número de segundos que deseja converter: "))

dia = entradaSeg // 86400
resto_seg = entradaSeg % 86400
horas = resto_seg // 3600
resto_seg %= 3600
minutos = resto_seg // 60
segundos = resto_seg % 60

print(f"{dia} dias, {horas} horas, {minutos} minutos e {segundos} segundos")
