def meal(day,time):
    if day=="sunday":
        if time=="breakfast":
            return "dosa"
        elif time=="lunch":
            return "dal rice"
        elif time=="dinner":
            return "panir and chapati"
        else:
            return "time not found"
    elif day=="monday":
        if time=="breakfast":
            return "phoha"
        elif time=="lunch":
            return "polav"
        elif time=="dinner":
            return "roti sabji"
        else:
            return "time not found"
    elif day=="other":
        if time=="breakfast":
            return "halwa"
        elif time=="lunch":
            return "dal rice and sabji"
        elif time=="dinner":
            return "puri sabji"
        else:
            return "time not found"
print(meal("sunday","lunch"))
print(meal("monday","dinner"))
