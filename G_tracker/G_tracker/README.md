GitHub Profile Tracker
A small Python project that takes a GitHub username, gets the user's public profile details from the GitHub API, and saves them into an Excel file.

I made this project to practise using APIs, Python and Excel files.
What it does
1. Asks for a GitHub username.
2. Sends a request to the GitHub API.
3. Gets public profile information such as:
   - Name and username
   - Bio and location
   - Public repository count
   - Followers and following
   - Account creation date
4. Saves the information in new.xlsx.
Built with
- Python
- requests – to get data from the GitHub API
- pandas – to organise the data
- openpyxl – to write the Excel file
Run it:
Install the required packages:


pip install requests pandas openpyxl


Run the Python file:
python github_tracker.py
Enter a GitHub username when asked. After a successful request, the Excel file new.xlsx will be created in the same folder.
A small note
The project uses real, public profile data from GitHub. It does not access private repositories or private account information. Some profile details, such as a user's name, bio or location, may be empty if the user has not added them.

This is a beginner project, and I plan to improve it as I learn more Python.
