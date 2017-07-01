var signUpBtn = document.querySelector("#signup");

function signup(){
    var template = this.responseText;
    console.log(this.responseText);
    document.querySelector('.wrap-content').innerHTML = template;
}

signUpBtn.addEventListener("click", function(){
    console.log("hello");
    sendAjax("POST", "http://localhost:8000/nunucast/signup", null, "application/json", signup);
})
