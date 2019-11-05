function cambiarValoresLibro() {
        cadVariables = window.location.toString();

            arrVariables = cadVariables.split("/");
            var link = document.getElementById("cierre de sesion");
            link.href="/er2/"+arrVariables[arrVariables.length-1]+"/";
            var usuario = document.getElementById("btnUsuario");
            usuario.innerText=arrVariables[arrVariables.length-1];

        var inputFModificacion = document.getElementById("id_fecha_modificacion_libro");
        var inputFCreacion = document.getElementById("id_fecha_creacion_libro");
        var inputStatus = document.getElementById("id_status_libro");
        var inputvistas = document.getElementById("id_vistas");
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
        inputFCreacion.value = fecha;
        inputStatus.value = 'A';
        inputvistas.value = 0;


        /*document.getElementById("id_fecha_modificacion").disabled = true;
        document.getElementById("id_fecha_creacion").disabled = true;
        document.getElementById("id_status").disabled = true;

        $('input[id="id_fecha_creacion"').value()="h";
*/      var a = ['id_status_libro','id_fecha_creacion_libro','id_fecha_modificacion_libro','id_vistas'];
        for(var i=0; i<a.length; i++){
        $('label[for=' + a[i] + '], input#' + a[i]).hide();
        }

        }


function cambiarValores(opcion) {
         cadVariables = window.location.toString();

            arrVariables = cadVariables.split("/");
            var link = document.getElementById("cierre de sesion");
            link.href="/er2/"+arrVariables[arrVariables.length-1]+"/";
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
        inputFCreacion.value = fecha;
        inputStatus.value = 'A';

        /*document.getElementById("id_fecha_modificacion").disabled = true;
        document.getElementById("id_fecha_creacion").disabled = true;
        document.getElementById("id_status").disabled = true;

        $('input[id="id_fecha_creacion"').value()="h";
*/      var a = ['id_status_'+opcion,'id_fecha_creacion_'+opcion,'id_fecha_modificacion_'+opcion];
        for(var i=0; i<a.length; i++){
        $('label[for=' + a[i] + '], input#' + a[i]).hide();
        }


        }

function cambiarValoresUsuario() {



        var inputFModificacion = document.getElementById("id_fecha_modificacion");
        var inputFCreacion = document.getElementById("id_fecha_creacion");
        var inputStatus = document.getElementById("id_status");
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

        document.getElementById("id_fecha_modificacion").value= fecha
        document.getElementById("id_fecha_creacion").value= fecha
        document.getElementById("id_status").value='B'

        /*document.getElementById("id_fecha_modificacion").disabled = true;
        document.getElementById("id_fecha_creacion").disabled = true;
        document.getElementById("id_status").disabled = true;

        $('input[id="id_fecha_creacion"').value()="h";*/
      var a = ['id_status','id_fecha_creacion','id_fecha_modificacion'];
        for(var i=0; i<a.length; i++){
        $('label[for=' + a[i] + '], input#' + a[i]).hide();
        }
         document.getElementById("nav").style.display = 'none';





        }

function cambiarValoresUsuarioLogin() {



        var inputFModificacion = document.getElementById("id_fecha_modificacion");
        var inputFCreacion = document.getElementById("id_fecha_creacion");
        var inputStatus = document.getElementById("id_status");
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

        document.getElementById("id_fecha_modificacion").value= fecha
        document.getElementById("id_fecha_creacion").value= fecha
        document.getElementById("id_status").value='B'

        /*document.getElementById("id_fecha_modificacion").disabled = true;
        document.getElementById("id_fecha_creacion").disabled = true;
        document.getElementById("id_status").disabled = true;

        $('input[id="id_fecha_creacion"').value()="h";*/
      var a = ['id_status','id_fecha_creacion','id_fecha_modificacion'];
        for(var i=0; i<a.length; i++){
        $('label[for=' + a[i] + '], input#' + a[i]).hide();
        }







        }

function lowerNombre(opcion){

        var inputNombre = document.getElementById("id_nombre_"+opcion);
        document.getElementById("id_nombre_"+opcion).value = inputNombre.value.toLowerCase();



        }

function lowerNombreL(opcion){

        var inputNombre = document.getElementById("id_titulo_"+opcion);
        document.getElementById("id_titulo_"+opcion).value = inputNombre.value.toLowerCase();



        }