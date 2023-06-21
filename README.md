# SR3-Schlieren
## Google's SR3 model for super-resolution of high-speed Schlieren images

Link to original Paper --> [Saharia et al. 2021](https://arxiv.org/abs/2104.07636)\
Code adapted from --> [Janspiry_SR3](https://github.com/Janspiry/Image-Super-Resolution-via-Iterative-Refinement)

## Abstract
This work proposes the usage of modern Denoising Diffusion Probabilistic Models for Super-Resolution tasks applied to experimentally obtained high-speed Schlieren images. The objective is to take low-resolution Schlieren images, which are captured at a high frame rate, and super-resolve them to eventually obtain a high-resolution high-frame rate set which can be instrumental in understanding complex supersonic and hypersonic flows by enhancing visual quality and subsequent techniques like Proper Orthogonal Decomposition and Dynamic Mode Decomposition. The SR3 model was modified to work with Schlieren images and was observed to produce good results as evaluated by FID score. Furthermore, the results were validated for consistency with flow physics using Proper Orthogonal Decomposition based mode comparisons between high-resolution and super-resolved images. The model's versatility is demonstrated through stress testing with out-of-distribution image sets, affirming its robustness and adaptability.

## Usage Directions
### 1. Creating Environment
All dependencies mentioned in the 'requirement.txt' file have to be installed. Compatibility between PyTorch and the existing CUDA driver has to be checked.
```shell
pip install -r requirements.txt
```

### 2. Train Dataset Preparation
Store the square HR images within the root directory. The first argument corresponds to the absolute path of the data. The second argument is the directory within which the training files will be stored. The first entry in the size argument prescribes the dimension of the input while the second prescribes the output dimension. The example below is for a 4x super-resolution. The processed data can be used in LMDB or PNG format by changing the last argument.
```
# 16x16 image --> 256x256 image
python data/prepare_data.py  --path [input_data_path]  --out [output_data_path] --size 64,256 -l
```
The entire training process is controlled by the config file 'run_sr3' in the config folder.
