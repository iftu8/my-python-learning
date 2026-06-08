import random
import string


def evaluate_strength(password):
    """মানুষের পাসওয়ার্ডটি কতটা শক্তিশালী তা পরীক্ষা করার ফাংশন।"""
    length = len(password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)

    # স্কোর হিসাব করা (সর্বোচ্চ ৫)
    score = sum([length >= 12, has_upper, has_lower, has_digit, has_special])

    if score == 5:
        return "Extremely Strong 💪 (নিরাপদ)"
    elif score >= 3:
        return "Moderate ⚠️ (আরেকটু কঠিন করুন)"
    else:
        return "Weak ❌ (খুবই দুর্বল! হ্যাক হতে পারে)"


def generate_secure_password(length=14):
    """মানুষের জন্য একটি হ্যাকার-প্রুফ শক্তিশালী পাসওয়ার্ড তৈরি করার ফাংশন।"""
    if length < 6:
        length = 6

    # সব ধরণের ক্যারেক্টার মিক্স করা
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    # নিশ্চিত করা যেন সব রকমের ক্যারেক্টার অন্তত একটি করে থাকে
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special),
    ]

    # বাকি ক্যারেক্টারগুলো র্যান্ডমলি নেওয়া
    all_characters = lower + upper + digits + special
    password += [random.choice(all_characters) for _ in range(length - 4)]

    # পাসওয়ার্ডের সিরিয়াল এলোমেলো করা যেন কেউ অনুমান করতে না পারে
    random.shuffle(password)

    return "".join(password)


if __name__ == "__main__":
    print("=== WELCOME TO CYBER SECURITY SHIELD ===")

    # ১. মানুষের জন্য একটি নিরাপদ পাসওয়ার্ড তৈরি
    generated_pass = generate_secure_password(16)
    print(f"\n[+] আপনার জন্য তৈরি করা শক্তিশালী পাসওয়ার্ড: {generated_pass}")

    # ২. সেটির শক্তি পরীক্ষা করা
    strength = evaluate_strength(generated_pass)
    print(f"[+] পাসওয়ার্ডের নিরাপত্তা লেভেল: {strength}")

    print("\n=======================================")
