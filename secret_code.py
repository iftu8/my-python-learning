# সিক্রেট মেসেজ লক ও আনলক করার ইউনিক টুল

def encrypt_message(plain_text):
    encrypted_text = ""
    for char in plain_text:
        if char.isalpha():
            shift = 3
            start = ord('a') if char.islower() else ord('A')
            new_char = chr(start + (ord(char) - start + shift) % 26)
            encrypted_text += new_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt_message(cipher_text):
    decrypted_text = ""
    for char in cipher_text:
        if char.isalpha():
            shift = 3
            start = ord('a') if char.islower() else ord('A')
            new_char = chr(start + (ord(char) - start - shift) % 26)
            decrypted_text += new_char
        else:
            decrypted_text += char
    return decrypted_text

# ইউজার মেনু
print("১. মেসেজ লক করুন (Encrypt)")
print("২. মেসেজ আনলক করুন (Decrypt)")
choice = input("আপনার পছন্দ বেছে নিন (1/2): ")

if choice == "1":
    user_message = input("আপনার গোপন মেসেজটি ইংরেজিতে লিখুন: ")
    secret_result = encrypt_message(user_message)
    print(f"\nআপনার লক করা মেসেজ: {secret_result}")
elif choice == "2":
    secret_message = input("লক করা হিজিবিজি মেসেজটি দিন: ")
    original_result = decrypt_message(secret_message)
    print(f"\nআপনার আসল মেসেজ: {original_result}")
else:
    print("ভুল অপশন সিলেক্ট করেছেন!")
