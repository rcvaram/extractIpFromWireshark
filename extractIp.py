def checkLine(line):
  words = line.split()
  ip_addresses = []
  for word in words:
    value_check = True
    address = word.split(".")
    if len(address) == 4:
      for digit in address:
        try:
          if 0 > int(digit) or 255 < int(digit):
            value_check = False
        except ValueError as e:
          value_check = False
    else:
      value_check = False
    if value_check:
      ip_addresses.append(word)

  return ip_addresses


with open("wireShark.txt", "r") as file:
  for line in file:
    result = checkLine(line)
    if len(result) == 2:
      with open("ipAddress.txt", "a") as f:
        f.write("Source Destination {} {} \n".format(result[0], result[1]))
        f.close()
file.close()
