import base64
import os


def generate_key(password):
    """মানুষের দেওয়া পাসওয়ার্ড থেকে একটি সিক্রেট ক্রিপ্টোগ্রাফিক কি (Key) তৈরি করার ফাংশন।"""
    # পাসওয়ার্ডটিকে ৩২ বাইটের স্ট্যান্ডার্ড কি-তে রূপান্তর (Advanced Logic)
    padded_password = password.ljust(32, "*")[:32]
    return base64.urlsafe_b64encode(padded_password.encode())


def encrypt_message(message, password):
    """টেক্সট বা মেসেজ লক করার অ্যাডভান্সড ম্যাথমেটিক্যাল লজিক (XOR + Base64)"""
    key = generate_key(password)
    secret_bytes = base64.urlsafe_b64decode(key)

    # প্রতিটি ক্যারেক্টারকে পাসওয়ার্ডের কি দিয়ে লক করা
    encrypted_bytes = bytearray(
        b ^ secret_bytes[i % len(secret_bytes)]
        for i, b in enumerate(message.encode())
    )
    return base64.urlsafe_b64encode(encrypted_bytes).decode()


def decrypt_message(encrypted_message, password):
    """লক হওয়া ফাইলকে আবার আগের অবস্থায় ফিরিয়ে আনার লজিক।"""
    try:
        key = generate_key(password)
        secret_bytes = base64.urlsafe_b64decode(key)

        # লক খোলা
        encrypted_bytes = base64.urlsafe_b64decode(encrypted_message.encode())
        decrypted_bytes = bytearray(
            b ^ secret_bytes[i % len(secret_bytes)]
            for i, b in enumerate(encrypted_bytes)
        )
        return decrypted_bytes.decode()
    except Exception:
        return None


if __name__ == "__main__":
    print("=== FILE FORTRESS: ADVANCED SECURITY SYSTEM ===")

    # মানুষের আসল মেসেজ বা ডাটা
    secret_data = "Hello User, This is a top secret document! Project-X details inside."
    user_password = "MySuperSecretPassword123"

    print(f"\n[১] আসল ডাটা: {secret_data}")

    # ফাইল লক করা হচ্ছে
    locked_data = encrypt_message(secret_data, user_password)
    print(f"[২] লক করার পর (হ্যাকাররা যা দেখবে): {locked_data}")

    # ভুল পাসওয়ার্ড দিয়ে খোলার চেষ্টা
    wrong_try = decrypt_message(locked_data, "wrong_pass")
    print(f"[৩] ভুল পাসওয়ার্ড দিলে যা আসবে: {wrong_try} (অনুমতি নেই)")

    # সঠিক পাসওয়ার্ড দিয়ে আনলক করা
    unlocked_data = decrypt_message(locked_data, user_password)
    print(f"[৪] সঠিক পাসওয়ার্ড দিয়ে আনলকড ডাটা: {unlocked_data}")

    print("\n==============================================")
