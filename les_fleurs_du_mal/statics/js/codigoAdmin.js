function numeroAleatorio(min, max) {
  return Math.round(Math.random() * (max - min) + min);
}

function agregarCodigo(){
    var codigo6="";
    codigo6+=numeroAleatorio(0,9);
        codigo6+=numeroAleatorio(0,9);
            codigo6+=numeroAleatorio(0,9);
                codigo6+=numeroAleatorio(0,9);
                    codigo6+=numeroAleatorio(0,9);
                        codigo6+=numeroAleatorio(0,9);


    document.getElementById("id_codigo").value=codigo6;


}


function encontrarcodigo(){//este metodo busca en tu url el usuario que inicio sesion

             var cont = 0;
            cadVariables = window.location.toString();

            arrVariables = cadVariables.split("/");
            return arrVariables[arrVariables.length-1];
        }

function agregarCodigoAdmin(){

     var cod = document.getElementById("codigoA");
     cod.value=encontrarcodigo();
     document.getElementById("codigoA").readOnly = true;

}

function iniciodesesion(){//este metodo nos manda a generar el reporte de libros agregados con el rango de fechas



        var cod = document.getElementById("codigoA");

        var url = "/"+cod.value+"/er"
        var formulario = document.getElementById("inicio");

        formulario.setAttribute('action',url);
        formulario.submit();
        }

