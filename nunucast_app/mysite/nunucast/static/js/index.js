var signUpBtn = document.querySelector("#signup");
var loginBtn = document.querySelector("#login");

signUpBtn.addEventListener("click", function(){
    location.href = "http://localhost:8000/accounts/signup";
})

loginBtn.addEventListener("click", function(){
    location.href = "http://localhost:8000/accounts/login";
})