# Web Traffic Transformation

This python script/program transforms web traffic data stored in time-record format where
each row is a page view into a per-user format where each row is a different user and the
columns represent the time spent on each of the pages.

The data set consists of 26 CSV files in an AWS S3 bucket. The files are named with lowercase
ascii letters (a.csv, b.csv. c.csv, ... z.csv). They can be accessed from the public root URL:
https://public.wiwdata.com/engineering-challenge/data/

The program uses pandas to read and manipulate the data and which requires pandas to be installed. Once start
running the program, the program will read in the 26 data files from the url, and the manipulation will be 
performed within the program. The url can be changed if the user want to perform the same transformation on another 
data set. The program will prompt user when the transformation is done. The program writes the 
result to a single csv file called "result.csv", which can be found within the same working directory. 