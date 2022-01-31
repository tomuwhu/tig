# adott tárgyak egy listája, minden tárgynak van mérete és fontossága, továbbá adott egy hátizsák adott mérettel
# feladat:
# mennyi a hátizsákba beférő maximális összes fontosság (fontosságok összege)
t = [(5, 1), (8, 7),(9, 8),(11, 6),(7, 3),(3, 9),(2, 4)] # tárgyak listája (méret, fontosság)
wmax = 20 # hátizsák mérete
def hatizsak(i, w):
    if w==0: return 0
    if i==0:
        if w > t[0][0]: return 0
        else:           return t[0][1]
    if t[i][0] > w:     return hatizsak(i - 1, w)
    return max(hatizsak(i - 1, w), t[i][1] + hatizsak(i - 1, w - t[i][0]))
n=len(t)
print("Hátizsák - rekurzív")
print(f'Idealis berakásnal az összfontosság: {hatizsak(n - 1, wmax)}')
