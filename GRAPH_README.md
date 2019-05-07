# GRAPH
The simple code below

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
