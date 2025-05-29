#y=mx+c

#4x-5y+33=0
#5y=4x+33
#y=(4/5)x+(33/5)

#20x-9y-107=0
#20x=9y+107
#x=(9/20)y+(107/20)

#b_yx = 4/5 --------------(m1)
#b_xy = 9/20 --------------(m2)

#b_yx*b_xy = r**2
#r = (b_yx*b_xy)**0.5
#r = ((4/5)*(9/20))**0.5

#b_yx = r * (sigma_y/sigma_x)
#sigma_y = b_yx*sigma_x / r
#sigma_y = b_yx*sigma_x / (b_yx*b_xy)**0.5
sigma_y = (4/5) * 3 / (((4/5)*(9/20))**0.5)
variance = sigma_y**2

print(round(variance, 1))

#r/b_xy = sigma_y / sigma_x
#sigma_y = r*sigma_x/b_xy

#sigma_y = (b_yx*b_xy)**0.5 * sigma_x / b_xy    # Both formulas gives same answer.
#sigma_y = (((4/5)*(9/20))**0.5) * 3 / (9/20)
#variance = sigma_y**2
#print(round(variance, 1))
