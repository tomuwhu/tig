xm = window.innerWidth
ym = window.innerHeight
tx = xm / 2 - 50
ty = ym - 150
xv = 0
yv = 0
speed = 50
function start(b) {
    b.style.display = "none"
    tank = document.getElementById("tank")
    tank.style.display = "inline-block"
    tank.style.position = "fixed"
    tank.style.top = `${ty}px`
    tank.style.left = `${tx}px`
}
function f(e) {
    switch (e.key) {
        case "ArrowRight":
            xv = speed
            yv = 0
            break
        case "ArrowLeft":
            xv = -speed
            yv = 0
            break
        case "ArrowUp":
            yv = -speed
            xv = 0
            break
        case "ArrowDown":
            yv = speed
            xv = 0
            break
        case " ":
            xv = 0
            yv = 0
            break
    }
}
setInterval(() => { 
    tx += xv
    ty += yv
    tank.style.top = `${ty}px`
    tank.style.left = `${tx}px`
}, 100)