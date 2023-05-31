document.addEventListener("DOMContentLoaded", function () {
    let form = document.querySelector("#form-login");
    let user = document.querySelector("#user");
    let password = document.querySelector("#password"); 
    

    function validateLogin() {
        let userValue = user.value;
        let passwordValue = password.value;

        
        if(userValue.length == 0 || passwordValue.length == 0){
            
            document.querySelector("#finalHelp").innerHTML = "Debe Ingresar una Cuenta Valida.";
        }else{
            document.querySelector("#finalHelp").innerHTML = " ";
            
        }
        
        if (userValue != "admin" || passwordValue != "admin" ) {
            
            document.querySelector("#finalHelp").innerHTML = "Usuario o contraseña incorrecto.";
            return false;
        } else{
            document.querySelector("#finalHelp").innerHTML = " ";
        }

        return true;
    }

    // document.querySelector("#boton").onclick = validateLogin;
    let validatebuttom = document.querySelector("#boton").onclick = validateLogin;
    
    form.addEventListener("submit", function (event) {
        if (!validatebuttom) {
            event.preventDefault();
        }else{
            alert("Usuario existente.")
        }
    })


})