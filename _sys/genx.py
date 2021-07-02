def f(fn):
    return "<option>"+fn+"</option>"

from os import listdir
from os.path import isfile, join
path = "./py"
files = [f for f in listdir(path) if isfile(join(path, f))]
myhtml = """
<meta charset="ISO-8859-2">
<script>
function load() {
    file="py/"+document.getElementById("sel").value
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("code").innerHTML= xhttp.responseText;
            hljs.highlightAll()
        }
    };
    xhttp.open("GET", "./"+file, true);
    xhttp.send();
}
</script>
<link rel="stylesheet" href="main.css">
<link rel="stylesheet"
      href="hljs/a11y-dark.css">
<script src="hljs/highlight.min.js"></script>
<h1>Python példaprogramok</h1>
<select onchange="load()" id="sel">
<option></option>
"""+''.join(map(f, files))+"""
</select>
<pre><code class="language-python" id="code"></code></pre>
"""

f = open("pyexamles.html", "w")
f.write(myhtml)
f.close()
