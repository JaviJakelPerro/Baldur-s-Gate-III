import random
def d4():
    return random.randint (1, 4)
def d6():
    return random.randint (1, 6)
def d8():
    return random.randint (1,8)
def d10():
    return random.randint (1, 10)
def d12():
    return random.randint( 1, 12)
def d20():
    return random.randint (1, 20)
def main():
    dado = input("Elige el dado que quieres tirar (d4, d6, d8, d10, d12, d20): ").lower() 
    if dado not in ['d4', 'd6', 'd8', 'd10', 'd12', 'd20']:
        print("Dado no válido, elige entre d4, d6, d8, d10, d12, d20.")
        return  # Salir si el dado no es válido
    turnos = int(input("¿Cuántos turnos quieres simular?: "))
    if dado == 'd4':
        func_dado = d4
    elif dado == 'd6':
        func_dado = d6
    elif dado == 'd8':
        func_dado = d8
    elif dado == 'd10':
        func_dado = d10
    elif dado == 'd12':
        func_dado = d12
    elif dado == 'd20':
        func_dado = d20
    total = 0
    for _ in range(turnos):
        total += func_dado()        
    media = total / turnos
    print(f"Total de los {turnos} lanzamientos de {dado}: {total}")
    print(f"La media de las tiradas es: {media:.2f}")
if __name__ == "__main__":
    main()