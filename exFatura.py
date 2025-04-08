nomeCliente = input("Qual nome do cliente? ")
dataVenc = int(input("Qual a data do vencimento? "))
mesVenc = input("Qual mês do vencimento? ")
valorFat = float(input("Qual o valor da Fatura? "))

print("Olá, ",nomeCliente, "!" )
print("A sua fatura vence no dia, ", dataVenc, "de ", mesVenc, ". O valor a pagar é de: ", valorFat)