class Node:
    def __init__(self, incident_id, bot, description):
        self.incident_id = incident_id
        self.bot = bot
        self.description = description
        self.next = None


class IncidentTicketList:
    def __init__(self):
        self.head = None
        self.size = 0

    def add_ticket(self, incident_id, bot, description):
        if self.search_ticket(incident_id, verbose=False):
            print(f"[!] Ticket {incident_id} already exists. Not added.\n")
            return False

        new_node = Node(incident_id, bot, description)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

        self.size += 1
        print(f"[+] Ticket {incident_id} added successfully.\n")
        return True

    def display_tickets(self):
        if self.head is None:
            print("[i] No active incident tickets.\n")
            return

        print("\n" + "-" * 70)
        print(f"{'Incident ID':<15}{'Bot':<20}{'Short Description'}")
        print("-" * 70)
        current = self.head
        while current is not None:
            print(f"{current.incident_id:<15}{current.bot:<20}{current.description}")
            current = current.next
        print("-" * 70 + "\n")

    def search_ticket(self, incident_id, verbose=True):
        current = self.head
        while current is not None:
            if current.incident_id.upper() == incident_id.upper():
                if verbose:
                    print("\n[i] Ticket found:")
                    print("-" * 70)
                    print(f"Incident ID : {current.incident_id}")
                    print(f"Bot         : {current.bot}")
                    print(f"Description : {current.description}")
                    print("-" * 70 + "\n")
                return current
            current = current.next

        if verbose:
            print(f"[!] Ticket {incident_id} not found.\n")
        return None

    def remove_ticket(self, incident_id):
        current = self.head
        previous = None

        while current is not None:
            if current.incident_id.upper() == incident_id.upper():
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                self.size -= 1
                print(f"[-] Ticket {incident_id} removed (resolved).\n")
                return True
            previous = current
            current = current.next

        print(f"[!] Ticket {incident_id} not found. Nothing removed.\n")
        return False

    def count_active_tickets(self):
        print(f"[i] Total active incident tickets: {self.size}\n")
        return self.size


def print_menu():
    print("=" * 70)
    print("                   INCIDENT TICKET MANAGEMENT SYSTEM ")
    print("=" * 70)
    print("1. Add a new incident ticket")
    print("2. Display all active incident tickets")
    print("3. Search for an incident ticket")
    print("4. Remove a resolved incident ticket")
    print("5. Display total number of active incident tickets")
    print("0. Exit")
    print("=" * 70)


def main():
    tickets = IncidentTicketList()

    while True:
        print_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            incident_id = input("Enter Incident ID: ").strip()
            bot = input("Enter Bot name: ").strip()
            description = input("Enter Short Description: ").strip()
            tickets.add_ticket(incident_id, bot, description)

        elif choice == "2":
            tickets.display_tickets()

        elif choice == "3":
            incident_id = input("Enter Incident ID to search: ").strip()
            tickets.search_ticket(incident_id)

        elif choice == "4":
            incident_id = input("Enter Incident ID to remove: ").strip()
            tickets.remove_ticket(incident_id)

        elif choice == "5":
            tickets.count_active_tickets()

        elif choice == "0":
            print("Exiting program. Goodbye!")
            break

        else:
            print("[!] Invalid choice. Please try again.\n")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("\n[ERROR] The program crashed with this message:")
        print(f"        {e}\n")
    finally:
        input("Press Enter to exit...")