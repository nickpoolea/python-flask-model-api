from pandas import read_csv, concat, get_dummies
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
import pickle
import os
from helpers import print_comment

pwd = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
data = read_csv( pwd + '/fish.csv')

# number of rows and columns
print_comment('Initial Data Shape:')
print(data.shape)

# sample first 6 rows
print_comment('Data Sample:')
print(data.head(6))

# setup independed and dependent variables
y = data['Weight']
x = data.drop('Weight', axis = 1)

# transform categorical Species variable
species = get_dummies(x, drop_first = False)
x.drop('Species', axis = 1)
x = concat([x.iloc[:, -1], species], axis = 1)

print_comment('Normalized x values')
print(x.head(6))

print_comment('Data Model Input Shape')
print(x.shape)
print(y.shape)

# split the data to train and test
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 1)

# fitting the training data with linear model
regressor = LinearRegression()
regressor.fit(x_train, y_train)

# test the model
prediction =  regressor.predict(x_test)

# model accuracy
print_comment('Model Stats:')
score =r2_score( y_test, prediction)
print ('R2 Score: ', score)
print('Mean squared error: ', mean_squared_error(y_test, prediction))

# dump the model for use with api
pickle.dump(regressor, open(pwd + '/model.pkl','wb'))

print_comment('Model generated and saved to file')
