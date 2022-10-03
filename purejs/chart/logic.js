const ctx = document.getElementById('myChart');
const myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Opel', 'Ford', 'Subaru', 'Suzuki', 'Mazda', 'Skoda'],
        datasets: [{
            label: '# of Votes',
            data: [12, 19, 3, 5, 2, 7],
            backgroundColor: 'rgba(54, 162, 235, 0.2)',
            borderColor: 'rgba(54, 162, 235, 1)',
            borderWidth: 1
        }]
    }
});