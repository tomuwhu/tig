SELECT 100*(SELECT SUM(letszam) FROM aerob WHERE mkod = 11)/(SELECT letszam FROM megye WHERE kod = 11) f6