next = "O", table = {}, n = 16
function f(e) {
    if (e.innerHTML == "") {
        next = next == "O" ? "X" : "O"
        e.innerHTML = next, e.setAttribute('class', next), x = e.cellIndex
        y = e.parentElement.rowIndex, table[x][y] = next
        setTimeout( () =>
            [[1,1],[1,0],[0,1],[-1,1]].forEach( direction => {
                xp=x, yp=y, maxh=0, [vx, vy] = direction
                while (table[xp][yp] === next) xp += vx, yp += vy, maxh++
                xp=x, yp=y
                while (table[xp][yp] === next) xp -= vx, yp -= vy, maxh++
                if (maxh > 5) alert(`Nyert: ${next}`), init()
            } 
        ), 100)
    }
}
function init() {
    table = Array(n).fill().map(() => Array(n).fill())
    document.getElementById('t').innerHTML = `
    <table>
        ${Array(n).fill(`
        <tr>
            ${Array(n).fill(`<td onmouseup="f(this)" />`).join('')}
        </tr>
        `).join('')}
    </table>`
}
init()