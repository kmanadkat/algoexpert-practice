keypad = {
  "1": [],
  "2": ['a', 'b', 'c'],
  "3": ['d', 'e', 'f'],
  "4": ['g', 'h', 'i'],
  "5": ['j', 'k', 'l'],
  "6": ['m', 'n', 'o'],
  "7": ['p', 'q', 'r', 's'],
  "8": ['t', 'u', 'v'],
  "9": ['w', 'x', 'y', 'z'],
  "0": [],
}


def phoneNumberMnemonics(phoneNumber):
  if len(phoneNumber) == 0:
    return [""]

  recAns = phoneNumberMnemonics(phoneNumber[1:])
  firstDigit = phoneNumber[0]
  output = []

  if firstDigit == "1" or firstDigit == "0":
    for element in recAns:
      output.append(firstDigit + element)
    
  else:
    for element in keypad[firstDigit]:
      for entry in recAns:
        output.append(element + entry)
    
  return output


print(phoneNumberMnemonics("1905"))