n = 60, m = 40, x = 50, y = 20, xd = -1, yd = 0
table = Array(n).fill().map(() => Array(n).fill())
to = document.getElementById('t'), to.innerHTML = `
<table>${Array(m).fill(`
    <tr>
    ${Array(n).fill(`<td/>`).join('')}
    </tr>`).join('')}
</table>`
to = to.children[0].children[0], table[y][x] = 1
to.children[y].children[x].style.backgroundColor = "red"
iv = setInterval(() => {
    x += xd, y += yd
    if (x >= n || y >= m || x < 0 || y < 0 || table[y][x] == 1)
        clearInterval(iv)
    else
        table[y][x] = 1,
        to.children[y].children[x].style.backgroundColor = "red"
}, 100)
addEventListener("keydown", e => { switch (e.key) {
    case "ArrowUp"    : [xd, yd] = [ 0,-1]; break
    case "ArrowDown"  : [xd, yd] = [ 0, 1]; break
    case "ArrowLeft"  : [xd, yd] = [-1, 0]; break
    case "ArrowRight" : [xd, yd] = [ 1, 0]; break
}})

