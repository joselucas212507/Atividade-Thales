"""José Lucas Silva Carvalho, Thyago Bezerra, Italo de Sousa e Antonio Lucca"""
"""Média de 4 notas"""
nota1 = float(input("Digite a nota da unidade 1: "))
nota2 = float(input("Digite a nota da unidade 2: "))
nota3 = float(input("Digite a nota da unidade 3: "))
nota4 = float(input("Digite a nota da unidade 4: "))
media = (nota1 + nota2 + nota3 + nota4) / 4
print(
    f"A media das notas {nota1:.2f}, {nota2:.2f}, "
    f"{nota3:.2f} e {nota4:.2f} é {media:.2f}"
)


"""Graus Celsius em Farenheit"""
graus_farenheit = float(input("Digite a temperatura em Farenheit: "))
graus_celsius = 5 * (graus_farenheit - 32) / 9
print(
    f"{graus_farenheit:.2f} graus Farenheit correspondem a "
    f"{graus_celsius:.2f} graus Celsius"
)


"""Calcular área e perímetro de um Retângulo"""
base = float(input("Digite a base de um Retângulo"))
altura = float(input("Digite a altura de um Retângulo"))
area = (base * altura)
perimetro = (2 * (base + altura))
print (
    f"A área do Retângulo é igual a: {area}:.2f,"
    f"O Perímetro do Retângulo é igual a: {perimetro:.2f}"
)



