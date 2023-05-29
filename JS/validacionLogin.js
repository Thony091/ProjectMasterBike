document.addEventListener("DOMContentLoaded", function () {
    let form = document.querySelector("#form-login");
    let user = document.querySelector("#user");
    let password = document.querySelector("#password"); 


    function validateLogin() {
        let userValue = user.value;
        let passwordValue = password.value;

        // if (!userValue.isEqual("admin") ) {
           
        //     document.querySelector("#finalHelp").innerHTML = "Usuario o contraseña incorrecto.";
        // } else if (userValue.length == 0){

        // }
        
        if(userValue.length == 0 || passwordValue.length == 0){
            
            document.querySelector("#finalHelp").innerHTML = "Debe Ingresar una Cuenta Valida.";
            return false;
        }

        return true;
    }
    form.addEventListener("submit", function (event) {
        if (!validateLogin) {
            event.preventDefault();
        }
    })


})

function isEqual(str1, str2)
{
  return str1.toUpperCase() === str2.toUpperCase()
}