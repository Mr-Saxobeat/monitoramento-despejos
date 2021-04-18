var map = L.map('map', {
    center: [-19.47177130210513, -40.41320800781251],
    zoom: 7,
    // layers: [streets, City_Layer],
  });

L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'pk.eyJ1Ijoid2VpZ2xhcyIsImEiOiJja2l1cGZ2cWYwOThjMnJyd3hvdWUyOGU1In0.cpuHLClWLI4IZPfxHp8fog'
}).addTo(map);