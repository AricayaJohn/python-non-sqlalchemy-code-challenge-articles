class Article:
    all = []
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if isinstance(title, str) and 5 <= len(title) <= 50 and not hasattr(self, "_title"):
            self._title = title
        # elif not isinstance(title, str):
        #     raise TypeError("Title needs to be a string")
        # elif not (5 <= len(title) <= 50):
        #     raise IndexError("Title length value error")
        # elif hasattr(self, "_title"):
        #     raise ValueError("Title already has value set")
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, magazine):
        if isinstance(magazine, Magazine):
            self._magazine = magazine

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
        # elif not isinstance(name, str):
        #     raise TypeError("Name must be a string")
        # elif len(name) == 0:
        #     raise IndexError("Name length must be greater than 0")
        # elif hasattr(self, "_name"):
        #     raise ValueError("Name already has value set")
             
    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list({article.magazine for article in self.article()})

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
        # elif not isinstance(name, str):
        #     raise TypeError("Magazine name is not a string")
        # elif not (2 <= len(name) <= 16):
        #     raise IndexError("String length must have 2 - 16 characters")
        # elif hasattr(self, "_name"):
        #     raise ValueError("Magazine has value name already set")
        if isinstance(name, str) and 2 <= len(name) <= 16 and not hasattr(self, "_name"):
            self._name = name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        # if not isinstance(category, str):
        #     raise TypeError("Magazine Category must be a string")
        # if len(category) == 0:
        #     raise IndexError("Category length must be greater than zero")
        # if hasattr(self, "_category"):
        #     raise ValueError("Magazine Category is already set")
        # self._category = category
        if isinstance(category, str) and len(category) > 0 and not hasattr(self, "_category"):
            self._category = category
        
    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass