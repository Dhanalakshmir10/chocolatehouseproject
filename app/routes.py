import sqlite3
from flask import render_template, request, redirect, url_for, flash
from app import app

DB_PATH = "chocolate_house.db"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/flavors', methods=['GET', 'POST'])
def flavors():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        cursor.execute("INSERT INTO SeasonalFlavor (name, description) VALUES (?, ?)", (name, description))
        conn.commit()
        flash("Flavor added!")
        return redirect(url_for('flavors'))

    cursor.execute("SELECT * FROM SeasonalFlavor")
    flavors = cursor.fetchall()
    conn.close()
    return render_template('flavors.html', flavors=flavors)

@app.route('/inventory', methods=['GET', 'POST'])
def inventory():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    if request.method == 'POST':
        name = request.form['name']
        quantity = request.form['quantity']
        cursor.execute("INSERT INTO Ingredient (name, quantity) VALUES (?, ?)", (name, float(quantity)))
        conn.commit()
        flash("Ingredient added!")
        return redirect(url_for('inventory'))

    cursor.execute("SELECT * FROM Ingredient")
    ingredients = cursor.fetchall()
    conn.close()
    return render_template('inventory.html', ingredients=ingredients)

@app.route('/suggestions', methods=['GET', 'POST'])
def suggestions():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    if request.method == 'POST':
        flavor_suggestion = request.form['flavor_suggestion']
        allergy_concern = request.form['allergy_concern']
        cursor.execute("INSERT INTO CustomerSuggestion (flavor_suggestion, allergy_concern) VALUES (?, ?)",
                       (flavor_suggestion, allergy_concern))
        conn.commit()
        flash("Suggestion added!")
        return redirect(url_for('suggestions'))

    cursor.execute("SELECT * FROM CustomerSuggestion")
    suggestions = cursor.fetchall()
    conn.close()
    return render_template('suggestions.html', suggestions=suggestions)
