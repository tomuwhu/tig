import svgwrite

dwg = svgwrite.Drawing('test.svg', profile='tiny')
dwg.add(dwg.line((0, 0), (10, 10), stroke=svgwrite.rgb(10, 10, 16, '%')))
dwg.add(dwg.text('SVG Test', insert=(10, 20), fill='red'))
dwg.save()