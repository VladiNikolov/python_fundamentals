class Catalogue:
    def __init__(self, name: str):
        self.name = name
        self.products = []


    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        return [product for product in self.products if product.startswith(first_letter)]


    def __repr__(self):
        string_for_return = f"Items in the {self.name} catalogue:\n"
        string_for_return += '\n'.join(sorted(self.products))
        return string_for_return


# catalogue = Catalogue("Furniture")
# catalogue.add_product("Sofa")
# catalogue.add_product("Mirror")
# catalogue.add_product("Desk")
# catalogue.add_product("Chair")
# catalogue.add_product("Carpet")
# print(catalogue.get_by_letter("C"))
# print(catalogue)



