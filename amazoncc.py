import getpass
import re 
import time


# --=--=-=-=-=-=-=-=- 1 - Codigo da parte cadastral -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

#cadastro, nome, email, senha e CPF
class  Register: 
        Nome=None
        Email=None
        Senha=None
        CPF=None

        

#1 Função para cadastrar novos clientes       
def check_register(users):  
        register = Register()
        register.Nome = input("Nome:  ")
        register.Email = input("Email: ")
        register.Senha = getpass.getpass(prompt = "Senha: ")
        register.CPF = input("CPF: ")

        # verifica se Email e Cpf já existem
        for i in users:
                if register.CPF == i.CPF:
                        print("\n*𝐂𝐏𝐅 𝐣𝐚́ 𝐞𝐱𝐢𝐬𝐭𝐞\n")
                        return check_register(users)

                elif register.Email == i.Email:
                        print("\n*Email já existe")
                        return check_register(users)

        # Expressoes regures a serem comparadas, um para email e outra para o CPF
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        words = r'[a-zA-Z\s]+$'

        soma = 0
        soma2 = 0


         # Compara o CPF com a expressão regular, se não fechar com as características da erro
        if not (re.fullmatch(r'\d{3}[\.]?\d{3}[\.]?\d{3}[-]?\d{2}', register.CPF)):
                print("\n*CPF Inválido :(\n\n")
                return check_register(users)
        

                # verifica se o numero de CPF sao iguais
        elif register.CPF == register.CPF[::-1]:
                print("\n*CPF Invalido :(\n\n")
                return check_register(users)
          
        # coverter a string em um int e chama o isdigit para ler apenas digitos
        cpfvalidate = [int(i) for i in register.CPF if i.isdigit()]
        

        #validação do primeiro digito
        for a, b in zip(cpfvalidate[0:9], range(10, 1, -1)):
                sum = a*b
                soma+=sum	

        valid = (soma % 11)

        if valid<2:
                if cpfvalidate[9] != 0:
                        print("\n*CPF Invalido :(\n\n")
                        return check_register(users)
        elif valid>=2:	
                x = 11 - valid
                if cpfvalidate[9] != x:
                        print("\n*CPF Invalido :(\n\n")
                        return check_register(users)

        #validação do segundo digito
        for a, b in zip(cpfvalidate[0:10], range(11, 1, -1)):
                sum = a*b
                soma2+=sum
        valid2 = (soma2 % 11)


        if valid2<2:
                if cpfvalidate[10] != 0:
                        print("\n*CPF Invalido :(\n\n")
                        return check_register(users)
        elif valid2>=2:	
                x = 11 - valid2
                if cpfvalidate[10] != x:
                        print("\n*CPF Invalido :(\n\n")
                        return check_register(users)


        # Compara o email com a expressão regular, se não fechar com as características da erro
        if not (re.fullmatch(regex, register.Email)):
                print("\n*𝐄𝐦𝐚𝐢𝐥 𝐞𝐫𝐫𝐚𝐝𝐨, 𝐭𝐞𝐧𝐭𝐞 𝐧𝐨𝐯𝐚𝐦𝐞𝐧𝐭𝐞\n\n")
                return check_register(users)

        #verifica a senha possui de 3 a 6 digitos
        elif len(register.Senha) < 6 :
                print("\n*𝐀 𝐬𝐞𝐧𝐡𝐚 𝐝𝐞𝐯𝐞 𝐜𝐨𝐧𝐭𝐞𝐫 𝟔 𝐝𝐢́𝐠𝐢𝐭𝐨𝐬\n\n")
        elif len(register.Senha) > 6:
                print("\n*𝐀 𝐬𝐞𝐧𝐡𝐚 𝐝𝐞𝐯𝐞 𝐜𝐨𝐧𝐭𝐞𝐫 𝟔 𝐝𝐢́𝐠𝐢𝐭𝐨𝐬\n\n")
                return check_register(users)

        # Expressao regular para validar nome com apenas letras e espaçamento
        elif not (re.match(words, register.Nome)):
                print("\n*𝐍𝐨𝐦𝐞 𝐝𝐞𝐯𝐞 𝐜𝐨𝐧𝐭𝐞𝐫 𝐚𝐩𝐞𝐧𝐚𝐬 𝐥𝐞𝐭𝐫𝐚𝐬!\n\n")
                return check_register(users)
       
        else:
                users.append(register)
                print(f"\n----𝐒𝐞𝐣𝐚 𝐛𝐞𝐦 𝐕𝐢𝐧𝐝𝐨(𝐚) {register.Nome} !----\nVocê tem um limite de 𝐑$ 𝟏.𝟎𝟎𝟎,𝟎𝟎")
        time.sleep(1)                      

#Consulta de clientes no sistema
def client(CPF, users):
        for register in users:
                if CPF == register.CPF:
                        print(f"/nCliente: {register.Nome}")
                        print(f"Email: {register.Email}")
                else:
                        print("*𝐂𝐏𝐅 𝐈𝐧𝐯𝐚́𝐥𝐢𝐝𝐨 :(")
        time.sleep(1)

#Funcao para login de usuario
def user_login(EMAIL,SENHA, users):
        if users != []:
                for register in users:
                        if (EMAIL == register.Email and SENHA == register.Senha):
                                print(f"\n𝐒𝐞𝐣𝐚 𝐛𝐞𝐦 𝐕𝐢𝐧𝐝𝐨(𝐚) de volta {register.Nome} !\n\nVocê tem um limite de 𝐑$ 𝟏.𝟎𝟎𝟎,𝟎𝟎")
                        elif not EMAIL == register.Email :
                                print("\n*𝐄𝐦𝐚𝐢𝐥 𝐈𝐧𝐯𝐚́𝐥𝐢𝐝𝐨, 𝐭𝐞𝐧𝐭𝐞 𝐧𝐨𝐯𝐚𝐦𝐞𝐧𝐭𝐞\n\n")

                        elif  not SENHA == register.Senha:                       
                                print("\n*𝐒𝐞𝐧𝐡𝐚 𝐈𝐧𝐜𝐨𝐫𝐫𝐞𝐭𝐚, 𝐭𝐞𝐧𝐭𝐞 𝐧𝐨𝐯𝐚𝐦𝐞𝐧𝐭𝐞\n\n")
        else:
                print("\n𝐔𝐬𝐮𝐚́𝐫𝐢𝐨 𝐨𝐮 𝐒𝐞𝐧𝐡𝐚 𝐢𝐧𝐜𝐨𝐫𝐫𝐞𝐭𝐨 :(")
        time.sleep(1)

# --=--=-=-=-=-=-=-=- 2 - Codigo da parte de compras -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

#2 produtos     
class Products(object):
      def __init__(self, name, value):
        self.name = name
        self.value = value
        def __repr__(self):
                return "name: %s value: %d" % (self.name, self.value)


arroz_1kg = Products("Arroz Branco 1kg", 6.50 ) 
arroz_integral = Products("Arroz Integral 1kg", 7.50)
creme_dental = Products("Creme Dental", 5)
acucar_refinado = Products("Açúcar Refinado 1kg", 4.50)
mouse_gamer = Products("Mouse Gamer FULL RGB", 65.00)
borracha = Products("Borracha", 5.00)
gabinete_rgb = Products("Gabinete RGB", 300.00)
pasta_termica = Products("Pasta Térmica", 35.00)
fonte_600 = Products("Fonte 600W", 300.00)
feijao_1kg = Products("Feijão 1kg", 5.00)
fita_led = Products("Fita Led", 50.00)
hdd_1tb = Products("HDD 1TB", 270.00)
ssd_250GB = Products("SSD 250GB", 250.00)
vassoura = Products("Vassoura", 15.00)
ssd_120GB = Products("SSD 120GB", 180.00)
processadori3 = Products("Processador i3", 750.00)
refrigerante = Products("Refrigerante", 9.00)
windows_xp = Products("Windows XP Pro", 100.00)
caderno = Products("Caderno", 15.00)
celular = Products("Seusung Pro Max 300gb", 500.00)


#mostra os produtos no sistema
def show_products(product):
        for i in product:
                print(i.name + " - R$", i.value)
        print()

#2 sistema de compras, seleciona o produto e adiciona ao carrinho por meio do append.
def purchases(product, itens):
        credito=1000.00
        soma=0

        for i in itens:
                soma+=i.value
        resultado = credito - soma

        if resultado>=0:
                print(f"Limite de Crédito Atual: {resultado}")    

        while resultado>=1:   

                n = input("\n") 
             

                if n == '1':
                        itens.append(product[0])
                        print(f"\nArroz Branco 1kg - adicionado ao carrinho!\n") 
                        return purchases(product, itens)
                elif n == '2':
                        itens.append(product[1])
                        print("\nArroz Integral 1kg - adicionado ao carrinho!\n") 
                        return purchases(product, itens) 
                elif n == '3':
                        itens.append(product[2])
                        print("\nPasta de dente - adicionado ao carrinho!\n")  
                        return purchases(product, itens)
                elif n == '4':
                        itens.append(product[3])
                        print("\nAçúcar Refinado 1kg - adicionado ao carrinho!\n")
                        return purchases(product, itens)  
                elif n == '5':
                        itens.append(product[4])
                        print("\nMouse Gamer FULL RGB - adicionado ao carrinho!\n") 
                        return purchases(product, itens) 
                elif n == '6':
                        itens.append(product[5])
                        print("\nBorracha - adicionado ao carrinho!\n")  
                        return purchases(product, itens)
                elif n == '7':
                        itens.append(product[6])
                        print("\nGabinete RGB - adicionado ao carrinho!\n")  
                        return purchases(product, itens)
                elif n == '8':
                        itens.append(product[7])
                        print("\nPasta Térmica - adicionado ao carrinho!\n") 
                        return purchases(product, itens) 
                elif n == '9':
                        itens.append(product[8])
                        print("\nFonte 600W - adicionado ao carrinho!\n")  
                        return purchases(product, itens)
                elif n == '10':
                        itens.append(product[9])
                        print("\nFeijão 1kg - adicionado ao carrinho!\n") 
                        return purchases(product, itens)
                elif n == '11':
                        itens.append(product[10])
                        print("\nFita Led - adicionado ao carrinho!\n") 
                        return purchases(product, itens)
                elif n == '12':
                        itens.append(product[11])
                        print("\nHDD 1TB - adicionado ao carrinho!\n") 
                        return purchases(product, itens)
                elif n == '13':
                        itens.append(product[12])
                        print("\nFSSD 250GB - adicionado ao carrinho!\n") 
                        return purchases(product, itens)
                elif n == '14':
                        itens.append(product[13])
                        print("\nVassoura -  adicionado ao carrinho!\n") 
                        return purchases(product, itens)
                elif n == '15':
                        itens.append(product[14])
                        print("\nSSD 120GB - adicionado ao carrinho!\n") 
                        return purchases(product, itens)
                elif n == '16':
                        itens.append(product[15])
                        print("\nProcessador i3 - adicionado ao carrinho!\n") 
                        return purchases(product, itens)
                elif n == '17':
                        itens.append(product[16])
                        print("\nRefrigerante - adicionado ao carrinho!\n") 
                        return purchases(product, itens)
                elif n == '18':
                        itens.append(product[17])
                        print("\nWindows XP Pro - adicionado ao carrinho!\n") 
                        return purchases(product, itens)
                elif n == '19':
                        itens.append(product[18])
                        print("\nCaderno - adicionado ao carrinho!\n") 
                        return purchases(product, itens)
                elif n == '20':
                        itens.append(product[19])
                        print("\nSeusung Pro Max - adicionado ao carrinho!\n") 
                        return purchases(product, itens)
                elif n == '0':
                        return
                else:
                        print("\nOpção Inválida\n")
                        return purchases(product, itens)
        else:
                #se o limite estourar é deletado o ultimo valor do carrinho, impedindo a compra do produto
                print("\nProduto não comprado :(\n\nSeu limite estourou, não poderá realizar mais compras, pague \nou escolha outro produto!")
                del itens[-1]       
        
                

#função para realizar o pagamento e resetar o credito            
def payment(itens):
        credito=1000.00
        soma=0
        
        for i in itens:
                #soma todos os valores do carrinho
                soma+=i.value  
                resultado = credito - soma
        print(f"\nCrédito Atual: {resultado}\n")

        print("Digite 99 para PAGAR,\nou 0 para SAIR e cancelar\no pagamento e os itens do carrinho")
        n=input('\n')

        #Paga as compras e reseta o carrinho
        if n == '99': 
                time.sleep(1.5)
                print(f'Pago!\nNovo crédito: R$ {credito}')
                itens.clear()
        #sai e reseta o carrinho
        elif n=='0':
                itens.clear()

# interface não gráfica
def menu() :
        users=[]
        itens=[]
        product=[arroz_1kg, arroz_integral, creme_dental, acucar_refinado, mouse_gamer, borracha, gabinete_rgb, pasta_termica, fonte_600, feijao_1kg, fita_led, hdd_1tb, ssd_250GB, vassoura, ssd_120GB, processadori3, refrigerante, windows_xp, caderno, celular]
        while True:
                opcao = input("\n--------𝑨𝒎𝒂𝒛𝒐𝒏𝑪𝑪 𝑺𝒕𝒐𝒓𝒆--------\n\n\n 𝘗𝘳𝘦𝘤̧𝘰𝘴 𝘪𝘯𝘤𝘳𝘪́𝘷𝘦𝘪𝘴 𝘦́ 𝑎𝑝𝑒𝑛𝑎𝑠 𝘢𝘲𝘶𝘪!\n\n\n-------------MENU-------------\n\n Cadastre-se e confirme sua\n    conta fazendo login!!\n\nOPÇÕES:\n\n1- Cadastro\n2- Login\n3- Consultar Cliente\n4- Comprar\n5- Carrinho de compras\n6- Pagamento \n7- Produtos\n0- Sair\n\n")
                if opcao == '1':
                        print("------CADASTRO DE CLIENTES------\n")
                        check_register(users)

                elif opcao =='2':
                        print("LOGIN\n")
                        login=input("Email: ")
                        senha=getpass.getpass(prompt="Senha: ")
                        user_login(login, senha, users)

                elif opcao =='3':
                        print("CONSULTA DE CLIENTE\n")
                        consulta=input("Insira seu CPF: ")
                        if users != []:
                                client(consulta, users)
                        else:
                                print("\n*𝐂𝐥𝐢𝐞𝐧𝐭𝐞 𝐧𝐚̃𝐨 𝐞𝐧𝐜𝐨𝐧𝐭𝐫𝐚𝐝𝐨 𝐨𝐮 𝐂𝐏𝐅 𝐢𝐧𝐜𝐨𝐫𝐫𝐞𝐭𝐨!")

                elif opcao =='4':
                        if users != []:
                                print("COMPRAR\n")
                                print("\nSelecione os produtos!\n\nDigite 0 para voltar para o\nMenu e realizar o pagamento!\n")
                                print("Escolha itens de 1 a 20\nSeu limite é de R$ 1.000,00\n1. Arroz Branco 1kg - R$ 6.50\n2. Arroz Integral 1kg - R$ 7.50\n3. Pasta de dente - R$ 5\n4. Açúcar Refinado 1kg - R$ 4.50\n5. Mouse FULL RGB - R$ 65.00\n6. Borracha - R$ 5.00\n7. Gabinete RGB - R$ 300.00\n8. Pasta Térmica - R$ 15.00\n9. Fonte 600W - R$ 300.00")
                                print("10. Feijão 1kg - R$ 5.00\n11. Fita Led - R$ 50.00\n12. HDD 1TB - R$ 270.00\n13. SSD 250GB - R$ 250.00\n14. Vassoura - R$ 15.00\n15. SSD 120GB - R$ 180.00\n16. Processador - R$ 750.00\n17. Refrigerante  - R$ 9.00\n18. Windows XP Pro - R$ 100.00\n19. Caderno - R$ 15.00\n20. Seusung Pro Max 300gb - R$ 500.00\n")
                                purchases(product, itens)
                        else:
                                print("\nCrie uma conta !")
                                
                elif opcao =='5':
                #3 mostra produtos comprados se ocorrer erro por estar vazio, chama o except
                      
                        print("\nCARRINHO\n")
                        soma=0
                        for i in itens:
                                print(i.name + " - R$", i.value)
                                soma+=i.value
                                resultado = soma
                        if itens != []:
                                print(f"\nTotal: R$ {resultado}")
                        else:
                                print("Sem Itens no carrinho :(")
                                        
                elif opcao == '6':
                        #chama a função pagamento, se o carrinho estiver vazio chama o except
                        try:
                                print("\nPagamento")
                                payment(itens)
                        except: 
                                print("Faça seu cadastro!")

                elif opcao =='7':
                        print("\n PRODUTOS-------PREÇO\n")
                        show_products(product)       

                elif opcao =='0':
                        print("---------Volte Sempre!!--------\n")
                        break

                else:
                        print("\n𝐎𝐩𝐜̧𝐚̃𝐨 𝐢𝐧𝐯𝐚́𝐥𝐢𝐝𝐚, 𝐭𝐞𝐧𝐭𝐞 𝐧𝐨𝐯𝐚𝐦𝐞𝐧𝐭𝐞.\n")
menu()
