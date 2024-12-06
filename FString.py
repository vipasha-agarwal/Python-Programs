letter='Hey my name is {} and I am from {}'
country="India"
name="Vipasha"
print(letter.format(name,country))


letter='Hey my name is {1} and I am from {0}'
country="India"
name="Vipasha"
print(letter.format(country,name))


print(f"Hey my name is {name} and I am from {country}")
print(f"Hey my name is {{name}} and I am from {{country}}")

txt="For only {price:.2f} dollars!"
print(txt.format(price=49.0999))

price=49.0999
txt=f"For only {price:.2f} dollars!"
print(txt)