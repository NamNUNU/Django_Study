var login = document.querySelector("#login");

function result(){
    console.log(this.responseText);
    // var result = JSON.parse(oReq.responseText);
    // document.querySelector('.result').innerHTML = result.email;
}

login.addEventListener("click", function(){
    console.log("hello");
    sendAjax("POST", "http://localhost:8000/nunucast/login/", null, "application/json", result);
})
