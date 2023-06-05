#### 2. feladat

SELECT cim, eredeti FROM film WHERE magyarszoveg = "Heltai Olga"

#### 3. feladat

SELECT rendezo, szinkronrendezo FROM film WHERE ev > 2000 GROUP BY rendezo, szinkronrendezo

#### 4. feladat

SELECT magyarszoveg, cim FROM film WHERE rendezo = "Christopher Nolan" and studio = "Mafilm Audio Kft." ORDER BY magyarszoveg