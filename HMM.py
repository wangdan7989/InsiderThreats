# coding=utf-8
'''
Created on 2017-04-9

@author: Wangan
'''


import string
import matplotlib.pyplot as plt
from pylab import *
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import numpy as np
import UserSequences


def load_file(file_name):
    """
    读取文件，按列返回列表
    :param file_name: 文件路径
    :return: 文本内容列表
    """
    f1 = open(file_name)
    line = f1.readline()
    line_list = []
    while line:
        line_list.append(line)
        line = f1.readline()
    return line_list
class HMM:
    def __init__(self):
        """
        初始化
        :return:
        """
        self.state_list = load_file('./data/state_map.txt')
        self.state_map = dict(zip(self.state_list, range(self.state_list.__len__())))  # 词性映射哈希表
        self.trans_pro_matrix = np.loadtxt('./data/A.txt') # 转移概率矩阵
        vocab_list = load_file('./data/state_map.txt')
        self.vocab_map = dict(zip(vocab_list, range(vocab_list.__len__())))  # 词语映射哈希表
        #print self.state_map
        del vocab_list
        print '初始化完毕'

    def hmm(self, usersequences):
        """
        :param usersequences: 用户的行为序列
        :return: 对应用户行为序列的转移概率序列
        """
        state_seq = []
        usersequences = usersequences
        state = ''
        pre_state = usersequences[0][1]+'\n'
        prob = 0
        for i in range(len(usersequences)):
            state = usersequences[i][1]
            state = state+'\n'

            try:
                if self.state_map.has_key(state) == False:
                    state = 'other\n'
                prob = self.trans_pro_matrix[self.state_map[state]][self.state_map[pre_state]]

            except KeyError:
                pass
            state_seq.append(prob)
            pre_state = state

        result_state = state_seq
        return result_state

def average(list):
    return sum(list)/len(list)

if __name__ == '__main__':

    H = HMM()
    import time
    t1 = time.time()
    user14 = 'MAR0955'
    user12 = 'JLM0364'
    user13 = 'MAS0025'
    user01 = 'CRD0624'
    user02 = 'CEL0561'
    user00 ='RSC0089'
    user11 = 'ABC0174'
    usersequence = UserSequences.GetUserSequences(user14)
    result = H.hmm(usersequence)
    #for i in range(len(result)):
     #   print i,result[i]
    t2 = time.time()

    print average(result)

    '''
    xmajorLocator = MultipleLocator(100)

    ymajorLocator = MultipleLocator(2)
    fig = plt.figure()
    ax = subplot(111)
    y = result[:1500]
    x=range(len(y))
    plt.ylim(-3,3)
    #print x
    #y=[0.1,0.2,0.3,0.4,0.5]
    #plt.plot(x,result,'--r*')
    plt.plot(x,y)
    #plt.plot(x, result)
    #plt.legend()
    plt.show()
    '''
