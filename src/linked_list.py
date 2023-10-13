class Node:
    """Класс для узла односвязного списка"""
    def __init__(self, data):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = None


class LinkedList:
    """Класс для односвязного списка"""

    def __init__(self):
        self.head = None

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next_node is not None:
                current_node = current_node.next_node
            current_node.next_node = new_node

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        return ll_string

    def get_data_by_id(self, id):
        """Возвращает первый найденный словарь с ключом 'id'"""
        current_node = self.head
        try:
            while current_node:
                data = current_node.data
                if isinstance(data, dict) and data.get('id') == id:
                    return data
                current_node = current_node.next_node
        except TypeError:
            print("Неподходящий формат данных")

        #return None

    def to_list(self):
        """Возвращает список с данными, содержащимися в односвязном списке"""
        result = []
        current_node = self.head
        while current_node:
            result.append(current_node.data)
            current_node = current_node.next_node
        return result



