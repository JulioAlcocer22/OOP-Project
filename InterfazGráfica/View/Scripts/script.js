
//Cambiar imagen de acuerdo a la licenciatura seleccionada
document.getElementById('licenciatura').addEventListener('change', function() {
    var nuevaImagen = 'Images/'+ this.value + '.jpg';
    document.getElementById('img-licenciatura').src = nuevaImagen;
});
