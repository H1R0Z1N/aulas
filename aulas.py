from termux import *

def main ():
    os.system('clear')
    cont = input(c+"\npress ENTER para cotinuar ou press '0' para sair\n>>> "+y)
    while cont == '':
        banner()
        print (c+"[00] Introdução"+c+" \n[01] Aula: "+g+"Abrir Diretorios\n"+c+"[02] Aula: "+g+"Ver Diretorios \n"+c+"[03] Aula: "+g+"Criar Pastas \n"+c+"[04] Aula: "+g+"Remover Pasta e Arquivos \n"+c+"[05] Aula: "+g+"Mover Arquivos e Pastas\n"+c+"[06] Introdução Das Aulas Vim \n"+c+"[07] Aula:"+g+" Tudo Sobre Vim \n"+c+"[09] Aula: "+g+"Visualizando arquivo\n"+c+"[10] "+r+"Exit\n\n")
        num = int (input (g+"Digite o numero da aula de hoje:\n>>> "+y))
        if num == 0:
            intro()
        elif num == 1:
            aula_1()
        elif num == 2:
            aula_2()
        elif num == 3:
            aula_3()
        elif num == 4:
            aula_4()
        elif num == 5:
            aula_5()
        elif num == 6:
            intro_vim()
        elif num == 7:
            aulas_vim()
        elif num == 9:
            aula_vim1()
        elif num == 10:
            banner()
            print (c+"\n _____    _                   /\    /\ \n|_   _|__| |__   __ _ _   _  |/\|  |/\|\n  | |/ __| '_ \ / _` | | | |\n  | | (__| | | | (_| | |_| |\n  |_|\___|_| |_|\__,_|\__,_|    _____\n                               |_____|")
            print (red+'Digite "python3 aulas.py" para voltar\n')
            exit ()
        else:
            print (r+"      NUMERO INVALIDO!!!")
            cont = input(c+"\n\npress ENTER para tentar novamente... "+y)
    if cont != '':
        banner()
        print (c+"\n             Tchau!!! ^_^\n")
        print (red+'Digite "python3 aulas.py" para voltar')

main()
