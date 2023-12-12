#izveidot tukšu vārdnīcu
vardnica={}

ievade_atsl= input('Ievadiet atslēgu:')
ievade_vert= input('Ievadiet vērtību:')

#pārbauda lietotāja ievadi un rediģē vārdnīcu
if ievade_atsl in vardnica:
    vardnica[ievade_atsl]=ievade_vert
    print('Vārdnīca tika atjaunināta')

else:
    vardnica[ievade_atsl]=ievade_vert
    print('Jauns pāris tika pievienots vārdnīcai')

print('Atjaunotā vārdnīca:', vardnica)