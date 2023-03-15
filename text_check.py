raw_rude = open("text check/rude.txt", "r")

rude = []

for line in raw_rude:
  rude.append(line)

def check(text):
  text.lower()
  for i in rude:
    if i in text:
      return False
    else:
      continue
  return True