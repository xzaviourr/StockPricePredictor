# Stock Price Prediction Using Stock Correlation and Advanced Feature Generation
Stock market price prediction model trained using historical data of 12 stocks, using correlation factor and advanced feature generation. 

## Selected Stocks
- Banking sector
    - SBIN
    - HDFCBANK
    - AXISBANK
- Pharmaceutical sector
    - SUNPHARMA
    - DRREDDY
    - CIPLA
- Information technology sector
    - INFY
    - WIPRO
    - TCS
- Energy sector
    - BPCL
    - COALINDIA
    - POWERGRID
- Target stock for price prediction : SBIN

## Methodology
Our model can be broken down into following major parts -
- Input feature generation
- Preprocessing of the new found features
- Finding correlation between various stocks
- Building custom optimizer taking into consideration correlation values
- Designing structure of RNN
- Training of RNN

### **Input Feature Generation**
- Using feature engineering, we are looking for several methods
that can act as individual prediction models for predicting the
stock price. Furthermore using these predictions as the custom
built features into our main RNN model.
- First we break down the data into chunks of 30 days, to convert
it into time series data.
    - These individual chunks of data are passed onto various
    polynomial regression models with variable degrees,
    which returns a vector of predicted price of the next day
    by all the models. Polynomial degrees are chosen in a
    manner to diversify the possible predicted values by
    taking degrees that lead to some under-fitted, balanced
    and overfitted models.
    - These individual chunks of data are passed onto a curve
    similarity model that tries to find the similarity of the
    current curve, with curves obtained from the historical
    data of all the stocks used for training. To keep this model
    balanced, curve lengths are taken in a range starting from
    5 days going upto 30 days to take in account the effect of
    long term and short term movements in the stock.
- These 2 techniques generate nearly 10-15 new features that
will be passed further onto the RNN model.
- Other commonly used features like Moving average,
Exponential moving average, etc of various ranges are also
used for the RNN model.

### **Preprocessing of the features**
Features need to be normalized, and scaled in order to
generate meaningful results from the models.

### **Finding correlation between stocks**
This idea is based on the effect of one stock on another. To
train a specialized model for prediction of price for a particular
stock, data of only that stock can be used. But we have taken
into consideration that every stock depends on other stocks and
hence the same correlation can be seen in their stock prices. If
this correlation can be taken into consideration, then we can
use data of other stocks as well, weighted with their correlation
values to train a partial generalized model that has the
possibility of generating better results. This generalization can
be balanced by taking appropriate normalized weight for the
correlation values of all the stocks, and hence keeping a
variable ratio in the range of 40-90% between the effect of the
selected stock, and all other stocks.


### **Building custom optimizer taking into consideration the correlation values**
- Custom gradient descent function is being created to bring in
the effect of correlation values of all the stocks while modifying
the weights of RNN in backpropagation.
- During backpropagation, instead of taking a simple average of
all the weight gradients, weighted average using correlation
values of weight gradients is taken to update the weights.

### **Designing and training of RNN**
We are experimenting with various RNN structures and
hyperparameters to generate the best results of the program,
taking RMSE as loss function.