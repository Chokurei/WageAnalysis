#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 10:09:29 2017

@author: kaku
"""


import pandas as pd
import MeCab, os
import numpy as np
from pattern_reconstruction import check_pattern_reconstruction

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

def wage_del_vague_word(wage, ID):
    """
    Delete rows with vague words in wage
    """
    id_no_vague_word = ID[:]
    wage_no_vague_word = []
    del_idx_vague_word = []
    for idx in range(len(wage)):
        wage_split_one = wage[idx] 
        if ('月' in wage_split_one or '月給' in wage_split_one) and ('時給' not in wage_split_one):
            del_idx_vague_word.append(idx)
        elif '以降' in wage_split_one:
            del_idx_vague_word.append(idx)
        elif '研修' in wage_split_one:
            del_idx_vague_word.append(idx)
        elif 'A' in wage_split_one and 'B' in wage_split_one:
            del_idx_vague_word.append(idx)
        else:
            wage_no_vague_word.append(wage_split_one)
    idx_reverse = del_idx_vague_word[::-1]
    for i in idx_reverse:    
        del id_no_vague_word[i]
    return wage_no_vague_word, id_no_vague_word

def list_num(lis):
    for x in lis:
        try:
            float(x)
            return True
        except ValueError:
            return False

def wage_del_vague_num(wage, ID):
    """
    Delete rows or digits with vague num in wage
    """
    id_no_vague_num = ID[:]
    wage_no_vague_num = []
    wage_no_vague_num_1 = []
    wage_no_vague_num_2 = []
    del_idx_vague_num= []
    
    # change digits
    for i in range(len(wage)):
        wage_split_one = wage[i]
        numlist = [s for s in wage_split_one if list_num(s)]
        for j in numlist:
            idx = wage_split_one.index(j)
            try:
                if wage_split_one[idx + 1] == 'ヶ月' or \
                wage_split_one[idx + 1] == 'ヵ月' or \
                wage_split_one[idx + 1] == '日' or \
                wage_split_one[idx + 1] == '日間' or \
                wage_split_one[idx + 1] == '週間' or \
                wage_split_one[idx + 1] == '週' or \
                wage_split_one[idx + 1] == '時間' or \
                wage_split_one[idx + 1] == '代' or \
                wage_split_one[idx + 1] == '％' or \
                wage_split_one[idx + 1] == '%' or \
                wage_split_one[idx + 1] == '.' or \
                wage_split_one[idx + 1] == '倍' or \
                wage_split_one[idx + 1] == 'h' or \
                wage_split_one[idx + 1] == '回' or \
                wage_split_one[idx + 1] == '万' or \
                wage_split_one[idx - 1] == '月給' or \
                wage_split_one[idx - 1] == '月':
                    del wage_split_one[idx]
            except:
                print(wage_split_one)
        wage_no_vague_num_1.append(wage_split_one)
    
    # delele rows
    for i in range(len(wage_no_vague_num_1)):
        wage_split_one = wage_no_vague_num_1[i]
        numlist = [s for s in wage_split_one if list_num(s)]
        if ('1' in numlist and '2' in numlist) or \
        ('1' in numlist and '3' in numlist) or \
        ('1' in numlist and '4' in numlist):
            del_idx_vague_num.append(i)
        else:
            wage_no_vague_num_2.append(wage_split_one)
    idx_reverse = del_idx_vague_num[::-1]
    for i in idx_reverse:    
        del id_no_vague_num[i]
        
    # delete digits, some useless number in specific range still need to be deleted
    for i in range(len(wage_no_vague_num_2)):
        wage_split_one = wage_no_vague_num_2[i]
        numlist = [s for s in wage_split_one if list_num(s)]
        for j in numlist:
            if 24 < float(j) < 30 or 30 < float(j) < 500:
                wage_split_one.remove(j)
        wage_no_vague_num.append(wage_split_one)
            
    return wage_no_vague_num, id_no_vague_num

def wage_convert(wage):
    """
    standardize rows in wage
    """
    wage_converted = []
    for i in range(len(wage)):
        wage_split_one = wage[i]
        for j in wage_split_one:
            if j == '時半':
                idx_half = wage_split_one.index('時半')
                time_new = str(int(wage_split_one[idx_half-1])+0.5)
                del wage_split_one[idx_half]
                wage_split_one[idx_half-1] = time_new
            elif j == '00':
                wage_split_one.remove(j)
            elif j == '30':
                idx_half = wage_split_one.index('30')
                try:
                    if wage_split_one[idx_half-1] == ':':
                        time_new = str(int(wage_split_one[idx_half-2])+0.5)
                        del wage_split_one[idx_half]
                        del wage_split_one[idx_half-1]
                        wage_split_one[idx_half-2] = time_new
                    else:
                        del wage_split_one[idx_half]
                except:
                    del wage_split_one[idx_half]
            else:
                continue
        wage_converted.append(wage_split_one)
    return wage_converted

def wage_bool(wage):
    """
    convert into bool number
    """
    wage_digit = []
    wage_booled = []
    for i in range(len(wage)):
        wage_split_one = wage[i]
        digit_list = [s for s in wage_split_one if list_num(s)]
        booled_list = digit_list[:]
        for j in range(len(booled_list)):
            if float(booled_list[j]) > 500:
                booled_list[j] = '1'
            else:
                booled_list[j] = '0'
        booled_str = ''.join(booled_list)
        wage_digit.append(digit_list)
        wage_booled.append(booled_str)
    return wage_digit, wage_booled

def pattern_print(wage):
    """
    print pattern and representative example
    """
    wage_unique = np.unique(list(set(wage)))
    for i in range(len(wage_unique)):
        pattern = wage_unique[i]
        pattern_idx = wage_booled.index(pattern)
        print(pattern)
        print(wage_converted[pattern_idx])

data_path = '../data/wage_analysis_ver02.csv'
result_path = '../result/'
show_pattern = True

data_ori = pd.read_csv(data_path, encoding = 'shift_jis')
data_todo = data_ori[['Unnamed: 0','rqmt_cmpny_nm_txt', 'sal_txt']]
data_todo.columns = [['ID','name', 'salary']]
ID = list(data_todo.values[:,0])
wage = list(data_todo.values[:,-1])

wage_split = wage_split_MeCab(wage)
wage_no_vague_word, id_no_vague_word = wage_del_vague_word(wage_split, ID)
wage_no_vague_num, id_no_vague_num = wage_del_vague_num(wage_no_vague_word, id_no_vague_word)
wage_converted = wage_convert(wage_no_vague_num)
wage_digit, wage_booled = wage_bool(wage_converted)

if show_pattern:
    pattern_print(wage_booled)

data_pattern_dict = {'ID': id_no_vague_num, 'origin': wage_digit, 'pattern': wage_booled}
data_pattern = pd.DataFrame(data = data_pattern_dict )

data_ori = data_ori.rename(columns={'Unnamed: 0':'ID'})
data_pattern_rec = check_pattern_reconstruction(data_pattern)

output = pd.merge(data_pattern_rec, data_ori, on = 'ID', how= 'outer')
output.to_csv(os.path.join(result_path,os.path.basename(data_path)[:-4] + '_output.csv'))






