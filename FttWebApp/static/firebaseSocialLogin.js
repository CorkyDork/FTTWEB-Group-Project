var firebaseConfig = {
  apiKey: "AIzaSyAkfFcXXg4_8T2yNSoyZMYt3mEOG_SwZak",
  authDomain: "fttweb-2fefa.firebaseapp.com",
  databaseURL: "https://fttweb-2fefa-default-rtdb.europe-west1.firebasedatabase.app/",
  projectId: "fttweb-2fefa",
  storageBucket: "fttweb-2fefa.appspot.com",
  messagingSenderId: "666615681546",
  appId: "1:666615681546:web:81cef76f1f7117068dc5f3",
  measurementId: "G-RS0D55DVCF"
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);
firebase.analytics();


// sign in with google
  var googleLogin = document.getElementById("googleLogin");

  googleLogin.onclick = function(){
    var provider = new firebase.auth.GoogleAuthProvider();
    
    firebase.auth().signInWithPopup(provider).then(function(response){ 
      var userobj = response.user;
      var token = userobj.xa;
      var provider = "google";
      var email = userobj.email;

      if(token != null && token != undefined && token != ""){
        sendDataToServer(email,provider,token,userobj.displayName);
      }
    }).catch(function(error){
        console.log(error);
      })
  }


// sign in with Facebook
  var facebooklogin = document.getElementById("facebooklogin");

  facebooklogin.onclick = function(){
    var provider = new firebase.auth.FacebookAuthProvider();

    firebase.auth().signInWithPopup(provider).then(function(response){
      var userobj = response.user;
      var token = userobj.xa;
      var provider = "facebook";
      var email = userobj.email;

      if(token != null && token != undefined && token != ""){
        sendDataToServer(email,provider,token,userobj.displayName);
      }
    }).catch(function(error){
        console.log(error);
      })
  }


function sendDataToServer(email,provider,token,username){
  var xhr = new XMLHttpRequest();
  
  xhr.addEventListener("readystatechange", function(){
    
    if(this.readyState === 4) {
      console.log(this.responseText);

      if(this.responseText == "login_success"){
        alert("Signed in successfully");
      }
      else{
        alert("Error");
      }
    }
  });

  xhr.open("POST", "http://127.0.0.1:8000/auth/post-firebase-social-signin/",true);
  xhr.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
  xhr.send("email="+email+"&provider="+provider+"&username="+username+"&token="+token);
}