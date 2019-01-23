from veiculo import Veiculo
from carro import Carro
carro_azul = Carro('Azul', 'Renault',30)

print(carro_azul)
print(type(carro_azul))

print("Cor:",carro_azul.cor,"\nMarca:",carro_azul.marca, "\nTanque:", carro_azul.tanque)
carro_azul.abastecer(30)
print("\nTanque:", carro_azul.tanque)