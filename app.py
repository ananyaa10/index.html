from flask import Flask, request, jsonify, render_template


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/bfhl', methods=['POST'])
def process_data():
    try:
        data = request.json.get('data', [])

        numbers = [item for item in data if item.isdigit()]
        alphabets = [item for item in data if item.isalpha()]

        lowercase_alphabets = sorted([item for item in alphabets if item.islower()])
        highest_lowercase_alphabet = lowercase_alphabets[-1] if lowercase_alphabets else None

        response = {
            "is_success": True,
            "user_id": "ananya123",
            "email": "ananya.mohanty2021@vitbhopal.ac.in",
            "roll_number": "21BHI10046",  
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": [highest_lowercase_alphabet] if highest_lowercase_alphabet else []
        }

        return jsonify(response)

    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)