#Formative Assessment 1: Calvario_FA1.py
class Publication:
    def __init__(self, title_name, author_name):
        self.__p_title = title_name
        self.__p_author = author_name

    def fetch_title(self):
        return self.__p_title

    def fetch_author(self):
        return self.__p_author

    def update_title(self, new_title):
        self.__p_title = new_title

    def update_author(self, new_author):
        self.__p_author = new_author

    def display_info(self):
        print(f"Title: {self.__p_title}\nAuthor: {self.__p_author}")


class Book(Publication):
    def __init__(self, title_name, author_name, page_count):
        super().__init__(title_name, author_name)
        self.__total_pages = 0
        self.change_pages(page_count)

    def fetch_pages(self):
        return self.__total_pages

    def change_pages(self, page_count):
        if page_count <= 0:
            print("The number of pages must be positive.")
        else:
            self.__total_pages = page_count

    def display_info(self):
        super().display_info()
        if self.__total_pages > 0:
            print(f"Number of pages: {self.__total_pages}")


class Magazine(Publication):
    def __init__(self, title_name, author_name, issue_id):
        super().__init__(title_name, author_name)
        self.__num_issue = 0
        self.change_issue(issue_id)

    def fetch_issue(self):
        return self.__num_issue

    def change_issue(self, issue_id):
        if issue_id <= 0:
            print("The issue number must be positive.")
        else:
            self.__num_issue = issue_id

    def display_info(self):
        super().display_info()
        if self.__num_issue > 0:
            print(f"Issue number: {self.__num_issue}")


if __name__ == "__main__":
    print("=== Library Publication Records ===")
    p1 = Publication("Research Journal A", "Dr. Smith")
    p2 = Publication("Historical Review B", "Prof. Jones")
    p1.display_info()
    print("-" * 20)
    p2.display_info()
    print()

    print("=== Library Book Inventory ===")
    b1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
    b2 = Book("Invalid Book Entry", "Anonymous", -12)
    b1.display_info()
    print("-" * 20)
    b2.display_info()
    print()

    print("=== Library Magazine Inventory ===")
    m1 = Magazine("National Geographic", "Various Authors", 202)
    m2 = Magazine("Invalid Magazine Entry", "Various Authors", 0)
    m1.display_info()
    print("-" * 20)
    m2.display_info()
