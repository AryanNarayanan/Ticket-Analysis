CATEGORIES = ("Billing", "Technical", "Account", "Delivery", "General")
PRIORITIES = ("Low", "Medium", "High", "Critical")


PRIORITY_SCORE = {"Low": 1, "Medium": 2, "High": 3, "Critical": 4}


def print_header(title):

    print("\n" + "=" * 60)
    print(title.center(60))
    print("=" * 60)


def show_table(df):
    
    if len(df) == 0:
        print("No records found.")
    else:
        print(df.to_string(index=False))


def get_number(message, low, high):
   
    while True:
        text = input(message)
        if text.isdigit() and low <= int(text) <= high:
            return int(text)
        print("Please enter a number between", low, "and", high)


def unique_values(records, key):

    result = set()
    for r in records:
        result.add(r[key])
    return sorted(result)


def count_by(records, key):

    counts = {}
    for r in records:
        value = r[key]
        counts[value] = counts.get(value, 0) + 1     # dict method get()
    return counts


def list_methods_demo():

    hours = [10, 25, 8]
    hours.append(40)
    hours.extend([5, 60])
    hours.insert(0, 15)
    hours.remove(25)
    hours.sort()
    return hours


def dict_methods_demo():
 
    scores = dict(PRIORITY_SCORE)
    scores.update({"Urgent": 5})
    print("keys   :", list(scores.keys()))
    print("values :", list(scores.values()))
    for name, score in scores.items():
        print("  ", name, "->", score)
    scores.pop("Urgent")
