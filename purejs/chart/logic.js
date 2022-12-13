const ctx = document.getElementById('myChart')
ksz = 1
dsz = 10
data = [0, 0, 0, 0, 0, 0]
const myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: [1, 2, 3, 4, 5, 6],
        datasets: [{
            label: `Dobások összegének darabszáma ${ksz} kockával ${dsz} dobás után`,
            data: [0, 0, 0, 0, 0, 0],
            backgroundColor: 'rgba(54, 162, 235, 0.2)',
            borderColor: 'rgba(54, 162, 235, 1)',
            borderWidth: 1
        }]
    }
})
function f(v) {
    ksz = Number(v)
    document.getElementById("ksz").innerHTML = ksz
    rd()
}
function g(v) {
    dsz = 2 ** Number(v)
    document.getElementById("dsz").innerHTML = dsz
    rd()
}
function rd() {
    data = Array(ksz*5+1).fill(0)
    for (i=0; i < dsz; i++) {
        dobo = 0
        for (j=0; j < ksz; j++) {
            dobas = Math.floor(Math.random()*6 + 1)
            dobo += dobas 
        }
        data[dobo-ksz]++
    }
    myChart.data = {
        labels: data.map((v, i) => i + ksz),
        datasets: [{
            label: `Dobások összegének darabszáma ${ksz} kockával ${dsz} dobás után`,
            data: data,
            backgroundColor: 'rgba(54, 162, 235, 0.2)',
            borderColor: 'rgba(54, 162, 235, 1)',
            borderWidth: 1
        }]
    }
    myChart.update()
}
setTimeout(() => {
    rd()
}, 1000);
