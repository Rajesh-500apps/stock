
from flask import request
import yfinance
import datetime as dt
import matplotlib.pyplot as plt
import numpy as np


from flask import Flask ,request,jsonify
from flask_cors import CORS, cross_origin


app = Flask(__name__)  
app.config['CORS_HEADERS'] = 'application/json'
cors = CORS(app)


@app.route("/stock",methods=['POST'])
@cross_origin()
# Return line graph with 7 day support and resistance
def get_support_resistance():

    # Read user input
    start = request.form["start_date"]
    end = request.form["end_date"]
    name = request.form["stock_name"]
    interval = request.form["time_interval"]
    n = int(request.form["range"])

    # Get stock data
    ticker = yfinance.Ticker(name)

    # Get stock dataframe based on interval (like 1d,1h,15m)
    df = ticker.history(interval=interval, start=start, end=end)

    # Plot all high prices
    df['High'].plot(label='high')

    # Track Resistance or Support
    pivots = []
    pivot_range = [0 for i in range(n)]

    counter = 0

    # Track dates of corresponding pivots
    dates = []
    daterange = [0 for i in range(n)]

    # read dataframe and fetch Resistance or Support values
    for key in df.index:

        currentMax = max(pivot_range)
        value = round(df["High"][key], 2)

        pivot_range = pivot_range[1:9]
        pivot_range.append(value)
        daterange = daterange[1:9]
        daterange.append(key)

        s = np.mean(df['High'][key] - df['Low'][key])

        if currentMax == max(pivot_range):
            counter += 1
            if counter == 5:
                dateloc = pivot_range.index(currentMax)
                lastDate = daterange[dateloc]
                if np.sum([abs(currentMax-x) < s for x in pivots]) == 0:
                    pivots.append(currentMax)
                    dates.append(lastDate)

        else:
            counter = 0

    # Setup horizontal line for next 7 days
    timeD = dt.timedelta(days=7)

    # Get points to draw horizontal line
    for index in range(len(pivots)):
        plt.plot_date([dates[index], dates[index]+timeD],
                      [pivots[index], pivots[index]], linestyle='-', linewidth=2, marker=',', c='g', animated=False)

    #save plot graph
    plt.savefig('plot.png', dpi=300, bbox_inches='tight')

    plt.show()

    return "Success"


if __name__ =="__main__":  
    app.run(debug = True)