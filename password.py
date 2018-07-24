passwordFile = open('SecretPasswordFile.txt')
secretPassword = passwordFile.read().strip("\n")
print('Enter your password.')
typedPassword = input()

if typedPassword == secretPassword:
   print('Access granted!')
   if typedPassword == '1234':
       print('That password is one that an idiot puts on their luggage.')
else:
    print('Access denied!')
