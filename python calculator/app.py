from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This allows frontend to talk to backend

@app.route('/calculate', methods=['POST'])
def calculate():
    # Get the expression from frontend
    data = request.get_json()
    expression = data.get('expression', '')
    
    try:
        # Use Python's eval to calculate (simple but works)
        result = eval(expression)
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    print("Calculator backend running on http://127.0.0.1:5000")
    app.run(debug=True)