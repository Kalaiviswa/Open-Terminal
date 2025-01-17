from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/get-data', methods=['GET'])
def get_data():
    # Retrieve query parameters
    param1 = request.args.get('param1', 'default_value1')
    param2 = request.args.get('param2', 'default_value2')
    return jsonify({"message": "This is a GET request!", "param1": param1, "param2": param2})

@app.route('/post-data', methods=['GET', 'POST'])
def post_data():
    if request.method == 'POST':
        # Get form data
        symbol = request.form.get('symbol')
        quantity = request.form.get('quantity')
        exchange = request.form.get('exchange')

        if not all([symbol, quantity, exchange]):
            return jsonify({"error": "All fields are required!"}), 400

        # Respond with the received data
        return jsonify({
            "message": "Data received successfully!",
            "symbol": symbol,
            "quantity": quantity,
            "exchange": exchange
        })

    # Render the form
    return render_template('post_data.html')

if __name__ == '__main__':
    app.run(debug=True)
