def grade(student_answers, correct_answers):
    score = 0
    for q, ans in correct_answers.items():
        if student_answers.get(q) == ans:
            score += 1
    return score

def pass_fail(score, total, passing_percentage=50):
    if total == 0:
        return False
    percent = (score / total) * 100
    return percent >= passing_percentage

if __name__ == "__main__":
    # Example usage
    student = {"q1": "A", "q2": "B", "q3": "C"}
    correct = {"q1": "A", "q2": "C", "q3": "C"}
    sc = grade(student, correct)
    print(f"Score: {sc}/{len(correct)}")
    print("Pass?" , pass_fail(sc, len(correct)))
