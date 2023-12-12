#izveidot vārdnīcu ar datiem par automašīnu(4)
auto={
    'Zīmols':'volvo',
    'Krāsa':'Balts',
    'Gads':2021,
    'Modelis':'xc90'
}
dati = input('Ievadiet zīmolu, lai pārbaudītu:')
if dati== auto['Zīmols']:
    print('🚘 ir vārdnīcā ')
elif dati==auto.values():
    print('🚘ir kā vērtība')
else:
    print('🚘 nav')
