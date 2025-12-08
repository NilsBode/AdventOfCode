import pandas as pd


def product(list):
    product = 1
    for i in list:
        product *= i
    return product


def read_data(fname):
    file = open(fname)
    data = file.readlines()
    file.close()
    df = pd.read_csv(fname, delim_whitespace=True, header=None)
    transposed_df = df.transpose()
    transposed_df.rename(columns={0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'method'}, inplace=True)
    transposed_df = transposed_df.astype({'a': 'string', 'b': 'string', 'c': 'string', 'd': 'string', 'method': 'string'})
    print(transposed_df.dtypes)
    sums = transposed_df.loc[transposed_df['method'] == "+"].sum(axis=1, numeric_only=True).sum()
    products = transposed_df.loc[transposed_df['method'] == "*"].prod(axis=1, numeric_only=True).sum()
    print(sums + products)


def read_data_part2(name):
    file = open(name)
    data = file.readlines()
    file.close()
    return data

def do_calc(data):
    results = []
    number_array = []
    counter = 0
    for i in range(len(data[0])-1, -1, -1):
        new_number = ""
        for j in range(len(data)-1):
            new_number += data[j][i]

        if new_number == '    ':
            if data[j+1][i+1] == "+":
                results.append(sum(number_array))
            elif data[j+1][i+1] == "*":
                results.append(product(number_array))
            else:
                print("Keine Rechnung")
            number_array = []

        elif new_number != '\n\n\n\n':
            print(new_number)
            try:
                number = int(new_number.replace("\n", ""))
                number_array.append(number)
            except:
                print("Fehler")

    if data[j+1][i] == "+":
        results.append(sum(number_array))
    elif data[j+1][i] == "*":
        results.append(product(number_array))
    else:
        print("Keine Rechnung")


    print(sum(results))


if __name__ == '__main__':
    data = read_data_part2('input/day6.txt')
    do_calc(data)