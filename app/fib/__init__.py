"""Blueprint for Fibonacci calculator web interface."""
from flask import Blueprint, jsonify, render_template, request

from app.fib.calculator import FibCalculator

bp = Blueprint('fibonacci', __name__, url_prefix='/fibonacci')
calculator = FibCalculator()


@bp.route('/', methods=['GET'])
def index():
    """Render the calculator interface."""
    return render_template('fibonacci/index.html')


@bp.route('/calculate', methods=['POST'])
def calculate():
    """Calculate Fibonacci number."""
    try:
        n = int(request.json['n'])
        result = calculator.calculate(n)
        return jsonify({
            'success': True,
            'result': result,
            'input': n
        })
    except (ValueError, TypeError) as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400