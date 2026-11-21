import csv
import random
import datetime

random.seed(7)

categories = ["Billing", "Technical", "Account", "Delivery", "General"]
priorities = ["Low", "Medium", "High", "Critical"]
agents = ["Amit", "Neha", "Rohit", "Sana", "Vikas"]
customers = ["Aarav", "Diya", "Rahul", "Priya", "Karan", "Isha", "Arjun", "Meera",
             "Rohan", "Kavya", "Sneha", "Aditya", "Pooja", "Kabir", "Riya", "Sai"]


def make_tickets(file_name="tickets.csv", count=80):
    file = open(file_name, "w", newline="")
    writer = csv.writer(file)
    writer.writerow(["ticket_id", "customer", "category", "priority", "status", "agent",
                     "created_date", "response_hours", "resolution_hours", "satisfaction"])

    start = datetime.date(2026, 1, 1)
    for i in range(1, count + 1):
        category = random.choice(categories)
        priority = random.choice(priorities)
        status = random.choice(["Open", "In Progress", "Resolved", "Resolved", "Closed", "Closed"])
        created = start + datetime.timedelta(days=random.randint(0, 300))
        response = random.randint(1, 24)

        if status == "Open" or status == "In Progress":
            resolution = ""
            rating = ""
        else:
            if priority == "Critical":
                resolution = random.randint(2, 12)
            elif priority == "High":
                resolution = random.randint(6, 30)
            elif priority == "Medium":
                resolution = random.randint(12, 60)
            else:
                resolution = random.randint(24, 120)
            # faster resolution -> better rating
            if resolution < 15:
                rating = random.randint(4, 5)
            elif resolution < 50:
                rating = random.randint(3, 4)
            else:
                rating = random.randint(1, 3)

        if i in (12, 33, 58):        # a few missing response times
            response = ""

        writer.writerow([5000 + i, random.choice(customers), category, priority, status,
                         random.choice(agents), created, response, resolution, rating])
    file.close()
    print("Created", file_name, "with", count, "records")


if __name__ == "__main__":
    make_tickets()
