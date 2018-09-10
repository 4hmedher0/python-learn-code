import winsound
print('\t WELCOME TO EVEN-ODD GAME \t')
print("x if you want 2 end game")
#bo=True
while(True):
 num=input("Enter number ")
 if num=='x' or num=='X':
     print("close Game")
     #print('\tGAME OVER')
     #bo=False هيكمل دورة للوب كاملة ثم يخرج 
     break # هيخرج من اللوب مباشرة قبل مايكمل 
 try:    
   num=int(num)    
   if num % 2 == 0 :
         print('even')
   else:
         print('Odd')
 except ValueError:
     print("enter vaild input")
     winsound.Beep(800,300)

     print("_______________________________")
print('\tGAME OVER')
winsound.PlaySound('sound.wav',winsound.SND_FILENAME)
