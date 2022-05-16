class DataSet:
    out = []
class Userinput:
    def user(self):
        for i in range(1, 11):
            distance = float(input("Enter Distance in KM:"))
            time = float(input("Enter Time Taken in Hrs:"))
            DataSet.out.append([distance, time])
class Measure:
    def measure(self):
        a = DataSet.out
        for item in a:
            item.append(item[0]/item[1])
class ShowResults:
    def display(self):
        for item in DataSet.out:
            print(item)

obj1 = Userinput()
obj1.user()
obj2 = Measure()
obj2.measure()
obj3 = ShowResults()
obj3.display()



import csv
data = ['distance', 'time', 'speed']
res = DataSet.out
file = open('sample.csv', 'w')
file1 = csv.writer(file)
file1.writerow(data)
file1.writerows(res)
file.close()