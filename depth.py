import sys
sys.path.append('./MiDaS')
from midas.dpt_depth import DPTDepthModel
from midas.model_loader import default_models, load_model
from run import process as PRC



from tqdm import tqdm
from glob import glob
from pathlib import Path

import numpy as np
import torch, torchvision
import cv2

from skimage import transform

from matplotlib import pylab as plt
from moviepy.video.io.bindings import mplfig_to_npimage as fig_to_np

import plotting


def model_init(model_path,device = "cpu"):
    model_type = model_path.split("/")[-1].split(".")[0]#"midas_v21_small_256"
    optimize   = False
    model, model_transform, net_w, net_h = load_model(device, model_path,
                                                       model_type = model_type
                                                 )

    return [model, model_type, device, model, model_transform, net_w, net_h, device, optimize]

def read_image(path):
    """Read image and output RGB image (0-1).

    Args:
        path (str): path to file

    Returns:
        array: RGB image (0-1)
    """
    img = cv2.imread(path)

    if img.ndim == 2:
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) / 255.0

    return img

def midas_inference(path,model_pars):
    model, model_type, device, model, model_transform, net_w, net_h, device, optimize = model_pars
    original_image_rgb = read_image(path)  # in [0, 1]
    image              = model_transform({"image": original_image_rgb})["image"]
    with torch.no_grad():
        prediction = PRC(device, model,
                         model_type,
                         image,
                         (net_w, net_h),
                         original_image_rgb.shape[1::-1],
                         optimize, False)

    #frame = plotting.plot_sbs(original_image_rgb,prediction)
    return [original_image_rgb, prediction]

def get_obj_dept(depth_maps, bin_masks):
    depth_maps = np.repeat(depth_maps[:,None,:,:],bin_masks.shape[1],axis=1).astype("float")
    depth_maps[bin_masks==False] = np.nan
    return depth_maps



def midas_plots(data, static=True, vmin=1500, vmax=4500):

    if static==True:
        vmin=vmin
        vmax=vmax
    else:
        dists = np.stack([i[1] for i in data])
        vmin=dists.min()
        vmax=dists.max()

    frames = []
    for i in tqdm(data):
        frame = plotting.plot_sbs(i[0],i[1], vmin=vmin, vmax=vmax)
        frames.append(frame)
    return np.stack(frames)
