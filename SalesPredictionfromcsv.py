# Importing required libraries
import numpy as np
import pandas as pd
from pandas import DataFrame
from statsmodels.tsa.seasonal import seasonal_decompose
from pmdarima import auto_arima
import matplotlib.pyplot as plt
# Ignore harmless warnings
import warnings
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

warnings.filterwarnings("ignore")
from statsmodels.tsa.statespace.sarimax import SARIMAX
# Load specific evaluation tools
from sklearn.metrics import mean_squared_error
from statsmodels.tools.eval_measures import rmse

#global someVar
someVar = False

def run():
    # Read the AirPassengers dataset
    global someVar
    if (someVar == True):
        return plt.figure(1)
    elif (someVar == False):
        csv_path = r'C:\Users\Lior Barsky\Desktop\jhonsonclean\\JhonsonCleanApp\algorithms\outputs\salesPred2015.csv'
        sales = pd.read_csv(csv_path, index_col='Month', parse_dates=True, encoding='utf-8')

        # Print the first five rows of the dataset
        #print(sales.head())

        # ETS Decomposition
        result = seasonal_decompose(sales['numofsales'].values, freq=29, model='multiplicative')

        # ETS plot
        # todo : run this code in jupyter notebook

        # Fit auto_arima function to orders[sales] dataset
        stepwise_fit = auto_arima(sales['numofsales'], start_p=1, start_q=1,
                                  max_p=3, max_q=3, m=12,
                                  start_P=0, seasonal=True,
                                  d=None, D=1, trace=True,
                                  error_action='ignore',  # we don't want to know if an order does not work
                                  suppress_warnings=True,  # we don't want convergence warnings
                                  stepwise=True)  # set to stepwise

        # To print the summary
        stepwise_fit.summary()

        # Split data into train / test sets
        train = sales.iloc[:len(sales) - 12]
        test = sales.iloc[len(sales) - 12:]  # set one year(12 months) for testing

        # Fit a SARIMAX(0, 1, 1)x(2, 1, 1, 12) on the training set
        model = SARIMAX(train['numofsales'],
                        order=(0, 1, 1),
                        seasonal_order=(2, 1, 1, 12))

        result = model.fit()
        result.summary()

        start = len(train)
        end = len(train) + len(test) - 1

        # Predictions for one-year against the test set
        predictions = result.predict(start, end,
                                     typ='levels').rename("Predictions")

        # plot predictions and actual values
        #predictions.plot(legend = True)
        # todo: delete the following line, need more data in order to plot
        #print("predictions:")
        #print(predictions)
        #plt.figure(1)
        #plt.plot(train)
        #plt.plot(test)
        #plt.plot(predictions)
        #test['numofsales'].plot(legend = True)

        # Calculate root mean squared error
        # print("rmse:")
        # print(rmse(test['numofsales'], predictions))

        # Calculate mean squared error
        # print("mean_squared_error:")
        # print(mean_squared_error(test['numofsales'], predictions))

        # Train the model on the full dataset
        model = SARIMAX(sales['numofsales'],
                                order=(0, 1, 1),
                                seasonal_order=(2, 1, 1, 12))
        result = model.fit()

        # Forecast for the next 3 years
        forecast = result.predict(start=len(sales) - 1,
                                  end=(len(sales) - 1) + 3 * 12,
                                  typ='levels').rename('Forecast')
        print("!!!!!!!!!")
        print(forecast)
        print("!!!!!!!!!")
        print(sales['numofsales'])
        #forecast_result = pd.DataFrame([[forecast.index.values, forecast.values]], columns=['index', 'values'])
        #forecast_result.to_csv('forecast_result.csv')
        forecast_df = pd.DataFrame([forecast])
        forecast_df.to_csv('forecast_df.csv')

        # Plot the forecast values
        someVar = True
        plt.title('Sales Forecast - for the next three years:')
        sales['numofsales'].plot(figsize=(12, 5), legend=True)
        #plt.plot(forecast.index.values, forecast.values)
        #print(forecast.values)
        #print(forecast.index.values)
        forecast.plot(legend = True)
        plt.savefig('sales_pred.png')
        return plt.figure(1)
        #plt.figure(2)
        #plt.show()
        #d = DataFrame(np.array([forecast.index.values, forecast.values]))

print(run())

