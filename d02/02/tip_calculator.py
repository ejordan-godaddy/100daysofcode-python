print('Welcome to the tip calculator')

total = input('What was the total bill? ')
perc_tip = input('What percentage tip would you like to give? 10, 12, or 15? ')
split = input('How many people are splitting the bill? ')

if int(perc_tip) not in (10,12,15):
    raise TypeError('Use the number dumbass')

amount = ( float(total) + (float(total) * int(perc_tip) / 100) ) / int(split)

print(f'Each person should pay: {round(amount, 2)}')
