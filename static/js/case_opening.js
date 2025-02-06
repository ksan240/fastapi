const weapons = [
    { name: "AK-47 | Fire Serpent", image: "static/IMG/AK/fireserpent.png", condition: "Factory New" },
    { name: "AWP | Dragon Lore", image: "static/IMG/AWP/dragonlore.png", condition: "Minimal Wear" },
    { name: "Desert Eagle | Blaze", image: "static/IMG/deagle/blaze.png", condition: "Field-Tested" },
    { name: "AK-47 | Hydroponic", image: "static/IMG/AK/hydroponic.png", condition: "Well-Worn" },
    { name: "USP | Twilight Galaxy", image: "static/IMG/glockusp/twilightgalaxy.png", condition: "Factory New" },
    { name: "AWP | Asiimov", image: "static/IMG/AWP/asiimov.png", condition: "Battle Scarred" },
    { name: "M4A1 | Blue Phosphor", image: "static/IMG/m4a1/bluephosphor.png", condition: "Minimal Wear" },
    { name: "AK-47 | Inheritance", image: "static/IMG/AK/inheritance.png", condition: "Field-Tested" },
    { name: "M4A1 | Hot Rod", image: "static/IMG/m4a1/hotrod.png", condition: "Minimal Wear" },
    { name: "Desert Eagle | Golden Koi", image: "static/IMG/deagle/goldenkoi.png", condition: "Battle Scarred" },
    { name: "M4A1 | Black Lotus", image: "static/IMG/m4a1/blacklotus.png", condition: "Minimal Wear" }

];

document.getElementById('open-case').addEventListener('click', function() {
    // Simula la animación de apertura de la caja
    document.getElementById('case-lid').classList.add('open');
    document.getElementById('case-body').classList.add('open');
    
    // Espera un poco para simular el tiempo de apertura
    setTimeout(function() {
        const randomWeapon = weapons[Math.floor(Math.random() * weapons.length)];
        document.getElementById('item-image').src = randomWeapon.image;
        document.getElementById('item-name').textContent = `Arma: ${randomWeapon.name}`;
        document.getElementById('item-condition').textContent = `Condición: ${randomWeapon.condition}`;
        document.getElementById('case-item').style.display = 'block';
    }, 1000); // Tiempo de espera de 1 segundos para simular la animación
});

