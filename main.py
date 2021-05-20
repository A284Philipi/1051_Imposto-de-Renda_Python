salario = float(input())
imposto = float(0)
imposto_renda = float(0)
if salario <= 2000 and salario >= 0:
    print("Isento")
elif salario > 2000 and salario <= 3000:
    imposto_renda = (salario - 2000) * 0.08
    print("R$ %.2f" % (imposto_renda))
elif salario > 3000 and salario <= 4500:
    imposto_renda = (1000 * 0.08) + ((salario - 3000) * 0.18)
    print("R$ %.2f" % (imposto_renda))
else:
    imposto_renda = (1000 * 0.08) + (1500 * 0.18) + ((salario - 4500) * 0.28)
    print("R$ %.2f" % (imposto_renda))