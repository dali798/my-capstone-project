'use strict';

function initMap() {

    const coords = document.querySelector('#coords').innerText;
    const trailLst = coords.split(',');
    const trailLst1 = trailLst[0].split(':');
    const trailLat = parseFloat(trailLst1[1]);
    const trailLst2 = trailLst[1].split(':');
    let trailLng = trailLst2[1].replace('}', '')
    trailLng = parseFloat(trailLng);
    

    const trailCoords = {lat: trailLat, lng: trailLng};
  
    const basicMap = new google.maps.Map(document.querySelector('#map'), {
      center: trailCoords,
      zoom: 11,
    });
    const trailName = document.querySelector('#trail_name').innerText;
  
    const trailMarker = new google.maps.Marker({
      position: trailCoords,
      title: trailName,
      map: basicMap,
    });
  
    trailMarker.addListener('click', () => {
      alert(trailName);
    });
  
    const trailInfo = new google.maps.InfoWindow({
      content: `<h1>${trailName}</h1>`,
    });
  
    trailInfo.open(basicMap, trailMarker);
      
  }

  