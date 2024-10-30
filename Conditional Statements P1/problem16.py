# 16. Take the length of three sides and classify the triangle (equilateral(all side equal), isosceles(two side equal), or scalene(All three sides in different lengths)).
s1 = int(input("Enter first side of the triangle : "))
s2 = int(input("Enter second side of the triangle : "))
s3 = int(input("Enter third side of the triangle : "))
if s1==s2==s3:
    print("The triangle is equilateral.")
elif (s1 == s2 and s2 == s1) or (s2==s3 and s3==s2) or (s3==s1 and s1==s3):
    print("The triangle is isosceles.")
else:
    print("The triangle is scalene.")