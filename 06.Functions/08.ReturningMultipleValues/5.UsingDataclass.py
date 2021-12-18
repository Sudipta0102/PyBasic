# i do not quite understand this yet
# what don't i understand?
# 1. somehow i can take values in the constructor without creating one. how?

from dataclasses import dataclass

@dataclass
class book_list:
    name:str
    perUnit_cost: float
    quantity_available: int = 0

    def total_cost(self) -> float: 
        return self.perUnit_cost * self.quantity_available

book = book_list("Last But not Least", 300, 3)
x = book.total_cost()

print(x)
print(book)