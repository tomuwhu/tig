
suly = [5, 8, 9, 11, 7, 3, 2]
fontossag = [1, 7, 8, 6, 3, 9, 4] 
wmax=20
def hatizsak(i, w):
    if w==0: return 0
    if i==0:
        if w > suly[0]:
            return 0
        else:
            return fontossag[0]
    if suly[i] > w:
        return hatizsak(i - 1, w)
    return max(hatizsak(i - 1, w), fontossag[i] + hatizsak(i - 1, w-suly[i]))

n=len(suly)
print("Hátizsak - rekurzív")
print(f'Idealis berakásnal az összfontossag: {hatizsak(n-1, wmax)}')

