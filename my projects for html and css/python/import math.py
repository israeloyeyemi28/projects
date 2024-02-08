import math
radius = int(input("what is the radius of the circle :"))

l_o_a_c = int(input("what is the angle of the circle :"))

for_area = radius*3.142**2
print(f"the area is :{for_area}")
for_arc = l_o_a_c/360 *2*math.pi*radius
print(f"the lenght of an arc is :{for_arc}")

   