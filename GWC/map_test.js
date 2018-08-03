var my_view = new ol.View({
  center: ol.proj.fromLonLat([-122.394962, 37.794006]),
  zoom: 15
});

var schoolM = new ol.View({
  center:ol.proj.fromLonLat([25.744333, -100.391209]),
  zoom: 15
})

function init() {
  var map = new ol.Map({
    target: 'map',
    layers: [
      new ol.layer.Tile({
        source: new ol.source.OSM()
      })
    ],
    view: my_view
  });
  }

function panHome() {
  my_view.animate({
    center: ol.proj.fromLonLat([-122.394962, 37.794006]),
    duration: 2000,
    zoom: 15
  });
}

function schoolMexico() {
  schoolM.animate({
    center: ol.proj.fromLonLat([25.744333, -100.391209]),
    duration:2000,
    zoom: 15
  });
}

window.onload = init;
