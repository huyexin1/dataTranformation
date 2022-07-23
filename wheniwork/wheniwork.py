import string
import pandas as pd
import ssl


def data_merge(file_list):
    """Function -- Reads in a list of files and pivot the data to desired result,
    and writes result to a single csv file.
    Parameters:
        file_list -- a list of url to read data into dataframe
    """
    df = pd.DataFrame()
    for file in file_list:
        df_temp = pd.read_csv(file)
        df = pd.concat([df, df_temp])
    df.pivot(index='user_id', columns='path', values='length').to_csv("result.csv")


def main():
    files = []
    url_prefix = "https://public.wiwdata.com/engineering-challenge/data/"
    for letter in string.ascii_lowercase:
        file_name = url_prefix + letter + ".csv"
        files.append(file_name)
    data_merge(files)
    print("Process done, please look for file: result.csv")


if __name__ == "__main__":
    ssl._create_default_https_context = ssl._create_unverified_context
    main()
