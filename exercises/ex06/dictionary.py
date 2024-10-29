"""Exercise that uses utility functions with dictionaries"""

__author__ = "730735704"


def invert(org_dict: dict[str, str]) -> dict[str, str]:
    """Inverts keys and values in a dictionary"""
    inverted_dict: dict[str, str] = {}  # empty dictionary to be returned
    for item in org_dict:  # goes through each item in the input dictionary
        if org_dict[item] in inverted_dict:  # error if two of the same key
            raise KeyError("Can't have two of the same key")
        key: str = item
        inverted_dict[org_dict[item]] = key  # inverts the key and values
    return inverted_dict


def favorite_color(colors_dict: dict[str, str]) -> str:
    """Finds and returns the most popular color from a dictionary"""
    if colors_dict == {}:
        return ""
    colors: list[str] = []  # empty string to track the colors
    totals: dict[str, int] = {}  # empty dictionary to be returned
    for item in colors_dict:  # adds each color to colors list
        colors.append(colors_dict[item])
    for color in colors:  # goes through each item in colors list
        count: int = 0  # counts number of times a color occurs
        idx: int = 0
        while idx < len(colors):
            if colors[idx] == color:
                count += 1  # adds to count if color appears
            idx += 1
        totals[color] = count  # key is color and value is count
    most_popular: str = colors[0]  # sets most popular as the first color
    for clr in totals:  # goes through each item in totals dictionary
        if (
            totals[clr] > totals[most_popular]
        ):  # checks if value for current is bigger than value for most_popular
            most_popular = clr  # replaces most_popular
    return most_popular


def count(org_list: list[str]) -> dict[str, int]:
    """Counts the number of items that appear in a list and returns a dictionary"""
    result: dict[str, int] = {}  # empty list to be returned
    for item in org_list:  # goes through each item in org_list
        if item in result:  # if item has already been added to the dictionary
            result[item] += 1
        else:
            result[item] = 1  # adds item as a key to the dictionary with value 1
    return result


def alphabetizer(org_list: list[str]) -> dict[str, list[str]]:
    """Each key is a letter and value is a list of words beginning with the letter"""
    result: dict[str, list[str]] = {}  # empty dictionary to return
    first_letter: list[str] = []  # creates a list of the first letters
    for item in org_list:  # adds each first letter to first_letter
        first_letter.append(item[0].lower())
    for letter in first_letter:  # goes through each item in first_letter
        current_letter: str = letter  # current_letter is the item it is going through
        current_letter_list: list[str] = []  # list of words beginning with the letter
        for word in org_list:  # goes through each item in org_list
            if word[0].lower() == current_letter:  # first letter = the current letter
                current_letter_list.append(word)
            result[current_letter] = current_letter_list  # creates new key/value
    return result


def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> None:
    """Updates a given attendance dictionary with additional students and days"""
    students_that_day: list[str] = []  # empty string that tracks attendance
    if day in attendance:  # checks if day is already in attendance dictionary
        for item in attendance:  # creates a list for input students
            students_that_day = attendance[item]
        if student not in students_that_day:  # does not repeat
            students_that_day.append(student)  # adds new student to that list
        attendance[day] = students_that_day  # updates value for the key(day)
    else:  # if day is not already in attendance dictionary
        students_that_day = [student]  # list = the one student for the day
        attendance[day] = students_that_day  # creates new key/value in dictionary
