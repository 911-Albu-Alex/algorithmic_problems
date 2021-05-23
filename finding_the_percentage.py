def find_the_percentage(student_mark, student_name):
    students_grades = student_mark[student_name]
    sum = 0
    for grade in students_grades:
        sum += float(grade)

    print("{:.2f}".format(sum/len(students_grades)))


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    find_the_percentage(student_marks, query_name)