from flask import Blueprint, request, jsonify, render_template
from app.aml.csv_validation import validate_csv_records

bp = Blueprint('aml', __name__, url_prefix='/aml')

from flask import redirect, url_for


@bp.route('/')
def aml_index():
    return redirect(url_for('aml.upload'))

@bp.route('/upload', methods=['GET', 'POST'])
def upload():
    result = None
    error = None
    if request.method == 'POST':
        file = request.files.get('file')
        if not file:
            error = {'error': 'No file uploaded'}
            return render_template('aml/upload.html', result=None, error=error)
        content = file.read().decode('utf-8')
        result = validate_csv_records(content)
    return render_template('aml/upload.html', result=result, error=error)
