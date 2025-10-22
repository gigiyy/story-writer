from flask import Blueprint, request, jsonify, render_template
from app.aml.upload_csv import validate_csv_records

bp = Blueprint('aml', __name__, url_prefix='/aml')

from flask import redirect, url_for

@bp.route('/')
def aml_index():
    return redirect(url_for('aml.upload_csv'))

@bp.route('/upload_csv', methods=['GET', 'POST'])
def upload_csv():
    result = None
    if request.method == 'POST':
        file = request.files.get('file')
        if not file:
            error = {'error': 'No file uploaded'}
            if request.accept_mimetypes.accept_json and not request.accept_mimetypes.accept_html:
                return jsonify(error), 400
            return render_template('aml/upload_csv.html', result=None, error=error)
        content = file.read().decode('utf-8')
        result = validate_csv_records(content)
        # If API request, return JSON
        if request.accept_mimetypes.accept_json and not request.accept_mimetypes.accept_html:
            return jsonify(result)
    return render_template('aml/upload_csv.html', result=result)
