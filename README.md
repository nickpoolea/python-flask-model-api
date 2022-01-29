# simple-flask-model-api

## Description

A simple linear model pridicting fish weight exposed via a Flask api.

The input data is provided by:
- https://www.kaggle.com/aungpyaeap/fish-market

More details on the data can be found here:
- http://jse.amstat.org/datasets/fishcatch.txt

Project inspired by
- https://towardsdatascience.com/deploy-a-machine-learning-model-using-flask-da580f84e60c
- https://www.analyticsvidhya.com/blog/2021/05/multiple-linear-regression-using-python-and-scikit-learn/

## Usage

Install dependencies
```
pip install pandas sklearn flask numpy
```
Generate and test the model, save locally to a pickle file for use in the Flask API
```
python3 model.py
```
Start the Flask server and expose the <code>POST /weight</code> endpoint
```
python3 api.py
```
Send an example request to the exposed endpoint to predict weight
```
python3 request.py
```

