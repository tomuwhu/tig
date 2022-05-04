from browser import document as D, html as H
SB = H.DIV( Class = "SB" )
Sx = H.DIV( Class = "Sx" )
D <= H.DIV((
    H.HEADER("GYAKBANK - SZEGED"), SB,
    H.H2( "Fizetési felszólítás", Class="C" ), SB,
    H.DIV( f"Tisztelt {adat['nev']}!", Class="L" ), Sx,
    H.DIV( f"""
        Tartozása nyilvántartásunk szerint {adat["tartozas"]} Ft, 
        melyet kérünk 1199-1119-34727456 számú bankszámlára befizetni!
        """, Class="L"), SB,
    H.TABLE((
        H.TD(),
        H.TD( "Dr. Árva Aladár Ákos<br>főosztályvezető", Class = "AI" )
    )), SB,
    H.FOOTER( """
        Információ, adategyeztetés: (70) 727-34-56 - http://www.gyakbankszeged.hu
    """ ), H.HR()
) for adat in [
    { "nev": "Kiss Béla", "tartozas": 76325 },
    { "nev": "Nagy Endre Zoltán", "tartozas": 26320 },
    { "nev": "Országh Zsófia", "tartozas": 16300 },
    { "nev": "Palócz Péter Pál", "tartozas": 21190 },
])