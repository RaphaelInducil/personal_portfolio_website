from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/works')
def works():
    return render_template('works.html')

@app.route('/works/touppercase', methods=['GET', 'POST'])
def touppercase():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)

@app.route('/works/area/circle', methods=['GET', 'POST'])
def acircle():
    result = None
    if request.method == 'POST':
        radius = request.form.get('radius', '')
        result = int(radius)*3.14*int(radius)
    return render_template('circle.html', result=result)

@app.route('/works/area/triangle', methods=['GET', 'POST'])
def atriangle():
    result = None
    if request.method == 'POST':
        width = request.form.get('width', '')
        height = request.form.get('height', '')
        result = (int(width)*int(height))*.5
    return render_template('triangle.html', result=result)

@app.route('/home')
def home():
    return render_template('homepage.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)