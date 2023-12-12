svari_aboli = float(input("Ievadiet cik kilogramus ābolu jūs vēlaties izmantot: "))
budgets=int(input('Kāds ir jūsu budžets ievārijumam?'))
majas_cukurs = input("Vai jums ir cukurs mājās? (j=jā, n=nē) ")
majas_udens = input("Vai jums ir ūdens mājās? (j=jā, n=nē) ")
majas_citrons = input("Vai jums ir citroni mājās? (j=jā, n=nē) ")
majas_mandelu_ekstrakts = input("Vai jums ir mandeļu ekstrakts mājās? (j=jā, n=nē) ")
majas_kanelis = input("Vai jums ir kanelis mājās? (j=jā, n=nē) ")

svari_cukurs = 1.0  # 1 kg
svari_udens = 500.0  # 500 ml
svari_citrons = 1  # 1 gab
svari_mandelu_ekstrakts = 5.0  # 5 ml
svari_kanelis = 10.0  # 10 grami

cukura_veids = input("Vai vēlaties izmantot parasto cukuru (p) vai ievārījumu cukuru (i)? ")

# Cenu saraksts
cena_cukurs_parastais = 1.20  # eiro par 1 kg
cena_cukurs_ievarijumu = 1.50  # eiro par 1 kg
cena_udens = 1.00  # eiro par 1 litru
cena_citrons = 0.50  # eiro par gabalu
cena_mandelu_ekstrakts = 1.00  # eiro par 10 ml
cena_kanelis = 0.62  # eiro par 10 gramiem

# Produktu pieejamība pēc noklusējuma
izmaksas_cukurs = 0
izmaksas_udens = 0
izmaksas_citrons = 0
izmaksas_mandelu_ekstrakts = 0
izmaksas_kanelis = 0

# Aprēķinu izmaksas
if svari_aboli > 0:
    izmaksas_cukurs = svari_cukurs * (cena_cukurs_parastais if cukura_veids == 'p' else cena_cukurs_ievarijumu)
    izmaksas_udens = svari_udens / 1000 * cena_udens
    izmaksas_citrons = svari_citrons * cena_citrons
    izmaksas_mandelu_ekstrakts = (svari_mandelu_ekstrakts / 10) * cena_mandelu_ekstrakts
    izmaksas_kanelis = (svari_kanelis / 10) * cena_kanelis
    # Aprēķinu izmaksas
if svari_aboli > 0:
   
    if majas_cukurs == 'n':
        izmaksas_cukurs = svari_cukurs * (cena_cukurs_parastais if cukura_veids == 'p' else cena_cukurs_ievarijumu)
    if majas_udens == 'n':
        izmaksas_udens = svari_udens / 1000 * cena_udens
    if majas_citrons == 'n':
        izmaksas_citrons = svari_citrons * cena_citrons
    if majas_mandelu_ekstrakts == 'n':
        izmaksas_mandelu_ekstrakts = (svari_mandelu_ekstrakts / 10) * cena_mandelu_ekstrakts
    if majas_kanelis == 'n':
        izmaksas_kanelis = (svari_kanelis / 10) * cena_kanelis


# Kopējās izmaksas
kopigas_izmaksas = izmaksas_cukurs + izmaksas_udens + izmaksas_citrons + izmaksas_mandelu_ekstrakts + izmaksas_kanelis

print("Izmaksas veikā par produktiem, kuri nav mājās vai ir izvēlēti:")
print(f"Cukurs: {izmaksas_cukurs} eiro")
print(f"Ūdens: {izmaksas_udens} eiro")
print(f"Citroni: {izmaksas_citrons} eiro")
print(f"Mandelu ekstrakts: {izmaksas_mandelu_ekstrakts} eiro")
print(f"Kanelis: {izmaksas_kanelis} eiro")
print(f"Kopējās izmaksas: {kopigas_izmaksas} eiro")

#papildopcija
if budgets>kopigas_izmaksas:
    print('Nauda sanāk!')
else:
    print('Nauda ir par maz!')