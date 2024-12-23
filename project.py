

class CustomMap:
    def __init__(self, data):
        self.data = data 

    def sort_by_value(self):
        sorted_items = sorted(self.data.items(), key=lambda item: item[1])
        self.data = dict(sorted_items)

    def __repr__(self):
        return str(self.data)
    
input_data = {101: "John Doe", 102: "Jane Smith", 103: "Peter Johnson"}

custom_map = CustomMap(input_data)


print(custom_map)

custom_map.sort_by_value()

print(custom_map)