x = 'killer rabbit'
if x == 'roger':
 print("shave and a haircut")
elif x == 'bugs':
 print("what's up doc?")
else:
 print('Run away! Run away!')

#While loops
x = 10
while x:
 x -= 1
 if x % 2 != 0: continue # Odd? -- skip print
 print(x, end=' ') 
