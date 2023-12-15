let map;

function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    center: new google.maps.LatLng(0, 0),
    zoom: 2,
  });



function httpGet(url) {
  var xmlHttp = new XMLHttpRequest();
  xmlHttp.open("GET", url, false); // false for synchronous request
  xmlHttp.send(null);
  return xmlHttp.responseText;
}

  var response = httpGet("https://maps.googleapis.com/maps/api/geocode/json?address=New%20York&key=AIzaSyANfxrVcQLICz3lVf4CYjTmUB44Hy1IqsM");
  console.log(response);
  var location = JSON.parse(response);
  var lat = location.results[0].geometry.location.lat;
  var lng = location.results[0].geometry.location.lng;

  const iconBase =
    "https://developers.google.com/maps/documentation/javascript/examples/full/images/";
  const icons = {
    parking: {
      icon: iconBase + "parking_lot_maps.png",
    },
    library: {
      icon: iconBase + "library_maps.png",
    },
    info: {
      icon: iconBase + "info-i_maps.png",
    },
  };
  const features = [
    {
      position: new google.maps.LatLng(lat, lng),
      type: "library",
      title: "New York University",
    },
  ];

  // Create markers.
  for (let i = 0; i < features.length; i++) {
    const marker = new google.maps.Marker({
      position: features[i].position,
      icon: icons[features[i].type].icon,
      map: map,
      title: features[i].title,
      animation: google.maps.Animation.DROP,
    });
    marker.addListener('click', () => {
      console.log(marker.title);
    });
  }
}

window.initMap = initMap;