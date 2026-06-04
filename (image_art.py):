import cv2

def convert_to_sketch(image_path, output_path):
    # ছবি লোড করা
    img = cv2.imread(image_path)
    
    # ছবিটিকে গ্রে-স্কেল বা সাদা-কালো করা
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # ছবিটিকে ইনভার্ট করা (Invert)
    inverted_img = 255 - gray_img
    
    # ব্লার (Blur) করা
    blurred = cv2.GaussianBlur(inverted_img, (21, 21), 0)
    
    # পেনসিল স্কেচ তৈরি করা
    inverted_blurred = 255 - blurred
    pencil_sketch = cv2.divide(gray_img, inverted_blurred, scale=256.0)
    
    # রেজাল্ট সেভ করা
    cv2.imwrite(output_path, pencil_sketch)
    print(f"ধন্যবাদ! আপনার স্কেচটি সেভ হয়েছে এখানে: {output_path}")

# রান করার আগে আপনার কম্পিউটারে একটি ছবি রেখে সেটার নাম দিন 'my_photo.jpg'
# convert_to_sketch('my_photo.jpg', 'sketch_output.jpg')
