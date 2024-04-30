from flask import Flask, render_template, request
import copilot_module  # Your module for interacting with Copilot

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_code():
    description = request.form['description']
    generated_code = copilot_module.generate_code(description)
    return render_template('result.html', generated_code=generated_code)

if __name__ == '__main__':
    app.run(debug=True)
