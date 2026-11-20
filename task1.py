class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, data):
        new_node = Node(data)

        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1
        print(f"Елемент {data} додано до черги.")

    def dequeue(self):
        if self.head is None:
            print("Черга порожня!")
            return None

        removed_data = self.head.data
        self.head = self.head.next
        self.size -= 1

        if self.head is None:
            self.tail = None

        print(f"Видалено елемент: {removed_data}")
        return removed_data

    def get_size(self):
        return self.size

    def display(self):
        if self.head is None:
            print("Черга порожня!")
            return

        current = self.head
        print("Елементи черги:", end=" ")

        while current is not None:
            print(current.data, end=" ")
            current = current.next

        print()

queue = Queue()

while True:
    print("\n===== МЕНЮ ЧЕРГИ =====")
    print("1. Додати елемент")
    print("2. Видалити елемент")
    print("3. Показати кількість елементів")
    print("4. Вивести всі елементи")
    print("0. Вийти")

    choice = input("Оберіть дію: ")

    if choice == "1":
        value = input("Введіть значення: ")
        queue.enqueue(value)

    elif choice == "2":
        queue.dequeue()

    elif choice == "3":
        print(f"Кількість елементів: {queue.get_size()}")

    elif choice == "4":
        queue.display()

    elif choice == "0":
        print("Програму завершено.")
        break

    else:
        print("Неправильний вибір. Спробуйте ще раз.")
