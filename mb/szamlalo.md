# Számláló program specifikáció

## Számláló (n) demonstrációja a micro:bit-en

a következők szerint:

- n kezdetben 0, (n maximális értéke 25 lehet),
- a kijelzőn alapesetben n darab led világítson (*),
- a logóra kattintva a számláló (n) értéke eggyel nőjön,
- az A nyomógomb hatására a számláló (n) értéke legyen 0 (reset),
- a B nyomógomb hatására a kijelzőn jelenjen meg a számláló (n) értéke számmal, több számjegy esetén scrollozva, majd egy másodperc elteltével - illetve scrollozás után - térjen vissza az alapeset (*) módra,
- az eszközt megrázva írja ki a kijelzőre 2^n értéket (több számjegy esetén scrollozva) majd térjen vissza alapeset (*) módba!

[megoldás letöltése (micro:bit hex fájl)](mb/szamlalo.hex)

![...](mb/szamlalo.jpg)
