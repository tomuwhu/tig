from browser import document as D, html as H, timer as T

def h(n, i, j):
    t = ["⓵","⓶","⓷"]
    if n == 1: yield t[i], t[j]
    else:
        for i in [h(n-1, i, 3-i-j), h(1, i, j), h(n-1, 3-i-j, j)]:
            yield from i 

c = 0

l = [["❴", H.SPAN(i), "➺", H.SPAN(j), "❵"] for i, j in h(4, 0, 1)]

def f():
    global c
    D <= H.DIV(l[c])
    c += 1

iv = T.set_interval(f, 1000)