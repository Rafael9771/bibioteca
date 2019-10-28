function eliminar(opcion){
        var inputStatus = document.getElementById("id_status_"+opcion);
        inputStatus.value = "B";
        document.getElementById("borrar").click();
        deletes=true;

        }