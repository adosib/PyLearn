# ----------------------- Lists --------------------------
# Extend lists
courses = ['Hisotry', 'Math', 'CompSci', 'Physics']
courses2 = ['Japanese', 'Statistics']
courses.extend(courses2)
print(courses)

# Remove values from a list
courses.remove('Math')
print(courses)

# Remove last element of a list
courses.pop()  # returns the value removed
print(courses)

# Reverse list
courses.reverse()
print(courses)

# Sort list
courses.sort()
print(courses)


# Can sort without changing original list object stored to variable courses
sorted_courses = sorted(courses)  # courses variable doens't change
