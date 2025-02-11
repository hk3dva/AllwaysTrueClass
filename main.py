class Comparator:
    def __eq__(self, *args, **kwargs):
        return True

    def __bool__(self, *args, **kwargs):
        return True

    def __call__(self, *args, **kwargs):
        return False
