import time
import math

class ProjectTracker:
    def __init__(self, project_name):
        self.project_name = project_name
        self.tasks = {}

    def add_task(self, task_name):
        """Adds a new task to the project with an initial status of Incomplete."""
        self.tasks[task_name] = "Incomplete"
        print(f"➕ Task Added: '{task_name}'")

    def complete_task(self, task_name):
        """Marks a specific task as completed."""
        if task_name in self.tasks:
            self.tasks[task_name] = "Completed"
            print(f"✅ Task Completed: '{task_name}'")
        else:
            print(f"❌ Task '{task_name}' not found in this project.")

    def display_progress_bar(self, percentage):
        """Generates a visual text-based progress bar."""
        bar_length = 20
        filled_length = int(round(bar_length * percentage / 100))
        bar = '█' * filled_length + '-' * (bar_length - filled_length)
        return f"[{bar}] {percentage}%"

    def show_dashboard(self):
        """Displays the project dashboard with real-time tracking stats."""
        total_tasks = len(self.tasks)
        if total_tasks == 0:
            print("\n--- No tasks available to track! ---")
            return

        completed_tasks = sum(1 for status in self.tasks.values() if status == "Completed")
        progress_percentage = math.floor((completed_tasks / total_tasks) * 100)

        print(f"\n=========================================")
        print(f"📊 PROJECT DASHBOARD: {self.project_name.upper()}")
        print(f"=========================================")
        for task, status in self.tasks.items():
            icon = "🟢" if status == "Completed" else "🟡"
            print(f"{icon} {task:<30} -> {status}")
        
        print(f"-----------------------------------------")
        print(f"Overall Progress: {self.display_progress_bar(progress_percentage)}")
        print(f"=========================================\n")


# --- Main Program Execution ---
print("Initializing Project Tracking System...")
time.sleep(1)

# 1. Initialize a new project tracker
my_tracker = ProjectTracker("Python Learning Journey")

# 2. Add sample learning milestones
print("\n--- Adding Milestones ---")
my_tracker.add_task("Learn Python Basics")
my_tracker.add_task("Create Password Shield Tool")
my_tracker.add_task("Build Neon Geometric Art")
my_tracker.add_task("Complete GitHub Profile README")

# 3. Show initial dashboard (0% Progress)
my_tracker.show_dashboard()

# 4. Simulating progress by completing tasks
time.sleep(1.5)
print("--- Updating Progress ---")
my_tracker.complete_task("Learn Python Basics")
my_tracker.complete_task("Create Password Shield Tool")

# 5. Show final updated dashboard
my_tracker.show_dashboard()
