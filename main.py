print('''
                                              #############
                                            #               #
                                           #                  #
                                         #                      #
                                         #                       #
                                         I ----------------------I      
                                         I ///////////////////// I
                                         I ///////////////////// I
                                         I ///////////////////// I
                                         I //////password/////// I
                                         I ///////////////////// I
                                         I ///////////////////// I
                                         ( ///////////////////// )
                                          =======================
                                        
#====================================================================================#
#  Brute Force (Fun)          my instagram ==> tck6          hacker                  #
#  my snapchat ==> qzmq1      my Github ==> qzmq1           my name ==> naif         #
#====================================================================================#
''')

import string, random

pasw = input('ENTER THE PASSWORD TARGET :')
ch = string.printable

while True:
       pGuess = random.choices(ch, k=len(pasw))
       pGuess = ''.join(pGuess)
       print(pGuess)

       if pasw == pGuess :
           print(f"HACKED THE PASSWORD TARGET: -----------<><><><><>((((((((((        {pGuess}        ))))))))))<><><><><>---------------")
           break