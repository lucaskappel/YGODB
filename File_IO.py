# -*- coding: utf-8 -*-
"""
File IO
Created on Mon Jul 26 16:14:54 2021
@author: Lucas
"""

import os, io, re

def PrintTextFile(FilePath: str, FileContents: str, OverwritePrevious = False):
    
    ## Submethod to rename a duplicate file
    def Rename_Duplicate(Savepath):
        
        ## Sub-Submethod to get current working directory of the parent
        def Get_Parent_Directory(path = os.getcwd()): return path.split('\\')[:-1]
        
        duplicate_copy_counter = []
        file_array = Savepath.split('\\')[-1].split('.')
        
        if len(file_array) <= 1: 
            raise Exception(message = 'Error in \'Rename_Duplicate\'; \'Savepath\' must be splittable by \'.\'')
            
        filename_regex = re.compile(file_array[0] + '\d*')
        
        for list_file in os.listdir('\\'.join(Savepath.split('\\')[:-1])):
            if re.match(filename_regex, list_file.split('.')[0]): 
                duplicate_copy_counter.append(list_file)
                
        return '\\'.join(Get_Parent_Directory(Savepath)) + '\\' + file_array[0] + str(len(duplicate_copy_counter)) + '.' + file_array[1]
    
    ## Rename the duplicate file if we don't want to overwrite
    if(not OverwritePrevious): FilePath = Rename_Duplicate(FilePath)
    
    ## Write the file contents
    with io.open(FilePath, "w+", encoding="utf-8") as TargetFile: TargetFile.write(FileContents)
    
    return