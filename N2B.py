print("Tarefa N2B Gerador de senhas")
print("Luiz Fernando da Costa")
print("Melissa Lima Miranda\n")
import random
def gerar_senha(tamanho, tipo):
    caracteres = []
    digitos = [str(i) for i in range(10)]
    if tipo == 'a':
        caracteres = digitos
    elif tipo == 'b':
        caracteres.extend([chr(i) for i in range(65, 91)])  # Letras maiúsculas
        caracteres.extend([chr(i) for i in range(97, 123)])  # Letras minúsculas
    elif tipo == 'c':
        caracteres.extend([chr(i) for i in range(65, 91)])  # Letras maiúsculas
        caracteres.extend(digitos)
        numero = random.choice(digitos)
        tamanho -= 1
        senha = numero
        for _ in range(tamanho):
            senha += random.choice(caracteres)
        senha = ''.join(random.sample(senha, len(senha)))  # Embaralha a senha
        return senha
    elif tipo == 'd':
        caracteres.extend([chr(i) for i in range(65, 91)])  # Letras maiúsculas
        caracteres.extend([chr(i) for i in range(97, 123)])  # Letras minúsculas
        caracteres.extend(digitos)
        # Adiciona pelo menos um número
        numero = random.choice(digitos)
        tamanho -= 1
        senha = numero
        for _ in range(tamanho):
            senha += random.choice(caracteres)
        senha = ''.join(random.sample(senha, len(senha)))  # Embaralha a senha
        return senha
    elif tipo == 'e':
        caracteres.extend([chr(i) for i in range(65, 91)])  # Letras maiúsculas
        caracteres.extend([chr(i) for i in range(97, 123)])  # Letras minúsculas
        caracteres.extend(['-', '_', ':', '@', '#', '$', '&', '?'])
        caracteres.extend(digitos)
        # Adiciona pelo menos um caractere de cada tipo
        senha = ''
        senha += random.choice([chr(i) for i in range(65, 91)])  # Letra maiúscula
        senha += random.choice([chr(i) for i in range(97, 123)])  # Letra minúscula
        senha += random.choice(['-', '_', ':', '@', '#', '$', '&', '?'])
        senha += random.choice(digitos)
        tamanho -= 4
        for _ in range(tamanho):
            senha += random.choice(caracteres)
        senha = ''.join(random.sample(senha, len(senha)))  # Embaralha a senha
        return senha
    senha = ''
    for _ in range(tamanho):
        senha += random.choice(caracteres)
    return senha
tipo_senha = input("Digite o tipo de senha desejado: ")
tamanho_desejado = 0
while tamanho_desejado < 6 or tamanho_desejado > 20:
    tamanho_desejado = int(input("Digite o tamanho desejado para a senha (entre 6 e 20): "))
senha_gerada = gerar_senha(tamanho_desejado, tipo_senha)
print("Senha gerada:", senha_gerada)
