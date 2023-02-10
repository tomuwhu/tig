const ctx = document.getElementById('myChart')
ksz = 1, dsz = 10, data = Array(6).fill(0)
ds  = {
    backgroundColor: 'rgba(54, 162, 235, 0.2)',
    borderColor: 'rgba(54, 162, 235, 1)',
    borderWidth: 1
}
lab = (ksz, dsz) =>`Dobások összegének darabszáma ${ksz} kockával ${dsz} dobás után`
const myChart = new Chart(ctx, { type: 'bar', data: {
    labels: data.map((v, i) => i + ksz),
    datasets: [{ label: lab(ksz, dsz), data, ...ds }]
}})
f = v => ( ksz = Number(v), document.getElementById("ksz").innerHTML = ksz, r.d() )
g = v => ( dsz = 10 ** Number(v), document.getElementById("dsz").innerHTML = dsz, r.d() )
r = { d() {
    data = Array(ksz*5+1).fill(0)
    for (i = 0; i < dsz; i++) {
        összeg = 0
        for (j = 0; j < ksz; j++) 
            dobas = Math.floor(Math.random() * 6 + 1),
            összeg += dobas 
        data[összeg - ksz]++
    }
    myChart.data = {
        labels: data.map((v, i) => i + ksz),
        datasets: [{ label: lab(ksz, dsz), data, ...ds }]
    }
    myChart.update()
}}
setTimeout(() => r.d(), 1000);
