import random

def roll_dice():
    print("🎲 ডাইস রোলিং গেম-এ স্বাগতম! 🎲")
    print("-" * 35)
    
    # ১ থেকে ৬ এর মধ্যে র‍্যান্ডম সংখ্যা তৈরি করবে
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    
    print(f"প্রথম ডাইস: {dice1}")
    print(f"দ্বিতীয় ডাইস: {dice2}")
    print("-" * 35)
    print(f"আপনার মোট স্কোর: {dice1 + dice2}")
    print("\nদারুণ! আপনার কোডটি একদম পারফেক্টলি রান করছে। 🚀")

if __name__ == "__main__":
    roll_dice()
