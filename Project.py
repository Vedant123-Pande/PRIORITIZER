class StudyTaskPrioritizer:
    def __init__(self):
        self.tasks = []

    def _get_valid_score(self, prompt: str):
        """Get a valid score between 1 and 5 from user input."""
        while True:
            try:
                score = int(input(prompt))
                if 1 <= score <= 5:
                    return score
                else:
                    print("Score must be an integer between 1 and 5. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a whole number.")

    def add_task_interactive(self):
        print("\n" + "="*50)
        print("          ADD NEW STUDY TASK")
        print("="*50)
        
        name = input("Task description: ").strip()
        while not name:
            print("Task name cannot be empty!")
            name = input("Task description: ").strip()

        importance = self._get_valid_score("Importance (1=Low, 5=Very High): ")
        urgency = self._get_valid_score("Urgency (1=Not urgent, 5=Due soon): ")

        priority_score = importance * urgency

        task = {
            'name': name,
            'importance': importance,
            'urgency': urgency,
            'priority_score': priority_score
        }
        self.tasks.append(task)
        print(f"\nTask added! → '{name}'")
        print(f"Priority Score: {priority_score} (Importance×Urgency = {importance}×{importance}×{urgency})")
        print("="*50)

    def prioritize_tasks(self):
        """Sort tasks by priority score descending."""
        self.tasks.sort(key=lambda t: t['priority_score'], reverse=True)

    def display_tasks(self):
        if not self.tasks:
            print("\nNo tasks yet. Add some using option 1!")
            return

        self.prioritize_tasks()
        print("\n" + "="*90)
        print("                PRIORITIZED STUDY TASK LIST")
        print("="*90)
        print(f"{'Rank':<4} {'Task':<40} {'Imp':<6} {'Urg':<6} {'Priority':<10} {'Category'}")
        print("-"*90)

        for i, task in enumerate(self.tasks, 1):
            category = (
                "Do Now!" if task['importance'] >= 4 and task['urgency'] >= 4 else
                "Plan" if task['importance'] >= 4 else
                "Delegate" if task['urgency'] >= 4 else
                "Later"
            )
            print(f"{i:<4} {task['name']:<40} {task['importance']:<6} {task['urgency']:<6} "
                  f"{task['priority_score']:<10} {category}")

        print("-"*90)

    def get_top_priority_task(self):
        if not self.tasks:
            print("\nNo tasks available. Add one first!")
            return

        self.prioritize_tasks()
        top = self.tasks[0]
        category = "CRITICAL – DO FIRST!" if top['priority_score'] >= 16 else "High Priority"

        print("\n" + "!"*60)
        print("                   TOP PRIORITY TASK")
        print("!"*60)
        print(f"   Task: {top['name']}")
        print(f"   Priority Score: {top['priority_score']} ({top['importance']} × {top['urgency']})")
        print(f"   Category: {category}")
        print("   Get this done now to reduce stress and make progress!")
        print("!"*60)

    def run(self):
        print("Welcome to Your Study Task Prioritizer!")
        print("Based on the Eisenhower Principle (Importance × Urgency)\n")

        while True:
            print("\n--- Menu ---")
            print("1. Add a new study task")
            print("2. View all tasks (prioritized)")
            print("3. Show today's top priority task")
            print("4. Exit")
            choice = input("\nChoose an option (1-4): ").strip()

            if choice == '1':
                self.add_task_interactive()
            elif choice == '2':
                self.display_tasks()
            elif choice == '3':
                self.get_top_priority_task()
            elif choice == '4':
                print("\nKeep up the great work! Goodbye! 👋\n")
                break
            else:
                print("Invalid option. Please enter 1, 2, 3, or 4.")


# Run the assistant
if __name__ == "__main__":
    assistant = StudyTaskPrioritizer()
    assistant.run()
