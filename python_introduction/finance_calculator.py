
# Define variables, x,y, m and ym.
x = input("Enter your monthly income")
y = input("Enter your total monthly expenses")
a =int(x)
b= int(y)
m = a - b
ym = (m *12) + (m*12*0.05)
#Calculating savings and interest
print( "Your monthly savings are", m)
print("Projected savings after one year""," "with interest" "," "is", ym)
