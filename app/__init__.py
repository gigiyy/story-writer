"""Flask application entry point."""
from flask import Flask, render_template, request, jsonify
from .fib.calculator import calculate_fibonacci

app = Flask(__name__)

@app.route('/')
def index():
    """Render the main page with the Fibonacci calculator."""
    return render_template('index.html')

@app.route('/api/fibonacci', methods=['POST'])
def calculate():
    """API endpoint to calculate Fibonacci numbers."""
    try:
        data = request.get_json()
        n = data.get('number')
        if n is None:
            return jsonify({'error': 'No number provided'}), 400

        result = calculate_fibonacci(n)
        return jsonify({'result': result})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True)