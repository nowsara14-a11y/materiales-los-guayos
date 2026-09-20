
const openCartBtn = document.getElementById('open-cart-btn');
const closeCartBtn = document.getElementById('close-cart-btn');
const sideCart = document.getElementById('side-cart');

// Al hacer clic en el carrito, añade la clase 'open' para deslizarlo
openCartBtn.addEventListener('click', () => {
    sideCart.classList.add('open');
});

// Al hacer clic en la 'X', remueve la clase 'open' para ocultarlo
closeCartBtn.addEventListener('click', () => {
    sideCart.classList.remove('open');
});