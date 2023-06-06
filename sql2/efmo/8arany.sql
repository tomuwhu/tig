SELECT megye.nev Megye, ROUND(0.1 * 10 * SUM(aerob.letszam) / megye.letszam, 4) Arány
FROM megye, aerob
WHERE mkod = megye.kod GROUP BY mkod ORDER BY Arány DESC LIMIT 1