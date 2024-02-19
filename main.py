# dictionary for conversion
decode = {"·-": "A",
          "-···": "B",
          "-·-·": "C",
          "-··": "D",
          "·": "E",
          "··-·": "F",
          "--·": "G",
          "····": "H",
          "··": "I",
          "·---": "J",
          "-·-": "K",
          "·-··": "L",
          "--": "M",
          "-·": "N",
          "---": "O",
          "·--·": "P",
          "--·-": "Q",
          "·-·": "R",
          "···": "S",
          "-": "T",
          "··-": "U",
          "···-": "V",
          "·--": "W",
          "-··-": "X",
          "-·--": "Y",
          "--··": "Z",
          "-----": "0",
          "·----": "1",
          "··---": "2",
          "···--": "3",
          "····-": "4",
          "·····": "5",
          "-····": "6",
          "--···": "7",
          "---··": "8",
          "----·": "9",
          ' ': ' '}

encode = {decode[key]: key for key in decode}

# blank list to store result
result = []

# get user input
user_input = input('Enter text to translate to morse code: ')

# convert to morse code
for char in user_input.upper():
    if char in encode:
        result.append(f'{encode[char]} ')
# print result
print(f"Morse code output:\n"
      f"Input: {user_input}\n"
      f"Result: {''.join(result)}")
