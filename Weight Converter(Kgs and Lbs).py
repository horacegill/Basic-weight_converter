
# static conversion
CONVERT = 0.45

# check for errors
try:
    weight = int(input("Weight: "))
except ValueError:
    print("Weight must be an integer!")
    exit(1) # exit gracefully

unit = input("(K)gs or (L)bs: ")
if unit.lower().startswith("k"):
    converted =  weight / CONVERT
    print(f"Weight in lbs: {converted}")
else:
    converted = weight * CONVERT
    print(f"Weight in kgs: {converted}")
