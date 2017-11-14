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


def wage_without_month(wage):
    
    wage_split = []
    for idx in range(len(wage)):
        wage_split_one = tokenize(wage[idx]).split(' ')
        wage_split.append(wage_split_one)
    
    del_idx = []
    wage_no_month = []
    for idx in range(len(wage_split)):
        wage_split_one = wage_split[idx] 
        if ('月' or '月給' in wage_split_one) and ('時給' not in wage_split_one):
            del_idx.append(idx)
        else:
            wage_no_month.append(wage_split_one)
    return wage_no_month, del_idx


data_path = '../data/wage_analysis_ver02.csv'
data = pd.read_csv(data_path, encoding = 'shift_jis')
data_todo = data[['Unnamed: 0','rqmt_cmpny_nm_txt', 'sal_txt']]
data_todo.columns = [['ID','name', 'sal']]

wage = list(data_todo.values[:,-1])

wage_hourly, del_idx = wage_without_month(wage)


        
    
        
        
