from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def hello_world():
    banner = """
    *****************************************
    *                                       *
    *           Hello, World!                *
    *                                       *
    *****************************************
    """
    assignment_message = "\nThis is MapUp Assignment 2."
    return render_template_string(f"{banner}{assignment_message}")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
