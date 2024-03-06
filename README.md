# MSC-RCNN
Multi-Scale Context Mask-RCNN Network for Slant Angled Aerial Imagery in Instance Segmentation in a Sim2Real setup
# [Learning Multi-Scale Context Mask-RCNN Network for Slant Angled Aerial Imagery in Instance Segmentation in a Sim2Real setup](https://arxiv.org/pdf/)




### Overview of Multi-Scale Context Mask-RCNN Network for Slant Angled Aerial Imagery in Instance Segmentation in a Sim2Real setup



 <div align="center">
    
  ![overview_new-1](https://user-images.githubusercontent.com/.png)

 </div>

## Environment Setup

 - ***Download Repo***   
   ````shell
   $ git clone https://github.com/Saddy21/MSC-RCNN.git
   ````
   
   
 
   

   
   
## How To Use: ./input --output_folder ./output --checkpoint ./translation_weights.pt --a2b 0 --seed 1234 --num_style 5 --synchronized --output_only --config configs/tir2rgb_folder.yaml
 - ***Inference***  
   ````
   $ python3 inference_batch.py --input_folder
   ````
   
    ````
   $python3 inference_batch.py --input_folder 
    ````
    
   
- ***Network weights***

Please download them from here: [{link to google drive}]()

*If the link doesn't work, please file an issue!
