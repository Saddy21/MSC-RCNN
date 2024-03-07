# MSC-RCNN
Multi-Scale Context Mask-RCNN Network for Slant Angled Aerial Imagery in Instance Segmentation in a Sim2Real setup
# [Learning Multi-Scale Context Mask-RCNN Network for Slant Angled Aerial Imagery in Instance Segmentation in a Sim2Real setup](https://arxiv.org/pdf/)




### Overview of Multi-Scale Context Mask-RCNN Network for Slant Angled Aerial Imagery in Instance Segmentation in a Sim2Real setup

***Abstract***
While instance segmentation models excel at object detection in satellite imagery, their performance drops when applied to slant-angled aerial images due to occlusion and scale variation. This is mainly caused by a lack of training data for such diverse viewpoints and scales. To address this limitation, we propose the Sim2Real-based Multi-Scale Context Mask-RCNN (MSC-RCNN) network, specifically designed for slant-angled aerial imagery. Sim2Real-based transfer learning is adapted to compensate for the limited availability of real-world slant-angle training data. A synthetic dataset is generated using Unreal Engine, detailing the methodology of replicating the real-world scene, for producing diverse slant-angle drone datasets with various weather conditions and backgrounds. The model leverages two distinct feature pyramid backbones, with one incorporating dilated convolutions to address large-scale objects and the other optimized for regular convolutions. Their outputs are fused to effectively detect objects across various scales and angles. Through experiments, it was demonstrated that incorporating this synthetic data significantly reduces reliance on real data while maintaining high mean Average Precision (mAP) scores. Compared to the baseline Mask R-CNN, the proposed approach with Sim2Real adaptation and the MSC-RCNN architecture achieves a remarkable 7.6\% performance improvement in instance segmentation accuracy with only a 6\% increase in model size.

## Environment Setup

 - ***Download Repo***   
   ````shell
   $ git clone https://github.com/Saddy21/MSC-RCNN.git
   ````
   
   
 
   

   
   
## How To Use: 
** Code to be released soon **

-  ***Train***
   ````
   $ python3 train.py
   ````
   
 - ***Inference***  
   ````
   To visulize the results
   $ python3 test.py

   To obtain metrics
   $ python3 testacc.py
   
   ````
   
   
   
    
   
- ***Network weights***

Please download pretrained weights from here: [{https://shorturl.at/vGJS5}]()

*If the link doesn't work, please file an issue!
