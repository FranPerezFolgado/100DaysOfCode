import pandas

CSV_INPUT_PATH = 'Day25/squirrel_census/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv'
CSV_OUTPUT_PATH = 'Day25/squirrel_census/2018_squirrel_census.csv'

def count_color(input_data, color):
    #return input_data[input_data['Primary Fur Color'] == color]['Primary Fur Color'].count()
    return len(input_data[input_data['Primary Fur Color'] == color])

input_data = pandas.read_csv(CSV_INPUT_PATH)


grey_count = count_color(input_data=input_data, color='Gray')
red_count = count_color(input_data=input_data, color='Cinnamon')
black_count = count_color(input_data=input_data, color='Black')

output_data= {
    'Fur Color' :['grey', 'red', 'black'],
    'Count':[grey_count,red_count,black_count]
}
pandas.DataFrame(output_data).to_csv(CSV_OUTPUT_PATH)