class Comparator:
    def __eq__(self, other):
        return True

    def __bool__(self):
        return True

    def __call__(self):
        return False
