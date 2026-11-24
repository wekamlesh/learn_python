
# Creating a class like a blueprint
class StudySession:
    def __init__(self, topic, minutes):
        self.topic = topic
        self.minutes = minutes
    # describing the fuction in the class
    def describe(self):
        return f'{self.topic}: {self.minutes} minutes'

# loop though the session to provide the data (the session is created below)
def total_minutes(sessions):
    return sum(session.minutes for session in sessions)

# Creating a session array
python_session = StudySession("python functions", 30)
git_session = StudySession("Git basics", 20)

# adding the session data to the session array
sessions = [python_session, git_session]

# Loop though the sessions
for session in sessions:
    print(session.describe())

# print the sessions
print(f"Total: {total_minutes(sessions)} ,minutes")
