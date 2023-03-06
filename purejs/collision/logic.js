function coll(el1, el2) {
    var rect1 = el1.getBoundingClientRect()
    var rect2 = el2.getBoundingClientRect()
    return !(
      rect1.top > rect2.bottom ||
      rect1.right < rect2.left ||
      rect1.bottom < rect2.top ||
      rect1.left > rect2.right
    )
}
setInterval(() => {
    x1 = document.getElementById("o1")
    x2 = document.getElementById("o2")
    if (coll(x1, x2)) {
        setTimeout(() => {
            x1.style.display = "none"
            x2.style.display = "none"
            document.getElementById("go").style.display = "block"
        }, 50)
    }
})