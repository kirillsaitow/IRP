from flask import Flask, request, render_template
# from main import recognize

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test.html')
def test():
    return render_template('test.html')

if __name__ == '__main__':
    app.run(debug=True)