document.addEventListener("DOMContentLoaded", function(){

    let form = document.querySelector("#form-contact");
    let nombre = document.querySelector("#name");
    let email = document.querySelector("#email");
    let marca = document.querySelector("#marca") ;
    let fechaCompra = document.querySelector("#fech_comp");
    let boleta = document.querySelector("#boleta");
    let nChasis = document.querySelector("#nChasis");
    let rut = document.querySelector("#rut");
    let texto = document.querySelector("#text-area");
    let region = document.querySelector("#region");
    let comuna = document.querySelector("#comuna");

    function registerBike(){
        let nombreValue = nombre.value;      
        let emailValue = email.value;
        let fechaCompraValue = fechaCompra.value;
        let boletaValue = boleta.value;
        let nChasisValue = nChasis.value;
        let rutValue = rut.value;
        let textoValue = texto.value;
        let marcaValue = marca.value;
        let comunaValue = comuna.value;
        let regionValue = region.value;

        //Expresión Regular : Para seguir el patron de un correo
        let emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        //Expresión Regular : Nombres y Apellidos (excluye números)
        let nombreRegex = /^[A-ZÑa-zñáéíóúÁÉÍÓÚ'° ]+$/;
        let fechaRegex =  /^([0-2][0-9]|3[0-1])(\/|-)(0[1-9]|1[0-2])\2(\d{4})$/
        let boletaRegex = /^[0-9]+$/
      
         //* Validando nombre      
        if(!nombreRegex.test(nombreValue) ){
            document.querySelector("#nameHelp").innerHTML = "El nombre debe ser solo de letras"; 
        }else{
           document.querySelector("#nameHelp").innerHTML = " ";
        }
     
        if(!emailRegex.test(emailValue)){
           document.querySelector("#mailHelp").innerHTML = "Ingrese un email valido";           
        }else{
            document.querySelector("#mailHelp").innerHTML = " ";            
        }
        
        if(fechaCompraValue.length == 0 ){
            document.querySelector("#fechaHelp").innerHTML = "El campo no puede quedar vacio";
        }else if(!fechaRegex.test(fechaCompra)){
            document.querySelector("#fechaHelp").innerHTML = "Debe cumplir el formato DD/MM/AAAA";
            
        }
        
        if(boletaValue.length < 6){
            document.querySelector("#boletaHelp").innerHTML = "ingrese un número de boleta valido";            
        }else if (!boletaRegex.test(boletaValue)){
            document.querySelector("#boletaHelp").innerHTML = "Solo puede ingresar números";            
        }else{
            document.querySelector("#boletaHelp").innerHTML = " ";

        }

        if(nChasisValue.length == 0 ){
            document.querySelector("#chasisHelp").innerHTML = "El espacio no puede quedar vacio"
        }else if(nChasisValue.length < 5 ){
            document.querySelector("#chasisHelp").innerHTML = "El número de chasis debe tener almenos 5 digitos."
        }
        
        if(rutValue.length == 0 ){
            document.querySelector("#rutHelp").innerHTML = "El espacio ni puede quedar vacio"
        }else if(rutValue.length < 9 ){
            document.querySelector("#rutHelp").innerHTML = "El rut debe contener al menos 9 digitos"            
        }else {
            document.querySelector("#rutHelp").innerHTML = " "
        }
     
        if(textoValue.trim() == "" ){
            document.querySelector("#textHelp").innerHTML = "El campo no puede estar vacio.";            
        }else{
            document.querySelector("#textHelp").innerHTML = " ";      
        }
        

        if(marcaValue == null){
            document.querySelector("#marcaHelp").innerHTML = "Debe elegir una de las opciones.";
        }else{
            document.querySelector("#marcaHelp").innerHTML = " ";
        }

        if(comunaValue == null){
            document.querySelector("#comunaHelp").innerHTML = "Debe elegir una de las opciones.";
        }else{
            document.querySelector("#comunaHelp").innerHTML = " ";
        }

        if(regionValue == null){
            document.querySelector("#regionHelp").innerHTML = "Debe elegir una de las opciones.";
        }else{
            document.querySelector("#regionHelp").innerHTML = " ";
        }
        console.log("Aqui llegue");
        if (textoValue == "" || !emailRegex.test(emailValue) || !nombreRegex.test(nombreValue) ||
        !fechaRegex.test(fechaCompra) || boletaValue == "" || nChasisValueh == ""
            || rutValue == ""){
           
            document.querySelector("#finalHelp").innerHTML = "Debe llenar todos los campos correctamente.";
            return false;
        }
        return true
    }

    form.addEventListener("submit", function(event){

        //* Si la funcion validate retorna un false no enviar el formulario

        if(!registerBike()){

            event.preventDefault();
            
        } else {
            alert('El formulario se envio correctamente.');
        }
    })

})


// function validarSelect() {
//     let select = document.getElementById("comuna");
//     if(select.value == '') {
//         alert("Selecciona una opcion");
//         return false;
//     }
// }