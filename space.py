def kiiras(lista):
    szamlalo = 1
    for _ in range(3):
        legnagyobb_honap = lista.index(max(lista)) + 1
        legnagyobb_ertek = max(lista)
        legnagyobb_helye = lista.index(max(lista))
        lista[legnagyobb_helye] = 0
        print(f'{szamlalo}. legtöbb születés számú hónap:{legnagyobb_honap}. hónap, ennyi százaleka:{legnagyobb_ertek:.1f}%')
        szamlalo += 1

def ossze_szamolas(lista):
    szuletesek_szama = len(lista) - 1
    szuletesi_honapok = ['1','2','3','4','5','6','7','8','9','10','11','12']
    szuletesi_szazalek = []
    for honap in szuletesi_honapok:
        honap_szam = lista.count(honap) / szuletesek_szama * 100
        szuletesi_szazalek.append(honap_szam)
    kiiras(szuletesi_szazalek)


def main():
    with open('astronauts.csv', 'r', encoding='utf-8') as forrasfajl:
        szuletesek = []
        for sor in forrasfajl:
            adatok = sor.strip().split(',')
            adat = adatok[4].split('/')
            szuletesek.append(adat[0])
        ossze_szamolas(szuletesek)

main()