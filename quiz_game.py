import random

def run_quiz():
    print("🧠 কুইজ গেম-এ স্বাগতম! 🧠")
    print("=" * 40)
    
    # প্রশ্ন, অপশন এবং সঠিক উত্তরের লিস্ট
    quiz_data = [
        {
            "question": "১. পাইথন (Python) কী ধরণের ল্যাঙ্গুয়েজ?",
            "options": ["A) Programming Language", "B) Database", "C) Operating System"],
            "correct": "A"
        },
        {
            "question": "২. গিটহাব (GitHub) মূলত কীসের জন্য ব্যবহার করা হয়?",
            "options": ["A) Video Editing", "B) Code Hosting & Version Control", "C) Gaming"],
            "correct": "B"
        },
        {
            "question": "৩. HTML এর পূর্ণরূপ কী?",
            "options": ["A) HighText Machine Language", "B) HyperText Markup Language", "C) HyperLink Text Language"],
            "correct": "B"
        }
    ]
    
    score = 0
    
    for item in quiz_data:
        print(item["question"])
        for option in item["options"]:
            print(option)
            
        # গিটহাবের অটো-রানের জন্য রোবট র‍্যান্ডমলি একটি উত্তর বেছে নেবে (A, B, অথবা C)
        bot_answer = random.choice(["A", "B", "C"])
        print(f"আপনার দেওয়া উত্তর: {bot_answer}")
        
        if bot_answer == item["correct"]:
            print("✅ সঠিক উত্তর! +১ পয়েন্ট")
            score += 1
        else:
            print(f"❌ ভুল উত্তর! সঠিক উত্তর ছিল: {item['correct']}")
        print("-" * 40)
        
    print(f"🏆 কুইজ শেষ! আপনার মোট স্কোর: {score}/{len(quiz_data)}")
    print("কোডটি সফলভাবে রান করেছে! 🚀")

if __name__ == "__main__":
    run_quiz()
