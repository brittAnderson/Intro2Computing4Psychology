import requests
import zipfile
import pandas as pd

def pandas_function():
    url = "http://openpsychometrics.org/_rawdata/HSQ.zip"
    download_data(url)
    pandas_data = pd.read_csv("./HSQ/data.csv")
    print_columns(pandas_data)
    print("The length of one of the rows is: "
          + str(len(pandas_data['Q1'])) + "\n")
    print_mean(pandas_data.copy(), 'Q15', 'age')

def download_data(url):
    request = requests.get(url)
    filename = url.split("/")[-1]
    with open(filename, 'wb') as output_file:
        output_file.write(request.content)

    with zipfile.ZipFile('./HSQ.zip', 'r') as zip_ref:
        zip_ref.extractall('.')

def print_columns(data):
    print("The names of the columns are:\n")
    for column in data.columns:
        print(column)
    print("\n")

def print_mean(data, column, sort_by):
    ages = [20,21,22,23,24,25]
    data_within_ages = data[data[sort_by].isin(ages)]
    
    print("The mean of Q15 for participants ages 20-25 is: "
          + str(data_within_ages[column].mean()))

if __name__ == "__main__":
    pandas_function()
