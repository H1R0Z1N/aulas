import os

def banner ():
    global c,r,g,y
    os.system ('clear')
    print (r+"\n          ------------------------\n         | AULAS DE TERMUX DO ZERO |\n          ------------------------\n                                  by: hiro\n")

red = '\033[31m'
yellow = '\033[93m'
green = '\033[92m'
clear = '\033[0m'
bold = '\033[01m'
cyan = '\033[96m'
c = clear+bold+cyan
r = clear+bold+red
g = clear+bold+green
y = clear+bold+yellow
def intro ():
    banner()
    print (c+"\tOlá, Me chamo hiro, e nessas aulas vou te ensinar como gerenciar seus arquivos no termux e começar a usar o termux no seu dia a dia como uma ferramenta para criar e execultar seus programas e arquivos de txt.\n\t vou mostrar tambem como mover os arquivos criados no termux para o SD para você ultilizar como quiser...\n")
    print (y+"\n\n\tE isso, tenham uma boua aula! ^_^")
    cont = input(g+"\n\npress ENTER para voltar...")

def aula_1 ():
    banner()
    print(y+"--> pastas com espaços no termux\n"+c+"Exp:. pasta\ de\ exemplo\nExp:. 'pasta de exemplo'\n"'Exp:. "pasta de exeplo"')
    print(y+"\n--> para abrir uma parta\n"+c+"'-> cd nome_da_pasta")
    print(y+"\n--> Voltar para pasta anterior\n"+c+"'-> cd ..")
    print(y+"\n--> Para Sair de uma pasta e entrar em outra\n"+c+"  cd ../nome_da_pasta")
    print(y+"\n--> para entrar em uma pasta pela loc dela\n"+c+"'->cd /data/data/com.termux/files/home")
    print(y+"\n--> para ir pra pasta anterior\n"+c+"'-> cd -")
    print(y+"\n--> Da para entrar em pastas com espaços tambem\n"+c+"cd 'pastas com espaços'")
    cont = input(g+"\n\npress ENTER para voltar...")

def aula_2 ():
    banner()
    print(y+"--> para ver as pastas\n"+c+"'-> ls")
    print(y+"\n--> para ver o que tem dentro de um determinado diretorio\n"+c+"'-> ls data/data/com.termux/files/home/nome_da_pasta")
    print(y+"\n-->Para ver arquivos ocultos \n"+c+"'-> ls -a")
    print(y+"\n--> para ver as permissões dos arquivos\n"+c+"'-> ls -l")
    print(y+"\n--> para mostras o inode dos arquivos\n"+c+"'-> ls -i")
    print(y+"\n--> para ver as pastas em ordem invertida) \n"+c+"'-> ls -r ")
    print (y+"\n--> Para exibir os arquivos em coluna \n"+c+"'-> ls -1")
    print(y+"\n--> sim, isso são dois comendos que estão sendo usados ao mesmo tempo 'r'= reverse + '1'= coluna, a ordem das letras tanto faz\n"+c+"'-> ls -r1")
    cont = input(g+"\n\npress ENTER para voltar...")

def aula_3 ():
    banner()
    print(y+"--> Mostrar á localização do diretorio em que você esta \n"+c+"'-> pwd")
    print(y+"\n--> criar uma pasta \n"+c+"'-> mkdir nome_da_pasta ")
    print(y+"\n--> criar varias pastas \n"+c+"'-> mkdir pst1 pst2 pst3")
    print(y+"\n--> Da para criar pastas com espaços tambem\n"+c+"'-> mkdir 'pastas com espaços'")
    print(y+"\n--> criando pastas dentro de pasta em uma única linha\n"+c+"'-> mkdir pst1 pst1/pst2 pst1/pst2/pst3")
    cont = input(g+"\n\npress ENTER para voltar...")

def aula_4 ():
    banner()
    print(y+"--> para excluir arquivos obs: exclui apenas arquivos\n"+c+"'-> rm arquivos")
    print(y+"\n--> para excluir pastas vazias \n"+c+"'-> rmdir nome_da_pasta")
    print(y+"\n--> para excluir varias pasta vazias ao mesmo tempo\n"+c+"'-> rmdir pst1 pst2 pst3 ")
    print(y+"\n--> Da para criar pastas com espaços tambem \n"+c+"'-> rmdir 'pastas com espaços'")
    print(y+"\n--> para excluir uma pasta ou arquivo, obsv: ele pedirar para confirmar a exclusão\n"+c+"'-> rm -r nome_da_pasta ")
    print(y+"\n--> para excluir uma pasta ou arquivo sem presisar confirmar\n"+c+"'-> rm -rf nome_da_pst ")
    cont = input(g+"\n\npress ENTER para voltar...")
def aula_5():
    banner()
    print(y+"--> comando para renomear um arquivo ou pasta \n"+c+"'-> mv nome_arquivo novo_nome")
    print(y+"--> para mover um arquivo ou pasta digite o caminho de origem e o caminho de destino\n"+c+"'-> mv data/data/com.termux/files/home/nome_da_pasta data/data/com.termux/files/home/logar_do_novo_lugar_da_pasta")
    cont = input(g+"\n\npress ENTER para voltar...")
    
def intro_vim():
    banner()
    print (c+"\tO vim é usado para criar e editar arquivos eu txt e nele é possivel criar programas em quaquer linguagem de programação por exeplo .py, .txt, .rd, .sh e etc..")
    print (y+"\n\n\tE isso, tenham uma boua aula! ^_^")
    cont = input(g+"\n\npress ENTER para voltar...")

def aulas_vim():
    banner()
    print(y+"--> para criar um arquivo vim \n"+c+"'-> vim nome_do_arquivo")
    print(y+"--> para criar ou editar dois arquivos ao mesmo tempo \n"+c+"'-> vim arq_1 arq_2")
    print(y+"\n--> aperte ESC e : para entrar nas configurações \n"+c+"'-> :")
    print(y+"--> para trocar de arq entre na configuação e digite \n"+c+"'-> 'next' para ir pro poximo\n'-> 'prev' para voltar")
    print(y+"\n--> para começar á escrever digite a letra 'i'\n"+c+"'-> i = insert")
    print(y+"\n--> esses são executados na opção ESC \n"+c+"'-> h = esquerda l = direita j = baixo k = cima")
    print(y+"\n--> voltar pro último save \n"+c+"'-> u")
    print(y+"\n--> para volta o que fez\n"+c+"'-> ctrl + r")
    print(y+"\n--> é para começar a escrever tbm\n"+c+"'-> a = append --> adicionar no final")
    print(y+"\n--> entre nas opções e aperte w + enter para salvar.\n"+c+"'-> w ou written ")
    print(y+"\n--> entre nas opções e aperte q + enter para sair \n"+c+"'-> q ou quit")
    print(y+"\n--> entre nas opções e aperte wq + enter para salvar e sair\n"+c+"'-> wq ou writtenquit --> salvar e sair")
    cont = input(g+"\n\npress ENTER para voltar...")
def aula_vim1():
    banner()

    print(y+"--> \n"+c+"'->")
    cont = input(g+"\n\npress ENTER para voltar...")
def aula_vim2():
    banner()
    print(y+"--> para ver o que tem dentro do arquivo\n"+c+"'-> cat nome_do_arquivo")
    print(y+"--> para ver o que tem dentro do arquivo em orde oposta\n"+c+"'-> tac")
    print(y+"--> para ver o que tem dentro do arquivo com as linas numeradas \n"+c+"'-> cat -n nome_do_arquivo")
    cont = input(g+"\n\npress ENTER para voltar...")
