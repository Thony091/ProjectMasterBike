//Validacion de Campos con JQuery
$(document).ready( function () {    
    $("#registrar").click(function(){
        const inputName = $("#name").val().trim();
        const inputLastName = $("#lastName").val().trim();
        const inputRut = $("#rut").val().trim();
        const inputEmail = $("#email").val().trim();
        const inputPassword = $("#password").val().trim();
        const inputPasswordConfirm = $("#passwordConfirm").val().trim();
        const nombreRegex= /^[A-ZÑa-zñáéíóúÁÉÍÓÚ'° ]+$/;
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;


        if(inputName.length == 0){
            $("#nameHelp").text("El nombre no puede quedar vacio");
            return false
        }else if(inputName.length < 2){
            $("#nameHelp").text("El nombre debe contener al menos 2 letras");
            return false
        }else if(!nombreRegex.test(inputName)){
            $("#nameHelp").text("El nombre debe contener solo letras");
            return false
        }else{
            $("#nameHelp").text(" ");
        }

        if(inputLastName.length == 0){
            $("#lastNameHelp").text("El apellido no puede quedar vacio");
            return false
        }else if(inputLastName.length < 2){
            $("#lastNameHelp").text("El apellido debe contener al menos 2 letras");
            return false
        }else if(!nombreRegex.test(inputLastName)){
            $("#lastNameHelp").text("El apellido debe contener solo letras");
            return false
        }else{
            $("#lastNameHelp").text(" ");
        }

        if(inputRut.length < 9){
            $("#rutHelp").text("El rut debe contener almenos 9 digitos");
            return false
        }else{
            $("#rutHelp").text(" ");
        }

        if(!emailRegex.test(inputEmail)){
            $("#mailHelp").text("Ingrese un correo valido.")
            return false
        }else{
            $("#mailHelp").text(" ");
        }

        if(inputPassword.length < 7){
            $("#passwordHelp").text("La contraseña debe tener almenos 7 letras o números.")
            return false
        }else{
            $("#passwordHelp").text(" ");
        }

        if(inputPassword.length == 0 || inputPasswordConfirm.length == 0){
            $("#passwordConfirmHelp").text("Debe confirmar la contraseña.")
            return false
        }else if(inputPasswordConfirm != inputPassword){
            $("#passwordConfirmHelp").text("Las contraseñas no coinciden, verifique que coincidan.")
            return false
        }else{
            $("#passwordConfirmHelp").text(" ");

        }

        if (inputName.length == 0 || 
            inputLastName.length == 0 || 
            inputEmail.length == 0 || 
            inputPhone.length == 0 ||
            inputAddress.length == 0){
            $("#finalHelp").text("Debe llenar todos los campos");
            return false
        } 
        

    })

});