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