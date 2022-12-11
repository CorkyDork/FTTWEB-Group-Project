function toggleResetPswd(e){
    e.preventDefault();
    $('#auth-forms .form-signin').toggle();
    $('#auth-forms .form-reset').toggle();
}

function toggleSignUp(e){
    e.preventDefault();
    $('#auth-forms .form-signin').toggle();
    $('#auth-forms .form-signup').toggle();
}

$(()=>{
    // signin / signup form
    $('#auth-forms #forgot_pswd').click(toggleResetPswd);
    $('#auth-forms #cancel_reset').click(toggleResetPswd);
    $('#auth-forms #btn-signup').click(toggleSignUp);
    $('#auth-forms #cancel_signup').click(toggleSignUp);
})


// sigin with Email+Password
    var signinBtn = document.getElementById("signinBtn");

    signinBtn.onclick = function(){

        //TODO validate form and show toasts if any errors

        signinBtn.disabled = true;

        var xhr = new XMLHttpRequest();
        var email = document.getElementById("signinEmail");
        var pass = document.getElementById("signinPass");

        xhr.addEventListener("readystatechange", function() {
            if(this.readyState === 4) {
                console.log(this.responseText);

                var responseObj = JSON.parse(this.responseText);

                if(responseObj.code == "signin_success"){
                    alert("Successfully signed in");
                    location='/';
                }
                else if(responseObj.code == "signin_error"){
                    alert("Error: "+ responseObj.msg);
                    signinBtn.disabled = false;
                }
                else{
                    alert("Error occured, try again!");
                }
            }
        });

        xhr.open("POST", "http://127.0.0.1:8000/auth/post-signin/",true);
        xhr.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
        xhr.send("email="+email.value+"&pass="+pass.value);
    };


// signup with Email+Password
    var signupBtn = document.getElementById("signupBtn");

    signupBtn.onclick = function(){

        //TODO validate form and show toasts if any errors

        signupBtn.disabled = true;

        var xhr = new XMLHttpRequest();
        var username = document.getElementById("signupUserName");
        var email = document.getElementById("signupUserEmail");
        var pass = document.getElementById("signupUserPass");
        var passRepeat = document.getElementById("signupUserRepeatPass");

        xhr.addEventListener("readystatechange", function() {
            if(this.readyState === 4) {
                console.log(this.responseText);

                var responseObj = JSON.parse(this.responseText);

                if(responseObj.code == "signup_success"){
                    alert("Successfully signed up, you may login now!");
                    window.location.reload(true);
                }
                else if(responseObj.code == "signup_error"){
                    alert("Error: "+ responseObj.msg);
                    signupBtn.disabled = false;
                }
                else{
                    alert("Error occured, try again!");
                }
            }
        });

        xhr.open("POST", "http://127.0.0.1:8000/auth/post-signup/",true);
        xhr.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
        xhr.send("username="+username.value+"&email="+email.value+"&pass="+pass.value);
    };


// password reset 
    var resetPassBtn = document.getElementById("resetPassBtn");

    resetPassBtn.onclick = function(){

        //TODO validate form and show toasts if any errors

        resetPassBtn.disabled = true;

        var xhr = new XMLHttpRequest();
        var email = document.getElementById("passResetEmail");

        xhr.addEventListener("readystatechange", function() {
            if(this.readyState === 4) {
                console.log(this.responseText);

                var responseObj = JSON.parse(this.responseText);

                if(responseObj.code == "reset_success"){
                    alert("Success, check your email!");
                }
                else if(responseObj.code == "reset_error"){
                    alert("Error: "+ responseObj.msg);
                    resetPassBtn.disabled = false;
                }
                else{
                    alert("Error occured, try again!");
                }
            }
        });

        xhr.open("POST", "http://127.0.0.1:8000/auth/post-password-reset/",true);
        xhr.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
        xhr.send("email="+email.value);
    };
