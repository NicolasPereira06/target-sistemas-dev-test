def inverter_string(string):
    string_invertida = ""

    #corre a string  de trás pra frente
    for i in range(len(string) - 1, -1, -1):
        string_invertida += string[i]

    return string_invertida

def main():
    string_original = input("Digite uma string para inverter: ")
    
    string_resultado = inverter_string(string_original)

    print(f"String invertida: {string_resultado}")

if __name__ == "__main__":
    main()