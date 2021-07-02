def f(fn):
    return f"<option>{fn}</option>"

from os import listdir
from os.path import isfile, join
path = "./py"
files = [f for f in listdir(path) if isfile(join(path, f))]
files.sort()
myhtml = """<meta charset="UTF-8">
<script src="hljs/markdown.min.js"></script>
<script>
function load() {
    file="py/"+document.getElementById("sel").value
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            if (file.split('.')[1]=='md') {
                html_content = markdown.toHTML( xhttp.responseText )
                document.getElementById("code").innerHTML=''
                document.getElementById("content").innerHTML= html_content
                document.getElementById('content').style.visibility = "visible"
                document.getElementById('code').style.visibility = "hidden"
            } else {
                html_content = xhttp.responseText
                document.getElementById("code").innerHTML= html_content;
                document.getElementById("content").innerHTML=''
                document.getElementById('content').style.visibility = "hidden"
                document.getElementById('code').style.visibility = "visible"
            }
            hljs.highlightAll()
        }
    };
    xhttp.open("GET", "./"+file, true);
    xhttp.send();
}
</script>
<link rel="stylesheet"
      href="hljs/a11y-dark.css">
<link rel="stylesheet" href="main.css">
<script src="hljs/highlight.min.js"></script>
<h1>Python p&eacute;ldaprogramok</h1>
<select onchange="load()" id="sel">
<option></option>
"""+''.join(map(f, files))+"""
</select>
<pre><code class="language-python" id="code"></code></pre>
<div style="text-align: center;">
    <div id="content" style="visibility: hidden;"></div>
</div>
"""

f = open("pyexamples.html", "w")
f.write(myhtml)
f.close()
