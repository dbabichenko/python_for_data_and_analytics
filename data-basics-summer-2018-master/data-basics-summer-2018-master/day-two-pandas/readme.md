# Data Processing with Python and Pandas


This directory contains the content for day two of the Data Basics workshop. 


## Topics

* High level introduction to Pandas. What *is* it, why does it exist, situating it within the Python Data Science ecosystem. Quick demo of something pandasy. 
* Introduce the Pandas data structures: Series, Dataframe, Index - iloc vs. loc. . 
* Reading files into dataframe - from memory from disk and the web. read_csv. delimitors. show shift-tab. relative vs. absolute paths.
* Exploring and summarizing data - head, describe, sample. shape. mean. value_counts. sum. median. std. var. etc. dtypes.
    * EXERCISE - Analyzing PGH tree data with descriptive statistics.  
        * What is the average height and width of PGH trees.
        * ON what street is the tallest tree?
        * In what neighborhood is the widest tree?
* Making plots to see what your data look like -   1D data - histogram. 2D data - bar.line. scatter plot. time series?
    * EXERCISE - Plotting fake stock market data. 
        * Make a histogram for each stock
        * Make a line chart of the stock value over time.
* Split Apply Combine. groupby. 
    * EXERCISE - 311 Data. Tree data.  
        * What neightborhood complains the most?
        * What is the tallest type of tree in pittsburgh on average?
* Working with dates and times. Reading columns as datetimes. Datetime indexes. Resampling.
* Querying and subsetting - Masking. Variables 
    * EXERCISE - time indexing and subsetting data and visuzlaing that subset 
        * Create a sub dataset of just the potholes in a neighborhood
        * Create a plot of number of pothole complaints per month of that data subset





### Pandas Sugar

* discretizing contiuous data - cut 

* Reshaping data with Pivot and pivot tables and stacking
* Merging datasets into a sigle dataframe. Merge, Join, Concat
* Transformation - vectorized functions. Vectorized string operations. apply?
    * EXERCISE - Recipe database example
* Working with Missing data - dropna and fillna
