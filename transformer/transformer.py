import torch.nn.functional as F
import torch
import torch.nn as nn

import TabTransformer from tab_transformer_pytorch.tab_transformer_pytorch
import FTTransformer from tab_transformer_pytorch.ft_transformer

file_path = "./2021PRofile Fire incident.xlsx"
data = pd.read_excel(file_path)


