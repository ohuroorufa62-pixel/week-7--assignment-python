# Python Lists Practice

This project contains Python exercises for practicing lists, loops, and list methods.

The `in` keyword is important because it checks whether an item exists in a list before we try to remove it. For example, using `if item in shopping_list:` prevents the program from trying to remove an item that is not in the list. Without this check, Python can give a `ValueError` when `.remove()` is used on an item that does not exist.

Using `in` makes the program safer and helps give the user a clear message when the item is not on the list.
