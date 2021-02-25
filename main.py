counter = 1
while(counter <= 10):
  print(counter)
  counter += 1

#default start number is 0
for counter in range(11):
  print(counter)

print(" ")

#using a for loop, pring numbers 1-100 but only the evens
for counter in range (0, 101):
  if(counter%2 == 0):
    print(counter)

#OR
print(" ")

for counter in range (0, 101, 2):
  print(counter)