#piemērs sarakstam ar dažādiem datu tipiem
mixed_list= ['suns', 7.25, 8, True]
print(mixed_list[2])

#apgriezt skaitļu sarakstu
skaitli= [1,2,4,5,6,7,3,4,8,9]
apgriezts= list(reversed(skaitli))
print(apgriezts)

#filtret tikai pāra skaitlus
para_skaitli= [num for num in skaitli if num%2==0]
print(para_skaitli)

#saraksta garums
#garums= len(skaitli)

videjais= sum(skaitli)/len(skaitli)
print(f'Videjais skaitlis:{videjais}')

#atrast lielāko un mazāko skaitli
lielakais= max(skaitli)
mazakais= min(skaitli)
print(f'Skaitļu kopā lielākais skaitlis ir {lielakais} un mazākais ir {mazakais} ')


augli= ['banani', 'apelsini', 'arbuzi', 'aboli', 'bumbieri']
#atrast vardus kas sakas ar konkrētu burtu
varda_sakums=[vards for vards in augli if vards.startswith('a')]
print(f'Vardi kas sākas ar burtu (a):{varda_sakums}')