# B_R_R
# M_S_A_W


questions = open('questions.txt', 'r')  
question_list = [line.strip() for line in
                 questions.readlines()] 
questions.close()


score = 0
total = len(question_list)  


for line in question_list:
    q, a = line.split('=')  
    ans = input('{}='.format(q))  
    if a == ans:  
        score += 1  


result = open('result.txt', 'w')  
result.write('Your final score is {}/{}.'.format(score, total))  # write final score to result.txt
result.close()
