import ast
import logging
from pathlib import Path
from typing import Optional
import json

import numpy as np
import torch.nn.functional
from e3nn import o3
from torch.optim.swa_utils import SWALR, AveragedModel
from torch_ema import ExponentialMovingAverage

import mace
from mace import data, modules, tools
from mace.tools import torch_geometric
from mace.tools.scripts_utils import create_error_table, get_dataset_from_xyz

def ttt():
    print('sdfsdfsd')