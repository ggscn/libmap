function url_encode_dict(params){
    let data = Object.entries(params);

    data = data.map(([k, v]) => `${encodeURIComponent(k)}=${encodeURIComponent(v)}`);

    let query = data.join('&');

    return query
}

async function do_get(url, params={}) {
    if (!(Object.entries(params).length === 0 && params.constructor === Object)){
        url_encoded_params = url_encode_dict(params);
        url = url + '?' + url_encoded_params;
    }
    
    let response = await fetch(url, {
        method: 'GET',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
    });

    let content = await response.json();

    return content;
}

function get_input_value(ele_id){
    return document.getElementById(ele_id).value;
}

function populate_map(){
    author = get_input_value('author');
    title = get_input_value('title');

    params = {
        'title': title,
        'author': author
    };
    do_get('/query', params)
        .then(content => draw_markers(content['data']))
        .catch(reason => console.log(reason.message));
  
}

function draw_markers(rows){

    var features = [];

    for (var i = 0; i < rows.length; i++) {
        var item = rows[i];
        var longitude = item.long;
        var latitude = item.lat;
        console.log(longitude, latitude);
        var iconFeature = new ol.Feature({
            geometry: new ol.geom.Point(ol.proj.transform([longitude, latitude], 'EPSG:4326', 'EPSG:3857'))
        });

        var iconStyle = new ol.style.Style({
            image: new ol.style.Icon(({
                anchor: [0.5, 1],
                src: "http://cdn.mapmarker.io/api/v1/pin?text=P&size=50&hoffset=1"
            }))
        });

        iconFeature.setStyle(iconStyle);
        features.push(iconFeature);

    }

    var vectorSource = new ol.source.Vector({
        features: features
    });

    var vectorLayer = new ol.layer.Vector({
        source: vectorSource
    });
    libmap.addLayer(vectorLayer);
}

window.onload = function () {
    document.getElementById('query_button').addEventListener('click', function () { 
    populate_map();
}, false)};