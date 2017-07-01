
function parse_cookies() {
    var cookies = {};
    if (document.cookie && document.cookie !== '') {
        document.cookie.split(';').forEach(function (c) {
            var m = c.trim().match(/(\w+)=(.*)/);
            if(m !== undefined) {
                cookies[m[1]] = decodeURIComponent(m[2]);
            }
        });
    }
    return cookies;
}

var cookies = parse_cookies();

function sendAjax(method, url, data, type, func) {
        const oReq = new XMLHttpRequest();

        oReq.open(method, url);
        
        if(type){
            oReq.setRequestHeader('X-CSRFToken', cookies['csrftoken']);
            oReq.setRequestHeader('Content-Type', type);
        }
        if (data !== null) {
            oReq.send(data);
        } else {
            oReq.send();
        }

        oReq.addEventListener('load', func);
    }