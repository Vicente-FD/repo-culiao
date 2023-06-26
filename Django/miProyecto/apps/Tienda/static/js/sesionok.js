function login() {
    var user = document.getElementById("form3Example1cg").value;
    var pass = document.getElementById("form3Example4cg").value;
    if (user == "admin@little.cl" && pass == "admin123") {
        alert("Bienvenido!");
        window.location = "/";
    }else if(user == "user@little.cl" && pass == "user1234"){
        alert("Bienvenido!");
        window.location = "suscripcion.html";
    } 
    else {
        alert("Los datos ingresados son incorrectos");
    }
}