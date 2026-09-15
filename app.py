from model import model_lead
import control

def add_lead():
    name = input("nome: ")
    email = input("email: ")
    stage = input("Etapa no funil: ")

    # validar os dados
    # depois dos dados validados.. precisamos modelar o lead como dict
    #  usaremos o model para isso
    print(model_lead(name,email,stage))


    control.create_lead(model_lead(name, email, stage))

    print("Lead adicionado (func)")
def list_leads():
    leads = control.read_leads()
    print(leads)


# validar os dados.....
# depois dos dados validados... precisamos modelar o lead como um dict
# usaremos o model para isso

def main():

    while True:
        print('\nMini CRM de Leads')
        print("[1] Adicionar lead")
        print("[2] Listar Leads")
        print("[3] Sair do programa")

        opt = input("Escolha uma opção: ")

        if opt == '1':
            add_lead()
        elif opt == "2":
            list_leads()
        elif opt == "3":
            print("Até mais...")
            break
        else:
            print("Opção Invalida")

if __name__ == '__main__':
    main()