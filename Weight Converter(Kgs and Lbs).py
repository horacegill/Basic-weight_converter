weight = int(input("Weight: "))
unit = input("(K)gs or (L)bs: ")
if unit.upper() == "K":
    converted =  weight / 0.45
    print("Weight in (L)bs "+ str(converted))
else:
    converted = weight * 0.45
    print("Weight in (K)gs "+ str(converted))
