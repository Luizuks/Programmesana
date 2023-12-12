#1 uzdevums
import math 
ievaditais_gads=int(input('Ievadi gadu:'))
gada_ped_cip= str(ievaditais_gads)[-2:]
gada_ped_cip2=int(gada_ped_cip)
summa=sum(gada_ped_cip)

if gada_ped_cip/4==0:
    print(f'{ievaditais_gads} ir garais gads.')
else: 
    print(f'{ievaditais_gads} ir īsais gads.')