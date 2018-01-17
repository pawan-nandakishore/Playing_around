

import numpy as np
import matplotlib.pyplot as plt
import os 
import csv
from itertools import chain
import pandas as pd
import re
import random


def remove_urls (text):
    """Remove URL from a piece of text
    """
    text = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', text, flags=re.MULTILINE)
    return(text)

def remove_email_address(article): 
    """Remove multiple email addresses from a string 
    article is a list that contains string
    """
    match = re.findall(r'[\w\.-]+@[\w\.-]+', article)
    for x in match :
        
        article =article.replace(x, ' ')
    
    return article

def check_if_num(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

    
def remove_symbols(article) : 
    
    replace_symbols = ['"', ' "', '" ', '@','!', ':','RT','~','/', "#", "&", " ' ", "...", "_", ";", "|", 
                       '\\','http', '- -', '<<', '>>', '*', '{','}','[', ']', '>', '<' , '++', '--', '\"' ]
    for sym in replace_symbols:
        article =article.replace(sym, ' ')
    return article




def get_num_to_word_ratio(article_list, threshold = 0.10):
    """provide index list to remove articles with too many numbers
       - This is done by calculating the num_word_ratio ratio 
       - current ratio set to 10% for threshold
       
       return: 
            articles_with_charts - list of num_to_word ratios 
            remove_article_index - list which gives the index 
                                      of articles to remove
    """
    articles_with_charts = []
    remove_article_index =[]
    
    for counter, article in enumerate(article_list): 
        all_words = article.split()
        number_check = [check_if_num(x) for x in all_words]
        
        if len(number_check)>0 : 
            num_word_ratio = sum(number_check)/len(number_check)
            if num_word_ratio>threshold: 
                remove_article_index.append(counter)
            articles_with_charts.append(num_word_ratio)
        
    return articles_with_charts, remove_article_index

def get_new_list(original_list, index_list):
    """remove elements from a list based on a list of indicies
    input: 
        original list  is a list 
        index list is a list 
        
    output: 
         new list is a list smaller than the original list 
    """
    length_list  = range(len(original_list))
    keep_these = set(range(len(length_list))).difference(set(index_list))
    new_list = [original_list[x] for x in keep_these]
    return new_list 



