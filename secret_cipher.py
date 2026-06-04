# সিক্রেট মেসেজ এনক্রিপ্ট করার ইউনিক কোড

def encrypt_message(plain_text):
    encrypted_text = ""
    for char in plain_text:
        # শুধুমাত্র ইংরেজি অক্ষরগুলোকে পরিবর্তন করবে
        if char.isalpha():
            shift = 3
            # অক্ষরের পজিশন পরিবর্তন করার লজিক
            start = ord('a') if char.islower() else ord('A')
            new_char = chr(start + (ord(char) - start + shift) % 26)
            encrypted_text += new_char
        else:
            # স্পেস বা সংখ্যা থাকলে তা আগের মতোই রাখবে
            encrypted_text += char
    return encrypted_text

# ইউজার থেকে ইনপুট নেওয়া
user_message = input("আপনার গোপন মেসেজটি ইংরেজিতে লিখুন: ")
secret_result = encrypt_message(user_message)

print("\n--- এনক্রিপ্টেড মেসেজ ---")
print(f"আপনার লক করা মেসেজ: {secret_result}")
print("------------------------")
