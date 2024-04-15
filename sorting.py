import os
import csv


def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)


    data = {}
    with open(file_path,mode= 'r',  newline= '') as csvfile:
        csv_read = csv.reader(csvfile)
        headers = next(csv_read)


        #pre kazdy stlpec prazdny zoznam v datovom slovniku
        for header in headers:
            data[header] = []

        for row in csv_read:
            for i, value in enumerate(row):
                data[headers[i]].append(float(value))

    return data


def selection_sort(zoznam, direct = 'desc'):
    for i in range(len(zoznam)):
        min_idx = i
        max_idx = i
        for j in range(i+1, len(zoznam)):
            if direct == 'asc':
                if zoznam[j] < zoznam[min_idx]:
                    min_idx = j
            else:
                if zoznam[j] > zoznam[max_idx]:
                    max_idx = j
        if direct == 'asc':
            (zoznam[i], zoznam[min_idx]) = (zoznam[min_idx], zoznam[i])
        else:
            (zoznam[i], zoznam[max_idx]) = (zoznam[max_idx], zoznam[i])

    return zoznam



def main():
    #pass
    file_name = 'numbers.csv'
    data = read_data(file_name)
    data1 = data['series_1']
    sel_sort = selection_sort(data1)
    print(sel_sort)
    #print(data)


if __name__ == '__main__':
    main()
