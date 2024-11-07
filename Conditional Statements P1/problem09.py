# 9. Take three sides of a triangle as input and check if they form a valid triangle. There are many types of triangls and in the given case it is equilitery triangle whose two sides are equivalent to the third side also.
s1= int(input("Enter first side of triange: "))
s2= int(input("Enter second side of triangle: "))
s3= int(input("Enter third side of triangle: "))
if  s1==s2==s3:
    print("The given sides form an equilateral triangle.")
else:
    print("The given sides do not form an equilateral triangle.")