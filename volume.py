def volumeCube(length):
  length = float(length)
  return length * length * length

def main(length):
  if length.isdigit() == True:
    return volumeCube(length)
  else:
    return "Error"
