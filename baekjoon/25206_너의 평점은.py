grade_to_credit = {
    'A+':	4.5,
    'A0':	4.0,
    'B+':	3.5,
    'B0':	3.0,
    'C+':	2.5,
    'C0':	2.0,
    'D+':	1.5,
    'D0':	1.0,
    'F':	0.0,
}
total_credit = 0
credit_grade = 0
for _ in range(20):
    data = list(input().split())
    subject = data[0]
    credit = int(float(data[1]))
    grade = data[2]
    if grade != 'P':
        total_credit += credit
        credit_grade += credit * grade_to_credit[grade]
print(credit_grade / total_credit)
