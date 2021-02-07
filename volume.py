def volumeCube(length):
  length = float(length)
  return length * length * length

while True:
  l = input("Enter the cube's length: ")
  if l.isdigit() == True:
    print("The volume is:", volumeCube(l))
    break;
  else:
    print("Please enter a positive integer or decimal.")
