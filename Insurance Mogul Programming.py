## Insurance Mogul Programming

import pandas as pd
import numpy as np
from scipy.stats import norm, chisquare, ttest_ind, ttest_1samp, pearsonr
import matplotlib.pyplot as plt
import csv
from collections import defaultdict

# Step 1: Load all data and load into array with headers for each datatype

file_name = "C:/Users/jcuzz_zici3uw/Desktop/School/PROGRAMMING/Super-awesome-315-final/DataRepository/imports-85.data"

no_qm = []

with open(file_name, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        # Clean each string in the row
        cleaned_row = [cell.replace('?', '') for cell in row]
        no_qm.append(cleaned_row)

def parse_data(data): 
    file = pd.DataFrame(data)    # Convert the cleaned list of lists to a DataFrame
    i_rating = file.iloc[:,0].tolist()
    n_risk = file.iloc[:,1].tolist()
    make = file.iloc[:,2].tolist()
    price = file.iloc[:,25].tolist()

    return i_rating, n_risk, make, price

i_rating, n_risk, make, price = parse_data(no_qm)

car_sets = list(zip(make, price, i_rating, n_risk)) 

make_c = defaultdict(int)
make_sum = defaultdict(int)
make_losses = defaultdict(int)
make_price = defaultdict(int)

for car in car_sets:
    make = car[0].strip().lower()
    try:
        rating = int(car[2])
        n_loss = int(car[3])
        c_price = int(car[1])
    except ValueError:
        continue

    make_c[make] += 1
    make_sum[make] += rating
    make_losses[make] += n_loss
    make_price[make] += c_price

i_rating_a = []
i_losses = []
car_prices = []

for make, count in make_c.items():
    i_rating_calc = make_sum[make] / count
    i_loss_calc = make_losses[make]/count
    car_price_calc = make_price[make]/count
    print(f"{make}: Insurance rating = {i_rating_calc:.4f}\n")
    print(f"{make}: Insurance Losses, Normalized = {i_loss_calc:.2f}\n ")
    print(f"{make}: Car Price = {car_price_calc:2f}\n ")
    i_rating_a.append(i_rating_calc)
    i_losses.append(i_loss_calc)
    car_prices.append(car_price_calc)

    
make_c_l = list(make_c)
## Basic Bar
plt.bar(make_c_l, i_rating_a)
plt.xticks(rotation=90)
plt.xlabel("Make")
plt.ylabel("Average Insurance Rating")
plt.title("Average Insurance Rating for Make")
plt.show()

## Dual Plot, Risk rating + Losses
fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('Make')
ax1.set_ylabel('Insurance Risk Rating', color=color)
ax1.bar(make_c_l, i_rating_a, color=color)
ax1.tick_params(axis='y', labelcolor=color)
ax1.axhline(0, color='black', linewidth=1)

ax2 = ax1.twinx()

color = 'tab:blue'
ax2.set_ylabel('Average Insurance Losses, Normalized', color=color) 
ax2.stem(make_c_l, i_losses, bottom = 121)
ax2.tick_params(axis='y', labelcolor=color)

ax1.tick_params(axis="x", rotation= 90)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.title("Insurance Risk Rating vs. Insurance Company Normalized Losses")
plt.show()

## Dual Plot, Losses + Price
fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('Make')
ax1.set_ylabel('Insurance Normalized Losses', color=color)
ax1.bar(make_c_l, i_losses, color=color)
ax1.tick_params(axis='y', labelcolor=color)
ax1.axhline(0, color='black', linewidth=1)


ax2 = ax1.twinx()

color = 'tab:blue'
ax2.set_ylabel('Prices', color=color) 
ax2.scatter(make_c_l, car_prices, s=40, color = color)
ax2.tick_params(axis='y', labelcolor=color)

ax1.tick_params(axis="x", rotation= 90)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.title("Insurance Losses vs. Price")
plt.show()

## Dual Plot, Risk Rating vs Price
fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('Make')
ax1.set_ylabel('Insurance Rating Risk', color=color)
ax1.bar(make_c_l, i_rating_a, color=color)
ax1.tick_params(axis='y', labelcolor=color)
ax1.axhline(0, color='black', linewidth=1)
ax1.yaxis.set_inverted(True)

ax2 = ax1.twinx()

color = 'tab:blue'
ax2.set_ylabel('Prices', color=color) 
ax2.stem(make_c_l, car_prices, bottom =24500)
ax2.tick_params(axis='y', labelcolor=color)

ax1.tick_params(axis="x", rotation= 90)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.title("Insurance Risk Rating vs. Price")
plt.show()

correlation, p_value = pearsonr(i_losses, i_rating_a)

print(f"The Pearson Correlation p_value is {p_value:.4f}")
if p_value > 0.05:
    print("The correlation is not statistically significant")
else: 
    print("The correlation is statistically significant")


"""
  1. symboling:                -3, -2, -1, 0, 1, 2, 3.
  2. normalized-losses:        continuous from 65 to 256.
  3. make:                     alfa-romero, audi, bmw, chevrolet, dodge, honda,
                               isuzu, jaguar, mazda, mercedes-benz, mercury,
                               mitsubishi, nissan, peugot, plymouth, porsche,
                               renault, saab, subaru, toyota, volkswagen, volvo
  4. fuel-type:                diesel, gas.
  5. aspiration:               std, turbo.
  6. num-of-doors:             four, two.
  7. body-style:               hardtop, wagon, sedan, hatchback, convertible.
  8. drive-wheels:             4wd, fwd, rwd.
  9. engine-location:          front, rear.
 10. wheel-base:               continuous from 86.6 120.9.
 11. length:                   continuous from 141.1 to 208.1.
 12. width:                    continuous from 60.3 to 72.3.
 13. height:                   continuous from 47.8 to 59.8.
 14. curb-weight:              continuous from 1488 to 4066.
 15. engine-type:              dohc, dohcv, l, ohc, ohcf, ohcv, rotor.
 16. num-of-cylinders:         eight, five, four, six, three, twelve, two.
 17. engine-size:              continuous from 61 to 326.
 18. fuel-system:              1bbl, 2bbl, 4bbl, idi, mfi, mpfi, spdi, spfi.
 19. bore:                     continuous from 2.54 to 3.94.
 20. stroke:                   continuous from 2.07 to 4.17.
 21. compression-ratio:        continuous from 7 to 23.
 22. horsepower:               continuous from 48 to 288.
 23. peak-rpm:                 continuous from 4150 to 6600.
 24. city-mpg:                 continuous from 13 to 49.
 25. highway-mpg:              continuous from 16 to 54.
 26. price:                    continuous from 5118 to 45400."""
