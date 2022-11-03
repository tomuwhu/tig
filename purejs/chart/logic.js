const ctx = document.getElementById('myChart')
const myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Opel', 'Ford', 'Subaru', 'Suzuki', 'Mazda', 'Skoda'],
        datasets: [{
            label: 'Szavazatok száma',
            data: [12, 19, 7, 5, 12, 14],
            backgroundColor: 'rgba(54, 162, 235, 0.2)',
            borderColor: 'rgba(54, 162, 235, 1)',
            borderWidth: 1
        }]
    }
})
function f() {
    myChart.data.datasets.push({
            label: 'Eladási számok',
            data: [17, 16, 3, 15, 8, 17],
            backgroundColor: 'rgba(154, 62, 135, 0.2)',
            borderColor: 'rgba(154, 62, 135, 1)',
            borderWidth: 1
    })
    myChart.update()
    document.getElementById("g").style.display = "none"
}