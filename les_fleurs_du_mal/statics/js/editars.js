function cambiarValoreseditar(opcion) {
        cadVariables = window.location.toString();

            arrVariables = cadVariables.split("/");
            var link = document.getElementById("cierre de sesion");
            link.href="http://127.0.0.1:8000/biblioteca/er2/"+arrVariables[arrVariables.length-1]+"/";
            var usuario = document.getElementById("btnUsuario");
            usuario.innerText=arrVariables[arrVariables.length-1];

        var inputFModificacion = document.getElementById("id_fecha_modificacion_"+opcion);

        var inputFCreacion = document.getElementById("id_fecha_creacion_"+opcion);
        var inputStatus = document.getElementById("id_status_"+opcion);
        var f = new Date();
        var dia = f.getDate();
        if(dia<10){
        dia = "0"+dia;
        }
        var mes=(f.getMonth()+1);
        if(mes<10){
        mes="0"+mes;
        }


        var fecha =f.getFullYear() + "-"+mes+ "-"+dia ;

        inputFModificacion.value = fecha;


        /*document.getElementById("id_fecha_modificacion").disabled = true;
        document.getElementById("id_fecha_creacion").disabled = true;
        document.getElementById("id_status").disabled = true;

        $('input[id="id_fecha_creacion"').value()="h";
*/      var a = ['id_status_'+opcion,'id_fecha_creacion_'+opcion,'id_fecha_modificacion_'+opcion];
        for(var i=0; i<a.length; i++){
        $('label[for=' + a[i] + '], input#' + a[i]).hide();
        }

        }