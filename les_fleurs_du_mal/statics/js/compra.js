function comprar(){

$("#compra").submit(
            function(e){
                if(document.getElementById("saldo").value < document.getElementById("costo").value){
                    alert("No tiene el saldo suficiente");
                    e.preventDefault();
                }

                //resto código
            }
        );

}

function ordenarCategorias(){
var arrayLis=new Array();
var coleccionLis= document.getElementsByTagName("LI");
for (var i=0;i<coleccionLis.length;i++){
    arrayLis[i]=coleccionLis[i].innerHTML;
}




arrayLis.sort(function(a,b){return b - a});
for (var i=0;i<coleccionLis.length;i++){
    coleccionLis[i].innerHTML=arrayLis[i];
}
}