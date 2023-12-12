valstis={
    'Somija':['Helsinki', 'Tampere', 'Rovaniemi ','Kemijarvi','Jyvaskyle'],
    'Italija':['Venēcija', 'Roma', 'Piza', 'Florence', 'Palermo'],
    'Anglija':['Londona,', 'Mančestera', 'Stoke-on-trent', 'Birmingham', 'Edingburga']
    }

for atslega,vertiba in valstis.items():
    for i in vertiba:
        print('{}:{}'.format(atslega,i))
    print('💖💖💖')

#izdrūkāt vārdnīcas elementus piekļūstot vārdnīcas konkrētai
for i in valstis['Anglija']:
    print(i)

#izdrukā pirmās 3 Somijas pilsētas
print(valstis['Somija'][:3])

#izdrukā pēdējās 2 pilsētas no Itālijas
print(valstis['Italija'][-2:])

#iegūst visas pilsētas no Anglijas izņemot 3 pēdējās
print(valstis['Anglija'][:-3])

#iegūt no 2-5 pilsētai no Anglijas
print(valstis['Anglija'][1:6])