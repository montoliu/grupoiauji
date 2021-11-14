# return True is actual_card is better than prev_card
def is_better_card(actual_card, prev_card, trump_card, round_card):
    # both cards are trump type
    if actual_card.get_type() == trump_card.get_type() and prev_card.get_type() == trump_card.get_type():
        if actual_card.get_value() > prev_card.get_value():
            return True
        else:
            return False
    elif actual_card.get_type() == trump_card.get_type():
        return True
    elif prev_card.get_type() == trump_card.get_type():
        return False
    elif actual_card.get_type() == round_card.get_type() and prev_card.get_type() == round_card.get_type():
        if actual_card.get_value() > prev_card.get_value():
            return True
        else:
            return False
    elif actual_card.get_type() == round_card.get_type():
        return True
    elif prev_card.get_type() == round_card.get_type():
        return False
    if actual_card.get_value() > prev_card.get_value():
        return True
    return False