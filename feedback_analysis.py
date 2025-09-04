def feedback(ratings):
    if(not ratings):
        return 0.0
    else:
        c=0
        for i in ratings:
            if(i>=4):
                c+=1
        rate_per= (c/len(ratings))*100
        return round(rate_per,2)

ratings = [5, 4, 3, 5, 2, 4, 1, 5]
result = feedback(ratings)
print(f"Positive Feedback: {result}%")