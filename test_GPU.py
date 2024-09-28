# import torch
#
# # 检查 CUDA 是否可用
# if torch.cuda.is_available():
#     print("CUDA is available. Number of GPUs:", torch.cuda.device_count())
#     # 打印每个 GPU 的名称
#     for i in range(torch.cuda.device_count()):
#         print(f"GPU {i}: {torch.cuda.get_device_name(i)}")
# else:
#     print("CUDA is not available. Using CPU.")
import torch

# 检查是否有可用的 GPU
if torch.cuda.is_available():
    # 检查 cuda:0 是否可用
    device = torch.device("cuda:0")
    try:
        # 尝试创建一个张量并将其移动到 cuda:0
        test_tensor = torch.tensor([1.0, 2.0, 3.0]).to(device)
        print(f"Device {device} is available and working.")
        print(f"Tensor on cuda:0: {test_tensor}")
    except Exception as e:
        print(f"Error when using {device}: {e}")
else:
    print("CUDA is not available. Using CPU.")
