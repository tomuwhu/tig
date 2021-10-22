def tsz(s):
    def f(i=0, j=len(s)-1):
        nonlocal s
        if j <= i:
            return 0
        elif s[i] == s[j]:
            return f(i + 1, j - 1)
        else:
            return 1 + min(f(i + 1, j), f(i, j - 1))
    return f()
print(tsz("géza kék az ég"))
# http://www.inf.u-szeged.hu/~tnemeth/examples/algoexamples/Tukorszo_forras.html