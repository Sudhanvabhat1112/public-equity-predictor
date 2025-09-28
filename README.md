# public-equity-predictor


the readme file is for me only


file #1 = fetch_features = it pulls financial indicators from alpha vantage api and puts it in a csv file
file#2= alphabet_stock_analysis.csv = the csv file
file #3= Predictor.ipynb = predicts high for alphabet by using multiple ml models and then the accuracies of these models are compared
file #4= gitignore = to ignore the .env file


file#1
1.api key is stored in a variable (the api key is stored in an env file which is basically a txt file)
2.take the input of the ticker name (company stock name on nasdaq or any other stock exchange)
3.take parameters for financial indicators( they are of dictionary datatype)
4.time period for ema,dema is 14 days because the multiplier value would be very little so the most recent high would highly influence your high
5. .get is used to get the info from the api , the api call uses parametr and url 
6. the values of financial indicators are stored in a dictionary , the dates are extracted fromn one of the indicators
7.unlike dema,ema,cci... high values are not single key value when we're using time series  it returns high,low,open,close so to access only high we use high_price = float(daily_data["2. high"])
8. stock[0] would contain all financial indicator values of the latest day
9. these values are stored in a dataframe and then into a csv file


file #3
1.i read the csv file put the data into a dataframe, checks its shape(size), check if there are any null values( by using .info to know more info on datatypes as well)
2. i use .describe to check for outliers or to have an idea of how my data is spread, .t to transpose it so that i can read it more easily
3.use pairplot to see relation between everything (.set sets default values)
4.im going through every single column (financial idnicators) and plotting it as a distribution plot with figsize i set the size of the plot and 
    plt.title(f"{col}", size=15) i set the size of title
5.find correlation between everything then plot it as a heatmap. annot=true puts the correlation value on top of colours, fmt sets no of decimal points, 
6. x has values of all indicators , y has high value of alphabet , train test dataset is split, test_dates = df.loc[X_test.index, 'Date']  takes dates of the the test dataset  x-test.. is the index and date is the key you want and .loc is used to get data from labels
7.i train the models =linear regression,ridge regression, lasso regression, gradient boosting and random forest. the same data set is used for training and testing. i find each models r2 score
i plot its accuracies on a bar plot
8.for more accurate data representation i plotted the ml model values and date values side by side to know where certain models are having difficulty, alpha=0.85 is for transparency, .xticks rotation =45 to rotate date by 45 degrees for better visiblity
