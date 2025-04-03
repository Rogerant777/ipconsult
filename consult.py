import requests
import sys
from colorama import Fore, Style
import os


while True:
    print('')   
    print('')    
    print(f'{Fore.RED}▪   ▄▄▄· ▄▄·        ▐ ▄ .▄▄ · ▄• ▄▌▄▄▌  ▄▄▄▄▄{Style.RESET_ALL}')
    print(f'{Fore.RED}██ ▐█ ▄█▐█ ▌▪▪     •█▌▐█▐█ ▀. █▪██▌██•  •██  {Style.RESET_ALL}')
    print(f'{Fore.RED}▐█· ██▀·██ ▄▄ ▄█▀▄ ▐█▐▐▌▄▀▀▀█▄█▌▐█▌██▪   ▐█.▪{Style.RESET_ALL}')
    print(f'{Fore.RED}▐█▌▐█▪·•▐███▌▐█▌.▐▌██▐█▌▐█▄▪▐█▐█▄█▌▐█▌▐▌ ▐█▌·{Style.RESET_ALL}')
    print(f'{Fore.RED}▀▀▀.▀   ·▀▀▀  ▀█▄▀▪▀▀ █▪ ▀▀▀▀  ▀▀▀ .▀▀▀  ▀▀▀ {Style.RESET_ALL}')
    print(f'{Fore.BLUE}                                   by Roger{Style.RESET_ALL}')

    
    print(' ')
    print(f'{Fore.BLUE}[1] informações geográficas;{Style.RESET_ALL}')
    print(f'{Fore.BLUE}[2] Download/instruções NMAP;{Style.RESET_ALL}')
    print(f'{Fore.BLUE}[3] Download/instruções WHOIS;{Style.RESET_ALL}')
    print(f'{Fore.BLUE}[4] informações WHOIS;{Style.RESET_ALL}')
    print(f'{Fore.BLUE}[0] fechar;{Style.RESET_ALL}')
    
    i = input('- ')
    
    if i == '1':
        try:
            ip = input('Digite seu IP. Ex: 192.168.0.10 -  ')
            r = requests.get(f'https://ipinfo.io/{ip}/json')
            d = r.json()

            print('Cidade:', d.get('city'))
            print('Região:', d.get('region'))
            print('País:', d.get('country'))
            print('Timezone:', d.get('timezone'))
            print('Localização:', d.get('loc'))
            print('Org:', d.get('org'))
            print('Hostname:', d.get('hostname'))
            print('Postal:', d.get('postal'))
        
        except ValueError:
            print('- Comando Falhou')
    
    elif i == '2':
       print(' ')
       print('Deseja investigar mais um endereço ip? esses comandos vão te ajudar.')
       print('NMAP investigação:')
       print('instalação-')
       print(f'{Fore.GREEN}Linux: sudo apt-get install nmap;{Style.RESET_ALL}')
       print(f'{Fore.RED}Termux: pkg install nmap{Style.RESET_ALL}')
       print(f'{Fore.BLUE}Windows: site - nmap.org{Style.RESET_ALL}')
       print('-----------------------------------------')
       print('comandos básicos-')
       print('nmap -sV 193.168.0.10; Descobrir serviços e versões em execução nas aportas abertas;')
       print('nmap -O <ip>; Verificar o sistema do dispositivo;')
       print('nmap -A <ip>; Fazer uma varredura agressiva(descobre portas, serviços e sistema operacional;)')
       print('Lembre-se, qualquer ação que seja feito, fique por sua responsabilidade;')
       print('Sujeiro a dar erro, pois a maioria dos IPs tem um firewall')
       print('nmap -sA <ip>; detecta se há firewall(precida de root).')
       print('-Alguns comandos de nmap para investigação; Brevemente terá atualização.')

       print(f'{Fore.BLUE}[1]NMAP download Termunx{Style.RESET_ALL}')
       print(f'{Fore.BLUE}[2]NMAP download Linux{Style.RESET_ALL}')
       print(f'{Fore.BLUE}[0]Fechar{Style.RESET_ALL}')
       dw = input('- ')

       try:
           if dw == '1':
               os.system('pkg install nmap')
           elif dw == '2':
               os.system('sudo apt-get install nmap')
           elif dw == '0':
               break
       except ValueError:
           print('- Comando inválido.')
       
    elif i == '4':
        print(f'{Fore.GREEN}[1]Prosseguir;{Style.RESET_ALL}')
        print('[0]Caso não tenha instalado o WHOIS, sujeito a ocorrer erros(Fechar);')

        m = input('- ')

        try:
            if m =='1':
                print('Digite seu IP. Ex: 192.168.0.10')
                per = input('- ')

                re = requests.get(f'https://ipinfo.io/{per}/json')
                da = re.json()
                
                if 'ip' in da and da['ip'] == per:
                    ipe = da['ip']                  
                    print('  ')
                    print('ip:', ipe)
                    print(f'{Fore.GREEN}WHOIS:{Style.RESET_ALL}')
                    print('####################################')
                    try:
                        print(os.system(f'whois -H {ipe}'))
                    except Exception as e:
                        print('- Falha:', e)
                else:
                    print('IP inválido/ Falha')
    

                
            elif m == '0':
                break    
        except ValueError:
            print('- Comando inválido/Erro no sistema.')

    elif i == '3':
        print('Deseja investigar mais um endereço ip? esses comandos vão te ajudar.') 
        print('WHOIS investigação:')
        print('instalação-')
        print(f'{Fore.GREEN}Linux: sudo apt-get install whois;{Style.RESET_ALL}')
        print(f'{Fore.RED}Termux: pkg install whois{Style.RESET_ALL}')
        print('whois -H 192.168.0.10; O comando básico para investigar um IP público;')
        print('whois -h whois.ripe.net <ip>; Para consultar o servidor de RIPE (usado para IPs da Europa)')
        print('whois -h whois.arin.net <ip>; Para consultar o servidor de ARIN (usado para IPs da América do Norte)')
        print('Lembre-se, qualquer ação que seja feito, fique por sua responsabilidade;')
        print('Talvez, brevemente terá atualizações;')
        
        print(f'{Fore.BLUE}[1]WHOIS download Termunx{Style.RESET_ALL}')
        print(f'{Fore.BLUE}[2]WHOIS download Linux{Style.RESET_ALL}')
        print(f'{Fore.BLUE}[0]Fechar{Style.RESET_ALL}')

        dw2 = input('- ')
        try:
         if dw2 == '1':
            os.system('pkg install whois')
         elif dw2 == '2':
            os.system('sudo apt-get install whois')
         elif dw2 == '0':
            break
            
        except ValueError:
            print('- Comando inválido/Erro no sistema.')
    elif i == '0':
        print(' ')
        print('Fechando...')
        sys.exit()
    
    else:
        print('- Comando inválido.')
