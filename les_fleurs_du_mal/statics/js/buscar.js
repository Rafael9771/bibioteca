

function buscarNombre(opcion){

cadVariables = window.location.toString();

            arrVariables = cadVariables.split("/");
         var usuario = arrVariables[arrVariables.length-1];

        var inputBuscar = document.getElementById("buscar");
        var busqueda = urlBuscar('/biblioteca/buscar-'+opcion+'/',inputBuscar.value.toLowerCase(),usuario);

        formulario = document.getElementById("formulario");
        formulario.setAttribute('action',busqueda);
}

