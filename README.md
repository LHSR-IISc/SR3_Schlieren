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
Training requires data stored in the manner below.
```
├── hr_256 # It's the same as the sr_16_128 directory if ground-truth images are unavailable. If ground truth HR images corresponding to LR are available, then they should be stored here.
├── lr_64 # Vanilla low-resolution images
└── sr_64_256 # Images ready to super-resolution. They are obtained by bicubically upsampling the lr_64 images.
```
If only HR images are available, the dataset can be prepared by first storing them in the root directory. The first argument corresponds to the absolute path of the data. The second argument is the directory within which the training files will be stored. The first entry in the size argument prescribes the dimension of the input while the second prescribes the output dimension. The example below is for a 4x super-resolution. The processed data can be used in LMDB or PNG format by changing the last argument.
```
# 16x16 image --> 256x256 image
python data/prepare_data.py  --path [input_data_path]  --out [output_data_path] --size 64,256 -l
```
### 3. Training
The entire training process is controlled by the config file 'run_sr3' in the config folder. Some important settings are described below.
```
{
   "name": "Schlieren",
   "phase": "train", // train or val --> val is for inference on a trained model
   .
   .
   "path": { //set the path
          .
          .
        "resume_state": null // training from scratch; else enter path of existing model
    .
    .
    .
    "datasets": {
        "train": {
            "name": "Schlieren", // name for experiment
            "mode": "HR", // in case no corresponding LR images available, keep it as "HR"; keep "LRHR" if corresponding LR & HR images available
            "dataroot": "train_dir", // folder in SR3/ where the processed training data is kept --> output_path from the prepare_data.py step
            "datatype": "img", //lmdb or img
            "l_resolution": 64, // low resolution need to super_resolution
            "r_resolution": 256, // high resolution
           .
           .
           .   
        },
```
The command to run the script is given below.
```
python sr.py -p train -c config/sr_sr3.json
```
### 4. Inference
Once the model is trained, the model can be used for inference. The first step therein is to create the dataset as required by the codebase to run on vanilla LR images for which the below code snippet has to be executed.
```
python data/prepare_infer_only_LR.py ['absolute_path_of_input_LR_Images']
```
It will give a prompt saying "Data prepared for inference" once completed.

Inference requires a few changes to the config file as shown below.
```
{
    "name": "Schlieren",
    "phase": "val", // train or val --> val is for inference on a trained model
    .
    .
    "path": { //set the path
        .
        .
        "resume_state": "experiments/Schlieren_230417_103038/checkpoint/I50000_E396" // --> path of trained model in case of inference or also resumed training
    },

     "val": {
         "name": "Schlieren",
         "mode": "LR", // in case of doing inference with LR images, change this to LR
         "dataroot": "test_dir", // path where inference data is stored
         "datatype": "img", //lmdb or img
         "l_resolution": 64,
         "r_resolution": 256,
         "data_len": -1 // data length in validation; like above -1 represents the whole dataset; when training keep it to the actual validation size
        }
```
The command to run the script is given below.
```
python infer.py -c config/sr_sr3.json
```
