class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        
class Author:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 0 and not hasattr(self, "_name"):
            self._name = name
        elif not isinstance(name, str):
            raise TypeError("Name must be a string")
        elif len(name) == 0:
            raise IndexError("Name length must be greater than 0")
        elif hasattr(self, "_name"):
            raise ValueError("Name already has value set")
             
    def articles(self):
        pass

    def magazines(self):
        pass

    def add_article(self, magazine, title):
        pass

    def topic_areas(self):
        pass

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 2 <= len(name) <= 16 and not hasattr(self, "_name"):
            self._name = name
        elif not isinstance(name, str):
            raise TypeError("Magazine name is not a string")
        elif not (2 <= len(name) <= 16):
            raise IndexError("String length must have 2 - 16 characters")
        elif hasattr(self, "_name"):
            raise ValueError("Magazine has value name already set")

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category) > 0 and not hasattr(self, "_category"):
            self._category = category

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass