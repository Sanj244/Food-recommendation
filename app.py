from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# Dish categories and their respective dishes
breakfast_categories = {
    "Breakfast Curries": [
        "Pesarattu (Green Gram Pancake)", 
        "Chana Masala", 
        "Methi Thepla with Yogurt", 
        "Baingan Bharta", 
        "Vegan Rajma Masala"
    ],
    "Pulavs and Rice Items": [
        "Tamarind Rice", 
        "Lemon Rice", 
        "Coconut Rice", 
        "Vegetable Biryani"
    ],
    "Tawa-Based Dishes": [
        "Tawa Veggies with Paratha", 
        "Tawa Idli", 
        "Tawa Paneer", 
        "Tawa Chapati"
    ],
    "Snacks/Light Meals": [
        "Puffed Rice Upma", 
        "Poha", 
        "Vegan Samosa", 
        "Cucumber Sandwiches"
    ],
    "Healthier Options": [
        "Flaxseed Smoothie", 
        "Chia Pudding", 
        "Fruit Salad with Lemon Dressing"
    ]
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/suggest')
def suggest():
    category = random.choice(list(breakfast_categories.keys()))
    dish = random.choice(breakfast_categories[category])
    return jsonify({"category": category, "dish": dish})

if __name__ == '__main__':
    app.run(debug=True)
