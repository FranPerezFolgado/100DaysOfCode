#import csv
#
#with open('Day25/weather_data.csv') as weather_data:
#    data = csv.reader(weather_data,)
#    print(data)
#    temperatures = []
#    for row in data:
#        if row[1] != 'temp': 
#            temperatures.append(int(row[1]))
#        print(row)
#    
#    print(temperatures)
import pandas

data = pandas.read_csv('Day25/weather_data.csv')
data_dict = data.to_dict()
print(data_dict)

temp_list = data['temp'].to_list()
print(temp_list)

print(data['temp'].mean())
print(data['temp'].max())
print(data[data.temp == data.temp.max()].temp)

monday = data[data.day == 'Monday'].temp
farenheit = int(monday) * 1.8 + 32
print(farenheit)

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

scores = pandas.DataFrame(data_dict)
print(scores)
scores.to_csv('Day25/new_data.csv')