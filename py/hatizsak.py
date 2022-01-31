# adott tárgyak egy listája, minden tárgynak van mérete és fontossága, továbbá adott egy hátizsák adott mérettel
# feladat:
# mennyi a hátizsákba beférő maximális összes fontosság (fontosságok összege)
t = [(5, 1), (8, 7),(9, 8),(11, 6),(7, 3),(3, 9),(2, 4)] # tárgyak listája (méret, fontosság)
n = len(t)
wmax = 20 # hátizsák mérete
def h(i, w):
    if w==0: return 0
    if i==0:
        if w > t[0][0]: return 0
        else:           return t[0][1]
    if t[i][0] > w:     return h(i - 1, w)
    return max(h(i - 1, w), t[i][1] + h(i - 1, w - t[i][0]))
print("Hátizsák - rekurzív")
print(f'Idealis berakásnal az összfontosság: {h(n - 1, wmax)}')
# https://web.cs.elte.hu/blobs/diplomamunkak/bsc_matelem/2016/horvath_akos.pdf
# https://prog.hu/tudastar/189582/hatizsak-feladat-megoldasa-dinamikus-programozassal
# https://www.youtube.com/watch?v=PLJHuErj-Tw