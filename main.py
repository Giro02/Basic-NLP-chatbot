import re
from data import datalist



def prob_checker(split_message):
    prob = []
    for i in split_message:
        for key,value in datalist.items():
            if i in value:
                prob.append(key)
                
    
    return(prob)
        
def check_words (split_message ):
    prob_answer = prob_checker(split_message)
    return(prob_answer)

def finallistcounter(list):
    if list == []:
        list.append("I didnt understand!")
        return(list)
    else:
        most_likely_answer = []
        most_likely_answer.append(max(set(list), key = list.count))  
        return(most_likely_answer)

while True:

    userinput = input('you:')
    split_message = re.split(r'\s+|[,;?!.-]\s*', userinput.lower())
    response = check_words(split_message)
    botanswer= finallistcounter(response)

    print('bot:',botanswer[0])










    

