import sys

class SteganographyEngine:
    def __init__(self):
        # Hidden zero-width characters that are completely invisible in text editors
        self.ZERO_WIDTH_ONE = '\u200B'  # Zero-width space (represents binary 1)
        self.ZERO_WIDTH_ZERO = '\u200C' # Zero-width non-joiner (represents binary 0)
        self.DELIMITER = '\u200D'       # Zero-width joiner (marks start/end of secret)

    def encode_secret(self, cover_text, secret_text):
        """Hides a secret message inside a normal cover text invisibly."""
        # Converting the secret text into a binary string
        binary_secret = ''.join(format(ord(char), '08b') for char in secret_text)
        
        # Mapping binary 1s and 0s to invisible zero-width characters
        invisible_encoded = ''.join(
            self.ZERO_WIDTH_ONE if bit == '1' else self.ZERO_WIDTH_ZERO 
            for bit in binary_secret
        )
        
        # Injecting the invisible string wrapped inside delimiters inside the cover text
        return f"{cover_text}{self.DELIMITER}{invisible_encoded}{self.DELIMITER}"

    def decode_secret(self, encrypted_text):
        """Extracts and decodes the hidden invisible message from text."""
        # Finding the secret part hidden between the invisible delimiters
        try:
            parts = encrypted_text.split(self.DELIMITER)
            if len(parts) < 3:
                return "❌ No hidden secret data found in this text."
            
            invisible_string = parts[1]
            
            # Converting invisible characters back to normal binary 1s and 0s
            binary_bits = ''.join(
                '1' if char == self.ZERO_WIDTH_ONE else '0' 
                for char in invisible_string if char in (self.ZERO_WIDTH_ONE, self.ZERO_WIDTH_ZERO)
            )
            
            # Reconstructing the original text characters from raw binary chunks
            secret_chars = [chr(int(binary_bits[i:i+8], 2)) for i in range(0, len(binary_bits), 8)]
            return ''.join(secret_chars)
            
        except Exception as e:
            return f"❌ Decoding Matrix Failed: {str(e)}"


# --- Execution Matrix ---
if __name__ == "__main__":
    print("🔒 Initializing Invisible Steganography Engine...")
    engine = SteganographyEngine()

    # Step 1: Define the fake open message and the real hidden message
    public_message = "I am practicing Python code today."
    secret_password = "MY-SECRET-BANK-PASSWORD-1234"

    print(f"\n[+] Public Message: '{public_message}'")
    print(f"[+] Secret Data to Hide: '{secret_password}'")

    # Step 2: Hide the secret inside the public message
    stego_text = engine.encode_secret(public_message, secret_password)
    print("\n⚡ Encoding Complete! The secret is now 100% invisible.")
    
    # Notice that printing 'stego_text' looks EXACTLY like the public message!
    print(f"📦 Encrypted Output Display: '{stego_text}'")
    print(f"📊 Total Characters in Output: {len(stego_text)} (Includes hidden invisible bytes)")

    print("\n---------------------------------------------------------------")
    
    # Step 3: Extract the hidden data back using the decoder logic
    print("🔓 Attempting decryption from the encoded string...")
    recovered_secret = engine.decode_secret(stego_text)
    
    print(f"🎯 Recovered Secret Data: {recovered_secret}")
    print("===============================================================")
