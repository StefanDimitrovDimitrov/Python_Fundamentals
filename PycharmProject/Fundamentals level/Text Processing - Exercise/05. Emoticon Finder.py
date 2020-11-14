text = input()

for i,t in enumerate(text):
   if t == ":" and i+1 < len(text):
      print(f":{text[i+1]}")