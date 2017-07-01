
function sendAjax(method, url, data, type, func) {
        const oReq = new XMLHttpRequest();

        oReq.open(method, url);
        if(type){
            oReq.setRequestHeader('Content-Type', type);
        }
        if (data !== null) {
            oReq.send(data);
        } else {
            oReq.send();
        }

        oReq.addEventListener('load', func);
    }