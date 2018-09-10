from random import *
import winsound
class final:
    ## constructor and Chosices 
        def __init__(self):
            print("\twelcome to full GAme \n")
            winsound.Beep(1000,500)
            try:
                print("chose game please\n 1:ghost game\t 2:odd_even_game\n 3:multiplay Game  ")
                user=int(input(""))
                if user >=4 or user<=0:
                      print("enter vaild value  1 or 2 or 3 ")
                if user==1:
                    self.ghost()
                elif user==2:
                    self.odd_even()
                elif user==3:
                    self.multiplay()
            except :
                print("enter vaild value  1 or 2 or 3 ")
                ##AVAAILBLE CODES 
        def ghost(self):##ghost GAme CODE
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
######################################ODD EVEN CODE ##############################
        def odd_even(self):#odd even game code 
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
########################################################################
        def multiplay(slef):###MULTIPLAY Game code 
            print("welcome to multiplaly table")
            start=int(input("enter your start "))
            endd=int(input("enter your end "))
            for i in range (start,endd+1):
                print('___________________________')
                for y in range(1,13):
                 print(i ,'*' ,y ,'=',i*y)   
     

game=final()
