people_list = []

## Classifica as pessoas por idade
def person_classifier(l):
    new_l = []
    for p in l:
        if p[1] <= 12:
            new_l.append((p[0], p[1], "Criança"))
        elif p[1] <= 19:
            new_l.append((p[0], p[1], "Adolescente"))
        elif p[1] < 65:
            new_l.append((p[0], p[1], "Adulto"))
        else:
            new_l.append((p[0], p[1], "Idoso"))
    return new_l

## Faz o sort por nome e retorna uma nova lista
def list_sort_name(l):
    l.sort()
    return l

## Faz o sort por idade e retorna uma nova lista
def list_sort_age(l):
    l.sort(key=lambda x:x[1])
    return l

## Cria o loop interativo
while True:
    print("")
    print("O que gostaria de fazer?")
    print("1 - Inserir pessoa na lista\n2 - Exibir pessoas ordenadas por nome\n3 - Exibir pessoas ordenadas por idade\n4 - Exibir pessoas classificadas por idade\n5 - Sair\n")
    answer = input("Digite o número: ")
    
    try:
        answer = int(answer)
    except:
        print("")
        print("Resposta näo é um número")
        continue
    
    print("")
    if answer == 1:
        name = input("Nome: ").capitalize()
        age = input("Idade: ")
        
        try:
            people_list.append((name, int(age)))
        except:
            print("")
            print("Idade não é um número, tente novamente\n")

        print("")
        print(*people_list, sep='\n')

    elif answer == 2:
        print(*list_sort_name(people_list), sep='\n')

    elif answer == 3:
        print(*list_sort_age(people_list), sep='\n')

    elif answer == 4:
        print(*person_classifier(people_list), sep='\n')
        
    else:
        break