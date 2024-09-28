import torch

d_model = 512
n_heads = 8
n_layers = 6
d_k = 64
d_v = 64
d_ff = 2048
dropout = 0.1
padding_idx = 0
bos_idx = 2
eos_idx = 3
src_vocab_size = 32000
tgt_vocab_size = 32000
# batch_size = 32  # 有点大
batch_size = 16
epoch_num = 40
early_stop = 5
lr = 3e-4

# greed decode的最大句子长度
max_len = 60
# beam size for bleu
beam_size = 3
# Label Smoothing
use_smoothing = False
# NoamOpt
use_noamopt = True

data_dir = './data'
train_data_path = './data/json/train.json'
dev_data_path = './data/json/dev.json'
test_data_path = './data/json/test.json'
model_path = './experiment/model.pth'
log_path = './experiment/train.log'
output_path = './experiment/output.txt'

# gpu_id and device id is the relative id
# thus, if you wanna use os.environ['CUDA_VISIBLE_DEVICES'] = '2, 3'
# you should set CUDA_VISIBLE_DEVICES = 2 as main -> gpu_id = '0', device_id = [0, 1]
gpu_id = '0'
# device_id = [0, 1]  # 多gpu时
device_id = 0  # 只有一个gpu

# set device
if gpu_id != '':
    device = torch.device(f"cuda:{gpu_id}")
    # # 检查是否有可用的 GPU
    # try:
    #     # 尝试创建一个张量并将其移动到 cuda:0
    #     test_tensor = torch.tensor([1.0, 2.0, 3.0]).to(device)
    #     print(f"Device {device} is available and working.")
    #     print(f"Tensor on cuda:0: {test_tensor}")
    # except Exception as e:
    #     print(f"Error when using {device}: {e}")
else:
    device = torch.device('cpu')
