import os
import shutil
import time
from datetime import datetime, timedelta

def organize_downloads(download_path=None):
    if not download_path:
        download_path = os.path.expanduser("~/Downloads")  # ডিফল্ট ডাউনলোডস ফোল্ডার
    
    # ফোল্ডার তৈরি করা
    folders = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
        "Videos": [".mp4", ".mkv", ".mov", ".avi", ".webm"],
        "Documents": [".pdf", ".docx", ".xlsx", ".pptx", ".txt", ".md"],
        "Code": [".py", ".js", ".html", ".css", ".java", ".cpp", ".go"],
        "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
        "Others": []
    }
    
    for folder in folders.keys():
        os.makedirs(os.path.join(download_path, folder), exist_ok=True)
    
    for filename in os.listdir(download_path):
        file_path = os.path.join(download_path, filename)
        
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(filename)[1].lower()
            
            moved = False
            for folder, extensions in folders.items():
                if file_ext in extensions:
                    dest = os.path.join(download_path, folder, filename)
                    shutil.move(file_path, dest)
                    print(f"✅ Moved: {filename} → {folder}")
                    moved = True
                    break
            
            if not moved:
                dest = os.path.join(download_path, "Others", filename)
                shutil.move(file_path, dest)
                print(f"✅ Moved: {filename} → Others")

# চালানোর জন্য
if __name__ == "__main__":
    print("🚀 File Organizer চলছে...")
    organize_downloads()
    print("✅ সব ফাইল অর্গানাইজ হয়ে গেছে!")
