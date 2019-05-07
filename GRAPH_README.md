# GRAPH
The simple code below is jquery library to write function for graph/plot and html to retrieve from the above function.

Markup :  # function for graph #
```javascript
<script > window.onload = function () {


var options = {
  title: {
  text: "titel here"
  },
  data: [
  {
  type: " this is what you want to make this plot looks like(scatter, line, pie, chart) ",
  dataPoints: [label: "label title", y-axis:"" ]
  }
  ]
};

$("#chartContainer").CanvasJSChart(options);


}
</script>
```

The `option` function generate the basic function of graph, and in `type` you can insert `scatter`, `line`,`pie`,`chart`,`columns` to create different types of graph.

Markup :  # Retrieve from that function  #
```
<body>
<div id="chartContainer" style="height: ...px; max-width: ...px; "></div>
<script type="text/javascript" src="https://canvasjs.com/assets/script/jquery-1.11.1.min.js"></script>
<script type="text/javascript" src="https://canvasjs.com/assets/script/jquery.canvasjs.min.js"></script>
</body>
```
