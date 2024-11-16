from app import app

if __name__ == "__main__":
    # Set Flask to run on port 5001 instead of the default 5000
    app.run(debug=True, host='0.0.0.0', port=5001)
