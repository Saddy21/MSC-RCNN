# MSC-RCNN
Multi-Scale Context Mask-RCNN Network for Slant Angled Aerial Imagery in Instance Segmentation in a Sim2Real setup
# [Learning Multi-Scale Context Mask-RCNN Network for Slant Angled Aerial Imagery in Instance Segmentation in a Sim2Real setup](https://arxiv.org/pdf/)




### Overview of Multi-Scale Context Mask-RCNN Network for Slant Angled Aerial Imagery in Instance Segmentation in a Sim2Real setup



 <div align="center">
    
  ![overview_new-1](https://user-images.githubusercontent.com/91654037/192519743-d21b8957-176b-44c7-a138-22bbfc79fd7b.png)

 </div>

## Environment Setup

 - ***Download Repo***   
   ````shell
   $ git clone https://github.com/rpmsnu/sRGB-TIR.git
   ````
   
   
 - ***Docker support***   
   
   To make things alot easier for environmental setup, I have uploaded my docker image on Dockerhub,
   
   please use the following command to get the docker
   ````
   $docker pull donkeymouse/donkeymouse:icra
   ````
   *If there persists any problems, please file an issue!
   
   
## How To Use: RGB to TIR translation
 - ***Inference***  
   ````
   $ python3 inference_batch.py --input_folder {input dir to your RGB images} --output_folder {output dir to store your translated images} --checkpoint {weight_file address} --a2b 0 --seed {your choice} --num_style {number of tir styles to sample} --synchronized --output_only 
   ````
   
   For example, to translate RGB images stored under a folder called "input", and say you want to sample 5 styles, run the following command:
    ````
   $python3 inference_batch.py --input_folder ./input --output_folder ./output --checkpoint ./translation_weights.pt --a2b 0 --seed 1234 --num_style 5 --synchronized --output_only --config configs/tir2rgb_folder.yaml
    ````
   
- ***Network weights***

Please download them from here: [{link to google drive}](https://drive.google.com/file/d/1px5BfenEGXZL_J6EsPwFImai6wfmcrnq/view?usp=sharing)

*If the link doesn't work, please file an issue!
