from flask import Flask, render_template
app = Flask(__name__)


@app.route('/bmi/<int:weight>/<float:height>')
def calculate_bmi(weight, height):
    bmi = weight / (height * height)
    if bmi < 16:
        condition = "Severely underweight"
    elif bmi < 18.5:
        condition = "Underweight"
    elif bmi < 25:
        condition = "Normal"
    elif bmi < 30:
        condition = "Overweight"
    else:
        condition = "Obese"
    return "BMI: " + str(bmi) + " => " + condition

if __name__ == '__main__':
  app.run(debug=True)
