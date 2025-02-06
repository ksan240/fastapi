document.addEventListener('DOMContentLoaded', function() {
    let currentImageIndex = 0;
    const images = document.querySelectorAll('#carousel img');
    const totalImages = images.length;

    function showImage(index) {
        images.forEach((img, i) => {
            img.style.display = i === index ? 'block' : 'none';
        });
    }

    function nextImage() {
        currentImageIndex = (currentImageIndex + 1) % totalImages;
        showImage(currentImageIndex);
    }

    // Cambiar imagen cada 2,5 segundos
    setInterval(nextImage, 2500);

    // Mostrar la primera imagen al cargar la página
    showImage(currentImageIndex);
});