def NULL_not_found(object: any) -> int:
    """Function that checks different NULL types"""
    match object:
        case None:
            print(f"Nothing: {object} {type(object)}")
        case float() if str(object) == 'nan':
            print(f"Cheese: {object} {type(object)}")
        case 0:
            print(f"Zero: {object} {type(object)}")
        case '':
            print(f"Empty: {type(object)}")
        case False:
            print(f"Fake: {object} {type(object)}")
        case _:
            print("Type not Found")
            return 1
    return 0
