if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
finalMarks = student_marks[query_name]

Avg=sum(finalMarks)/3
format_float = "{:.2f}".format(Avg)
print(format_float)