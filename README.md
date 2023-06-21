# SR3_Schlieren
## Google's SR3 model for super-resolution of high-speed Schlieren images

Link to original Paper --> [Saharia et al. 2021](https://arxiv.org/abs/2104.07636)\
Code adapted from --> [Janspiry_SR3](https://github.com/Janspiry/Image-Super-Resolution-via-Iterative-Refinement)

## Abstract
This work proposes the usage of modern Denoising Diffusion Probabilistic Models for Super-Resolution tasks applied to experimentally obtained high-speed Schlieren images. The objective is to take low-resolution Schlieren images, which are captured at a high frame rate, and super-resolve them to eventually obtain a high-resolution high-frame rate set which can be instrumental in understanding complex supersonic and hypersonic flows by enhancing visual quality and subsequent techniques like Proper Orthogonal Decomposition and Dynamic Mode Decomposition. The SR3 model was modified to work with Schlieren images and was observed to produce good results as evaluated by FID score. Furthermore, the results were validated for consistency with flow physics using Proper Orthogonal Decomposition based mode comparisons between high-resolution and super-resolved images. The model's versatility is demonstrated through stress testing with out-of-distribution image sets, affirming its robustness and adaptability.\


