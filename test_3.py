# # Student Grade Book
# # Build a grade book that stores student names and scores in a dictionary. Your program calculates the class average, 
# finds the top and bottom scorer, and lets the user look up any student's grade.

# # What you need to use
# # ------------------------------------------------------------------------
# # 1.  dictionary      →  store at least 5 student name-score pairs
# # 2.  for loop        →  to calculate the class average
# # 3.  max() min()     →  to find the top and bottom scorer
# # 4.  .get()          →  to look up a student by name
# # 5.  input()         →  to let the user search for a student
# # ------------------------------------------------------------------------

# # What you'll be marked on
# # ------------------------------------------------------------------------
# # 1.  Dictionary created with at least 5 student name-score pairs  →   5 marks
# # 2.  A loop correctly calculates and prints the class average      →  10 marks
# # 3.  Highest and lowest scores and students identified             →  10 marks
# # 4.  .get() used to look up student — friendly message if missing  →  10 marks
# # 5.  Program runs without any errors                               →   5 marks
# # ========================================================================
# # Total  →  40 marks
# ========================================================================

print("Welcome to the Class-8F Grade Book!")

grade_book={"Vedant": 95 , "Vihaan": 90, "Nayan": 92, "Yuvraj": 85, "Parv": 87}
print("The Grade Book of Class 8-F is:", grade_book)

summ=0
for value in grade_book.values():
    summ+=value

average=summ/len(grade_book)
print(f"The average marks of the class is {average}")

maximum=max(grade_book.values())
minimum=min(grade_book.values())

print(f"The highest scorer of the class is {maximum} and the lowest scorer is {minimum}")

ask=input("Which student's marks do you want to see?")

print(f"The marks of {ask} is {grade_book.get(ask)}")

