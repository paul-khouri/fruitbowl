name = "Harold"
age = 16
school = "Rongotai"
assets = 14

output ='''My name is {:^10} and I am {:<6} years old 
and my school is {:>13}, 
I have ${:.2f} in my account
        '''.format(name, age, school, assets)

print(output)

