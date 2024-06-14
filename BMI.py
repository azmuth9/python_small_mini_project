print('Welcome to BMI calculator')

w = int(input('What is your weight in kg : '))
h = float(input('What is your height in m : '))

result = w / h**2
final_rersult = round(result, 2)
print('You are BMI is', final_rersult)

if result < 18.5:
  print('You are underweight.')
elif result > 18.5 and result < 25:
  print('You are normal weight.')
elif result > 25 and result < 30:
  print('You are slightly overweight.')  
elif result > 30 and result < 35:
  print('You are obese.')
else:
  print('You are clinically obese.')
