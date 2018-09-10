from random import *
import winsound
print("\tXxxX WELCOME TO CAVE OF GHOSTS XxxX\nthe GHOST HIDDEN BEHIND 3 DOORS OPEN THEM CAUTIOLY TO PASS FROM CATCH THE GHOST\ntoExit press X")
score=0
while(True):
  choose =input("\t ENTER THE NUMBER OF DOOR : ")
  if choose =='x' or choose=='X':
      print("closing Game .....")
      break
  try:
     choose=int(choose)
     if choose>=4 or choose<=0:
       print("enter valid Value 1:3")
       winsound.Beep(700,200)
       continue # هيزود لفة ومش هيزود سكور 
     rnd=randint(1,3)     
     if rnd==choose :
         winsound.Beep(10000,440)
         print("\t\a XxxX THE GHOST CATCH YOU XxxX")
         break
         
     else:
       print("\t ghost see you ")
       score+=1
  except ValueError:

      print("enter Valid number  1:3")

print("Score:  %d"%score)
print("\t GAME OVER \t")

winsound.PlaySound('sound.wav', winsound.SND_FILENAME)
