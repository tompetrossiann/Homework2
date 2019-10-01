import os
import shutil
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import ThreadPoolExecutor

def copyFiles():
    firstSourceFiles = os.listdir('./source_folder')
    for fileName in firstSourceFiles:
        fullFileName = os.path.join('./source_folder', fileName)
        if os.path.isfile(fullFileName):
            shutil.copy(fullFileName, './destination_folder')
        
def copyFilesProccesses():
    secondSourceFiles = os.listdir('./source_folder')
    for fileName in secondSourceFiles:
        fullFileName = os.path.join('./source_folder', fileName)
        if os.path.isfile(fullFileName):
            executor = ProcessPoolExecutor(5)
            future = executor.submit(shutil.copy, fullFileName, './process_folder')
            
def copyFilesThreads():        
    thirdSourceFiles = os.listdir('./source_folder')
    for fileName in thirdSourceFiles:
        fullFileName = os.path.join('./source_folder', fileName)
        if os.path.isfile(fullFileName):
            executor = ThreadPoolExecutor(5)
            executor.submit(shutil.copy, fullFileName, './thread_folder')        