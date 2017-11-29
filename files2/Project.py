##Tic-Tac_Toe



import random
new = ['','','','','','','','','']
man = ''
machine = ''
null = ''


def sign(man, machine):
    man = raw_input("What team you want to be? X or O ")#gives you the choices of which team you wanna be 
    while man not in ('x','X','o','O'): #Answers defined For what team you wanna be 
        print "Invalid Choice!"
        man = raw_input("What team you want to be? X or O ")#Type in What team you wanna be 
    if man == 'x' or man == 'X':
        print "Ok, X is yours!" #if X's Chosen Then it gives you the X's and the computor O's
        machine = 'o'
    else:
        print "Ok, O is yours!"# if O's chosen then it gives you the O's and the computor X's
        machine = 'x'
    return man.upper(), machine.upper()
    
    

def decide_turn():
    turn = None
    while turn not in ('y','Y','n','N'): #if you want to go first type lower or captial Y if you want to go second tyep lower case n or capitial N
        turn = raw_input("Do you want to go first? ") #If you want to go First or not Type Y or N
        if turn == 'y' or turn == 'Y': #When typing in Y it returns to the next line
            return 1
        elif turn == 'n' or turn == 'N':#when typing in N it returns to the next line
            return 0
        else:
            print "its an invalid choice." #elseif IF not Defined answer Print invalid choice

def draw(a):
    
    print "\n\t",a[0],"|",a[1],"|",a[2]# cordinates for where to place the X's or O's
    print "\t", "--------"
    print "\n\t",a[3],"|",a[4],"|",a[5]
    print "\t", "--------"
    print "\n\t",a[6],"|",a[7],"|",a[8], "\n"

def congo_man():
    print "You won!!" #if won Print You won

def congo_machine():
    print "Hahha, I won!!!" #if you lose it prints the computor won

def man_first(man, machine, new):#what order it goes in and the man goes first 
    while winn(man, machine, new) is None:
        move = man_move(man, new)
        new[int(move)] = man
        draw(new)
        if winn(man, machine, new) != None:
            break
        else:
            pass
        print "ummmm....i'll take.." #After you choose the cordinate you want to go to the computor chooses where it wants to go and prints Um i'll take 
        p_move = machine_move(man, machine, new)#
        print p_move
        new[int(p_move)] = machine
        draw(new)
    q = winn(man, machine, new)
    if q == 1:#if player wins then the code makes it to congo_man and you win 
        congo_man()
    elif q == 0:#if machine wins then code refers to congo_machine and prints they won 
        congo_machine()
    else:
        print "Its a tie man..." #if no one wins the code will print It's a Tie man
   


def machine_first(man, machine, new):#order in which man goes first then machine
    while not winn(man, machine, new):
        print "i'll take..."#it would print after you choose the cordinates 
        p_move = machine_move(man, machine, new)#it has the machine go first then you 
        print p_move
        new[p_move] = machine  #now it is repeated 
        draw(new)
        if winn(man, machine, new) != None:
            break
        else:
            pass
        move = man_move(man, new)#it is now the mans move and you pick where you want to go 
        new[int(move)] = man
        draw(new)
    q = winn(man, machine, new)#this is where q is defined and its for who wins 
    if q == 1:#if man wins the q==1 
        congo_man()#congo man is you and when youi win you make q=1 
    elif q == 0:
        congo_machine()#congo machine is the computor that plays when it wins the q=0
    else:
        print "Its tie man..."#if no one wins then it will go to else and print its a tie man 


def winn(man, machine, new):
    ways = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))#these are the ways that both man and machine can win 
    for i in ways:
        if new[i[0]] == new[i[1]] == new[i[2]] != null:#the code refers to which people win if you win it is 0 if machine wins its 1 if its a tie it is 2
            winner = new[i[0]]
            if winner == man:#defines winner being man
                return 1#if winner wins it returns to one 
            elif winner == machine:#defines who is machine 
                return 0#if machine wins it will be returns as 0
            if null not in new: #defines who the tie is and it returns a tie 
                return 'TIE'#if it is a tie it reutnrs the printed text of tie 
    if null not in new:#the code is repeated for the tying situation
        return 'TIE'#if it is tie code returns tie     
    return None#if it returns then it will return none 


def man_move(man, new): 
    a = raw_input("where you want to move? ")#the code asks you a question of where do you want to move 
    while True:#iuf you type in the correct number it will return ad true 
        if a not in ('0','1','2','3','4','5','6','7','8'):#this is the numbers you can put in to move where you want to 
            print "Sorry, invalid move"#if you dont print one of the numbers above then it will print sorry invalid  move
            a = raw_input("where you want to move? ")#this code asks you the same question again but it return to you a different answer defines where you pick the number but the postion is already taken 
        elif new[int(a)] != null:#it introduces the new line to the code 
            print "Sorry, the place is already taken"#if the place is already taken the code sees it and then prints this text 
            a = raw_input("where you want to move? ")#then it would return and ask the question again 
        else:
            return int(a)#if it is none of those it will ask the question again 



    
def machine_move(man, machine, new):#the order of which you pick the places 
    best = [4, 0, 2, 6, 8]#best places to put the X's or O's
    blank = []#this refers to the places that are blank 
    for i in range(0,9):#this is the range for the numbers you can pick
        if new[i] == null:#it is another word for return to a blank list 
            blank.append(i)#this refers to the line above as the list 
    
    for i in blank:#this is defining more of the line/question
        new[i] = machine#this code shows that it is the machines turn to pick
        if winn(man, machine, new) is 0:#if it is a win then the score turns to zero a

            return i#it will then return to another section of code to restart
        new[i] = null#it is gonna return to a list 

    for i in blank:#this is defining I for the question above
        new[i] = man#this is defining what is gonna happen for man
        if winn(man, machine, new) is 1:#if it is man that wins the score will go to 1

            return i#it will return back to the top 
        new[i] = null#it returns to the list of things to do 

    return int(blank[random.randrange(len(blank))])#it will return back to the top to rerun the code 
        



def display_instruction():#this is the code for it to display the instructions 
      """ Displays Game Instuructions. """
      print #the code will now print the intructions 
      """
      Welcome to the Game...
      You will make your move known by entering a number, 0 - 8.
      The will correspond to the board position as illustrated:


                          0 | 1 | 2            
                         -----------
                          3 | 4 | 5            
                         -----------
                          6 | 7 | 8

                          
      Prepare yourself, the ultimate bettel is about to begin.....
      """

  
def main(man, machine, new):#this displays the order of who gets the positions first 
    display_instruction()#it calls for the instruction
    print "so lets begin.."#it then prints this text after the instructions 
    a = sign(man, machine)#it then calls for the sign if you want to be X's or O's
    man = a[0]#this defines the number you are so the code knows which is who when it calls to restart after one of you wins or its a tie 
    machine = a[1]#this defines the number you are so the code knows which is who when it calls to restart after one of you wins or its a tie
    b = decide_turn()#it calls for the question who wants to go first 
    if b == 1:#this calls for if you pick to go first 
        print "Ok, you are first!"#the code then prints the text
        print "Lets get started, here's a new board!"#it then prints the text for us to get started
        draw(new)#the code asks for a new board to be drawn
        man_first(man, machine, new)#it has the order in which you will go in
    elif b == 0:#this is the second choice of you picking second
        print "Ok, I'll be the first!"#the code then prints the text of it going first 
        print "So, lets start.."#it will also print this text to 
        draw(new)#then calls for the next person to go 
        machine_first(man, machine, new)#this is the order when you want to go second
    else:
        pass#if none of this it overights it and keeps going


main(man, machine, new)#the order in which you pick the moves you want to make 
raw_input("Press enter to exit")# the code makes the enter button return and restart the code so you can re run the code and play the game 