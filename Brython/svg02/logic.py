from browser import document as D, html as H, svg as S
D <= H.SVG([
    S.circle(
        cx = 50 + 48 * i, 
        cy = 50 + 21 * i, 
        r  = 40, 
        stroke = "blue",
        fill=f'rgb({50 + 10 * i} ,{250 - 10 * i}, 220)'
    ) for i in range(20)], 
    viewBox = "0, 0, 1020, 500")