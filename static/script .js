function showBuyer() {
  document.getElementById('roleSelect').classList.add('hidden');
  document.getElementById('buyerSection').classList.remove('hidden');
}

function showSeller() {
  document.getElementById('roleSelect').classList.add('hidden');
  document.getElementById('sellerSection').classList.remove('hidden');
}

function addToCart(product, quantity) {
  if (!quantity || quantity <= 0) {
    alert("Please enter a valid quantity.");
    return;
  }
  alert(`Added ${quantity} units of ${product} to cart.`);
}

document.addEventListener('DOMContentLoaded', function () {
  const form = document.getElementById('sellForm');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      const name = document.getElementById('productName').value;
      const price = document.getElementById('productPrice').value;
      const image = document.getElementById('productImage').files[0];
      if (!image) {
        alert("Please upload an image.");
        return;
      }
      alert(`Posted item: ${name}, Price: ₹${price}`);
    });
  }
});
