from flask import Flask , request , render_template
from src.exception_file import CustomException 
from src.logger import logging 
from src.pipeline.predicting_pipeline import CustomData , predict_val

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict_val_page',methods=['POST'])
def predict_data():
    print("Hello")
    custom_data_object = CustomData(
        age = request.form.get('age'),
        job = request.form.get('job'),
        marital = request.form.get('marital'),
        balance = request.form.get('balance'),
        housing = request.form.get('housing'),
        loan = request.form.get('loan'),
        day = request.form.get('day'),
        duration = request.form.get('duration'),
        campaign = request.form.get('campaign'),
        pdays = request.form.get('pdays'),
        previous = request.form.get('previous'),
        poutcome = request.form.get('poutcome')
    )

    data = custom_data_object.get_data_as_df()
    pred_val = predict_val(data)
    print(pred_val)

    return render_template("index.html",result=pred_val)

if __name__ == "__main__":
    app.run(debug=True,port=8002)