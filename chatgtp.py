"""
Plant Care Tracker
------------------
A simple program to track plant watering schedules using a text file.
"""

from datetime import datetime, date

FILE_NAME = "plants.txt"


def load_plants():
    """
    Loads plant data from a file and returns a list of plant dictionaries.
    If the file does not exist, returns an empty list.
    """
    plants = []

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    name, interval, last_watered = line.split(",")
                    plants.append({
                        "name": name,
                        "interval": int(interval),
                        "last_watered": last_watered
                    })
    except FileNotFoundError:
        # File does not exist yet — start with empty list
        pass

    return plants


def save_plants(plants):
    """
    Saves all plant data back to the file.
    """
    with open(FILE_NAME, "w") as file:
        for plant in plants:
            line = f"{plant['name']},{plant['interval']},{plant['last_watered']}\n"
            file.write(line)


def add_plant(plants):
    """
    Adds a new plant based on user input.
    """
    name = input("Enter plant name: ").strip()

    try:
        interval = int(input("Watering interval (in days): "))
    except ValueError:
        print("Invalid number. Plant not added.")
        return

    today = date.today().isoformat()

    plants.append({
        "name": name,
        "interval": interval,
        "last_watered": today
    })

    print(f"{name} added successfully.")


def water_plant(plants):
    """
    Updates the last watered date for a selected plant.
    """
    if not plants:
        print("No plants to water.")
        return

    for i, plant in enumerate(plants, start=1):
        print(f"{i}. {plant['name']}")

    try:
        choice = int(input("Select a plant number: "))
        if choice < 1 or choice > len(plants):
            raise ValueError
    except ValueError:
        print("Invalid selection.")
        return

    plants[choice - 1]["last_watered"] = date.today().isoformat()
    print(f"{plants[choice - 1]['name']} has been watered.")


def check_thirsty_plants(plants):
    """
    Checks which plants need watering and alerts the user.
    """
    today = date.today()
    thirsty = False

    for plant in plants:
        last_watered_date = datetime.strptime(
            plant["last_watered"], "%Y-%m-%d"
        ).date()

        days_since = (today - last_watered_date).days

        if days_since > plant["interval"]:
            print(f"⚠️ {plant['name']} needs water!")
            thirsty = True

    if not thirsty:
        print("All plants are happy 🌱")


def view_plants(plants):
    """
    Displays all plants and their watering information.
    """
    if not plants:
        print("No plants to display.")
        return

    for plant in plants:
        print(
            f"{plant['name']} — every {plant['interval']} days "
            f"(last watered: {plant['last_watered']})"
        )


def menu():
    """
    Displays the menu and returns the user's choice.
    """
    print("\n🌱 Plant Care Tracker")
    print("1. View plants")
    print("2. Add a plant")
    print("3. Water a plant")
    print("4. Check thirsty plants")
    print("5. Save & Exit")

    return input("Choose an option: ").strip()


def main():
    """
    Main program loop.
    """
    plants = load_plants()

    while True:
        choice = menu()

        if choice == "1":
            view_plants(plants)
        elif choice == "2":
            add_plant(plants)
        elif choice == "3":
            water_plant(plants)
        elif choice == "4":
            check_thirsty_plants(plants)
        elif choice == "5":
            save_plants(plants)
            print("Goodbye! 🌿")
            break
        else:
            print("Invalid option. Please try again.")


# Run the program
main()

