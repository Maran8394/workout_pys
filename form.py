def Average(lst)->str:
    return f"{int(sum(lst)) // len(lst)}%"

l = [
{'course': 'ICICI_Batch 59_Term 1_Accountancy, Statistics and Data Analytics_PGD605', 
'sec': {'ICICI_Batch 59_Term 1_Section A_Accountancy, Statistics and Data Analytics'}, 
'quizCompletion': 0, 'contentComPletion': 25, 'quizScore': 0, 'dbCompletion': 27, 'assingmentCompletion': 89}, 
{
'course': 'ICICI_Batch 59_Term 1_Accountancy, Statistics and Data Analytics_PGD605', 
'sec': {'ICICI_Batch 59_Term 1_Section B_Accountancy, Statistics and Data Analytics'}, 
'quizCompletion': 0, 'contentComPletion': 25, 'quizScore': 0, 'dbCompletion': 27, 'assingmentCompletion': 91
}, 

{'course': 'ICICI_Batch 59_Term 1_Accountancy, Statistics and Data Analytics_PGD605', 
'sec': {'ICICI_Batch 59_Term 1_Section C_Accountancy, Statistics and Data Analytics'}, 
'quizCompletion': 0, 'contentComPletion': 23, 'quizScore': 0, 'dbCompletion': 24, 'assingmentCompletion': 82
}, 

{'course': 'ICICI_Batch 59_Term 1_Accountancy, Statistics and Data Analytics_PGD605', 
'sec': {'ICICI_Batch 59_Term 1_Section D_Accountancy, Statistics and Data Analytics'}, 
'quizCompletion': 0, 'contentComPletion': 0, 'quizScore': 0, 'dbCompletion': 0, 'assingmentCompletion': 0}
]

quizCompletion = []
contentComPletion = []
quizScore = []
dbCompletion = []
assingmentCompletion = []

for i in range(len(l)):
    quizCompletion.append(l[i]['quizCompletion'])
    contentComPletion.append(l[i]['contentComPletion'])
    quizScore.append(l[i]['quizScore'])
    dbCompletion.append(l[i]['dbCompletion'])
    assingmentCompletion.append(l[i]['assingmentCompletion'])

print(Average(quizCompletion))
print(Average(contentComPletion))
print(Average(quizScore))
print(Average(dbCompletion))
print(Average(assingmentCompletion))
