# find_ft_type.py
def all_thing_is_obj(object: any) -> int:
    """
    Print the type of the object and return 42.
    The type should be capitalized.
    """
    obj_type = type(object).__name__
    if obj_type in ['list', 'tuple', 'set', 'dict']:
        print(f"{obj_type.capitalize()} : {type(object)}")
    elif obj_type == 'str':
        print(f"{object} : {type(object)}")
    else:
        print("Type not found")
    return 42
