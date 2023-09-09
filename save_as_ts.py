import os
import random
import shutil

import numpy as np


def randomSplit(folder_path,output_folder1,output_folder2):
    # 获取文件列表
    file_list = os.listdir(folder_path)

    # 随机打乱文件列表
    random.shuffle(file_list)

    # 计算切分的索引
    split_index = int(0.8 * len(file_list))

    # 切分文件列表
    train_files = file_list[:split_index]
    test_files = file_list[split_index:]

    # 将文件分别复制到对应的输出文件夹
    for file_name in train_files:
        src_path = os.path.join(folder_path, file_name)
        dst_path = os.path.join(output_folder1, file_name)
        shutil.copy(src_path, dst_path)

    for file_name in test_files:
        src_path = os.path.join(folder_path, file_name)
        dst_path = os.path.join(output_folder2, file_name)
        shutil.copy(src_path, dst_path)


def saveAsTs():
    trainPath = 'split_data/train/'
    testPath = 'split_data/test/'
    saveTrainTsPath = 'CTG/CTG_TRAIN.ts'
    saveTestTsPath = 'CTG/CTG_TEST.ts'

    file_list = os.listdir(trainPath)
    for file in file_list:
        tempFile = trainPath+file
        if os.path.isdir(tempFile) != 1:
            continue
        tempFileList = os.listdir(tempFile)
        for trainFileName in tempFileList:
            if trainFileName.endswith('.npy') != 1:
                continue
            trainFileName = tempFile+'/'+trainFileName
            print('start save: '+trainFileName)
            data = np.load(trainFileName, allow_pickle=True)
            fhr = data[0]
            uc = data[1]
            ts_content = ",".join([str(val) for val in fhr])+":"+",".join([str(val) for val in uc])+":"+file+'\n'
            with open(saveTrainTsPath,"a") as file1:
                file1.write(ts_content)


    file_list = os.listdir(testPath)
    for file in file_list:
        tempFile = testPath+file
        if os.path.isdir(tempFile) != 1:
            continue
        tempFileList = os.listdir(tempFile)
        for trainFileName in tempFileList:
            if trainFileName.endswith('.npy') != 1:
                continue
            trainFileName = tempFile+'/'+trainFileName
            print('start save: '+trainFileName)
            data = np.load(trainFileName, allow_pickle=True)
            fhr = data[0]
            uc = data[1]
            ts_content = ",".join([str(val) for val in fhr])+":"+",".join([str(val) for val in uc])+":"+file+'\n'
            with open(saveTestTsPath,"a") as file1:
                file1.write(ts_content)



if __name__ == '__main__':
    # randomSplit('class/Early','split_data/train/Early','split_data/test/Early')
    # randomSplit('class/Late','split_data/train/Late','split_data/test/Late')
    # randomSplit('class/Normal','split_data/train/Normal','split_data/test/Normal')
    # randomSplit('class/Prolong','split_data/train/Prolong','split_data/test/Prolong')
    # randomSplit('class/Variety','split_data/train/Variety','split_data/test/Variety')
    saveAsTs()
