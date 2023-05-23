import numpy as np


def generate_students(privileged_students):

    students_MATH = np.random.normal(180, 10, 1500)
    students_EN = np.random.normal(180, 10, 1500)
    students_UA = np.random.normal(180, 10, 1500)
    student_id = np.array([i for i in range(1500)])

# students with privilege

    students_MATH[0:privileged_students] = np.random.normal(
        150, 20, privileged_students)
    students_EN[0:privileged_students] = np.random.normal(
        150, 20, privileged_students)
    students_UA[0:privileged_students] = np.random.normal(
        150, 20, privileged_students)

# max array value - 200

    students_MATH[students_MATH > 200] = 200
    students_EN[students_EN > 200] = 200
    students_UA[students_UA > 200] = 200

# students with privelege - 1, others - 0

    students_PRIV = np.zeros(1500)
    students_PRIV[0:privileged_students] = 1

# 1500x6 matrix with students grades, privelege and names

    students = np.zeros((1500, 6))

    students[:, 0] = students_MATH
    students[:, 1] = students_EN
    students[:, 2] = students_UA
    students[:, 3] = students_PRIV
    students[:, 4] = student_id

# shuffle students

    np.random.shuffle(students)
    return students


def exam_mark(results):
    return 0.4 * results[0] + 0.3 * results[1] + 0.3 * results[2]


def priv_student_good(results):
    return (exam_mark(results) > 144 and results[0] > 120 and results[1] > 120 and results[2] > 120 and results[3] == 1)


def non_priv_student_good(results):
    return (exam_mark(results) > 160 and results[3] == 0 and results[0] > 140)


def choose_students(students):

    sorted_students = sorted(students, key=lambda x: (
        0.4 * x[0] + 0.3 * x[1] + 0.3 * x[2]) + 200 * x[3], reverse=True)
    sorted_students = np.array(sorted_students)

    filtered_priv_students = list(
        filter(lambda x: priv_student_good(x), sorted_students))
    if len(filtered_priv_students) > 35:
        filtered_priv_students = filtered_priv_students[:35]

    filtered_non_priv_students = list(
        filter(lambda x: non_priv_student_good(x), sorted_students))
    if len(filtered_non_priv_students) > 350 - len(filtered_priv_students):
        filtered_non_priv_students = filtered_non_priv_students[:350 - len(
            filtered_priv_students)]

    filtered_priv_students = np.array(filtered_priv_students)
    filtered_non_priv_students = np.array(filtered_non_priv_students)

    for i in range(len(filtered_non_priv_students)):
        # if student with same is in students, then change 6 column of that student to 1 in students array
        if filtered_non_priv_students[i][4] in students[:, 4]:
            students[np.where(students[:, 4] ==
                              filtered_non_priv_students[i][4]), 5] = 1

    for i in range(len(filtered_priv_students)):
        # if student with same is in students, then change 6 column of that student to 1 in students array
        if filtered_priv_students[i][4] in students[:, 4]:
            students[np.where(students[:, 4] ==
                              filtered_priv_students[i][4]), 5] = 1

    return students


def choose_priv_students(students):
    sorted_students = sorted(students, key=lambda x: (
        0.4 * x[0] + 0.3 * x[1] + 0.3 * x[2]) + 200 * x[3], reverse=True)
    sorted_students = np.array(sorted_students)

    filtered_priv_students = list(
        filter(lambda x: priv_student_good(x), sorted_students))
    if len(filtered_priv_students) > 35:
        filtered_priv_students = filtered_priv_students[:35]

    filtered_priv_students = np.array(filtered_priv_students)

    for i in range(len(filtered_priv_students)):
        # if student with same is in students, then change 6 column of that student to 1 in students array
        if filtered_priv_students[i][4] in students[:, 4]:
            students[np.where(students[:, 4] ==
                              filtered_priv_students[i][4]), 5] = 1

    return students


def choose_non_priv_students(students):
    sorted_students = sorted(students, key=lambda x: (
        0.4 * x[0] + 0.3 * x[1] + 0.3 * x[2]) + 200 * x[3], reverse=True)
    sorted_students = np.array(sorted_students)

    filtered_non_priv_students = list(
        filter(lambda x: non_priv_student_good(x), sorted_students))
    if len(filtered_non_priv_students) > 350:
        filtered_non_priv_students = filtered_non_priv_students[:350]

    filtered_non_priv_students = np.array(filtered_non_priv_students)

    for i in range(len(filtered_non_priv_students)):
        # if student with same is in students, then change 6 column of that student to 1 in students array
        if filtered_non_priv_students[i][4] in students[:, 4]:
            students[np.where(students[:, 4] ==
                              filtered_non_priv_students[i][4]), 5] = 1

    return students
