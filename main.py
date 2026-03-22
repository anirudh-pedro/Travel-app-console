from user import User
from destination import Destination
from itinerary import Itinerary
from booking import Booking
from review import Review
from expense import Expense

current_user = None
user_itineraries = {}

while True:
    print("\n===== Travel Planning App =====")
    print("1. Register")
    print("2. Login")
    print("3. Add Destination")
    print("4. Search Destination")
    print("5. Create Itinerary")
    print("6. Add Itinerary Item")
    print("7. View Itinerary")
    print("8. Make Booking")
    print("9. Add Review")
    print("10. Add Expense")
    print("0. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        email = input("Enter email: ")
        password = input("Enter password: ")
        current_user = User.register(name, email, password)
        print("Registered successfully!")

    elif choice == "2":
        email = input("Enter email: ")
        password = input("Enter password: ")
        user = User.login(email, password)
        if user:
            current_user = user
            print("Login successful!")
        else:
            print("Invalid credentials")

    elif choice == "3":
        name = input("Destination name: ")
        region = input("Region: ")
        desc = input("Description: ")
        Destination(name, region, desc)
        print("Destination added!")

    elif choice == "4":
        name = input("Search name: ")
        results = Destination.search(name)
        for d in results:
            print(d)

    elif choice == "5":
        if not current_user:
            print("Login first!")
            continue

        title = input("Itinerary title: ")
        iti = Itinerary(current_user.get_user_id(), title)
        user_itineraries[current_user.get_user_id()] = iti
        print("Itinerary created!")

    elif choice == "6":
        if not current_user:
            print("Login first!")
            continue

        iti = user_itineraries.get(current_user.get_user_id())
        if not iti:
            print("Create itinerary first!")
            continue

        name = input("Place: ")
        desc = input("Description: ")
        date = input("Date: ")
        iti.add_item(name, desc, date)
        print("Item added!")

    elif choice == "7":
        if not current_user:
            print("Login first!")
            continue

        iti = user_itineraries.get(current_user.get_user_id())
        if iti:
            print("\nYour Itinerary:")
            for item in iti.get_items():
                print(item)
        else:
            print("No itinerary found")

    elif choice == "8":
        if not current_user:
            print("Login first!")
            continue

        btype = input("Booking type (Flight/Hotel): ")
        details = input("Details: ")
        Booking.create(current_user.get_user_id(), btype, details)
        print("Booking done!")

    elif choice == "9":
        if not current_user:
            print("Login first!")
            continue

        dest_id = int(input("Destination ID: "))
        rating = int(input("Rating (1-5): "))
        comment = input("Comment: ")
        Review.add_review(current_user.get_user_id(), dest_id, rating, comment)
        print("Review added!")

    elif choice == "10":
        if not current_user:
            print("Login first!")
            continue

        amount = float(input("Amount: "))
        category = input("Category: ")
        Expense.add_expense(current_user.get_user_id(), amount, category)
        print("Expense added!")

    elif choice == "0":
        print("Thank you for using the app!")
        break

    else:
        print("Invalid choice. Try again.")