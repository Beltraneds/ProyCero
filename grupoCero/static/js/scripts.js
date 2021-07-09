function validaNombre(){

    var nombre = document.getElementById("txtNombre").value;
    if(nombre.trim.length == 0){
        //alert("El nombre no puede quedar en blanco");
        Swal.fire({
            icon: 'error',
            title: 'Nombre de artista',
            text: 'El nombre no puede quedar en blanco'
        })
        return false;
    }
    return true;
}

function validarFormulario() {
    resp = validaNombre();
    if (resp==false) {
        return false; 
    }
    return true;
}