"""
Sproutl Technical Python Interview - Theory Assessment

@Test Author: Vishal Soomaney
"""

remove_duplicates_tuples_argument = [("plant_type_1","height_1"),("plant_type_2", "height_2"),("plant_type_1", "height_1")]
remove_duplicates_lists_argument = [["plant_type_1"],["plant_type_2"],["plant_type_1"]]
kwargs_argument = None

def remove_duplicate_tuples_unsolved(duplicate_tuples):
    """
    Remove potential duplicate tuples from list of tuples.
    """

def remove_duplicate_lists_unsolved(duplicate_lists):
    """
    Remove potential duplicate lists from list of lists.
    """

def fix_bug_1_unsolved(my_list):
    """
    Fix the bug in the function.
    """

    for element in my_list:
        print ("I will not kill my plants today")
        my_list.remove(element)

def fix_bug_2_unsolved(**kwargs):
    """
    Fix the bug in the function.
    """

    my_counter = 0

    for element in kwargs:
        my_counter += 1

    return my_counter

if __name__ == "__main__":
    """
    To run test solutions (replace contents with "unsolved" and remove the 'kwargs_argument' variable altogether)
    """
    print(remove_duplicate_tuples_unsolved(remove_duplicates_tuples_argument))
    print(remove_duplicate_lists_unsolved(remove_duplicates_lists_argument))
    fix_bug_1_unsolved(remove_duplicates_tuples_argument)
    print(fix_bug_2_unsolved(kwargs_argument))
