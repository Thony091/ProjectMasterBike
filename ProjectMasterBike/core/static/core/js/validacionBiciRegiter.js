// Validacion de Campos con JavaScript
document.querySelector("#form-register-bike").addEventListener("submit", function(event){
	event.preventDefault();
	// Obtener el formulario y sus campos
	
	let name        = document.querySelector("#name").value;
	let email       = document.querySelector("#email").value;
	let fechaCompra = document.querySelector("#fech_comp").value;
	let boleta      = document.querySelector("#boleta").value;
	let chasis      = document.querySelector("#nChasis").value;
	let run         = document.querySelector("#rut").value;
	let mensaje     = document.querySelector("#text-area").value;
    let comuna      = document.querySelector("#comuna").value;
	
	let isValid = true;
	let emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
		
		// Validando nombre
		if (name.trim() == "") {
			isValid = false;
			document.querySelector("#nameHelp").innerHTML = "El campo Nombre no puede estar vacío";			
		} else if(name.length < 3) {
			document.querySelector("#nameHelp").innerHTML = "El nombre debe contener almenos 3 caracteres.";
		} else {
			document.querySelector("#nameHelp").innerHTML = " ";
		}
		
		// Validando email
		if (email.trim() === "") {
			isValid = false;
			document.querySelector("#emailHelp").innerHTML = "El Campo Email no debe estar vacío";
		} else if (!emailRegex.test(email)) {
			isValid = false;
			document.querySelector("#emailHelp").innerHTML = "Por favor, ingresa un correo electronico válido";
		} else {
			document.querySelector("#emailHelp").style.display = "none";
		}
		

		// Validando fechaCompra. Ocultamos o mostramos mensaje de ayuda con (style="display:orden")" --OJO: debe estar en el DOM y en JS
		if (fechaCompra.length === 0) {
			isValid = false;
			document.querySelector("#fechaHelp").innerHTML = "El Campo no debe estar  vacio";
		} else {
			document.querySelector("#fechaHelp").style.display = "none";
		}
		// Validando boleta. Ocultamos o mostramos mensaje de ayuda con (style="display:orden")" --OJO: debe estar en el DOM y en JS
		if (boleta.length === 0) {
			isValid = false;
			document.querySelector("#boletaHelp").innerHTML = "El Campo no debe estar  vacio";
		} else {
			document.querySelector("#boletaHelp").style.display = "none";
		}
		// Validando chasis. Ocultamos o mostramos mensaje de ayuda con (style="display:orden")" --OJO: debe estar en el DOM y en JS
		if (chasis.length === 0) {
			isValid = false;
			document.querySelector("#motorHelp").innerHTML = "El Campo no debe estar  vacio";
		} else {
			document.querySelector("#motorHelp").style.display = "none";
		}
		
        // run
        if (run.trim() === "") {
            isValid = false;
            document.querySelector("#runclienteHelp").style.display = "block";
            document.querySelector("#runclienteHelp2").style.display = "none";
        } else if (run.length < 8) {
            isValid = false;
            document.querySelector("#runclienteHelp2").style.display = "block";
            document.querySelector("#runclienteHelp").style.display = "none";
        } else {
            document.querySelector("#runclienteHelp").style.display = "none";
        }

		// Validando mensaje. Ocultamos o mostramos mensaje de ayuda con (style="display:orden")" |--OJO: debe estar en el DOM y en JS
		if (mensaje.trim() ==="") {
			isValid = false;
			document.querySelector("#textHelp").style.display = "block";
		} else if (mensaje.length < 10) {
			isValid = false;
			document.querySelector("#textHelp").innerHTML = "Debe contener como mínimo 10 caracteres";
		} else {
			document.querySelector("#textHelp").style.display = "none";
		}

        if (comuna === 0) {
            isValid = false;
            document.querySelector("#comunaHelp").innerHTML = "Debe elegir una opcion valida";
        }else {
			document.querySelector("#comunaHelp").style.display = "none";
		}
		
		if(isValid) {
		event.target.submit();
	}

});