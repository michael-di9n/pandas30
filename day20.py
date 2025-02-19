import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    # group courses by class
    class_group = courses.groupby('class')
    # count number students in each class
    counts = class_group.size()
    # get a list of all classes with > 5 elements
    valid_count = counts >= 5
    #return those clases
    listOfValidClasses = valid_count[valid_count].index.tolist()
    return pd.DataFrame({'class': listOfValidClasses})
