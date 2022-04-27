def hight(bmi="weight/hight2"):
    if bmi<=18.5:
        return ("under weight")
    if bmi<=25.0:
        return ("normal")
    if bmi<=30.0:
        return ("over weight")
    if bmi>30:
        return ("obese")
z=hight(30)
print(z)
