import os

from flask import Flask, request, abort, jsonify, send_file

import firebasefirestore

s = firebasefirestore.FirebaseFirestore()

app = Flask(__name__)

@app.route('/', )
def home():
    return "PDF"

@app.route('/generate_pdf', methods=['POST'])
def generate():
    data = request.json
    docId = data.get("docId")
    
    if not docId:
        abort(400, description="Missing 'docId' in request data")
    
    try:
        print(docId)
        print(type(docId))
        s.generate_pdf(docId)
        file_path = f"{docId}_report.pdf"
        
        if os.path.exists(file_path):
            return send_file(file_path, as_attachment=True)
        else:
            abort(404, description="PDF file not found")
    except Exception as e:
        app.logger.error(f"Error generating PDF: {e}")
        abort(500, description="Internal server error")
        
if __name__ == '__main__':
    app.run(debug=True)