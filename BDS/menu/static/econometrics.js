import data from '../static/BoE.json' assert { type: 'json' };

// Create the chart
// Get the canvas element and its context
var ctx = document.getElementById("interestChart").getContext("2d");

var interestRates = data.map(function(entry) {
	return parseFloat(entry["Bank Rate"]);
}); // X values

var dates = data.map(function(entry) {
    return moment(entry.Date).format('YYYY');
}); // Y values



// Create a new line chart using Chart.js
var myChart = new Chart(ctx, {
	type: 'line', // Set the type of chart to be a line chart
	data: { // Set the data to be used for the chart
	labels: dates, // Use the dates array for the x-axis labels
	datasets: [{
		label: 'Interest Rates', // Set the label for the dataset
		data: interestRates, // Use the interestRates array for the y-axis data
		borderColor: 'blue', // Set the color of the line
		fill: true // Do not fill in the area under the line
	}]
	},
	options: { // Set the chart options
		responsive: true, // Allow the chart to be resized responsively
		title: {
			display: true, // Display the chart title
			text: 'Bank Interest Rates', // Set the text of the chart title
		},
		tooltips: { // Set the behavior of the tooltips
			mode: 'index', // Show all tooltips when hovering over the chart
			intersect: true,
		},
		hover: { // Set the behavior of the hover
			mode: 'nearest', // Highlight the nearest point when hovering over the chart
			intersect: true
		},
		scales: { // Set the options for the x- and y-axes
			xAxes: [{
				display: true, // Display the x-axis
				type: 'linear',
				scaleLabel: {
					display: true, // Display the x-axis label
					labelString: 'Date', // Set the x-axis label text
				},
				ticks: {
					stepSize: 15, // Display every other tick on the x-axis
					autoSkip: true, // Automatically skip ticks if there are too many
					maxTicksLimit: 5, // Maximum number of ticks to display
				}
			}],
			yAxes: [{
				type: 'linear',
				display: true, // Display the y-axis
				scaleLabel: {
					display: true, // Display the y-axis label
					labelString: 'Interest Rate' // Set the y-axis label text
				}
			}]
		}
	}
});



/*---------------------------------------------------
// Extract the dates and interest rates from the JSON data
// Map the Date and Bank Rate fields of the JSON data to create two new arrays
var dates = data.map(function(entry) {
	return entry.Date;
});

var interestRates = data.map(function(entry) {
return parseFloat(entry["Bank Rate"]);
});

// Create the chart
// Get the canvas element and its context
var ctx = document.getElementById("interestChart").getContext("2d");

// Create a new line chart using Chart.js
var myChart = new Chart(ctx, {
	type: 'line', // Set the type of chart to be a line chart
	data: { // Set the data to be used for the chart
	labels: dates, // Use the dates array for the x-axis labels
	datasets: [{
		label: 'Interest Rates', // Set the label for the dataset
		data: interestRates, // Use the interestRates array for the y-axis data
		borderColor: 'blue', // Set the color of the line
		fill: false // Do not fill in the area under the line
		}]
	},
	options: { // Set the chart options
		responsive: true, // Allow the chart to be resized responsively
		title: {
		display: true, // Display the chart title
		text: 'Bank Interest Rates' // Set the text of the chart title
		},
		tooltips: { // Set the behavior of the tooltips
		mode: 'index', // Show all tooltips when hovering over the chart
		intersect: false,
		},
		hover: { // Set the behavior of the hover
		mode: 'nearest', // Highlight the nearest point when hovering over the chart
		intersect: true
		},

		scales: { // Set the options for the x- and y-axes
			xAxes: [{
				display: true, // Display the x-axis
				scaleLabel: {
				display: true, // Display the x-axis label
				labelString: 'Date' // Set the x-axis label text
				}
				
			}],
			yAxes: [{
				display: true, // Display the y-axis
				scaleLabel: {
					display: true, // Display the y-axis label
					labelString: 'Interest Rate' // Set the y-axis label text
				}
			}]
		}
	}
});
-----------------------------------*/

/*
// Extract the dates and interest rates from the JSON data
var dates = jsonData.map(function(entry) {
    return entry.Date;
});
var interestRates = jsonData.map(function(entry) {
    return parseFloat(entry["Bank Rate"]);
});

// Create the chart
var ctx = document.getElementById("interestChart").getContext("2d");
var myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: dates,
        datasets: [{
            label: 'Interest Rates',
            data: interestRates,
            borderColor: 'blue',
            fill: false
        }]
    },
    options: {
        responsive: true,
        title: {
            display: true,
            text: 'Bank Interest Rates'
        },
        tooltips: {
            mode: 'index',
            intersect: false,
        },
        hover: {
            mode: 'nearest',
            intersect: true
        },
        scales: {
            xAxes: [{
                display: true,
                scaleLabel: {
                    display: true,
                    labelString: 'Date'
                }
            }],
            yAxes: [{
                display: true,
                scaleLabel: {
                    display: true,
                    labelString: 'Interest Rate'
                }
            }]
        }
    }
});*/
