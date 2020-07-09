import os 
import diceroller
clear = lambda: os.system('clear')


while True: # estrutura de repetição
    clear()
    resp = int(input("""
        ==== MENU DO PROGRAMA ====
        [0] - Sair do programa
        [1] - Rolar dado de 4 faces
        [2] - Rolar dado de 6 faces
        [3] - Rolar dado de 8 faces
        [4] - Rolar dado de 12 faces
        [5] - Rolar dado de 20 faces
    """))
    # if = se
    # else  = senão
    # elif  = senão se
    if resp == 0:
        break
    elif resp == 1:
        print(f"Resultado do D4: {diceroller.rolld4()}")
        input()
    elif resp == 2:
        print(f"Resultado do D6: {diceroller.rolld6()}")
        input()
    elif resp == 3:
        print(f"Resultado do D8: {diceroller.rolld8()}")
        input()
    elif resp == 4:
        print(f"Resultado do D12: {diceroller.rolld12()}")
        input()
    elif resp == 5:
        print(f"Resultado do D20: {diceroller.rolld12()}")
        input()
    else:
        print("Opção inválida amigo. Tenta de novo")
        input()
print("Finalizando o programa...")



