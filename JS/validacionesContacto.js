
//Validacion de Campos con Javascript

document.addEventListener("DOMContentLoaded", function(){
    //*Obtener el formulario y sus campos
    let form = document.querySelector("#form-contact");
    let nombre = document.querySelector("#name");
    let mail = document.querySelector("#email");
    let asunto = document.querySelector("#asunto");
    let texto = document.querySelector("#text-area");

    function contactValidate(){
        let nombreValue = nombre.value;      
        let emailValue = mail.value;
        let textoValue = texto.value;
        let asuntoValue = asunto.value;
        let emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        //Expresión Regular Nombres y Apellidos (excluye números)
        let nombreRegex= /^[A-ZÑa-zñáéíóúÁÉÍÓÚ'° ]+$/;
         
        //* Validando nombre      
        if(nombreValue.length == 0){
            document.querySelector("#nameHelp").innerHTML = "El campo no puede estar vacio";
            
        }else if(nombreValue.length < 2){
            document.querySelector("#nameHelp").innerHTML = "El nombre debe contener almenos 2 letras";     
            
        }else if(!nombreRegex.test(nombreValue) ){
            document.querySelector("#nameHelp").innerHTML = "El nombre debe ser solo de letras"; 

        }

        else{
           document.querySelector("#nameHelp").innerHTML = " ";
        }

        //* tiene que retornar true or false        
        if(emailValue.length == 0){
            document.querySelector("#mailHelp").innerHTML = "El campo no puede estar vacio";
            
        }else if(!emailRegex.test(emailValue)){
           document.querySelector("#mailHelp").innerHTML = "Ingrese un email valido";
            
        }else{
           document.querySelector("#mailHelp").innerHTML = " ";
           
        }
        
        if(asuntoValue.length == 0){
            document.querySelector("#asuntoHelp").innerHTML = "El campo no puede estar vacio";

        }else if(asuntoValue.length < 4){
            document.querySelector("#asuntoHelp").innerHTML = "El asunto debe contener mas de tres letras";

        }else {
            document.querySelector("#asuntoHelp").innerHTML = " "

        }


        //* Validando le textovacio.       
        if(textoValue.trim() == "" ){
            document.querySelector("#textHelp").innerHTML = "El campo no puede estar vacio.";
            
        }else{
            document.querySelector("#textHelp").innerHTML = " ";      
        }
        

        if (textoValue.length == 0 || emailValue.length == 0 || nombreValue.length <2){
            document.querySelector("#finalHelp").innerHTML = "Debe llenar todos los campos correctamente.";
            return false;
        }
        

        //* si todo esta bien y pasaron todas las validaciones, se enviara el formulario.
        return true;
    }
    
    //* Agregar la función de validación al evento  submit del formulario
    form.addEventListener("submit", function(event){

        //* Si la funcion validate retorna un false no enviar el formulario

        if(!contactValidate()){

            event.preventDefault();
            
        } else {
            alert('El formulario se envio correctamente.');
        }
    })

});