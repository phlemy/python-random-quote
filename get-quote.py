import random
def primary():
  
  f = open("quotes.txt")
  quotes = f.readlines() # quotes is an array of lines
  f.close()

  last = len(quotes) - 1
  rnd1 = random.randint(0,last)
  rnd2 = random.randint(0,last)
  while rnd2 == rnd1:
   rnd2 = random.randint(0,last)
  rndQuote1=quotes[rnd1]
  rndQuote2=quotes[rnd2]

  print(rndQuote1[0:len(rndQuote1)-1], rndQuote2[0:len(rndQuote2)-1], end=" -- ")
  
if __name__== "__main__":
  primary()
