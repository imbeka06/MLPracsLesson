study_hours = [3,5,8]
exam_scores = [45,65,85]

#calculating the AVERAGES OF EXAM exam_scores
average_score = sum(exam_scores) / len(exam_scores)

# Finding highest number of scores
highest_score = max(exam_scores)

print ("Avgerage score:", average_score)
print ("Highest score:", highest_score)

if average_score >= 60 :
    print ("High perfromer")
else:
    print("Needs improvement")