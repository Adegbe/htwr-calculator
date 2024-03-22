from flask import Flask, request, render_template

app = Flask(__name__)

def calculate_htwr(height_cm, waist_cm):
    return waist_cm / height_cm

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/htwr', methods=['GET', 'POST'])
def htwr():
    if request.method == 'POST':
        try:
            age = int(request.form['age'])
            nationality = request.form['nationality']
            gender = request.form['gender']
            height_cm = float(request.form['height'])
            waist_cm = float(request.form['waist'])

            htwr_ratio = calculate_htwr(height_cm, waist_cm)

            return render_template('result.html', age=age, nationality=nationality, 
                                   gender=gender, htwr=htwr_ratio)
        except ValueError:
            return "Invalid input. Please ensure all fields are correctly filled."
    return render_template('htwr_form.html')

if __name__ == '__main__':
    app.run(debug=True, port=8080)
