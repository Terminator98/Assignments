from flask import Flask,render_template,request
import joblib

app = Flask(__name__)
model = joblib.load('model.h5')
scaler = joblib.load('scaler.h5')

gender = ['Female','Male']
hypertension = ['No','Yes']
heart_disease = ['No','Yes']
work_type = ['Private','Self-Employed','Governmental Job','Children','Never-Worked']
Residence = ['Rural','Urban']
smoking = ['Formerly Smoked','Never Smoked','Smokes','Unknown']
married = ['No','Yes']

@app.route('/',methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/predict',methods=['GET'])
def predict():

    input_data = [int(gender.index(request.args.get('gender'))),
        float(request.args.get('age')),
        int(hypertension.index(request.args.get('Hypertension'))),
        int(heart_disease.index(request.args.get('Heart disease'))),
        int(married.index(request.args.get('Married'))),
        int(work_type.index(request.args.get('Work Type'))),
        int(Residence.index(request.args.get('Residence Type'))),
        float(request.args.get('agl')),
        float(request.args.get('bmi')),
        int(smoking.index(request.args.get('Smoking')))]

    input_data = [input_data]
    stroke = model.predict(scaler.transform(input_data))[0]

    #return render_template('index.html',stroke=stroke)
    return render_template('index.html',stroke=stroke)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')