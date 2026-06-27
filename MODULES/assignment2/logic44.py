from .logic33 import percentage
def grade(rollno):
    gra = percentage(rollno)

    if 100 >= gra >= 90:
        return "A+"
    elif 90 > gra >80:
        return ("A")
    elif 80 > gra > 70:
        return ("B")
    elif 70 > gra > 60:
        return ("C")
    elif 60 > gra > 50:
        return ("D")
    else:
        return ("Fail")