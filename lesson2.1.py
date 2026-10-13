#A function helps or allows one to write logic once snd reuse it with different inputs
def calculate_average(scores):
    average = sum(scores)/ len(scores)
    return average

exam_scores = [40,50,70,90]
result = calculate_average(exam_scores)

print("Average exam score:", result)

# the likes of def which defines a function,calculaye_average a s a func name all amter
# in Lesson 3 we shall later rewite resubale functions for preprocessing data, enginerring features evaluation of models 
#and calculating metrics
# So calculating R/sshp between  study hours and scores
