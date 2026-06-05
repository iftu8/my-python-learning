import random
import string

def generate_password(length=12):
    # সব ধরণের ক্যারেক্টার একসাথে করা হচ্ছে (অক্ষর, সংখ্যা এবং স্পেশাল ক্যারেক্টার)
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # র্যান্ডমলি ক্যারেক্টার সিলেক্ট করে পাসওয়ার্ড তৈরি
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

# ব্যবহারকারী কত বড় পাসওয়ার্ড চান তা ইনপুট নেওয়া
try:
    password_length = int(input("পাসওয়ার্ডটি কত অক্ষরের হবে? (যেমন: 12): "))
    if password_length < 4:
        print("নিরাপত্তার জন্য পাসওয়ার্ড অন্তত ৪ অক্ষরের হওয়া উচিত।")
    else:
        generated_password = generate_password(password_length)
        print(f"আপনার স্ট্রং পাসওয়ার্ড: {generated_password}")
except ValueError:
    print("দয়া করে একটি সঠিক সংখ্যা ইনপুট দিন।")
