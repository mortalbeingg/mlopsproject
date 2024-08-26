from flask import Flask,render_template,request
from src.pipeline.prediction_pipeline import prediction_pipeline,CustomData

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("index.html")

@app.route("/predict",methods=["GET","POST"])
def predictdatapoint():
    if request.method=="GET":
        return render_template("form.html")
    else:
       data = CustomData(
           carat = request.form.get("carat"),
           depth = request.form.get("depth"),
           table = request.form.get("table"),
           x = request.form.get("x"),
           y = request.form.get("y"),
           z = request.form.get("z"),
           cut = request.form.get("cut"),
           color = request.form.get("color"),
           clarity = request.form.get("clarity")  
       ) 
       final_data = data.data_as_df()
       predict_pipeline = prediction_pipeline()
       prediction = predict_pipeline.predict(final_data)
       result = round(prediction[0],3)
       
       return render_template("result.html",final_result=result)
        


if __name__=="__main__":
    app.run(host="0.0.0.0",port=8000)