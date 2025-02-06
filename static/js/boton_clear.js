let cart = [];

// Función para añadir al carrito
function addToCart() {
    const weapon = document.getElementById("weapon").value;
    const skinName = document.getElementById("skin").value;

    if (weapon && skinName) {
        const skin = weapons[weapon].find(skin => skin.name === skinName);
        if (skin) {
            cart.push({
                weapon: weapon,
                skin: skin.name,
                price: skin.price,
            });
            updateCartSummary();
        }
    }
}

// Función para actualizar el resumen del carrito
function updateCartSummary() {
    const purchaseSummary = document.getElementById("purchase-summary");
    const purchaseList = document.getElementById("purchase-list");
    const totalPrice = document.getElementById("total-price");
    let total = 0;

    // Limpiar lista de compra actual
    purchaseList.innerHTML = '';

    cart.forEach(item => {
        const li = document.createElement("li");
        li.textContent = `${item.weapon} - ${item.skin} ($${item.price})`;
        purchaseList.appendChild(li);
        total += item.price;
    });

    totalPrice.textContent = `Total: $${total}`;
    purchaseSummary.style.display = "block";

    // Mostrar botón "Finalizar Compra"
    document.getElementById("finalize-purchase").style.display = "inline-block";
}

// Nueva función para vaciar el carrito
function clearCart() {
    cart = []; // Vaciamos el carrito
    updateCartSummary(); // Actualizamos el resumen para reflejar el carrito vacío
    // Opcional: Ocultar el resumen si el carrito está vacío
    if (cart.length === 0) {
        document.getElementById("purchase-summary").style.display = "none";
        document.getElementById("finalize-purchase").style.display = "none";
    }
}