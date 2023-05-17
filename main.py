# This is a sample Python script.
import csv

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from faker import Faker
import csv
import pandas as pd

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # WRITE
    # output = open('myCSV.CSV', mode='w')
    #
    # mWriter = csv.writer(output)
    # header = ['name', 'age']
    # mWriter.writerow(header)
    #
    # data = ['Quang', 23]
    # mWriter.writerow(data)
    #
    # output.close()

    # WRITE FAKE DATA
    # output = open('data.CSV', 'w')
    # fakeData = Faker()
    # header = ['name', 'age', 'city', 'state', 'zip', 'lng', 'lat']
    #
    # mWriter = csv.writer(output)
    # mWriter.writerow(header)
    #
    # for r in range(1000):
    #     mWriter.writerow(
    #         [
    #             fakeData.name(),
    #             fakeData.random_int(min=18, max=80, step=1),
    #             fakeData.street_address(),
    #             fakeData.city(),
    #             fakeData.state(),
    #             fakeData.longitude(),
    #             fakeData.latitude()
    #         ]
    #     )
    # output.close()

    # READING CSVs
    # with open('data.CSV') as f:
    #     reader = csv.DictReader(f)
    #     headers = next(reader)
    #     print(headers)
    #     for row in reader:
    #         print(row['name'])


    # PANDAS
    df = pd.read_csv('data.CSV')
    print(df.head(10))
