def f(fn):
    return f"<option>{fn}</option>"
from os import listdir
from os.path import isfile, join as js
path = "./py"
files = [f for f in listdir(path) if isfile(js(path, f))]
files.sort()
h = open("_sys/genx.pth", "r")
myhtml = h.read().replace('$1$',"\n".join(map(f, files)))
h.close()
w = open("pyexamples.html", "w")
w.write(myhtml)
w.close()
