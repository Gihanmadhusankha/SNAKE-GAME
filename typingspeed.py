from time import time

def tperror(prompt):
    global inwords

    words = prompt.split()
    errors = 0

    for i in range(len(inwords)):
        if i in(0, len(inwords)-1):
            if inwords[i] == words[i]:
                continue
            else:
                errors = errors + 1
        else:
            if inwords[i] == words[i]:
                if(inwords[i+1] == words[i+1]) & (inwords[i-1] == words[i-1]):
                    continue
                else:
                    errors += 1
            else:
                errors += 1
    return errors


def speed(inprompt, stime, etime):
    global time
    global inwords

    inwords = inprompt.split()
    towards = len(inwords)
    speed = twords / time

    return speed

def elapsedtime(stime,etime):
    time =etime - stime
    return time

if __name__ == '_main_':
    prompt = "Python is a high-level, interpreted, object-oriented, and dynamic programming language with a simple syntax and a large standard library"

    print ("Type this:-",prompt,"")

    input("Press Enter when you ready to check your speed!!")

    stime = time()
    inprompt = input()
    etime = time()

    #collect alll the information retuned by the  functions
    time = round(elapsedtime(stime,etime),2)
    speed = speed(inprompt,stime,etime)
    errors = tperror(prompt)

    #Printing all the required  data to see result
    print("Total time elapsed: ",time,"seconde")
    print("Your Average Typing speed was ",speed ,"words per minute(w/m)")
    print("with the  total of",errors,"errors")


          
    
