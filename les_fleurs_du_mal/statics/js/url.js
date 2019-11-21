function urlBuscar(pagina,id,nombres) {


            pagina +=id+"/"+nombres;
            pagina = pagina.substring(0,pagina.length);
            return pagina;
        }

function link(){


            var cont = 0;
            cadVariables = window.location.toString();

            arrVariables = cadVariables.split("/");
            var link = document.getElementById("cierre de sesion");
            link.href="/er2/"+arrVariables[arrVariables.length-1]+"/";
            var ni=arrVariables[arrVariables.length-1];
            document.getElementById("btnUsuario").innerText=arrVariables[arrVariables.length-1];

        }

function cambiarlink(){


            var link = document.getElementById("cierre de sesion");
            var usuario = document.getElementById("usuario");
            if(usuario.value != null || usuario.value != undefined){
                us = usuario.value;
                document.getElementById("cierre de sesion").href="/er2/"+us+"/";
            }else{
                location.href="/";
            }
            history.pushState(null, "", "mengano.html");


        }


function carga(){
            cadVariables = window.location.toString();

            arrVariables = cadVariables.split("/");
            return arrVariables[arrVariables.length-1];

        }

function pasarUsuario(pagina, nombres) {

            var nombre='';
            var comp='';

            nomVec = nombres.split(",");
            for (i=0; i<nomVec.length; i++){
                nombre = eval(nomVec[i]);
                comp = nomVec[i] + "=" + escape(eval(nomVec[i]))+"&";
            }
            pagina +=nombre
            pagina = pagina.substring(0,pagina.length);
            location.href=pagina;
        }