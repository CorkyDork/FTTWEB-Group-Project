//const DOMAIN = 'https://fttweb.xyz'
const DOMAIN = "http://127.0.0.1:8000/";
const ENDPOINT_SIGN_IN = DOMAIN + "userauth/api/post-signin/";
const ENDPOINT_SIGN_UP = DOMAIN + "userauth/api/post-signup/";
const ENDPOINT_PASS_RESET = DOMAIN + "userauth/api/post-password-reset/";
const ENDPOINT_SIGN_IN_SOCIAL_MEDIA = DOMAIN + "userauth/api/post-firebase-social-signin/";

const ENDPOINT_VIEW_CLIENT_TRANSACTIONS = DOMAIN + "api/get-client-transactions/";

const FIREBASE_CONFIG = {
    apiKey: "AIzaSyDiSiQcmuTEHdHUio2tOprPOX65MJ8SkMk",
	authDomain: "test-4d090.firebaseapp.com",
	databaseURL: "https://test-4d090-default-rtdb.firebaseio.com",
	projectId: "test-4d090",
	storageBucket: "test-4d090.appspot.com",
	messagingSenderId: "1060349065580",
	appId: "1:1060349065580:web:1ee1a40ea145f1ef9a5b49",
	measurementId: "G-05JYEHXSQQ"
    
};



var currentUrl = window.location.href; // hold current url

// View Transactions ------------------------------------------------------------------------------------------------------
$('.view-transaction').on("click", function() {
    $(this).disabled = true; // Disable this button so no double request sent
    
    var clientId = $(this).attr("clientid");
    var xhr = new XMLHttpRequest();

    // Listen for server response
    xhr.addEventListener("readystatechange", function() {

        if(this.readyState === 4) {
            var responseData = JSON.parse(this.responseText);

            if(responseData) {
                console.log("YESSSSS");
            }
            else if(responseData){
                console.log("noooooo");
            }
        }
    });

    // Send request to server
    xhr.open("POST", ENDPOINT_VIEW_CLIENT_TRANSACTIONS, true);
    xhr.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
    xhr.send("clientId="+clientId);
});


// Hamburger ------------------------------------------------------------------------------------------------------
    $('.hamburger').on("click", function() {
        $(this).toggleClass("is-active");
    });



// Authenditication forms ------------------------------------------------------------------------------------------------------
    function toggleResetPswd(e) {
        e.preventDefault();
        $('#auth-forms #form-signin').toggle();
        $('#auth-forms #form-reset').toggle();
    }

    function toggleSignUp(e) {
        e.preventDefault();
        $('#auth-forms #form-signin').toggle();
        $('#auth-forms #form-signup').toggle();
    }

    // Signin / signup form visibility controll
    $(()=>{
        $('#auth-forms #forgot_pswd').click(toggleResetPswd);
        $('#auth-forms #cancel_reset').click(toggleResetPswd);
        $('#auth-forms #btn-signup').click(toggleSignUp);
        $('#auth-forms #cancel_signup').click(toggleSignUp);
    })

    // // Authenditication popup show/hide
    const auth_popup = document.getElementById('exampleModal');

    if (typeof(auth_popup) != 'undefined' && auth_popup != null) {
        auth_popup.addEventListener('hidden.bs.modal', () => {
            $('#auth-forms .form-signin').css('display', 'block');
            $('#auth-forms .form-signup').css('display', 'none');
            $('#auth-forms .form-reset').css('display', 'none');
        })
    }


// Sign in with email + password ------------------------------------------------------------------------------------------------------
    function signInWithEmailPassProcess() {    
        var signinBtn = document.getElementById("signinBtn");

        signinBtn.disabled = true;

        var xhr = new XMLHttpRequest();
        var email = document.getElementById("signinEmail");
        var pass = document.getElementById("signinPass");

        // Listen for server response
        xhr.addEventListener("readystatechange", function() {

            if(this.readyState === 4) {
                var responseData = JSON.parse(this.responseText);

                if(responseData.authData.isAuth) {
                    location="/myclients?codeIs=toast&showDuration=10000&type=isSuccess&title=Signed in successfully&msg=Welcome back "+responseData.authData.email;
                }
                else if(responseData.toasts && responseData.toasts.length > 0){ // Atleast 1 toast exist to display

                    // Go throught toasts obj and display all toasts for user
                    for (let i = 0; i < responseData.toasts.length; i++) {
                        spawnAndDisplayToastToUser(responseData.toasts[i]);
                    }
                    
                    signinBtn.disabled = false;
                }
            }
        });

        // Send request to server
        xhr.open("POST", ENDPOINT_SIGN_IN, true);
        xhr.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
        xhr.send("email="+email.value+"&pass="+pass.value);
    };



// Sign up with email + password ------------------------------------------------------------------------------------------------------
    function signUpWithEmailPassProcess() {
        var signupBtn = document.getElementById("signupBtn");

        signupBtn.disabled = true;

        var xhr = new XMLHttpRequest();

        var name = document.getElementById("signupName");
        var surname = document.getElementById("signupSurname");
        var email = document.getElementById("signupUserEmail");
        var pass = document.getElementById("signupUserPass");
        var finInstitution = document.getElementById('signupFinInstName');

        // Listen for server response
        xhr.addEventListener("readystatechange", function() {

            if(this.readyState === 4) {
                var responseData = JSON.parse(this.responseText);
                console.log(responseData);
                if(responseData.authData.isAuth) {
                    location="/myclients?codeIs=toast&showDuration=10000&type=isSuccess&title=Signed up successfully&msg=Welcome "+responseData.authData.email;
                }
                else if(responseData.toasts && responseData.toasts.length > 0){ // Atleast 1 toast exist to display

                    // Go throught toasts obj and display all toasts for user
                    for (let i = 0; i < responseData.toasts.length; i++) {
                        spawnAndDisplayToastToUser(responseData.toasts[i]);
                    }
                    
                    signupBtn.disabled = false;
                }
            }
        });

        // Send request to server
        xhr.open("POST", ENDPOINT_SIGN_UP, true);
        xhr.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
        xhr.send(
            "name=" + name.value+
            "&surname=" + surname.value+
            "&email=" + email.value+
            "&pass=" + pass.value+
            "&finInstitution=" + finInstitution.value
        );
    };



// Password reset ------------------------------------------------------------------------------------------------------
    function resetPassProcess() {
        var resetPassBtn = document.getElementById("resetPassBtn");

        resetPassBtn.disabled = true;

        var xhr = new XMLHttpRequest();
        var email = document.getElementById("passResetEmail");

        // Listen for server response
        xhr.addEventListener("readystatechange", function() {

            if(this.readyState === 4) {
                var responseData = JSON.parse(this.responseText);
                
                if(responseData.toasts && responseData.toasts.length > 0){ // Atleast 1 toast exist to display

                    // Go throught toasts obj and display all toasts for user
                    for (let i = 0; i < responseData.toasts.length; i++) {
                        spawnAndDisplayToastToUser(responseData.toasts[i]);
                    }
                }

                resetPassBtn.disabled = false;
            }
        });

        // Send request to server
        xhr.open("POST", ENDPOINT_PASS_RESET, true);
        xhr.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
        xhr.send("email="+email.value);
    };



// Sign in with social media ------------------------------------------------------------------------------------------------------    
    firebase.initializeApp(FIREBASE_CONFIG);
    firebase.analytics();

    // Sign in with Google
    function signInWithGoogleProcess() {
        var provider = new firebase.auth.GoogleAuthProvider();
        
        firebase.auth().signInWithPopup(provider).then(function(response){ 
            var userobj = response.user;
            var token = userobj.xa;
            var provider = "google";
            var email = userobj.email;

            if(token != null && token != undefined && token != ""){
                sendDataToServer(email,token);
            }
            
        }).catch(function(error){
            console.log(error);
        })
    }

    // Sign in with Facebook
    function signInWithFacebookProcess() {
        var provider = new firebase.auth.FacebookAuthProvider();

        firebase.auth().signInWithPopup(provider).then(function(response){
            var userobj = response.user;
            var token = userobj.xa;
            var provider = "facebook";
            var email = userobj.email;

            if(token != null && token != undefined && token != ""){
                sendDataToServer(email,token);
            }
        }).catch(function(error){
            console.log(error);
        })
    }

    // Process social login data on server
    function sendDataToServer(email,token){
        var xhr = new XMLHttpRequest();

        // Listen for server response
        xhr.addEventListener("readystatechange", function(){

            if(this.readyState === 4) {
                var responseData = JSON.parse(this.responseText);

                if(responseData.authData.isAuth) {
                    location="/myclients?codeIs=toast&showDuration=10000&type=isSuccess&title=Signed in successfully&msg=Welcome "+responseData.authData.email;
                }
                else if(responseData.toasts && responseData.toasts.length > 0){ // Atleast 1 toast exist to display

                    // Go throught toasts obj and display all toasts for user
                    for (let i = 0; i < responseData.toasts.length; i++) {
                        spawnAndDisplayToastToUser(responseData.toasts[i]);
                    }
                }
            }
        });


        // Send request to server
        xhr.open("POST", ENDPOINT_SIGN_IN_SOCIAL_MEDIA, true);
        xhr.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
        xhr.send("email="+email+"&token="+token);
    }



// Form validation for sign in ------------------------------------------------------------------------------------------------------
    function validateSignInForm() {
        var email = document.getElementById("signinEmail");
        var password = document.getElementById("signinPass");
        var errorMessageDiv = document.querySelector('#form-signin .errorMessage');

        // Email regex
        var emailRegex = /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$/i;

        // Validate email field
        if (!emailRegex.test(email.value)) { // Error in validation - email didnt pass regex
            errorMessageDiv.innerHTML = '<span class="text-danger"><i class="fa-solid fa-xmark"></i> Please enter a valid email address</span>';
            errorMessageDiv.classList.add("error");
            email.classList.add("error");
            return false;
        }
        else { // Validation possed
            errorMessageDiv.innerHTML = "";
            errorMessageDiv.classList.remove("error");
            email.classList.remove("error");
        }

        // Validate the password field
        if (password == "") { // Error in validation  - empty password
            errorMessageDiv.innerHTML = '<span class="text-danger"><i class="fa-solid fa-xmark"></i> Password field must be filled out';
            errorMessageDiv.classList.add("error");
            password.classList.add("error");
            return false;
        }
        else if (password.value.length < 6) { // Error in validation - password length to low
            errorMessageDiv.innerHTML = '<span class="text-danger"><i class="fa-solid fa-xmark"></i> Password must be at least 6 characters long';
            errorMessageDiv.classList.add("error");
            password.classList.add("error");
            return false;
        }
        else { // Validation possed
            errorMessageDiv.innerHTML = "";
            errorMessageDiv.classList.remove("error");
            password.classList.remove("error");
        }

        // If fields passed validation, submit the form
        signInWithEmailPassProcess();
    }



// Form validation for sign up ------------------------------------------------------------------------------------------------------
    function validateSignUpForm() {
        var name = document.getElementById("signupName");
        var surname = document.getElementById("signupSurname");
        var email = document.getElementById("signupUserEmail");

        var password = document.getElementById("signupUserPass");
        var passwordRepeat = document.getElementById("signupUserRepeatPass");

        var finInstitution = document.getElementById('signupFinInstName');

        var errorMessageDiv = document.querySelector('#form-signup .errorMessage');

        // Regex
        var emailRegex = /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$/i;
        var textRegex = /^[a-zA-Z0-9]+$/;

        // Validate name field
            if (name.value == "") { // Error in validation - empty name
                errorMessageDiv.innerHTML = '<span class="text-danger"><i class="fa-solid fa-xmark"></i> Please enter a name</span>';
                errorMessageDiv.classList.add("error");
                name.classList.add("error");
                return false;
            }
            if (!textRegex.test(name.value)) { // Error in validation - name didnt pass regex
                errorMessageDiv.innerHTML = '<span class="text-danger"><i class="fa-solid fa-xmark"></i> name can only consist of characters/numbers</span>';
                errorMessageDiv.classList.add("error");
                name.classList.add("error");
                return false;
            }
            else if (name.value.length < 3) { // Error in validation - name length to low
                errorMessageDiv.innerHTML = '<span class="text-danger"><i class="fa-solid fa-xmark"></i> Name must be at least 3 characters long';
                errorMessageDiv.classList.add("error");
                name.classList.add("error");
                return false;
            }
            else { // Validation possed
                errorMessageDiv.innerHTML = "";
                errorMessageDiv.classList.remove("error");
                name.classList.remove("error");
            }

        // Validate surname field
            if (surname.value == "") { // Error in validation - empty surname
                errorMessageDiv.innerHTML = '<span class="text-danger"><i class="fa-solid fa-xmark"></i> Please enter a surname</span>';
                errorMessageDiv.classList.add("error");
                surname.classList.add("error");
                return false;
            }
            if (!textRegex.test(surname.value)) { // Error in validation - surname didnt pass regex
                errorMessageDiv.innerHTML = '<span class="text-danger"><i class="fa-solid fa-xmark"></i> Surname can only consist of characters/numbers</span>';
                errorMessageDiv.classList.add("error");
                surname.classList.add("error");
                return false;
            }
            else if (surname.value.length < 3) { // Error in validation - surname length to low
                errorMessageDiv.innerHTML = '<span class="text-danger"><i class="fa-solid fa-xmark"></i> Surname must be at least 3 characters long';
                errorMessageDiv.classList.add("error");
                surname.classList.add("error");
                return false;
            }
            else { // Validation possed
                errorMessageDiv.innerHTML = "";
                errorMessageDiv.classList.remove("error");
                name.classList.remove("error");
            }

        // Validate email field
            if (!emailRegex.test(email.value)) { // Error in validation - email didnt pass regex
                errorMessageDiv.innerHTML = '<span class="text-danger"><i class="fa-solid fa-xmark"></i> Please enter a valid email address</span>';
                errorMessageDiv.classList.add("error");
                email.classList.add("error");
                return false;
            }
            else { // Validation possed
                errorMessageDiv.innerHTML = "";
                errorMessageDiv.classList.remove("error");
                email.classList.remove("error");
            }

        // Validate the password fields
            if (password == "" || passwordRepeat == "") { // Error in validation  - empty password
                errorMessageDiv.innerHTML = '<span class="text-danger"><i class="fa-solid fa-xmark"></i> Password fields must be filled out';
                errorMessageDiv.classList.add("error");
                password.classList.add("error");
                return false;
            }
            else if (password.value.length < 6) { // Error in validation - password length to low
                errorMessageDiv.innerHTML = '<span class="text-danger"><i class="fa-solid fa-xmark"></i> Password must be at least 6 characters long';
                errorMessageDiv.classList.add("error");
                password.classList.add("error");
                return false;
            }
            else if (password.value !== passwordRepeat.value) { // Error in validation - passwords do not match
                errorMessageDiv.innerHTML = '<span class="text-danger"><i class="fa-solid fa-xmark"></i> Passwords do not match';
                errorMessageDiv.classList.add("error");
                password.classList.add("error");
                passwordRepeat.classList.add("error");
                return false;
            }
            else { // Validation possed
                errorMessageDiv.innerHTML = "";
                password.classList.remove("error");
                passwordRepeat.classList.remove("error");
            }

        // Validate financial institution select field
        if (finInstitution != null && finInstitution.value == "") {
            errorMessageDiv.innerHTML = '<span class="text-danger"><i class="fa-solid fa-xmark"></i> Please select financial institution</span>';
            errorMessageDiv.classList.add("error");
            finInstitution.classList.add("error");
            return false;
        }
        else {
            errorMessageDiv.innerHTML = "";
            finInstitution.classList.remove("error");
        }

        // If fields passed validation, submit the form
        signUpWithEmailPassProcess();
    }



// Form validation for password reset ------------------------------------------------------------------------------------------------------
    function validateResetPasswordForm() {
        var email = document.getElementById("passResetEmail");
        var errorMessageDiv = document.querySelector('#form-reset .errorMessage');

        // Email regex
        var emailRegex = /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$/i;

        // Validate email field
        if (!emailRegex.test(email.value)) { // Error in validation - email didnt pass regex
            errorMessageDiv.innerHTML = '<span class="text-danger"><i class="fa-solid fa-xmark"></i> Please enter a valid email address</span>';
            errorMessageDiv.classList.add("error");
            email.classList.add("error");
            return false;
        }
        else { // Validation possed
            errorMessageDiv.innerHTML = "";
            errorMessageDiv.classList.remove("error");
            email.classList.remove("error");
        }

        // If fields passed validation, submit the form
        resetPassProcess();
    }



// Toast display functionality
    function spawnAndDisplayToastToUser(toastObj) {
        var toastContainer = document.getElementById('toast-container');
        console.log(toastObj);

        // Make toast from template and insert toast html into toast container
        toastContainer.innerHTML += `
            <div id="liveToast" class="cs-toast toast `+toastObj['type']+`" role="alert" aria-live="assertive" aria-atomic="true" data-bs-delay="`+parseFloat(toastObj['showDuration'])+`">
                <div class="toast-header">
                    <i class="fa-solid fa-triangle-exclamation fa-xl pe-2"></i>

                    <strong class="me-auto">`+toastObj['title']+`</strong>
                    
                    <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
                </div>
                
                <div class="toast-body">`+toastObj['msg']+`</div>
            </div>
        `;

        // Select most recently spawned toast
        const spawnedToastHTML = toastContainer.lastElementChild;
        console.log(spawnedToastHTML)

        // Add toast to bootstraps toast instance so we can show it
        var toast = new bootstrap.Toast(spawnedToastHTML);

        // Tell bootstraps to show toast
        toast.show();

        // Clean toast once toast hides
        spawnedToastHTML.addEventListener('hidden.bs.toast', () => {
            spawnedToastHTML.remove();
        })
    }


    function displayToastToUser(toastChild) {
  
        // Tell bootstraps to show toast
        var toast = new bootstrap.Toast(toastChild);
        toast.show();

        // Clean toast once toast hides
        toastChild.addEventListener('hidden.bs.toast', () => {
            toastChild.remove();
        })
    }

    // Check if the url has a variable that tells us its a toast that has to be shown
    //  EXAMPLE -> visit url
    //  http://127.0.0.1:8000/?codeIs=toast&title=SMOME COOL TOAST&msg=I LIKE NUTELLA TOASTS
    if (currentUrl.indexOf('codeIs=toast') != -1) {

        // Extract vars from URL to latter pass to toast function
        var urlVariables = extractVarsFromURL();

        // We proceed to showing toast and pass all url variables as they contain data to show in toast
        spawnAndDisplayToastToUser(urlVariables);
    }

    // Check if any toasts are present during page load and show it
    var toastContainer = document.getElementById('toast-container');
    var toastChildren = toastContainer.querySelectorAll('.toast');

    for (var i = 0; i < toastChildren.length; i++) {
        displayToastToUser(toastChildren[i]);
    }



// Helper functions
    function extractVarsFromURL() {
        //  EXAMPLE -> visit url
        //  http://127.0.0.1:8000/?codeIs=toast&title=SMOME COOL TOAST&msg=I LIKE NUTELLA TOASTS

        var urlVariables = {};

        // Split the url at the ? character to separate the base url from url variables
        var urlSplit = currentUrl.split('?');

        // Get the base url
        var baseUrl = urlSplit[0];
        console.log(baseUrl);

        // Split the variables string at the & character to separate the individual variables
        var variables = urlSplit[1].split('&');

        // Loop through the variables and store their values in the urlVariables object
        for (var i = 0; i < variables.length; i++) {

            // Split the variable at the = character to separate the variable name and value
            var variableSplit = variables[i].split('=');

            // Store the variable name and value in the urlVariables object
            var variableName = variableSplit[0];
            var variableValue = decodeURIComponent(variableSplit[1]);
            urlVariables[variableName] = variableValue;
        }

        // Remove all url variables from browser view
        window.history.replaceState({}, document.title, baseUrl);

        return urlVariables;
    }
