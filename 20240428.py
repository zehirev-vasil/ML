# region Task 1

# bmi_categories = {"Underweight": "less than 18.5",
#                   "Normal weight": "18.5–24.9",
#                   "Overweight": "25–29.9",
#                   "Obesity": "30 or more"}
#
#
# def calculate_bmi(weight, height):
#     return round(weight / (height ** 2), 2)
#
#
# user_weight = float(input("Enter your weight in kg: "))
# user_height = float(input("Enter your height in meters: "))
# user_bmi = calculate_bmi(user_weight, user_height)
#
# print(f"Your BMI is: {user_bmi}")
#
# for category, range in bmi_categories.items():
#     if user_bmi < float(range.split("–")[0]):
#         print(f"You are {category}")
#         break
#     elif user_bmi <= float(range.split("–")[1]):
#         print(f"You are {category}")
#         break


# endregion

# region Task 2

# def get_user_data(**kwargs):
#     while True:
#         try:
#             for key, value in kwargs.items():
#                 if key == "name" and len(value) <= 2:
#                     raise ValueError("Name is too short. Please re-enter it.")
#                 elif key == "height" and not (50 <= value <= 250):
#                     raise ValueError("Height is not within the valid range (50-250). Please re-enter it.")
#                 elif key == "weight" and not (5 <= value <= 300):
#                     raise ValueError("Weight is not within the valid range (5-300). Please re-enter it.")
#             break  # if no exception was raised, break the loop
#         except ValueError as e:
#             print(e)
# Here you can add the code to re-enter the data


# endregion

# region Task 3

# def generate_random_number():
#     import random
#     return random.randint(1, 100)
#
#
# def user_guess():
#     while True:
#         try:
#             user_input = int(input("Enter your guess: "))
#             if not (1 <= user_input <= 100):
#                 raise ValueError("Invalid input. Please enter a number between 1 and 100.")
#             break
#         except ValueError as e:
#             print(e)
#     return user_input
#
#
# def check_guess(random_number, user_guess):
#     if user_guess < random_number:
#         print("Your guess is too low.")
#     elif user_guess > random_number:
#         print("Your guess is too high.")
#     else:
#         print("Congratulations! You guessed the number correctly.")
#
#
# def play_game():
#     random_number = generate_random_number()
#     print("I have generated a random number between 1 and 100. Try to guess it.")
#     while True:
#         user = user_guess()
#         check_guess(random_number, user)
#         if random_number == user:
#             break
#
#
# play_game()

# endregion

# region Task 4

# list_of_books = []
#
#
# def add_new_book(ISBN, title, author, status='available', borrower=None):
#     # Check if the book is already in the list
#     for book in list_of_books:
#         if book['ISBN'] == ISBN:
#             print("Book already exists.")
#             break
#         else:
#             list_of_books.append(
#                 {'ISBN': ISBN, 'title': title, 'author': author, 'status': status, 'borrower': borrower})
#             print("Book added successfully.")
#
#
# def borrow_a_book(ISBN, borrower):
#     for book in list_of_books:
#         if book['ISBN'] == ISBN:
#             if book['status'] == 'available':
#                 book['status'] = 'borrowed'
#                 book['borrower'] = borrower
#                 print(f"{book['title']} has been borrowed by {borrower}.")
#             else:
#                 print(f"{book['title']} is not available for borrowing.")
#             break
#     else:
#         print("Book not found.")
#
#
# def return_a_book(ISBN):
#     for book in list_of_books:
#         if book['ISBN'] == ISBN:
#             if book['status'] == 'borrowed':
#                 book['status'] = 'available'
#                 book['borrower'] = None
#                 print(f"{book['title']} has been returned.")
#             else:
#                 print(f"{book['title']} is not borrowed.")
#             break
#     else:
#         print("Book not found.")
#
#
# def list_books():
#     for book in list_of_books:
#         print(
#             f"Title: {book['title']}, Author: {book['author']}, Status: {book['status']}, Borrower: {book['borrower']}")

# endregion
