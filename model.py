import torch


class Model():
    def __init__(self):
        # Model
        self.model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

    def getphoto(self, dir_photo):
        # Inference
        results = self.model(dir_photo)
        return results

