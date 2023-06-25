from flask import Flask, jsonify, request
import util

app = Flask(__name__)

@app.route('/get_locations')
def get_locations():
    response = jsonify({
        'locations':util.get_locations()
    })
    response.headers.add('Access-Control-Allow-Origin','*') #allow code from any origin to access the response
    return response

@app.route('/predict_price', methods = ['POST'])
def predict_price():
    sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bedrooms = int(request.form['bedrooms'])
    bath = int(request.form['bath'])
    balcony = int(request.form['balcony'])
    response = jsonify({
        'predicted_price':str(util.predict_price(location,sqft,bath,bedrooms,balcony))
    })
    response.headers.add('Access-Control-Allow-Origin','*') 
    return response


if __name__ == "__main__":
    print("Starting python flask server")
    util.get_data_columns()
    util.get_model()
    app.run()