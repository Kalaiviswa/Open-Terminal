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
        if request.is_json:
            # Handle JSON payload
            data = request.get_json()
            symbol = data.get('symbol')
            quantity = data.get('quantity')
            exchange = data.get('exchange')
            order_type = data.get('order_type')
        else:
            # Handle form submission
            symbol = request.form.get('symbol')
            quantity = request.form.get('quantity')
            exchange = request.form.get('exchange')
            order_type = request.form.get('order_type')

        # Validate required fields
        if not all([symbol, quantity, exchange, order_type]):
            error_message = "All fields are required!"
            if request.is_json:
                return jsonify({"error": error_message}), 400
            return render_template('post_data.html', error=error_message)

        # Create the response message
        message = f"Order received: {quantity} of {symbol} on {exchange} as {order_type}."
        if request.is_json:
            return jsonify({"message": message})

        # For form submission, render the response on the same page
        return render_template('post_data.html', message=message)

    # Render the form for GET requests
    return render_template('post_data.html')


if __name__ == '__main__':
    app.run(debug=True)
