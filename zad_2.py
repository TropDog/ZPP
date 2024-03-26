from datetime import datetime
from zad_1 import Student, student1, student2, student3


class Library:
    def __init__(
        self, city: str, street: str, zip_code: str, open_hours: str, phone: str
    ) -> None:
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f'''Library:
          {self.street},
          {self.city},
          {self.zip_code}\n
          Open Hours:{self.open_hours}\n
          Phone: {self.phone}'''


class Employee:
    def __init__(
        self,
        first_name: str,
        last_name: str,
        hire_date: datetime,
        birth_date: datetime,
        city: str,
        street: str,
        zip_code: str,
        phone: str,
    ) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f'''Employee: {self.first_name} {self.last_name}\n
        Hire Date: {self.hire_date}\nBirth Date: {self.birth_date}\n
        Address: {self.street}, {self.city}, {self.zip_code}\n
        Phone: {self.phone}'''


class Book:
    def __init__(
        self,
        library: Library,
        publication_date: datetime,
        author_name: str,
        author_surname: str,
        number_of_pages: int,
    ) -> None:
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f'''Book Details:\n
        Library city: {self.library.city}\n
        Publication Date: {self.publication_date}\n
        Author: {self.author_name} {self.author_surname}\n
        Number of Pages: {self.number_of_pages}'''


class Order:
    def __init__(
        self, employee: Employee, student: Student, books: list, order_date: datetime
    ) -> None:
        self.employee = employee
        self.student = student
        for book in books:
            if not isinstance(book, Book):
                raise TypeError(
                    "All elements in the 'books' list must be instances of the Book class."
                )
        self.books = books
        self.order_date = order_date

    def __str__(self):
        book_titles = [book.author_name for book in self.books]
        return f'''Order Details:\n
        Employee: {self.employee.first_name} {self.employee.last_name}\n
        Student: {self.student.name}\nBooks: {', '.join(book_titles)}\n
        Order Date: {self.order_date}'''

library1 = Library("Katowice", "3-maja", "40-507", "8-16", "997997997")
library2 = Library("Sosnowiec", "3-maja", "40-507", "8-16", "997997997")
# print(str(library1))

employee1 = Employee(
    "Mateusz",
    "P",
    datetime.strptime("2020-01-01", "%Y-%m-%d"),
    datetime.strptime("2000-01-01", "%Y-%m-%d"),
    "Katowice",
    "3-Maja",
    "40-501",
    "123123123",
)
print(str(employee1))

book1 = Book(
    library1, datetime.strptime(
        "2020-01-01", "%Y-%m-%d"), "author", "surname", 500
)
book2 = Book(
    library2, datetime.strptime(
        "2020-01-01", "%Y-%m-%d"), "author2", "surname", 500
)
book3 = Book(
    library1, datetime.strptime(
        "2020-01-01", "%Y-%m-%d"), "author3", "surname", 500
)
book4 = Book(
    library2, datetime.strptime(
        "2020-01-01", "%Y-%m-%d"), "author4", "surname", 500
)
book5 = Book(
    library2, datetime.strptime(
        "2020-01-01", "%Y-%m-%d"), "author5", "surname", 500
)

# print(str(book2))

order1 = Order(
    employee1,
    student1,
    [book1, book2, book3, book4, book5],
    datetime.strptime("2023-01-01", "%Y-%m-%d"),
)
print(str(order1))
