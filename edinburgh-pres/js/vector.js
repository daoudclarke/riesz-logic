
var margin = {top: 20, right: 40, bottom: 30, left: 20},
width = 960 - margin.left - margin.right,
height = 500 - margin.top - margin.bottom,
barWidth = Math.floor(width / 5) - 1;

var x = d3.scale.linear()
    .range([barWidth / 2, width - barWidth / 2]);

var y = d3.scale.linear()
    .range([height, 0]);

var yAxis = d3.svg.axis()
    .scale(y)
    .orient("right")
    .tickSize(-width)
    .tickFormat(function(d) { return d; }); //Math.round(d / 1e6) + "M"; });

// An SVG element with a bottom-right origin.
var svg = d3.selectAll(".disjunction").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

// A sliding container to hold the bars by birthyear.
var birthyears = svg.append("g")
    .attr("class", "birthyears");

// // A label for the current year.
// var title = svg.append("text")
//     .attr("class", "title")
//     .attr("dy", ".71em")
//     .text(2000);

d3.csv("/vectors.csv", function(error, data) {

  // Convert strings to numbers.
    data.forEach(function(d) {
	d.people = +d.people;
	d.year = +d.year;
	d.age = +d.age;
    });

  // Compute the extent of the data set in age and years.
    var age0 = d3.min(data, function(d) { return d.age; }),
    age1 = d3.max(data, function(d) { return d.age; }),
    year0 = d3.min(data, function(d) { return d.year; }),
    year1 = d3.max(data, function(d) { return d.year; }),
    people0 = d3.min(data, function(d) { return d.people; }),
    people1 = d3.max(data, function(d) { return d.people; }),
    year = year0;

  // Update the scale domains.
    x.domain([age0, age1]);
    y.domain([people0, people1]);
    //y.domain([-10, 10]);

  // Produce a map from year and birthyear to [male, female].
    data = d3.nest()
	.key(function(d) { return d.year; })
	.key(function(d) { return d.age; })
	.rollup(function(v) { return v.map(function(d) { return d.people; }); })
	.map(data);

  // Add an axis to show the population values.
    svg.append("g")
	.attr("class", "y axis")
	.attr("transform", "translate(" + width + ",0)")
	.call(yAxis)
	.selectAll("g")
	.filter(function(value) { return !value; })
	.classed("zero", true);

  // Add labeled rects for each birthyear (so that no enter or exit is required).
    //var y_displacement = y(0 - 
    var birthyear = birthyears.selectAll(".birthyear")
	// .data(d3.range(year0 - age1, year1 + 1, 1))
	.data(d3.range(0, age1 + 1, 1))
	.enter().append("g")
	.attr("class", "birthyear")
	.attr("transform", function(birthyear) { return "translate(" + x(birthyear) + "," + y(people1) + ")"; });

    birthyear.selectAll("rect")
	.data(function(birthyear) { return data[year][birthyear] || [0, 0]; })
	.enter().append("rect")
	.attr("x", -barWidth / 2)
	.attr("width", barWidth)
	.attr("y", y)
	// .attr("y", function(value) { return y(value - people0); })
	.attr("height", function(value) { return height - y(Math.max(value + people0)); });

  // // Add labels to show birthyear.
  //   birthyear.append("text")
  // 	.attr("y", height - 4)
  // 	.text(function(birthyear) { return birthyear; });

  // Add labels to show age (separate; not animated).
    svg.selectAll(".age")
  	.data(d3.range(0, age1 + 1, 1))
  	.enter().append("text")
  	.attr("class", "age")
  	.attr("x", function(age) { return x(age); })
  	.attr("y", height + 4)
  	.attr("dy", ".71em")
  	.text(function(age) { return "d" + age; });

  // Allow the arrow keys to change the displayed year.
    window.focus();
    d3.select(window).on("keydown", function() {
	switch (d3.event.keyCode) {
	case 38: year = Math.max(year0, year - 1); break;
	case 40: year = Math.min(year1, year + 1); break;
	}
	update();
    });

    function update() {
	if (!(year in data)) return;
	// title.text(year);

	// birthyears.transition()
        //     .duration(750);
            // .attr("transform", "translate(" + (x(year1) - x(year)) + ",0)");

	birthyear.selectAll("rect")
            .data(function(birthyear) { return data[year][birthyear] || [0, 0]; })
	    .transition()
            .duration(750)
	    .attr("y", function(value) { return y(Math.max(0, value)); })
	    // .attr("y", function(value) { return y(value - people0); })
            .attr("height", function(value) { return Math.abs(height - y(value + people0)); });

	var orange = "\\widehat{\\mathit{orange}}"
	var fruit = "\\widehat{\\mathit{fruit}}"
	new_title = {1: "$" + orange + "$",
		     2: "$" + fruit + "$",
		     3: "$" + orange + "\\lor" + fruit + "$",
		     4: "$" + orange + "\\lor" + fruit + "$",
		     5: "$" + orange + "\\land" + fruit + "$",
		     6: "$" + orange + "\\land" + fruit + "$",
		     7: "$" + orange + "$",
		     8: "$-" + orange + "$",
		     9: "$" + fruit + "-" + orange + "$",
		     10: "$\\mathit{orange}\\rightarrow\\mathit{fruit}$"
		     }[year];

	d3.selectAll(".disjunction-title").text(new_title)
	MathJax.Hub.Queue(["Typeset",MathJax.Hub]);
    }
});

