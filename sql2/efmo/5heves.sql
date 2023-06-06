SELECT megye.nev Megyenév, ROUND(0.1 * 10 * SUM(aerob.letszam) / megye.letszam, 4) Arány
FROM megye, aerob
WHERE mkod = megye.kod and allkod > 1 GROUP BY mkod HAVING Arány > 0.25