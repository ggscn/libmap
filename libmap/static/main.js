async function do_get(url, params={}) {
    const csrfToken = $('meta[name=csrf-token]').attr('content');

    if (!(Object.entries(params).length === 0 && params.constructor === Object)){
        url_encoded_params = url_encode_dict(params);
        url = url + '?' + url_encoded_params;
    }
    
    let response = await fetch(url, {
        method: 'GET',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        }
    });

    let content = await response.json();

    return content;
}

window.onload = function () {
    document.getElementById('query_button').addEventListener('click', function () { 
        console.log('test');
    }, false);


};