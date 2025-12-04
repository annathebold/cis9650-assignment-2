# Assignment 2
### Author: Anna Bold, 24761366
### Date: 12/3/25

## Project Overview
This project reads a file named 'stock_data_july_to_september.csv', which details the stock data for 5 different stocks from July to September of 2025. The stocks contained within the file are Apple, Goolge, Microsoft, Nvidia and Oracle. 

## Project Structure 
This project was made using Python with NumPy and Pandas. Ahead of running the code, please import those libraries. 

The following functions are contained within the code:
*read_ohlcv*: This function reads and parses the data file.
*stock_summary*: This function pulls the highest and lowest values of a particular stock. 
*technical_analysis*: This function finds the 30 day simple moving average, the 30 day exponential moving average, the three month return and the standard deviation of daily returns for any given stock.
*stock report*: This function presents the data from the data file. 

## Assumptions
For this project, these are the assumptions:
* The user already has the data file with the name 'stock_data_july_to_september.csv' present on their computer.
* The data file contains "High" and "Low" data, and is not missing partial data. 

## Conclusion
From running this program, the user will be able to understand the change in stock prices over a time period of 30+ days. This program can be adapted for other stocks in this time period as long as the file name remains consistent, or can have the file name within the code modified to be applicable to other time periods. As a next step, creating a function that can parse any file, regardless of name, will help make the program more broadly applicable.

## Thanks for reading! 
