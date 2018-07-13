if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    temp=list()
    if(student_marks.has_key(query_name)):
        temp=student_marks[query_name]
    s=0.00
  
    for i in range(3):
        s+=temp[i]
    print "%.2f" % (s/3)
