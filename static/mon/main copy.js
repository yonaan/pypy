const ctx = document.getElementById('myChart').getContext('2d');
var graphData = {
    type: 'line',
    data: {
        labels: ['', '', '', '', '',],
        datasets: [{
            label: 'Trend',
            data: [],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderWidth: 1
        }]
    },
    options: {
    }
}
const myChart = new Chart(ctx, graphData);

var socket = new WebSocket('ws://localhost:8000/ws/mon/');

socket.onmessage = function(e){
    
    var djangoData = JSON.parse(e.data);
    console.log(djangoData);
    var tempdata = graphData.data.datasets[0].data;
    tempdata.shift();
    tempdata.push(djangoData.value);
    graphData.data.datasets[0].data = tempdata;
    myChart.update();
}