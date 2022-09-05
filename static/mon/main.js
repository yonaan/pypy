const ctx = document.getElementById("myChart").getContext('2d');
  temperatur = JSON.parse(document.getElementById('temperatur').textContent);
  waktu = JSON.parse(document.getElementById('waktu').textContent);
var graphData = {
    type: 'line',
    data: {
        labels: ['good','warning','danger'],
        datasets: [{
            label: 'Trend',
            data:[temperatur,waktu],    
            backgroundColor: [
                "#16C79A",
                "#F7EA00",
                "#DD2C00"
            ],
            borderWidth: 1,
            borderColor: 'rgb(75, 192, 192)',
            tension:0.2
        }]
    },
    options: {
    }
}
const myChart = new Chart(ctx, graphData);
