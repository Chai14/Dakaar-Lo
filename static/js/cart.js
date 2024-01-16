document.addEventListener('DOMContentLoaded', function () {
   loadCartItems();
 });
 
 function loadCartItems() {
   // Fetch cart items from Django backend and update the cart view
   fetch('/api/get_cart_items/')
     .then(response => response.json())
     .then(data => {
       displayCartItems(data);
       updateTotalPrice(data);
     });
 }
 
 function displayCartItems(items) {
   const cartItemsDiv = document.getElementById('cart-items');
   cartItemsDiv.innerHTML = '';
 
   items.forEach(item => {
     const itemDiv = document.createElement('div');
     itemDiv.innerHTML = `
       <p>${item.product_name} - Quantity: ${item.quantity} - Price: $${item.price.toFixed(2)}</p>
     `;
     cartItemsDiv.appendChild(itemDiv);
   });
 }
 
 function updateTotalPrice(items) {
   const totalPriceSpan = document.getElementById('total-price');
   let total = 0;
 
   items.forEach(item => {
     total += item.price * item.quantity;
   });
 
   totalPriceSpan.innerText = total.toFixed(2);
 }
 
 function checkout() {
   // Implement the checkout logic (redirect to checkout page, process payment, etc.)
   // This will depend on your backend implementation
   alert('Thank You');
 }


 