def individual_person(person):
    return {
        # "id": person["_id"],
        "name": person["name"],
        "email": person["email"],
        "age": person["age"]
    }



def list_of_persons(persons):
    return [individual_person(p) for p in persons]