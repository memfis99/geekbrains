def salary(work_hour, amount_in_hour, bonus) :
    try:
        return work_hour * amount_in_hour + bonus
    except TypeError:
        return
