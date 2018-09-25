# 8-15. Printing Models: Put the functions for the example print_models.py in a
# separate file called printing_functions.py. Write an import statement at the top
# of print_models.py, and modify the file to use the imported functions.
"""Functions related to printing 3D models."""

def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until there are none left.
    Move each design  to completed_models after printing.
    """

    while unprinted_designs:
        current_design = unprinted_designs.pop()

        # Simulate creating a 3d print from the design.
        print("printing model: " + current_design)
        completed_models.append(current_design)
def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

# 8-16. Imports: Using a program you wrote that has one function in it, store that
# function in a separate file. Import the function into your main program file, and
# call the function using each of these approaches:
# import module_name
# from module_name import function_name
# from module_name import function_name as fn
# import module_name as mn
# from module_name import *
# 8-17. Styling Functions: Choose any three programs you wrote for this chapter,
# and make sure they follow the styling guidelines described in this section.

