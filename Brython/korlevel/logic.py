from browser import document as D, html as H

D <= H.DIV((
    H.HEADER("GYAKBANK - SZEGED"),
    H.DIV( Class = "SB" ),
    H.H2( "Fizetési felszólítás", Class="C" ),
    H.DIV( Class = "SB" ),
    H.DIV( f"Tisztelt {adat['nev']}!", Class="L" ),
    H.DIV( Class = "Sx" ),
    H.DIV( f"""
        Tartozása nyilvántartásunk szerint {adat["tartozas"]} Ft, 
        melyet kérünk 1199-1119-34727456 számú bankszámlára befizetni!
        """, Class="L"),
    H.DIV( Class = "SB" ),
    H.TABLE((
        H.TD(),
        H.TD( "Dr. Árva Aladár Ákos<br>főosztályvezető", Class = "AI" )
    )),
    H.DIV( Class = "SB" ),
    H.FOOTER( """
        Információ, adategyeztetés: (70) 727-34-56 - http://www.gyakbankszeged.hu
    """ ),
    H.HR()
) for adat in [
    { "nev": "Kiss Béla", "tartozas": 76325 },
    { "nev": "Nagy Endre Zoltán", "tartozas": 26320 },
    { "nev": "Országh Zsófia", "tartozas": 16300 },
    { "nev": "Palócz Péter Pál", "tartozas": 21190 },
])