"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """

    for i in range(len(student_scores)):
        student_scores[i] = round(student_scores[i])
    return student_scores


def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """

    sum = 0
    for student in student_scores:
        if student <= 40:
            sum += 1
    return sum


def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """
    best_ones = []
    for score in student_scores:
        if score >= threshold:
            best_ones.append(score)
    return best_ones


def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """

    letter_list = []
    incrument = round((highest - 40) / 4)
    for i in range(4):
        letter_list.append(41 + i * incrument)
    return letter_list


def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in ascending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """

    final_list = []
    for index, name in enumerate(student_names):
        final_list.append(f"{index+1}. {name}: {student_scores[index]}")
    return final_list


def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """

    perfect_score_list = []

    for student in student_info:
        if student[1] == 100:
            return student

    return perfect_score_list
