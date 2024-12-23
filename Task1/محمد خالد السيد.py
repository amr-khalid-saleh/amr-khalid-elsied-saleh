def scoresort(scores):
    n = len(scores)
    
    for i in range(n):
        min_score = i
        
        
        for j in range(i + 1, n):
            if scores[j] < scores[min_score]:
                min_score = j
        
        scores[i], scores[min_score] = scores[min_score], scores[i]

# Scores to sort
scores = [88, 95, 70, 85, 90]
scoresort(scores)
print(scores)
