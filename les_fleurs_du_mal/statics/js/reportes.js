
function encontrarusuario(){//este metodo busca en tu url el usuario que inicio sesion

             var cont = 0;
            cadVariables = window.location.toString();

            arrVariables = cadVariables.split("/");
            return arrVariables[arrVariables.length-1];
        }


function verfechas(opcion){//este metodo nos manda a generar el reporte de libros agregados con el rango de fechas

        var fechainicial = document.getElementById("finicio").value;
        var fechafinal = document.getElementById("ffinal").value;
        var url = "/biblioteca/reporte/"+opcion+"/"+fechainicial+"/"+fechafinal;
        var formulario = document.getElementById("fechas");

        formulario.setAttribute('action',url);
        formulario.submit();
        }

/* opciones de repostes para autor */

function verReporteAutor_libro(){
        var op = document.getElementById("lib");
        location.href="http://127.0.0.1:8000/biblioteca/reporte/autor-libro/"+op.value+"/"
        }

        function verReporteAutor_nacionalidad(){

            var op = document.getElementById("nac");
            location.href="http://127.0.0.1:8000/biblioteca/reporte/autor-nacionalidad/"+op.value+"/"

        }

        function verReporteAutor(){

            var valor = document.getElementsByName("opcion");
            for(i=0; i<valor.length; i++){

                if(valor[i].checked){
                    var op = valor[i].value;
                }
            }


            if(op=="1"){
                document.getElementById("libros").style.display = 'block';
                document.getElementById("nacionalidades").style.display = 'none';
            }else{
                document.getElementById("libros").style.display = 'none';
                document.getElementById("nacionalidades").style.display = 'block';
            }
        }

        function ocultarReportesAutor(){
            document.getElementById("nacionalidades").style.display = 'none';
            document.getElementById("libros").style.display = 'none';

             var cont = 0;
            cadVariables = window.location.toString();

            arrVariables = cadVariables.split("/");
            var link = document.getElementById("cierre de sesion");
            link.href="http://127.0.0.1:8000/biblioteca/er2/"+arrVariables[arrVariables.length-1]+"/";
            var ni=arrVariables[arrVariables.length-1];
            document.getElementById("btnUsuario").innerText=arrVariables[arrVariables.length-1];


        }

         function ocultarReportesAutor(){
            document.getElementById("nacionalidades").style.display = 'none';
            document.getElementById("libros").style.display = 'none';

             var cont = 0;
            cadVariables = window.location.toString();

            arrVariables = cadVariables.split("/");
            var link = document.getElementById("cierre de sesion");
            link.href="http://127.0.0.1:8000/biblioteca/er2/"+arrVariables[arrVariables.length-1]+"/";
            var ni=arrVariables[arrVariables.length-1];
            document.getElementById("btnUsuario").innerText=arrVariables[arrVariables.length-1];


        }



/* fin de opciones de reportes para autor*/


/*inicio de opciones de reportes para libro*/

function cal2(){

            var cont = 0;
            cadVariables = window.location.toString();

            arrVariables = cadVariables.split("/");
            var link = document.getElementById("cierre de sesion");
            link.href="http://127.0.0.1:8000/biblioteca/er2/"+arrVariables[arrVariables.length-1]+"/";
            var ni=arrVariables[arrVariables.length-1];
            document.getElementById("btnUsuario").innerText=arrVariables[arrVariables.length-1];

            var valor = document.getElementsByName("opcion");
            for(i=0; i<valor.length; i++){

                if(valor[i].checked){
                    var op=valor[i].value;

                 }
            }

            if(op=="1"){

            document.getElementById("fechas").style.display = 'block';
            document.getElementById("autores").style.display = 'none';
            document.getElementById("categorias").style.display = 'none';


            }else if(op == "2"){
             document.getElementById("fechas").style.display = 'none';
            document.getElementById("autores").style.display = 'block';
            document.getElementById("categorias").style.display = 'none';
            }
            else{
             document.getElementById("fechas").style.display = 'none';
            document.getElementById("autores").style.display = 'none';
            document.getElementById("categorias").style.display = 'block';
            }



        }

        function vercategoria(){
        var op = document.getElementById("select");
        location.href="http://127.0.0.1:8000/biblioteca/reporte/libro-categoria/"+op.value+"/"

        }

        function verautor(){
        var op = document.getElementById("au");
        location.href="http://127.0.0.1:8000/biblioteca/reporte/libro-autor/"+op.value+"/"
        }

        function desactivarC(){


            var link = document.getElementById("cierre de sesion");
            link.href="http://127.0.0.1:8000/biblioteca/er2/"+encontrarusuario()+"/";

            document.getElementById("btnUsuario").innerText=encontrarusuario();

        document.getElementById("fechas").style.display = 'block';
        document.getElementById("autores").style.display = 'none';
        document.getElementById("categorias").style.display = 'none';
        document.getElementsByName("opcion")[0].click();



        }


/*fin de opciones de reportes para libro*/


function calR(){

            var cont = 0;
            cadVariables = window.location.toString();

            arrVariables = cadVariables.split("/");
            var link = document.getElementById("cierre de sesion");
            link.href="http://127.0.0.1:8000/biblioteca/er2/"+arrVariables[arrVariables.length-1]+"/";
            var ni=arrVariables[arrVariables.length-1];
            document.getElementById("btnUsuario").innerText=arrVariables[arrVariables.length-1];

            var valor = document.getElementsByName("opcion");
            for(i=0; i<valor.length; i++){

                if(valor[i].checked){
                    var op=valor[i].value;

                 }
            }

            if(op=="1"){

            document.getElementById("fechas").style.display = 'block';

            document.getElementById("categorias").style.display = 'none';


            }else if(op == "2"){
             document.getElementById("fechas").style.display = 'none';

            document.getElementById("categorias").style.display = 'block';
            }




        }


        function desactivarR(){


            var link = document.getElementById("cierre de sesion");
            link.href="http://127.0.0.1:8000/biblioteca/er2/"+encontrarusuario()+"/";

            document.getElementById("btnUsuario").innerText=encontrarusuario();

        document.getElementById("fechas").style.display = 'block';

        document.getElementById("categorias").style.display = 'none';
        document.getElementsByName("opcion")[0].click();



        }

        function vercategoriaR(){
        var op = document.getElementById("select");
        location.href="http://127.0.0.1:8000/biblioteca/reporte/revista-categoria/"+op.value+"/"

        }



        function verReporteLibro_sucursal(){
        var op = document.getElementById("sucursal");
        location.href="http://127.0.0.1:8000/biblioteca/reporte/sucursal-libro/"+op.value+"/"
        }

        function cerrarsesion(){
            var link = document.getElementById("cierre de sesion");
            link.href="http://127.0.0.1:8000/biblioteca/er2/"+encontrarusuario()+"/";

            document.getElementById("btnUsuario").innerText=encontrarusuario();
        }