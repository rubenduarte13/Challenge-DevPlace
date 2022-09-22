function reemplazarMultiplesElementos(arreglo, valor, nuevoValor){
    while(arreglo.indexOf(valor) != -1){
        arreglo.splice(arreglo.indexOf(valor), 1, nuevoValor);
    }
}

let numeros = [1,2,3,4,2,1,5];
console.log(numeros);

reemplazarMultiplesElementos(numeros, 2, 1);
console.log(numeros);