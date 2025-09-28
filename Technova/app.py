from flask import Flask, render_template
app= Flask (__name__)
@app.route("/")
def home():
    return render_template("index.html")



@app.route("/shop")
def shop():
    products = [
        {"title": "Tiwi’s Candle Co.", "image": "https://via.placeholder.com/200", "description": "Handmade soy candles", "price": "$20"},
        {"title": "Glow Skincare", "image": "https://via.placeholder.com/200", "description": "Natural skincare products", "price": "$35"},
        {"title": "Code Queens Workshop", "image": "https://via.placeholder.com/200", "description": "Learn to code like a boss", "price": "$0"}
    ]
    return render_template("shop.html", products=products)

