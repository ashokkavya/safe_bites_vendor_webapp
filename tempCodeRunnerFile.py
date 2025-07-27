from flask import Flask, render_template, request, redirect, session, jsonify
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "safebite_secret"
app.permanent_session_lifetime = timedelta(days=7)

# ✅ Multilingual Texts
texts = {
    "en": {
        "title": "SafeBite Supply",
        "welcome": "Welcome to SafeBite Supply!",
        "description": "Connecting hygienic vendors to street food businesses.",
        "quality_note": "All products listed are verified for quality and hygiene.",
        "product_list": "Browse Products",
        "sell_heading": "Sell a Product",
        "cod": "Cash on Delivery",
        "sold_by": "Sold by",
        "delivery": "Delivery within 15–20 minutes",
        "post_product": "Post Product",
        "your_name": "Your Name",
        "product_name": "Product",
        "price": "Price",
        "use_case": "Intended Use",
        "order_confirmed": "Order Confirmed!",
        "thank_you": "Thank you for your purchase!",
        "payment_info": "Pay on delivery. A vendor will contact you shortly.",
        "your_location": "Your Location",
        "confirm_order": "Confirm Order",
        "marketplace": "Marketplace",
        "vendor_only_warning": "This item is only available to verified vendors.",
        "vendor_checkbox": "I am a registered vendor",
        "choose_role": "Are you here to buy or sell?",
        "buy": "Buy",
        "sell": "Sell",
        "cart": "Cart",
        "empty_cart": "Your cart is empty."
    },
    "hi": {
        "title": "सेफबाइट सप्लाई",
        "welcome": "सेफबाइट सप्लाई में आपका स्वागत है!",
        "description": "स्वच्छ विक्रेताओं को स्ट्रीट फूड व्यवसायों से जोड़ना।",
        "quality_note": "सभी उत्पाद गुणवत्ता और स्वच्छता के लिए सत्यापित हैं।",
        "product_list": "उत्पाद ब्राउज़ करें",
        "sell_heading": "उत्पाद बेचें",
        "cod": "डिलीवरी पर नकद भुगतान",
        "sold_by": "द्वारा बेचा गया",
        "delivery": "15–20 मिनट के भीतर डिलीवरी",
        "post_product": "उत्पाद पोस्ट करें",
        "your_name": "आपका नाम",
        "product_name": "उत्पाद",
        "price": "कीमत",
        "use_case": "उपयोग उद्देश्य",
        "order_confirmed": "ऑर्डर की पुष्टि हो गई!",
        "thank_you": "खरीदारी के लिए धन्यवाद!",
        "payment_info": "डिलीवरी पर भुगतान करें। विक्रेता आपसे शीघ्र ही संपर्क करेगा।",
        "your_location": "आपका स्थान",
        "confirm_order": "ऑर्डर की पुष्टि करें",
        "marketplace": "बाजार",
        "vendor_only_warning": "यह आइटम केवल पंजीकृत विक्रेताओं के लिए है।",
        "vendor_checkbox": "मैं पंजीकृत विक्रेता हूं",
        "choose_role": "क्या आप खरीदने या बेचने आए हैं?",
        "buy": "खरीदें",
        "sell": "बेचें",
        "cart": "कार्ट",
        "empty_cart": "आपका कार्ट खाली है।"
    },
    "kn": {
        "title": "ಸೇಫ್ಬೈಟ್ ಸರಬರಾಜು",
        "welcome": "ಸೇಫ್ಬೈಟ್ ಸರಬರಾಜಿಗೆ ಸ್ವಾಗತ!",
        "description": "ಹೆಜ್ಜೆದಾರರಿಗೂ ರಸ್ತೆ ಆಹಾರ ವ್ಯಾಪಾರಗಳಿಗೆ ಶುದ್ಧ ಪೂರೈಕೆದಾರರನ್ನು ಸಂಪರ್ಕಿಸುವುದು.",
        "quality_note": "ಎಲ್ಲಾ ಉತ್ಪನ್ನಗಳನ್ನು ಗುಣಮಟ್ಟ ಮತ್ತು ಸ್ವಚ್ಛತೆಯಿಗಾಗಿ ಪರಿಶೀಲಿಸಲಾಗಿದೆ.",
        "product_list": "ಉತ್ಪನ್ನಗಳನ್ನು ವೀಕ್ಷಿಸಿ",
        "sell_heading": "ಉತ್ಪನ್ನವನ್ನು ಮಾರಾಟ ಮಾಡಿ",
        "cod": "ಡಿಲಿವರಿಯಲ್ಲಿ ನಗದು",
        "sold_by": "ಮಾರಾಟ ಮಾಡಿದವರು",
        "delivery": "15–20 ನಿಮಿಷಗಳಲ್ಲಿ ಡೆಲಿವರಿ",
        "post_product": "ಉತ್ಪನ್ನವನ್ನು ಪೋಸ್ಟ್ ಮಾಡಿ",
        "your_name": "ನಿಮ್ಮ ಹೆಸರು",
        "product_name": "ಉತ್ಪನ್ನ",
        "price": "ಬೆಲೆ",
        "use_case": "ಬಳಕೆಯ ಉದ್ದೇಶ",
        "order_confirmed": "ಆದೇಶ ದೃಢೀಕರಿಸಲಾಗಿದೆ!",
        "thank_you": "ನಿಮ್ಮ ಖರೀದಿಗೆ ಧನ್ಯವಾದಗಳು!",
        "payment_info": "ಡಿಲಿವರಿಯ ಸಮಯದಲ್ಲಿ ಪಾವತಿ. ವಿತರಕರು ಶೀಘ್ರದಲ್ಲೇ ನಿಮ್ಮನ್ನು ಸಂಪರ್ಕಿಸುತ್ತಾರೆ.",
        "your_location": "ನಿಮ್ಮ ಸ್ಥಳ",
        "confirm_order": "ಆದೇಶವನ್ನು ದೃಢೀಕರಿಸಿ",
        "marketplace": "ಮಾರುಕಟ್ಟೆ",
        "vendor_only_warning": "ಈ ಉತ್ಪನ್ನವನ್ನು ಪ್ರಮಾಣಿತ ವಿತರಕರಿಗೆ ಮಾತ್ರ ಲಭ್ಯವಿದೆ.",
        "vendor_checkbox": "ನಾನು ನೋಂದಾಯಿತ ವಿತರಕನು",
        "choose_role": "ನೀವು ಖರೀದಿಸಲು ಬಂದಿದ್ದೀರಾ ಅಥವಾ ಮಾರಲು?",
        "buy": "ಖರೀದಿ",
        "sell": "ಮಾರಾಟ",
        "cart": "ಕಾರ್ಟ್",
        "empty_cart": "ನಿಮ್ಮ ಕಾರ್ಟ್ ಖಾಲಿಯಾಗಿದೆ."
    }
}

# ✅ Products
products = [
    {"name": "Rice (5kg)", "price": 250, "image": "rice.jpg"},
    {"name": "Disposable Gloves", "price": 80, "image": "gloves.jpg"},
    {"name": "Tea Packets (500g)", "price": 85, "image": "tea.jpg"},
]

vendor_products = []

# ✅ Get Language
def get_lang():
    lang = session.get("lang", "en")
    return lang if lang in texts else "en"

# ✅ Set Language
@app.route("/set-language", methods=["POST"])
def set_language():
    session["lang"] = request.form["language"]
    return redirect(request.referrer or "/")

# ✅ Home redirect to role selection
@app.route("/")
def index():
    return redirect("/choose-role")

# ✅ Role selection (with t and lang)
@app.route("/choose-role", methods=["GET", "POST"])
def choose_role():
    if request.method == "POST":
        role = request.form.get("role")
        if role == "buy":
            return redirect("/products")
        elif role == "sell":
            return redirect("/sell-product")
    return render_template("choose_role.html", t=texts[get_lang()], lang=get_lang())

# ✅ Show products
@app.route("/products")
def show_products():
    return render_template("products.html", t=texts[get_lang()], products=products, vendor_products=vendor_products, lang=get_lang())

# ✅ Sell a product
@app.route("/sell-product", methods=["GET", "POST"])
def sell_product():
    if request.method == "POST":
        vendor = request.form["vendor_name"]
        name = request.form["product_name"]
        price = float(request.form["price"])
        quantity = int(request.form["quantity"])
        use = request.form["use_case"]
        vendor_products.append({
            "vendor": vendor,
            "name": name,
            "price": price,
            "quantity": quantity,
            "use": use
        })
        return redirect("/products")
    return render_template("sell_product.html", t=texts[get_lang()], lang=get_lang())

# ✅ Add to cart
@app.route("/add-to-cart", methods=["POST"])
def add_to_cart():
    product = request.json.get("product")
    if "cart" not in session:
        session["cart"] = {}
    cart = session["cart"]
    cart[product] = cart.get(product, 0) + 1
    session["cart"] = cart
    return jsonify({"status": "added"})

# ✅ Remove from cart
@app.route("/remove-from-cart", methods=["POST"])
def remove_from_cart():
    product = request.json.get("product")
    cart = session.get("cart", {})
    if product in cart:
        cart[product] -= 1
        if cart[product] <= 0:
            del cart[product]
    session["cart"] = cart
    return jsonify({"status": "removed"})

# ✅ View cart
@app.route("/cart")
def view_cart():
    cart = session.get("cart", {})
    items = []
    total = 0
    for item, qty in cart.items():
        found = next((p for p in products + vendor_products if p["name"] == item), None)
        if found:
            subtotal = found["price"] * qty
            items.append({"name": item, "qty": qty, "price": found["price"], "subtotal": subtotal})
            total += subtotal
    return render_template("cart.html", cart_items=items, total=total, t=texts[get_lang()], lang=get_lang())

# ✅ Checkout
@app.route("/checkout")
def checkout():
    session["cart"] = {}
    return render_template("checkout.html", t=texts[get_lang()], lang=get_lang())

# ✅ Vendor map
@app.route("/vendor-map")
def vendor_map():
    locations = []
    for i, v in enumerate(vendor_products):
        locations.append({
            "vendor": v["vendor"],
            "product": v["name"],
            "price": v["price"],
            "quantity": v.get("quantity", 1),
            "location": f"Vendor Zone {i+1}",
            "lat": 12.9716 + i * 0.01,
            "lng": 77.5946 + i * 0.01
        })
    return render_template("vendor_map.html", locations=locations, t=texts[get_lang()], lang=get_lang())

# ✅ Run the app
if __name__ == "__main__":
    app.run(debug=True)