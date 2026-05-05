'''
Author: Sammy Nelms

What/which geometric features can affect the mpg of the cars and in what ways?

This file will calculate then needed metrics to answer the given question.
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv


def parse_data(file):
    data = []

    with open(file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            # Clean each string in the row
            cleaned_row = [cell.replace('?', '') for cell in row]
            data.append(cleaned_row)

    data = pd.DataFrame(data)  # Convert the cleaned list of lists to a DataFrame

    data = data.rename(columns={0: 'symboling',
                                1: 'normalized_losses',
                                2: 'make',
                                3: 'fuel_type',
                                4: 'aspiration',
                                5: 'num-of-doors',
                                6: 'body-style',
                                7: 'drive-wheels',
                                8: 'engine_location',
                                9: 'wheel_base',
                                10: 'length',
                                11: 'width',
                                12: 'height',
                                13: 'curb_weight',
                                14: 'engine_type',
                                15: 'num_of_cylinders',
                                16: 'engine_size',
                                17: 'fuel_system',
                                18: 'bore',
                                19: 'stroke',
                                20: 'compression_ratio',
                                21: 'horsepower',
                                22: 'peak_rpm',
                                23: 'city_mpg',
                                24: 'highway_mpg',
                                25: 'price'})  # Rename columns for clarity
    return data

# Print out the given Question
question = "What/which geometric features can affect the mpg of the cars and in what ways?"

print()
print(f'The question is "{question}"')
print()


# Pull the data with our awesome function
file_name = r"C:\Users\nelms\OneDrive - James Madison University\ENGR 315\Super-awesome-315-final\DataRepository\imports-85.data"
data = parse_data(file_name)

city_mpg = data['city_mpg'].astype(float)
highway_mpg = data['highway_mpg'].astype(float)


# Calculate the density of each car
length = (data['length'].astype(float)) / 12  # feet
width = (data['width'].astype(float)) / 12  # feet
height = (data['height'].astype(float)) / 12  # feet
mass = data['curb_weight'].astype(float)  # pounds
data['density'] = mass / (length * width * height) # calculate and add to data frame

# Pull some data to use
city_mpg = data['city_mpg'].astype(float)
highway_mpg = data['highway_mpg'].astype(float)
density = data['density'].astype(float)
price = pd.to_numeric(data['price'], errors='coerce')
body_style = data['body-style'].astype(str)


'''
Graph the relationship between density and city mpg in blue and the relationship between density and highway mpg in red
'''
plt.figure(figsize=(8, 6))
plt.scatter(density, city_mpg, color='blue', label='City MPG')
plt.scatter(density, highway_mpg, color='red', label='Highway MPG')

# Calculate the trendline (degree 1 for linear)
z = np.polyfit(density, city_mpg, 1)
p = np.poly1d(z)
plt.plot(density, p(density), color='blue', linestyle='--', label='City MPG Trend')
z = np.polyfit(density, highway_mpg, 1)
p = np.poly1d(z)
plt.plot(density, p(density), color='red', linestyle='--', label='Highway MPG Trend')

plt.title('Density vs MPG')
plt.xlabel('Density (lb/ft^3)')
plt.ylabel('MPG')
plt.legend()
plt.show()


'''
Graph the relationship between density and price
'''
plt.figure(figsize=(8, 6))
plt.scatter(density, price, color='green')
plt.title('Density vs Price')
plt.xlabel('Density (lb/ft^3)')
plt.ylabel('Price ($)')
plt.show()


'''
Bar graph of body type vs city mpg and highway mpg
'''
body_list = body_style.unique() # get the list of bodies

x = np.arange(len(body_list)) # set the lenght of x axis values
width = 0.35 # random width for the bars

city_mpg = []
highway_mpg = []

plt.figure(figsize=(8, 6))
for body_style in body_list:
    body_style_data = data[data['body-style'] == body_style] # get data for current style
    city_mpg.append(body_style_data['city_mpg'].astype(float).mean())
    highway_mpg.append(body_style_data['highway_mpg'].astype(float).mean())

# Plot actual bars for city and highway mpg
plt.bar(x - width/2, city_mpg, width, label='City MPG', color='blue')
plt.bar(x + width/2, highway_mpg, width, label='Highway MPG', color='red')

# make all the stuff for the graph
plt.title('Body Type vs MPG')
plt.xlabel('Body Type')
plt.ylabel('MPG')
plt.xticks(x, body_list)
plt.legend()
plt.tight_layout()
plt.show()
