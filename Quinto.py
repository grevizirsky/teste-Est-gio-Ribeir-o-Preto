def inverte_string(string):
    # Converte a string para uma lista de caracteres
    caracteres = list(string)
    
    # Obtém o tamanho da string
    tamanho = len(caracteres)
    
    # Itera pela metade da string, trocando os caracteres
    for i in range(tamanho // 2):
        # Troca os caracteres nas posições i e tamanho - 1 - i
        caracteres[i], caracteres[tamanho - 1 - i] = caracteres[tamanho - 1 - i], caracteres[i]
    
    # Junta os caracteres de volta em uma string
    string_invertida = ''.join(caracteres)
    
    return string_invertida

# Exemplo de uso
texto = input("Digite uma palavra ou frase para inverter: ")
texto_invertido = inverte_string(texto)
print("Texto invertido:", texto_invertido)
