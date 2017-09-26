# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 12:55:34 2017

@author: mtinti-x
"""
from string import strip

def create_dict(in_file, exclude_features=[], protein_id=None):
    feature_dict = {}
    file_open = open('P02920.txt')
    if protein_id == None:
        protein_id = next(file_open)
        protein_id = protein_id.split()[1]
    
    for line in file_open:
        item_list = line.split()
        if (item_list[0] == 'FT') and (len(item_list) >2) and \
            (item_list[1] not in exclude_features):
                print len(item_list), item_list[1]
                key = strip(item_list[1])
                start = item_list[2]
                end = item_list[3]
                desc = strip(' '.join(item_list[4:]))
                if key in feature_dict:
                    feature_dict[key]+=[(protein_id,start,end,desc)]
                else:
                    feature_dict[key]=[(protein_id,start,end,desc)]
    file_open.close()
    return feature_dict

    
def jalview_format(res_name = 'test.txt', in_dict = {}):
    file_res = open(res_name,'w')
    groups = in_dict.keys()
    for group in groups:
        items = in_dict[group]
        file_res.write('startgroup	'+group+'\n')
        for item in items:
            temp_res = [group,item[0],'-1',item[1],item[2],item[3],'0.0']
            file_res.write('\t'.join(temp_res)+'\n')
        file_res.write('endgroup\t'+group+'\n\n')
    file_res.close()
            
    
if __name__ == '__main__':
    
    exclude_features = ['CHAIN']
    in_file = 'P02920.txt'
    temp_dict = create_dict(in_file,exclude_features=exclude_features,
                            protein_id = 'P02920_LACY_ECOLI')
    #print temp_dict['TRANSMEM']
    jalview_format(res_name = 'P02920_jv.txt', in_dict=temp_dict)
    





