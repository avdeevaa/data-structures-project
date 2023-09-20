class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.head = None
        self.tail = None

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        new_node = Node(data, None)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        if not self.head:  # Если очередь пуста
            return None
        data = self.head.data
        self.head = self.head.next_node
        if not self.head:  # Если это был последний элемент в очереди
            self.tail = None
        return data

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next_node

        return "\n".join(result)
