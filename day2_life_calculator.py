# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
daysPassed = int(age) * 365
weeksPassed = int(age) * 52
yearsPassed = int(age)

expctd_life_days = 90 * 365
expctd_life_weeks = 90 * 52
expctd_life_years = 90 

leftDays = expctd_life_days - daysPassed
leftWeeks = expctd_life_weeks - weeksPassed
leftYears = expctd_life_years - yearsPassed

print(f"You have {leftDays} days, {leftWeeks} weeks, {leftYears} years")










