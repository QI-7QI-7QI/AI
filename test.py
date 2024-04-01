
import numpy as np

# 创建第一个元素，一个形状为 (84, 84, 4) 的随机数组
element1 = np.random.rand(84, 84, 4)

# 创建第二个元素，一个包含有关游戏状态信息的字典
element2 = {
    'lives': 5,
    'episode_frame_number': 12,
    'frame_number': 12
}

# 创建元组 obs
obs = (element1, element2)

obs = np.transpose(obs[0], [2, 0, 1]).astype(np.float32)

print(obs.shape)

# for i, item in enumerate(obs):
#     print(f"Element {i+1} type:", type(item))
#     if isinstance(item, np.ndarray):
#         print(f"Shape of element {i+1}:", item.shape)
#     elif isinstance(item, dict):
#         print(f"Content of element {i+1}:")
#         for key, value in item.items():
#             print(f"  {key}: {value}")