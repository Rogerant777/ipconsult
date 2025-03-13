import requests
import argparse

print('▪   ▄▄▄· ▄▄·        ▐ ▄ .▄▄ · ▄• ▄▌▄▄▌  ▄▄▄▄▄')
print('██ ▐█ ▄█▐█ ▌▪▪     •█▌▐█▐█ ▀. █▪██▌██•  •██  ')
print('▐█· ██▀·██ ▄▄ ▄█▀▄ ▐█▐▐▌▄▀▀▀█▄█▌▐█▌██▪   ▐█.▪')
print('▐█▌▐█▪·•▐███▌▐█▌.▐▌██▐█▌▐█▄▪▐█▐█▄█▌▐█▌▐▌ ▐█▌·')
print('▀▀▀.▀   ·▀▀▀  ▀█▄▀▪▀▀ █▪ ▀▀▀▀  ▀▀▀ .▀▀▀  ▀▀▀ ')
print('                                   by Roger')


print('ip do maluquete. exemplo (192.0.000.000)')
ip = input('-')

r = requests.get(f'https://ipinfo.io/{ip}')

d = r.json()

print('cidade:', d.get('city'))
print('região: ', d.get('region'))
print('país: ', d.get('country'))
print('timezone: ', d.get('timezone'))
print('seu ip: ', d.get('ip'))
print('localização: ', d.get('loc'))
print('org: ', d.get('org'))
print('hostname: ', d.get('hostname'))
print('postal: ', d.get('posta'))
