# PRIORITIZER

A small, friendly command-line Study Task Prioritizer that helps you decide what to work on next. Enter tasks, rate their importance and urgency (1–5), and PRIORITIZER computes a priority score and suggests what to do.

Project.py implements the CLI.

## Features
- Add tasks with a name, importance (1–5) and urgency (1–5)
- Priority score = importance × urgency
- Sorts tasks by priority score (highest first)
- Shows the top task with a quick action suggestion:
  - Critical tasks (score ≥ 16) — "DO THIS NOW!"
  - High importance — "Plan it"
  - High urgency — "Delegate/Maybe"
  - Otherwise — "Do later"

## Requirements
- Python 3.6 or newer
- No external packages required

## Installation
1. Clone the repository:
   git clone https://github.com/Vedant123-Pande/PRIORITIZER.git
2. Change into the project directory:
   cd PRIORITIZER

## Usage
Run the CLI script:
python Project.py

You will see a menu:
1. Add a new task
2. Show all tasks (sorted)
3. What's my #1 task right now?
4. Exit

When adding a task you'll be prompted for:
- Task name (cannot be empty)
- Importance (1 = meh, 5 = exam tomorrow)
- Urgency (1 = whenever, 5 = due in 2 hours)

Example session
```
Welcome to Your Study Task Prioritizer!

--- Menu ---
1. Add a new task
2. Show all tasks (sorted)
3. What's my #1 task right now?
4. Exit

What do you want to do? (1-4): 1

=== ADD NEW TASK ===
What do you have to do? Finish math homework
How important is it? (1 = meh, 5 = exam tomorrow) → 5
How urgent is it? (1 = whenever, 5 = due in 2 hours) → 4
Added! → Finish math homework (Priority: 20)
```

Show all (sorted) will display tasks with Importance, Urgency, Score and a suggested action.

## How scoring works
- Score = importance × urgency (range 1–25)
- Tasks are sorted by this score in descending order
- Suggestions are based on importance and urgency thresholds:
  - imp ≥ 4 and urg ≥ 4 → DO THIS NOW!
  - imp ≥ 4 → Plan it
  - urg ≥ 4 → Delegate/Maybe
  - otherwise → Do later

## Contributing
Contributions, bug reports and suggestions are welcome. Open an issue or submit a pull request.

If you'd like to:
- Add persistence (save/load tasks to a file)
- Add tags or due dates
- Add interactive filtering or search
these would be nice improvements.

## License
This project is open — feel free to use it and modify it.

## Author
Vedant123-Pande

Enjoy organizing your study tasks!
