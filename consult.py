import requests
import sys
from colorama import Fore, Style

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
    print(f'{Fore.BLUE}[1] informações ip;{Style.RESET_ALL}')
    print(f'{Fore.BLUE}[2] instruções de investigação;{Style.RESET_ALL}')
    print(f'{Fore.BLUE}[3] fechar;{Style.RESET_ALL}')
    
    i = input('- ')
    
    if i == '1':
        try:
            ip = input('Digite seu IP. Ex: 192.0.168.1 -  ')
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
       print('-Alguns comandos de nmap para investigação; Brevemente terá atualização.')
    elif i == '3':
        print(' ')
        print('Fechando...')
        sys.exit()
    
    else:
        print('Comando inválido, digite novamente.')