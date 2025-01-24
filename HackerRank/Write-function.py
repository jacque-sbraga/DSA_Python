def is_leap(year):
      leap = False

      # Write your logic here
      if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)): 
            leap = True

      
      return leap

print(is_leap(2024))
print(is_leap(2000))
print(is_leap(2400))
print(is_leap(1800))
print(is_leap(1900))
print(is_leap(2100))
print(is_leap(2200))
print(is_leap(2300))
print(is_leap(2500))


print(2100 % 400)

