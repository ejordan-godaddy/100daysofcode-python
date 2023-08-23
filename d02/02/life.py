d_year = 365
w_year = 52
m_year = 12

age = input("What is your current age? ")
age_diff = 90 - int(age)

days = age_diff * d_year
weeks = age_diff * w_year
months = age_diff * m_year


print(f'You have {days} days, {weeks} weeks, and {months} months left')
