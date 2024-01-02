import random



scissors = ('''
      
    ___,--------
           -----)-----
                ------)
        ----------------)
            (-----)
_ _ _ ,--,_ _(----)
           
      
      ''')


rock = ('''
        
        _ _ _,-----
              -----)
            -------)
            -------)
        ---,_ _ _ _)
        
        ''')

paper = ('''
         
         ______________
    ----,   ___________)____
            _______________)
            ______________)
    ----,_____________)   
     
         ''')



print("""
      =============      __(_-_)__      __(_-_)__       __(_-_)__    ======-=======
      
                    Welcome to the Rock Paper Scissors Playing Board
      
      =============      __(_-_)__      __(_-_)__       __(_-_)__    ======-=======
      
      """)




choice = int(input("What is your choose? 0-> Rock | 1-> Paper | 2-> Scissors"))
computer_choice = random.randint(0, 2)

if choice == computer_choice:
    if choice == 0:
        print(rock)
    elif choice == 1:
        print(paper)
    else:
        print(scissors)

    
    print("\nYou are win!!")
else:
    print("You lose!!")
    print(f"Computer Choose {computer_choice}..")
    if computer_choice == 0:
        print(rock)
    elif computer_choice == 1:
        print(paper)
    else:
        print(scissors)
    
