#配置环境，并导入包
import sys
path1 = "/home/nsy/nlp/exp3/CRF/bi-lstm-crf-master"
sys.path.append(path1)
path2 = "/home/nsy/nlp/exp3/CRF/keras-contrib-master"
sys.path.append(path2)
from keras.callbacks import ModelCheckpoint, TensorBoard
from keras.optimizers import Adam
from dl_segmenter import get_or_create, save_config, DLSegmenter
from dl_segmenter.custom.callbacks import LRFinder, SGDRScheduler, WatchScheduler
from dl_segmenter.data_loader import DataLoader
from dl_segmenter.utils import make_dictionaries
import os
import re

file_path = "bi-lstm-crf-master/data/2014_processed" #用于生成字典的标注文件
src_dict_path = "bi-lstm-crf-master/config/src_dict.json" #源字典保存路径
tgt_dict_path = "bi-lstm-crf-master/config/tgt_dict.json" #目标字典保存路径
min_freq = 1 #词频数阈值，小于该阈值的词将被忽略
print("开始生成...")
make_dictionaries(file_path,
                  src_dict_path=src_dict_path,
                  tgt_dict_path=tgt_dict_path,
                  filters="\t\n",
                  oov_token="<UNK>",
                  min_freq=min_freq)
print("生成字典结束.")

#可将文本文件2014_processed转换为hdf5格式，提升训练速度

txt_path ="bi-lstm-crf-master/data/2014_processed" #BIS标注的文本文件路径
h5_path = "bi-lstm-crf-master/data/2014_processed.h5" #转换为hdf5格式的保存路径
seq_len = 150  #语句长度
data_loader = DataLoader(src_dict_path, tgt_dict_path,
                             batch_size=1,
                             max_len=seq_len,
                             sparse_target=False)
print("开始转化...")
data_loader.load_and_dump_to_h5(txt_path, h5_path, encoding='utf-8')
print("转化完成.")
