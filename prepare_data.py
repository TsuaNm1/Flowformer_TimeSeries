from scipy.io import loadmat
import numpy as np
import os

if __name__ == '__main__':

    resLen = 1200

    labelPath = 'mat/CTU-CHB_label/'  # 文件夹路径
    ucPath = 'mat/CTU-CHB_train/'
    saveEarlyPath = 'class/Early/'
    saveLatePath = 'class/Late/'
    saveVarietyyPath = 'class/Variety/'
    saveProlongPath = 'class/Prolong/'
    saveNormalPath = 'class/Normal/'
    cnt = 1
    for filename in os.listdir(labelPath):
        print('start deal: ' + filename)
        # 获取前缀名
        preName = filename[:-4]

        # 读取label和fhr
        path_data = labelPath + filename
        mat_data1 = loadmat(path_data)
        fhr = mat_data1['data2']['FHR'][0][0][0]
        label = mat_data1['data2']['Label'][0][0][0]

        # 读取uc
        yuanshi = ucPath + filename
        mat_data = loadmat(yuanshi)
        uc = mat_data['data2']['UC'][0][0][0]

        # 获取做了预处理的fhr长度，截取uc长度统一
        fhrLen = len(fhr)
        uc1 = uc[:fhrLen]

        # 每次都从1开始保存数据
        earlyCnt = 1
        lateCnt = 1
        varietyCnt = 1
        prolongCnt = 1
        normalCnt = 1

        i = 0

        # 开始截取数据
        while i < fhrLen:
            flag = 0
            saveFhrLen = 0
            saveUcLen = 0
            # if (label[i] == 1):
            #     start = i
            #     while i<fhrLen and label[i] == 1:
            #         i = i+1
            #     saveFhr = fhr[start:i]
            #     saveUc = uc[start:i]
            #     if len(saveFhr) < resLen:
            #         # 在两侧补零
            #         padding_length = resLen - len(saveFhr)
            #         saveFhr = np.pad(saveFhr, (padding_length // 2, padding_length - padding_length // 2), 'constant')
            #         saveUc = np.pad(saveUc, (padding_length // 2, padding_length - padding_length // 2), 'constant')
            #     else:
            #         # 计算需要截取的长度
            #         trim_length = len(saveFhr) - resLen
            #         # 计算起始索引和结束索引
            #         start_index = trim_length // 2
            #         end_index = start_index + resLen
            #         saveFhr = saveFhr[start_index:end_index]
            #         saveUc = saveUc[start_index:end_index]
            #     saveArr = np.array((saveFhr,saveUc))
            #     np.save(saveEarlyPath+preName+'_'+str(earlyCnt)+'.npy',saveArr)
            #     earlyCnt = earlyCnt+1
            #     saveFhrLen = saveFhr.shape[0]
            #     saveUcLen = saveUc.shape[0]
            # elif (label[i] == 2):
            #     start = i
            #     while i < fhrLen and label[i] == 2:
            #         i = i + 1
            #     saveFhr = fhr[start:i]
            #     saveUc = uc[start:i]
            #     if len(saveFhr) < resLen:
            #         # 在两侧补零
            #         padding_length = resLen - len(saveFhr)
            #         saveFhr = np.pad(saveFhr, (padding_length // 2, padding_length - padding_length // 2), 'constant')
            #         saveUc = np.pad(saveUc, (padding_length // 2, padding_length - padding_length // 2), 'constant')
            #     else:
            #         # 计算需要截取的长度
            #         trim_length = len(saveFhr) - resLen
            #         # 计算起始索引和结束索引
            #         start_index = trim_length // 2
            #         end_index = start_index + resLen
            #         saveFhr = saveFhr[start_index:end_index]
            #         saveUc = saveUc[start_index:end_index]
            #     saveArr = np.array((saveFhr, saveUc))
            #     np.save(saveLatePath +preName+'_'+str(lateCnt) + '.npy', saveArr)
            #     lateCnt = lateCnt + 1
            #     saveFhrLen = saveFhr.shape[0]
            #     saveUcLen = saveUc.shape[0]
            # elif (label[i] == 3):
            #     start = i
            #     while i < fhrLen and label[i] == 3:
            #         i = i + 1
            #     saveFhr = fhr[start:i]
            #     saveUc = uc[start:i]
            #     if len(saveFhr) < resLen:
            #         # 在两侧补零
            #         padding_length = resLen - len(saveFhr)
            #         saveFhr = np.pad(saveFhr, (padding_length // 2, padding_length - padding_length // 2), 'constant')
            #         saveUc = np.pad(saveUc, (padding_length // 2, padding_length - padding_length // 2), 'constant')
            #     else:
            #         # 计算需要截取的长度
            #         trim_length = len(saveFhr) - resLen
            #         # 计算起始索引和结束索引
            #         start_index = trim_length // 2
            #         end_index = start_index + resLen
            #         saveFhr = saveFhr[start_index:end_index]
            #         saveUc = saveUc[start_index:end_index]
            #     saveArr = np.array((saveFhr, saveUc))
            #     np.save(saveVarietyyPath +preName+'_'+ str(varietyCnt) + '.npy', saveArr)
            #     varietyCnt = varietyCnt + 1
            #     saveFhrLen = saveFhr.shape[0]
            #     saveUcLen = saveUc.shape[0]
            # elif (label[i] == 4):
            #     start = i
            #     while i < fhrLen and label[i] == 4:
            #         i = i + 1
            #     saveFhr = fhr[start:i]
            #     saveUc = uc[start:i]
            #     if len(saveFhr) < resLen:
            #         # 在两侧补零
            #         padding_length = resLen - len(saveFhr)
            #         saveFhr = np.pad(saveFhr, (padding_length // 2, padding_length - padding_length // 2), 'constant')
            #         saveUc = np.pad(saveUc, (padding_length // 2, padding_length - padding_length // 2), 'constant')
            #     else:
            #         # 计算需要截取的长度
            #         trim_length = len(saveFhr) - resLen
            #         # 计算起始索引和结束索引
            #         start_index = trim_length // 2
            #         end_index = start_index + resLen
            #         saveFhr = saveFhr[start_index:end_index]
            #         saveUc = saveUc[start_index:end_index]
            #     saveArr = np.array((saveFhr, saveUc))
            #     np.save(saveProlongPath +preName+'_'+ str(prolongCnt) + '.npy', saveArr)
            #     prolongCnt = prolongCnt + 1
            #     saveFhrLen = saveFhr.shape[0]
            #     saveUcLen = saveUc.shape[0]
            if label[i] == 0:
                start = i
                while i < fhrLen and label[i] == 0:
                    i = i + 1
                if (i - start) > resLen:
                    saveFhr = fhr[start:start + resLen]
                    saveUc = uc[start:start + resLen]
                    saveArr = np.array((saveFhr, saveUc))
                    np.save(saveNormalPath + preName + '_' + str(prolongCnt) + '.npy', saveArr)
                    prolongCnt = prolongCnt + 1
                    saveFhrLen = saveFhr.shape[0]
                    saveUcLen = saveUc.shape[0]
                    print('save: ' + filename + ' saveFhrLen: ' + str(saveFhrLen) + ' saveUcLen:' + str(saveUcLen))
                else:
                    continue
    # flag = 1
            i = i + 1
    # if flag == 0:
