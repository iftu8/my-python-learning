import os
import shutil
import argparse
from datetime import datetime

def organize_files(path=None, delete_old=False, days=30):
    if not path:
        path = os.path.expanduser("~/Downloads")
    
    if not os.path.exists(path):
        print(f"❌ ফোল্ডার পাওয়া যায়নি: {path}")
        return
    
    folders = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".svg"],
        "Videos": [".mp4", ".mkv", ".mov", ".avi", ".webm", ".flv"],
        "Documents": [".pdf", ".docx", ".xlsx", ".pptx", ".txt", ".md", ".csv"],
        "Code": [".py", ".js", ".html", ".css", ".java", ".cpp", ".c", ".go", ".php"],
        "Archives": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2"],
        "Music": [".mp3", ".wav", ".flac", ".aac"],
        "Others": []
    }
    
    for folder in folders:
        os.makedirs(os.path.join(path, folder), exist_ok=True)
    
    moved_count = 0
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        
        if os.path.isfile(file_path):
            # পুরনো ফাইল ডিলিট করবে কিনা চেক
            if delete_old:
                age = (datetime.now() - datetime.fromtimestamp(os.path.getctime(file_path))).days
                if age > days:
                    os.remove(file_path)
                    print(f"🗑️  Deleted old file: {filename}")
                    continue
            
            file_ext = os.path.splitext(filename)[1].lower()
            moved = False
            
            for folder, extensions in folders.items():
                if file_ext in extensions:
                    dest_path = os.path.join(path, folder, filename)
                    # যদি একই নামের ফাইল থাকে তাহলে নতুন নাম দিবে
                    if os.path.exists(dest_path):
                        base, ext = os.path.splitext(filename)
                        dest_path = os.path.join(path, folder, f"{base}_{int(datetime.now().timestamp())}{ext}")
                    
                    shutil.move(file_path, dest_path)
                    print(f"✅ {filename} → {folder}")
                    moved_count += 1
                    moved = True
                    break
            
            if not moved:
                shutil.move(file_path, os.path.join(path, "Others", filename))
                print(f"✅ {filename} → Others")
                moved_count += 1
    
    print(f"\n🎉 সম্পন্ন! {moved_count}টা ফাইল অর্গানাইজ করা হয়েছে।")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="🔥 Advanced File Organizer")
    parser.add_argument("-p", "--path", help="যে ফোল্ডার অর্গানাইজ করতে চাও")
    parser.add_argument("-d", "--delete-old", action="store_true", help="৩০ দিনের পুরনো ফাইল ডিলিট করবে")
    parser.add_argument("--days", type=int, default=30, help="কত দিন পর ডিলিট করবে")
    
    args = parser.parse_args()
    organize_files(args.path, args.delete_old, args.days)
