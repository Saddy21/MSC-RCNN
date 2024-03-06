#################### Following is the psuedo code of MSC-RCNN ############################


class CombinedFPN(nn.Module):
    def __init__(self, fpn1, fpn2):
        super(CombinedFPN, self).__init__()
        self.fpn1 = fpn1
        self.fpn2 = fpn2
        self.conv = nn.Conv2d(512,512,1,stride=1,padding=0)
        # self.norm = nn.BatchNorm2d(512)
        self.norm = nn.GroupNorm(2,512)
        self.conv2 = nn.Conv2d(512,256,1,stride=1,padding=0)
        

    def forward(self, x):
        features1 = self.fpn1(x)
        features2 = self.fpn2(x)
        name = list(features1.keys())
        feat1 = list(features1.values())
        feat2 = list(features2.values())
        for i in range(len(feat1)-1,-1,-1):
          feat1[i] = torch.cat((feat1[i],feat2[i]),1)
          feat1[i] = self.conv(feat1[i])
          feat1[i] = self.norm(feat1[i])
          feat1[i] = self.conv2(feat1[i])
        out = OrderedDict([(k, v) for k, v in zip(name, feat1)])
        return out


def get_model(num_classes,pretrained):
    backbone1  = resnet_fpn_backbone("resnet101", pretrained, trainable_layers=5)
    backbone2  = resnet_fpn_backbone("resnet101", pretrained, trainable_layers=5)
    for layer in backbone2.body.layer1:
        layer.conv2 = nn.Conv2d(64, 64, kernel_size=(3, 3), stride=(1, 1), padding=2, bias=False,dilation = 2)
    for layer in backbone2.body.layer2:
        layer.conv2 = nn.Conv2d(128, 128, kernel_size=(3, 3), stride=(2, 2), padding=2, bias=False, dilation = 4)
    for layer in backbone2.body.layer3:
        layer.conv2 = nn.Conv2d(256,256, kernel_size=(3, 3), stride=(1, 1), padding=2, bias=False, dilation = 4)
    for layer in backbone2.body.layer4:
        layer.conv2 = nn.Conv2d(512,512, kernel_size=(3, 3), stride=(1, 1), padding=2, bias=False, dilation = 8)
    
    backbone_com = backbone1
    backbone_com.fpn = CombinedFPN(backbone1.fpn,backbone2.fpn)