from browser import document as D, html as H, timer as T
def h(n, i, j):
    t = ["","⓵","⓶","⓷"]
    if n == 1:
        yield t[i], t[j]
    else:
        yield from h(n - 1, i, 6 - i - j)
        yield t[i], t[j]
        yield from h(n - 1, 6 - i - j, j)
counter = 0
l = [(i, j) for i, j in h(4, 1, 2)]

def f():
    global counter
    D <= H.DIV( " ❴" + H.SPAN(l[counter][0]) + "➺" + H.SPAN(l[counter][1]) + "❵ " )
    counter += 1

iv = T.set_interval(f, 1000)