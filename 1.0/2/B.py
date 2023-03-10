data = []
answers = ["CONSTANT", "ASCENDING", "WEAKLY ASCENDING", "DESCENDING",
           "WEAKLY DESCENDING", "RANDOM"]
n = int(input())
while n != -2 * 10 ** 9:
    data.append(n)
    n = int(input())
for i in range(1, len(data)):
    if data[i - 1] > data[i]:
        if "CONSTANT" in answers:
            answers.remove("CONSTANT")
        if "ASCENDING" in answers:
            answers.remove("ASCENDING")
        if "WEAKLY ASCENDING" in answers:
            answers.remove("WEAKLY ASCENDING")
    elif data[i - 1] < data[i]:
        if "CONSTANT" in answers:
            answers.remove("CONSTANT")
        if "DESCENDING" in answers:
            answers.remove("DESCENDING")
        if "WEAKLY DESCENDING" in answers:
            answers.remove("WEAKLY DESCENDING")
    else:
        if "ASCENDING" in answers:
            answers.remove("ASCENDING")
        if "DESCENDING" in answers:
            answers.remove("DESCENDING")
print(answers[0])

