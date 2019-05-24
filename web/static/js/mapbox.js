mapboxgl.accessToken = 'pk.eyJ1IjoiamhhaXJndXptYW4iLCJhIjoiY2pqb2g4MXF6MmJ4aTNxc294aG1laHBqdiJ9.pm-HS9267RNDvEyVmrMt_A';

let map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/streets-v11',
    center: [-79.99588, 40.440624],
    zoom: 11
});


map.on('load', function () {

    map.addLayer({
        "id": "route",
        "type": "line",
        "source": {
            "type": "geojson",
            "data": {
                "type": "Feature",
                "properties": {},
                "geometry": {
                    "type": "LineString",
                    "coordinates": []
                }
            }
        },

        "layout": {
            "line-join": "round",
            "line-cap": "round"
        },

        "paint": {
            "line-color": "#888",
            "line-width": 8
        }
    });
});

function getPoints(path) {
    return [];
}

function drawPath(path) {
    
    let route = getPoints(path);

    map.addLayer({
        "id": "route",
        "type": "line",
        "source": {
            "type": "geojson",
            "data": {
                "type": "Feature",
                "properties": {},
                "geometry": {
                    "type": "LineString",
                    "coordinates": route
                }
            }
        },

        "layout": {
            "line-join": "round",
            "line-cap": "round"
        },

        "paint": {
            "line-color": "#888",
            "line-width": 8
        }
    });
}

function drawExplored(explored) {
    let points = getPoints(explored);

    map.addLayer({
        "id": "route",
        "type": "line",
        "source": {
            "type": "geojson",
            "data": {
                "type": "Feature",
                "properties": {},
                "geometry": {
                    "type": "Point",
                    "coordinates": points
                }
            }
        },

        "layout": {
            "line-join": "round",
            "line-cap": "round"
        },

        "paint": {
            "line-color": "#888",
            "line-width": 8
        }
    });
}


function startSearch(searchType) {
    
    let url = "http://127.0.0.1:8080/route/graph/"+searchType;
    let xmlhttp = new XMLHttpRequest();
    
    xmlhttp.onreadystatechange = function() {
        if (this.readyState === 4 && this.status === 200) {
            console.log("parsing");
            let res = JSON.parse(this.responseText);
            console.log(res);
            drawPath(res.path);
            drawExplored(res.explored);
        }
    };

    xmlhttp.open("GET", url, true);
    xmlhttp.send();
}