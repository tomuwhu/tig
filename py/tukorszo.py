def tsz(s):
    def f(i = 0, j = len(s) - 1):
        nonlocal s
        return 0 if not j > i else f(i + 1, j - 1) if s[i] == s[j] else 1 + min(f(i + 1, j), f(i, j - 1))
    return f()
print(tsz("géza kék az ég"))
# http://www.inf.u-szeged.hu/~tnemeth/examples/algoexamples/Tukorszo_forras.html