#### 2. feladat

SELECT cim, eredeti FROM film WHERE magyarszoveg = "Heltai Olga"

#### 3. feladat

SELECT rendezo, szinkronrendezo FROM film WHERE ev > 2000 GROUP BY rendezo, szinkronrendezo

#### 4. feladat

SELECT magyarszoveg, cim FROM film WHERE rendezo = "Christopher Nolan" and studio = "Mafilm Audio Kft." ORDER BY magyarszoveg

#### 5. feladat

SELECT cim, eredeti, szinesz, szerep FROM szinkron INNER JOIN film ON szinkron.filmaz = film.filmaz WHERE hang = "Anger Zsolt"

#### 6. feladat

SELECT cim, eredeti, count(*) `szinkronszerepek száma` 
FROM szinkron INNER JOIN film ON szinkron.filmaz = film.filmaz 
GROUP BY film.filmaz

#### 7. feladat

SELECT szerep, szinesz, hang FROM szinkron WHERE szerep like "% rab%" or szerep like "rab%"

#### 8. feladat

SELECT szinesz `Színész-rendező` FROM film, szinkron WHERE rendezo = szinesz GROUP BY szinesz

#### 9. feladat

SELECT cim, hang FROM film, szinkron WHERE film.filmaz = szinkron.filmaz and
szinkron.filmaz in (SELECT szinkron.filmaz FROM szinkron WHERE hang="Pap Kati") and hang!="Pap Kati"
GROUP BY hang ORDER BY cim, hang