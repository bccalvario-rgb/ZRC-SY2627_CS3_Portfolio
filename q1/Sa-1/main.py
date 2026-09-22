class AssignmentSubmission:
    def __init__(self, student_name: str, student_id: str, assignment_title: str, due_date: str):
        self.student_name = student_name
        self.student_id = student_id
        self._assignment_title = assignment_title
        self._due_date = due_date
        self.__is_submitted = False
        self.__grade = None
        self.__submitted_files = []

    def __validate_grade(self, score: float) -> bool:
        return 0 <= score <= 100

    def __check_submission_status(self) -> bool:
        return len(self.__submitted_files) > 0

    def __is_duplicate(self, filename: str) -> bool:
        return filename in self.__submitted_files

    def add_file(self, filename: str):
        if self.__grade is not None:
            print("Cannot add file. Already graded.")
            return
        
        if self.__is_duplicate(filename):
            print(f"Duplicate Warning: File '{filename}' is already inside the list.")
            return
        
        self.__submitted_files.append(filename)
        self.__is_submitted = True

    def remove_file(self, filename: str):
        if self.__grade is not None:
            print("Cannot remove file. Already graded.")
            return
        
        if filename in self.__submitted_files:
            self.__submitted_files.remove(filename)
            if not self.__check_submission_status():
                self.__is_submitted = False

    def assign_grade(self, score: float):
        if not self.__check_submission_status():
            print("Error: No files submitted")
            return
        
        if not self.__validate_grade(score):
            print("Error: Invalid grade")
            return
        
        self.__grade = float(score)

    def get_grade(self) -> str:
        if self.__grade is None:
            return "Not Graded"
        return str(self.__grade)

    def view_files(self) -> str:
        if not self.__submitted_files:
            return "No files"
        return ", ".join(self.__submitted_files)

    def get_status_report(self) -> str:
        status = "Submitted" if self.__is_submitted else "No files submitted"
        return f"Student: {self.student_name} ({self.student_id}) | Class: {self._assignment_title} | Status: {status} | Files: {self.view_files()} | Grade: {self.get_grade()}"


# --- INITIALIZING DROPBOX FOR STUDENTS ---
print("--- INITIALIZING DROPBOX FOR STUDENTS ---")
student1 = AssignmentSubmission(student_name="Alex Gonzaga", student_id="pshs-1090-x", assignment_title="CS-101", due_date="2026-10-01")
student2 = AssignmentSubmission(student_name="Adelle", student_id="pshs-1920-x", assignment_title="CS-103", due_date="2026-10-01")
student3 = AssignmentSubmission(student_name="Jacen Necesario", student_id="pshs-1077-x", assignment_title="CS-101", due_date="2026-10-01")
student4 = AssignmentSubmission(student_name="Bienvenido Calvario", student_id="pshs-1067-x", assignment_title="CS-101", due_date="2026-10-01")
student5 = AssignmentSubmission(student_name="Adriel Omalsa", student_id="pshs-1069-x", assignment_title="CS-101", due_date="2026-10-01")
print()

print("--- TEST SCENARIO 1: Multiple Files via List ---")
student1.add_file("main.py")
student1.add_file("report.pdf")
student1.assign_grade(95)
print(f"Alex's Files: {student1.view_files()}\n")

print("--- TEST SCENARIO 2: Removing Files from List ---")
student2.add_file("wrong_homework.docx")
student2.remove_file("wrong_homework.docx")
student2.add_file("correct_project.py")
student2.assign_grade(88)
print(f"Adelle's Files: {student2.view_files()}\n")

print("--- TEST SCENARIO 3: Preventing Duplicate Files ---")
student3.add_file("script.py")
student3.add_file("script.py")
print(f"Jacen's Files: {student3.view_files()}\n")

print("--- TEST SCENARIO 4: Removing file after being graded ---")
student4.add_file("exam_answers.pdf")
student4.assign_grade(75)
student4.remove_file("exam_answers.pdf")
print()

print("--- TEST SCENARIO 5: Empty List Handling ---")
student5.add_file("draft.txt")
student5.remove_file("draft.txt")
student5.assign_grade(100)
print()

print("--- FINAL SYSTEM REPORT ---")
print(student1.get_status_report())
print(student2.get_status_report())
print(student3.get_status_report())
print(student4.get_status_report())
print(student5.get_status_report())
