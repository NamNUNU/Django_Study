var signUpBtn = document.querySelector("#signup");

function signup(){
    var template = this.responseText;
    console.log(this.responseText);
    document.querySelector('.wrap-content').innerHTML = template;
}

signUpBtn.addEventListener("click", function(){
    location.href = "http://localhost:8000/accounts/signup";
})
