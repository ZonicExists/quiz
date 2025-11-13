questions = [
    {
        "q": "What is the capital of France?",
        "choices": ["A) Paris", "B) London", "C) Berlin", "D) Madrid"],
        "answer": "A"
    },
    {
        "q": "Which language is primarily used for system programming?",
        "choices": ["A) Python", "B) C", "C) HTML", "D) JavaScript"],
        "answer": "B"
    },
    {
        "q": "What does RAM stand for?",
        "choices": ["A) Readily Available Memory", "B) Random Access Memory", "C) Rapid Action Module", "D) None"],
        "answer": "B"
    }
]

def run_quiz():
    score = 0
    for i, item in enumerate(questions, start=1):
        print(f"\nQ{i}: {item['q']}")
        for c in item["choices"]:
            print("   " + c)
        ans = input("Your answer (A/B/C/D): ").strip().upper()
        if ans == item["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong. Correct answer: {item['answer']}")
    print(f"\nQuiz finished. Score: {score}/{len(questions)}")

if __name__ == "__main__":
    run_quiz()
