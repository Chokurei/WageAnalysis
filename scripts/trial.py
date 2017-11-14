#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 10:36:17 2017

@author: kaku
"""

import pandas as pd
import MeCab

wakachi = MeCab.Tagger("-O wakati")
def tokenize(text):
    """Retrun tokenized (Japanese Wakachi-Gaki) text

    Parameters
    ----------
    text: string
    """
    
    return wakachi.parse(text)

def wage_split_MeCab(wage):
    """
    Split wage using Mecab
    """
    wage_split = []
    for idx in range(len(wage)):
        wage_split_one = tokenize(wage[idx]).split(' ')
        wage_split.append(wage_split_one)
    return wage_split

def wage_del_vague_word(wage):
    """
    Delete rows with vague words in wage
    """
    wage_no_vague_word = []
    del_idx_vague_word = []
    for idx in range(len(wage)):
        wage_split_one = wage[idx] 
        if ('月' in wage_split_one or '月給' in wage_split_one) and ('時給' not in wage_split_one):
            del_idx_vague_word.append(idx)
        elif '以降' in wage_split_one:
            del_idx_vague_word.append(idx)
        elif 'A' in wage_split_one and 'B' in wage_split_one:
            del_idx_vague_word.append(idx)
        else:
            wage_no_vague_word.append(wage_split_one)
    return wage_no_vague_word, del_idx_vague_word

def list_num(lis):
    for x in lis:
        try:
            float(x)
            return True
        except ValueError:
            return False

def wage_del_vague_num(wage):
    """
    Delete rows with vague num in wage
    """
    wage_no_vague_num = []
    wage_no_vague_num_mid = []
    del_idx_vague_num = []   
    for i in range(len(wage)):
        wage_split_one = wage[i]
        numlist = [s for s in wage_split_one if list_num(s)]
        if '1' in numlist and '2' in numlist:
            del_idx_vague_num.append(i)
        else:
            wage_no_vague_num_mid.append(wage_split_one)
    # some useless number in specific range still need to be deleted
    for i in range(len(wage_no_vague_num_mid)):
        wage_split_one = wage_no_vague_num_mid[i]
        numlist = [s for s in wage_split_one if list_num(s)]
        for j in numlist:
            if 30 < float(j) < 600:
                wage_split_one.remove(j)
        wage_no_vague_num.append(wage_split_one)
    return wage_no_vague_num, del_idx_vague_num

def wage_convert(wage):
    """
    standardize rows in wage
    """
    wage_converted = []
    idx_converted = []
    for i in range(len(wage)):
        wage_split_one = wage[i]
        if '時半' in wage_split_one:
            idx_half = wage_split_one.index('時半')
            time_new = str(int(wage_split_one[idx_half-1])+0.5)
            del wage_split_one[idx_half]
            wage_split_one[idx_half-1] = time_new
            wage_converted.append(wage_split_one)
            idx_converted.append(i)
        elif '00' in wage_split_one:
            for j in wage_split_one:
                if j == '00':
                    wage_split_one.remove(j)
            wage_converted.append(wage_split_one)
        elif '30' in wage_split_one:
            idx_half = wage_split_one.index('30')
            if wage_split_one[idx_half-1] == ':':
                time_new = str(int(wage_split_one[idx_half-2])+0.5)
                del wage_split_one[idx_half]
                del wage_split_one[idx_half-1]
                wage_split_one[idx_half-2] = time_new
                wage_converted.append(wage_split_one)
                idx_converted.append(i)
        else:
            wage_converted.append(wage_split_one)
    return wage_converted, idx_converted

def wage_bool(wage):
    """
    convert into bool number
    """
    wage_booled = []
    for i in range(len(wage)):
        wage_split_one = wage[i]
        booled_list = [s for s in wage_split_one if list_num(s)]
        for j in range(len(booled_list)):
            if float(booled_list[j]) > 500:
                booled_list[j] = '1'
            else:
                booled_list[j] = '0'
        booled_str = ''.join(booled_list)
        wage_booled.append(booled_str)
    return wage_booled
            
data_path = '../data/wage_analysis_ver02.csv'
data = pd.read_csv(data_path, encoding = 'shift_jis')
data_todo = data[['Unnamed: 0','rqmt_cmpny_nm_txt', 'sal_txt']]
data_todo.columns = [['ID','name', 'salary']]
wage = list(data_todo.values[:,-1])

wage_split = wage_split_MeCab(wage)
wage_no_vague_word, del_idx_vague_word = wage_del_vague_word(wage_split)
wage_no_vague_num, del_idx_vague_num = wage_del_vague_num(wage_no_vague_word)
wage_converted, idx_converted = wage_convert(wage_no_vague_num)
wage_booled = wage_bool(wage_converted)

                
        
