#!/usr/bin/env python3
import ipdb;

from classes.many_to_many import Article
from classes.many_to_many import Author
from classes.many_to_many import Magazine

if __name__ == '__main__':
#     print("HELLO! :) let's debug :vibing_potato:")

    author1 = Author("John")
    magazine1 = Magazine("GQ", "Business")
    article1 = Article(author1, magazine1, "New in Tech")


    # don't remove this line, it's for debugging!
    ipdb.set_trace()
