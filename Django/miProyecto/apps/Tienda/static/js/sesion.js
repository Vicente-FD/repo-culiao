console.log("Sesion.js cargado");
document.getElementById("sus").style.display = "none";
document.getElementById("spas").style.display = "none";


$(function(){
    $("#loginForm").validate({
        rules: {
            userl: {
                required: true
            },
            pass: {
                required: true
            }
        },
        messages: {
            userl: {
                required: "El usuario es obligatorio",
            },
            pass: {
                required: "La contraseña es obligatoria",
            }
        }
    })
})



function validarLogin() {
    if (document.getElementById("userl").value.length === 0) {
        document.getElementById("userl").classList.add("is-invalid");
        showAlert("Debe ingresar un usuario", "danger");
        return;
    } else {
        document.getElementById("userl").classList.remove("is-invalid");
        document.getElementById("userl").classList.add("is-valid");
    }

    if (document.getElementById("pass").value.length === 0) {
        document.getElementById("pass").classList.add("is-invalid");
        showAlert("Debe ingresar la contraseña", "danger");
        return;
    } else {
        document.getElementById("pass").classList.remove("is-invalid");
        document.getElementById("pass").classList.add("is-valid");
    }

    document.getElementById("loginForm").submit();
}

function showAlert(message, type) {
    var alertContainer = document.getElementById("alertContainer");
    alertContainer.innerHTML = '<div class="alert alert-' + type + '">' + message + '</div>';
}