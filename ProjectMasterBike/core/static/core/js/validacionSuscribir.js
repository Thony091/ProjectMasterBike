/**
 * Validación con JQuery
 *  */

/*
$(document).ready( function() {
    $("#suscribir").on("click", function(){
        const inputSuscribir = $("#emailSuscribir").val().trim();
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

        if(!emailRegex.test(inputSuscribir)){
            $("#suscribirHelp").text("Ingrese un correo Valido");
        }else{
            $("#suscribirHelp").text(" ");
            $("#suscribirHelp2").text("suscripción existosa!");
            $("#emailSuscribir").val("")
        }
    })
});
*/


/**
 * Validación con JavaScript
 *  */
document.addEventListener("DOMContentLoaded", function(){
    let formSuscribir = document.querySelector("#formSuscribir")
    let suscribir = document.querySelector("#emailSuscribir");
    
    function suscribirValidate(){
        let suscribirValue = suscribir.value;
        let emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

        if(!emailRegex.test(suscribirValue)){
            document.querySelector("#suscribirHelp").innerHTML = "Ingrese un correo valido"
            return false;
        }else{
            document.querySelector("#suscribirHelp").innerHTML = " "
            
        }
        return true;
    }

    formSuscribir.addEventListener("submit", function(event){

        //* Si la funcion validate retorna un false no enviar el formulario

        if(!suscribirValidate()){

            event.preventDefault();
            
        } else {
            alert("Suscripción Exitosa")
        }
    })
})