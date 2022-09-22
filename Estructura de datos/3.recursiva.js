function sumaRecursivaArreglo(numeros) {
    if (numeros.length === 1) {
        return numeros[0];
    } else {
        return numeros.pop(0) + sumaRecursivaArreglo(numeros);
    }
}

console.log(sumaRecursivaArreglo([1, 2, 3, 4, 5])); // 15
