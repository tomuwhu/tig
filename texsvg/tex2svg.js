function convert(x) {
    var output = document.getElementById(x);
    var input = output.innerHTML.trim();
    output.innerHTML = '';
    MathJax.texReset();
    MathJax.tex2svgPromise(input)
        .then(function (node) {
            output.appendChild(node);
            MathJax.startup.document.clear();
            MathJax.startup.document.updateDocument();
        })
}

var list = document.getElementById("texcode").getAttribute("totex").split(',').reverse()

function f(i) {
    if (i>0) {
        setTimeout( () => {
            convert(list[i-1])
            f(i-1)
        }, 200 )
    }
}

window.onload = (event) => {
    f(list.length);
};


