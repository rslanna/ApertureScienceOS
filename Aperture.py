import time

def animacao_carregamento():
    print("Aperture Science OS v1.0")
    time.sleep(2)
    logo_ascii = r"""
              .,-:;//;:=,
          . :H@@@MM@M#H/.,+%;,
       ,/X+ +M@@M@MM%=,-%HMMM@X/,
     -+@MM; $M@@MH+-,;XMMMM@MMMM@+-
    ;@M@@M- XM@X;. -+XXXXXHHH@M@M#@/.
  ,%MM@@MH ,@%=             .---=-=:=,.
  =@#@@@MX.,                -%HX$$%%%:;
 =-./@M@M$                   .;@MMMM@MM:
 X@/ -$MM/                    . +MM@@@M$
,@M@H: :@:                    . =X#@@@@-
,@@@MMX, .                    /H- ;@M@M=
.H@@@@M@+,                    %MM+..%#$.
 /MMMM@MMH/.                  XM@MH; =;
  /%+%$XHH@$=              , .H@@@@MX,
   .=--------.           -%H.,@@@@@MX,
   .%MM@@@HHHXX$$$%+- .:$MMX =M@@MM%.
     =XMMM@MM@MM#H;,-+HMM@M+ /MMMX=
       =%@M@M#@$-.=$@MM@@@M; %M%=
         ,:+$+-,/H#MMMMMMM@= =,
               =++%%%%+/:-.
    """
    slogan = "We do what we must because we can."

    frases_carregamento = [
        "Carregando módulos principais...",
        "Configurando protocolos de teste...",
        "Inicializando testes de segurança...",
        "Verificando integridade do sistema...",
        "Aperture Science OS carregado com sucesso!",
        "Inicializando testes de laboratório...",
        "Conectando-se ao laboratório central...",
        "Calibrando portais...",
        "Inicialização concluída. Bem-vindo à Aperture Science!",
    ]

    print(logo_ascii)
    print(slogan)

    for frase in frases_carregamento:
        print("\n" + frase, end=" ")
        time.sleep(2)

    print("\nSistema Operacional da Aperture Science inicializado com sucesso!")
    
    print("\n--- Login ---")
    username = input("Nome de usuário: ")
    password = getpass.getpass("Senha: ")

    if username == "admin" and password == "password":
        print("Login bem-sucedido!")
        print(f"\nBem-vindo, {username}!")
        while True:
            current_directory = "~"  # Diretório atual fictício
            command_prompt = f"{username}@ApertureLab:{current_directory}$ "
            command = input(command_prompt)
            if command == "start GLaDOS":
                print("Iniciando GLaDOS...")
                time.sleep(2)
                print("Inicializando módulos de IA...")
                time.sleep(2)
                print("Carregando banco de dados de experimentos...")
                time.sleep(3)
                print("GLaDOS iniciada com sucesso!")
                continue
            elif command == "help":
                print("\nComandos disponíveis:")
                print(" - start GLaDOS: Inicia o sistema GLaDOS")
                print(" - check systems: Realiza a checagem dos sistemas do laboratório")
                print(" - check cores: Verifica o estado dos núcleos da GLaDOS")
                print(" - check lab stats: Verifica as estatísticas do laboratório")
                print(" - shutdown: Desliga o sistema")
                #Adicione aqui quaisquer outros comandos que você tenha
            elif command == "check cores":
                print("Verificando o estado dos núcleos da GLaDOS...")
                time.sleep(2)
                print("Núcleo de Moralidade - Estado: Funcionando")
                time.sleep(1)
                print("Núcleo de Curiosidade - Estado: Funcionando")
                time.sleep(1)
                print("Núcleo de Inteligência - Estado: Funcionando")
                time.sleep(1)
                print("Núcleo de Raiva - Estado: Funcionando")
                time.sleep(1)
                print("Núcleo de Amortecimento de Inteligência - Estado: Falha")
                time.sleep(1)
                # Adicione aqui outros núcleos, se necessário
                continue
            elif command == "check lab stats":
                print("Verificando estatísticas do laboratório...")
                time.sleep(2)
                print("Quantidade de Torretas Produzidas: 500")
                time.sleep(1)
                print("Quantidade de Torretas Destruidas: 100")
                time.sleep(1)
                print("Quantidade de Cubos Produzidos: 200")
                time.sleep(1)
                print("Quantidade de Cobaias em Estado de Suspensão: 50")
                time.sleep(1)
                print("Quantidade de Funcionários do Laboratório: 20")
                time.sleep(1)
                continue
            elif command == "check systems":
                print("Realizando checagem dos sistemas do laboratório...")
                time.sleep(2)
                print("Verificando sistemas de energia... [OK]")
                time.sleep(2)
                print("Verificando sistemas de segurança... [OK]")
                time.sleep(2)
                print("Verificando conexões de rede... [OK]")
                time.sleep(2)
                print("Verificando dispensadores de caixa... [OK]")
                time.sleep(2)
                print("Verificando funcionamento dos botões... [OK]")
                time.sleep(2)
                print("Verificando câmeras de segurança... [OK]")
                time.sleep(2)
                print("Verificando funcionamento dos lasers... [OK]")
                time.sleep(2)
                print("Verificando Gel de Propulsão... [OK]")
                time.sleep(2)
                print("Verificando Gel de Repulsão... [OK]")
                time.sleep(2)
                print("Verificando Gel de Conversão... [OK]")
                time.sleep(2)
                print("Checagem de sistemas concluída!")
                # Adicione aqui a lógica adicional para a checagem de sistemas
                continue
            elif command == "shutdown":  
                print("Aperture Science OS v1.0")
                time.sleep(2)
                print("Desligando...")
                time.sleep(2)            
            # Adicione aqui a lógica para executar os comandos do usuário
    else:
        print("Credenciais inválidas. Tente novamente.")
        
animacao_carregamento()

