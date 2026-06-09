import random

def play_game():
    print("✊ ✋ ✌️  রক-পেপার-সিজার গেমে স্বাগতম! ✊ ✋ ✌️")
    print("-" * 45)
    
    # অপশনগুলোর লিস্ট
    options = ["Rock", "Paper", "Scissors"]
    
    # কম্পিউটার এবং আপনার (ইউজার) জন্য র‍্যান্ডম চয়েস (যেহেতু গিটহাব অটো-রান করবে)
    your_choice = random.choice(options)
    computer_choice = random.choice(options)
    
    print(f"আপনার চাল: {your_choice}")
    print(f"কম্পিউটারের চাল: {computer_choice}")
    print("-" * 45)
    
    # বিজয়ী নির্ধারণ করার লজিক
    if your_choice == computer_choice:
        print("💥 ম্যাচটি ড্র হয়েছে! 💥")
    elif (your_choice == "Rock" and computer_choice == "Scissors") or \
         (your_choice == "Paper" and computer_choice == "Rock") or \
         (your_choice == "Scissors" and computer_choice == "Paper"):
        print("🎉 অভিনন্দন! আপনি জিতেছেন! 🏆")
    else:
        print("😢 কম্পিউটার জিতে গেছে! আবার চেষ্টা করুন।")
        
    print("\nকোডটি একদম সফলভাবে রান করেছে! 🚀")

if __name__ == "__main__":
    play_game()
