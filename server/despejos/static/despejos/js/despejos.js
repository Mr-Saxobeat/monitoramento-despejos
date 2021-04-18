function getColorSituacao(s){
  return s == "despejo" ? "#f70505" :
         s == "ameaça de despejo" ? "#19a641" :
         "red";
}

function styleSituacao(feature){
  var color = getColorSituacao(feature.properties.situacao);
  return {
    fillColor: color,
    weight: 2,
    opacity: 1,
    color: color,
    fillOpacity: 0.5
  };
}

var SituacaoDespejo_Layer = L.geoJson([], {
    style: styleSituacao,
    pointToLayer: function(feature, latlng) {
        return new L.CircleMarker(latlng, {radius: 10});
      },
    // onEachFeature: City_Layer_onEachFeature,
  })

var url_despejo = document.getElementById("url-despejo").value

$.getJSON(url_despejo, function (data) {
    SituacaoDespejo_Layer.addData(data);    
  })

SituacaoDespejo_Layer.addTo(map);

controlOptions = {
  collapsed: false,
  position: 'bottomright',
}
var layerControl = L.control.layers(null, null, controlOptions).addTo(map);
layerControl.addBaseLayer(SituacaoDespejo_Layer, "Situação");

var info = L.control({position:'bottomright'});
info.onAdd = function(map) {
  this._div = L.DomUtil.create('div', 'info');
  this.update();
  return this._div;
}

info.update = function (props) {
  this._div.innerHTML = '<h4>Mapa de despejos no Espírito Santo</h4>' +  (props ?
      '<b>' + props.name + '</b><br />' + props.density + ' people / mi<sup>2</sup>'
      : 'Hover over a state');
};

info.addTo(map);