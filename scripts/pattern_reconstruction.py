#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 16:37:41 2017

@author: kaku
"""
import pandas as pd
import numpy as np

wage_keep = []
def check_pattern_reconstruction(wage_numlist_pattern):
    wage_numlist_pattern.columns = ['ID', 'origin', 'pattern']
    for i in range(len(wage_numlist_pattern)):
        data_for_check = wage_numlist_pattern.iloc[i, :]
        if data_for_check.pattern == '001':
            result_ = data_for_check.origin[0] + '-' + data_for_check.origin[1] + ' ' + data_for_check.origin[2]
            result = np.str(data_for_check.ID) + 'M' + result_
            wage_keep.append(result)
        elif data_for_check.pattern == '00100001':
            result_ = data_for_check.origin[0] + '-' + data_for_check.origin[1] + ' ' + data_for_check.origin[2] \
            + '; ' + data_for_check.origin[3] + '-' + data_for_check.origin[4] + ',' + data_for_check.origin[5] + '-' + data_for_check.origin[6] \
            + ' ' + data_for_check.origin[7]
            result = np.str(data_for_check.ID) + 'M' + result_
            wage_keep.append(result)
        elif data_for_check.pattern == '00100001001':
            result_ = data_for_check.origin[0] + '-' + data_for_check.origin[1] + ' ' + data_for_check.origin[2] \
            + '; ' + data_for_check.origin[3] + '-' + data_for_check.origin[4] + ',' + data_for_check.origin[5] + '-' + data_for_check.origin[6] \
            + ' ' + data_for_check.origin[7] + '; ' + data_for_check.origin[8] + '-' + data_for_check.origin[9] + ' ' + data_for_check.origin[10]
            result = np.str(data_for_check.ID) + 'M' + result_
            wage_keep.append(result)
        elif data_for_check.pattern == '001001':
            result_ = data_for_check.origin[0] + '-' + data_for_check.origin[1] + ' ' + data_for_check.origin[2] \
            + '; ' + data_for_check.origin[3] + '-' + data_for_check.origin[4] + ' ' + data_for_check.origin[5]
            result = np.str(data_for_check.ID) + 'M' + result_
            wage_keep.append(result)
        elif data_for_check.pattern == '001001001':
            result_ = data_for_check.origin[0] + '-' + data_for_check.origin[1] + ' ' + data_for_check.origin[2] \
            + '; ' + data_for_check.origin[3] + '-' + data_for_check.origin[4] + ' ' + data_for_check.origin[5] \
            + '; ' + data_for_check.origin[6] + '-' + data_for_check.origin[7] + ' ' + data_for_check.origin[8]
            result = np.str(data_for_check.ID) + 'M' + result_
            wage_keep.append(result)
        elif data_for_check.pattern == '001001001001':
            result_ = data_for_check.origin[0] + '-' + data_for_check.origin[1] + ' ' + data_for_check.origin[2] \
            + '; ' + data_for_check.origin[3] + '-' + data_for_check.origin[4] + ' ' + data_for_check.origin[5] \
            + '; ' + data_for_check.origin[6] + '-' + data_for_check.origin[7] + ' ' + data_for_check.origin[8] \
            + '; ' + data_for_check.origin[9] + '-' + data_for_check.origin[10] + ' ' + data_for_check.origin[11]
            result = np.str(data_for_check.ID) + 'M' + result_
            wage_keep.append(result)
        elif data_for_check.pattern == '0010011':
            result_ = data_for_check.origin[0] + '-' + data_for_check.origin[1] + ' ' + data_for_check.origin[2] \
            + '; ' + data_for_check.origin[3] + '-' + data_for_check.origin[4] + ' ' + data_for_check.origin[5] \
            + '; ' + data_for_check.origin[4] + '-' + data_for_check.origin[0] + ' ' + data_for_check.origin[6]
            result = np.str(data_for_check.ID) + 'M' + result_
            wage_keep.append(result)
        elif data_for_check.pattern == '0011':
            result_ = data_for_check.origin[0] + '-' + data_for_check.origin[1] + ' ' + data_for_check.origin[2] \
            + '; ' + data_for_check.origin[1] + '-' + data_for_check.origin[0] + ' ' + data_for_check.origin[3]
            result = np.str(data_for_check.ID) + 'M' + result_
            wage_keep.append(result)
        elif data_for_check.pattern == '1':
            result_ = '0-24 ' + data_for_check.origin[0]
            result = np.str(data_for_check.ID) + 'M' + result_
            wage_keep.append(result)
        elif data_for_check.pattern == '100001':
            result_ = data_for_check.origin[4] + '-' + data_for_check.origin[1] + ' ' + data_for_check.origin[0] \
            + '; ' + data_for_check.origin[1] + '-' + data_for_check.origin[2] + ',' + data_for_check.origin[3] + '-' \
            + data_for_check.origin[4] + ' ' + data_for_check.origin[5]
            result = np.str(data_for_check.ID) + 'M' + result_
            wage_keep.append(result)
        elif data_for_check.pattern == '10000100':
            result_ = data_for_check.origin[1] + '-' + data_for_check.origin[2] + ',' \
            + data_for_check.origin[3] + '-' + data_for_check.origin[4] + ' ' + data_for_check.origin[0] \
            + '; ' + data_for_check.origin[6] + '-' + data_for_check.origin[7] + ' ' + data_for_check.origin[5]
            result = np.str(data_for_check.ID) + 'M' + result_
            wage_keep.append(result)
        elif data_for_check.pattern == '1001':
            result_ = data_for_check.origin[2] + '-' + data_for_check.origin[1] + ' ' + data_for_check.origin[0] \
            + '; ' + data_for_check.origin[1] + '-' + data_for_check.origin[2] + ' ' + data_for_check.origin[3]
            result = np.str(data_for_check.ID) + 'M' + result_
            wage_keep.append(result)
        elif data_for_check.pattern == '100100':
            result_ = data_for_check.origin[1] + '-' + data_for_check.origin[2] + ' ' + data_for_check.origin[0] \
            + '; ' + data_for_check.origin[4] + '-' + data_for_check.origin[5] + ' ' + data_for_check.origin[3]
            result = np.str(data_for_check.ID) + 'M' + result_
            wage_keep.append(result)
        elif data_for_check.pattern == '100100001':
            result_ = data_for_check.origin[1] + '-' + data_for_check.origin[2] + ' ' + data_for_check.origin[0] \
            + '; ' + data_for_check.origin[4] + '-' + data_for_check.origin[5] + ' ' + data_for_check.origin[3] \
            + '; ' + data_for_check.origin[6] + '-' + data_for_check.origin[7] + ' ' + data_for_check.origin[8]
            result = np.str(data_for_check.ID) + 'M' + result_
            wage_keep.append(result)
        elif data_for_check.pattern == '1001001':
            result_ = data_for_check.origin[5] + '-' + data_for_check.origin[1] + ' ' + data_for_check.origin[0] \
            + '; ' + data_for_check.origin[1] + '-' + data_for_check.origin[2] + ' ' + data_for_check.origin[3] \
            + '; ' + data_for_check.origin[4] + '-' + data_for_check.origin[5] + ' ' + data_for_check.origin[6]
            result = np.str(data_for_check.ID) + 'M' + result_
            wage_keep.append(result)
        elif data_for_check.pattern == '100100100':
            result_ = data_for_check.origin[1] + '-' + data_for_check.origin[2] + ' ' + data_for_check.origin[0] \
            + '; ' + data_for_check.origin[4] + '-' + data_for_check.origin[5] + ' ' + data_for_check.origin[3] \
            + '; ' + data_for_check.origin[7] + '-' + data_for_check.origin[8] + ' ' + data_for_check.origin[6] 
            result = np.str(data_for_check.ID) + 'M' + result_
            wage_keep.append(result)
        elif data_for_check.pattern == '1001001001':
            result_ = data_for_check.origin[1] + '-' + data_for_check.origin[2] + ' ' + data_for_check.origin[3] \
            + '; ' + data_for_check.origin[4] + '-' + data_for_check.origin[5] + ' ' + data_for_check.origin[6] \
            + '; ' + data_for_check.origin[7] + '-' + data_for_check.origin[8] + ' ' + data_for_check.origin[9] 
            result = np.str(data_for_check.ID) + 'M' + result_
            wage_keep.append(result)
        elif data_for_check.pattern == '100100100100':
            result_ = data_for_check.origin[1] + '-' + data_for_check.origin[2] + ' ' + data_for_check.origin[0] \
            + '; ' + data_for_check.origin[4] + '-' + data_for_check.origin[5] + ' ' + data_for_check.origin[3] \
            + '; ' + data_for_check.origin[7] + '-' + data_for_check.origin[8] + ' ' + data_for_check.origin[6] \
            + '; ' + data_for_check.origin[10] + '-' + data_for_check.origin[11] + ' ' + data_for_check.origin[9]
            result = np.str(data_for_check.ID) + 'M' + result_
            wage_keep.append(result)
        elif data_for_check.pattern == '1100':
            result_ = data_for_check.origin[3] + '-' + data_for_check.origin[2] + ' ' + data_for_check.origin[0] \
            + '; ' + data_for_check.origin[2] + '-' + data_for_check.origin[3] + ' ' + data_for_check.origin[1] 
            result = np.str(data_for_check.ID) + 'M' + result_
            wage_keep.append(result)
    wage_keep_result = pd.DataFrame(wage_keep)
    wage_keep_result.columns = ['str_']
    wage_result = wage_keep_result.str_.str.split('M').tolist()
    wage_result = pd.DataFrame(wage_result)
    wage_result.columns = ['ID', 'result']
    wage_result.ID = wage_result.ID.astype(int)
    return wage_result