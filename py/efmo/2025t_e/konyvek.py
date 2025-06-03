l = [(lambda xl: {'év': int(xl[0]), 'negyedév': int(xl[1]), 'magyar': True if xl[2]=='ma' else False,
    'Szerző_és_cím': xl[3], 'Példányszám': int(xl[4])})(i.split(";")) for i in open("kiadas.txt").readlines()]

print("2. feladat:")
szerző = "Benedek Elek"
# szerző = input("Szerző: ")
print(f"{sum([1 for i in l if szerző in i['Szerző_és_cím']])} könyvkiadás")

print("3. feladat:")
lnpsz = sorted(l, key = lambda x: x['Példányszám'])[-1]['Példányszám']
print(f"Legnagyobb példányszám: {lnpsz}, előfordult {sum([1 for i in l if i['Példányszám'] == lnpsz])} alkalommal") 

print("4. feladat:")
ekm = [i for i in l if not i['magyar'] and i['Példányszám'] > 40000][0]
print(f"{ekm.get('év')}/{ekm['negyedév']} {ekm.get('Szerző_és_cím')}")

print("5. feladat:")
stat = dict()
for i in l:
  if i['év'] not in stat:
    stat[i['év']] = {"mk": 0, "mplsz": 0, "kk": 0, "kplsz": 0}
  if i['magyar']:
    stat[i['év']]['mk'] += 1
    stat[i['év']]['mplsz'] += i['Példányszám']
  else:
    stat[i['év']]['kk'] += 1
    stat[i['év']]['kplsz'] += i['Példányszám']
print("Év", "Magyar kiadás", "Magyar példányszám", "Külföldi kiadás", "Külföldi példányszám", sep="\t")    
for év in stat:
  (mk, mplsz, kk, kplsz) = stat[év].values()
  print(év, mk, mplsz, kk, kplsz, sep = 2 * "\t")
with open("tabla.html", "w") as f:
  f.write("<table style='margin:auto;'>\n<tr><th>Év</th><th>Magyar kiadás</th><th>Magyar példányszám</th><th>Külföldi kiadás</th><th>Külföldi példányszám</th></tr>\n")
  for év in stat:
    (mk, mplsz, kk, kplsz) = stat[év].values()
    f.write(f"<tr><td>{év}</td><td>{mk}</td><td>{mplsz}</td><td>{kk}</td><td>{kplsz}</td></tr>\n")
  f.write("</table>\n")
  f.write("<style>td { text-align: center; width: 200px; height: 30px; box-shadow: 1px 1px 3px inset gray; border-radius: 10px;}</style>")

print("6. feladat:\nLegalább kétszer, nagyobb példányszámban újra kiadott könyvek:")
f6 = dict()
f62 = dict()
for i in l:
  if i['Szerző_és_cím'] not in f6:
    f6[i['Szerző_és_cím']] = i['Példányszám']
  elif f6[i['Szerző_és_cím']] < i['Példányszám']:
    if i['Szerző_és_cím'] in f62:
      f62[i['Szerző_és_cím']] += 1
    else:
      f62[i['Szerző_és_cím']] = 2
for csz in f62.keys():
  if f62[csz] > 2:
    print(csz)