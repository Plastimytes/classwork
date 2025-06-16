while True:
 reply = input('Enter text:')
 if reply == 'stop': break
 print(reply.upper())

##Example2:Math and user inputs
while True:
 ans = input('Enter text:')
 if ans == 'stop': break
 print(int(ans) ** 2)
print('Bye')

##Example 3: Nesting Code Three Levels Deep
while True:
 reply = input('Enter text:')
 if reply == 'stop':break
 elif not reply.isdigit():
  print('Bad!' * 8)
 else:
  num = int(reply)
 if num < 20:
  print('low')
 else:
  print(num ** 2)
print('Bye')

