def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # 1. Verificar tamanho (entre 2 e 6 carateres)
    if not (2 <= len(s) <= 6):
        return False

    # 2. Verificar se começa com pelo menos duas letras
    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    # 3. Verificar carateres especiais (apenas letras e números são permitidos)
    if not s.isalnum():
        return False

    # 4. Verificar regras dos números
    i = 0
    while i < len(s):
        if s[i].isdigit():
            # O primeiro número não pode ser '0'
            if s[i] == "0":
                return False
            # Todos os carateres a seguir têm de ser números
            if not s[i:].isdigit():
                return False
            break
        i += 1

    return True


if __name__ == "__main__":
    main()
