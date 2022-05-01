#配置环境，并导入包
import sys
path1 = "/home/nsy/nlp/exp3/CRF/bi-lstm-crf-master"
sys.path.append(path1)
path2 = "/home/nsy/nlp/exp3/CRF/keras-contrib-master"
sys.path.append(path2)
from keras.callbacks import ModelCheckpoint, TensorBoard
from keras.optimizers import Adam
from dl_segmenter import get_or_create, save_config,DLSegmenter
from dl_segmenter.custom.callbacks import LRFinder, SGDRScheduler, WatchScheduler
from dl_segmenter.data_loader import DataLoader
from dl_segmenter.utils import make_dictionaries
import os

segmenter: DLSegmenter = get_or_create("bi-lstm-crf-master/config/default-config.json",
                                       src_dict_path="bi-lstm-crf-master/config/src_dict.json",
                                       tgt_dict_path="bi-lstm-crf-master/config/tgt_dict.json",
                                       weights_path="bi-lstm-crf-master/models/weights.32--0.18.h5")
texts = [
   "华为是全球领先的ICT（信息与通信）基础设施和智能终端提供商，"
    "致力于把数字世界带入每个人、每个家庭、每个组织，构建万物互联的智能世界。"
    "我们在通信网络、IT、智能终端和云服务等领域为客户提供有竞争力、安全可信赖的产品、解决方案与服务，"
    "与生态伙伴开放合作，持续为客户创造价值，释放个人潜能，丰富家庭生活，激发组织创新。"
    "华为坚持围绕客户需求持续创新，加大基础研究投入，厚积薄发，推动世界进步。"
    "华为成立于1987年，是一家由员工持有全部股份的民营企业，目前有18万员工，业务遍及170多个国家和地区。"
]


for sent, tag in segmenter.decode_texts(texts):
    print(*zip(sent,tag))

