# Object detection with Flask

## Basic 
This app was developed as a final project 
for a [Deep Learning School](https://www.dlschool.org/).
I chose the first scenario in which it was necessary 
to develop a **web-demo** application using a 
pretrained model. [Model](https://pytorch.org/hub/ultralytics_yolov5/) taken from 
[PyTorch](https://pytorch.org/) official source. The site was 
hosted on google cloud with the address http://objdetvarfa.ipq.co:5000/

## How to run it?

Create a folder object-detection:
```
mkdir object-detection
cd object-detection
```

Git clone:
```
git clone https://github.com/Varfalamei/obj-det-flask.git
```

Install requirements:
```
pip install -r requirements.txt
```
run application:
```
python3 app.py
```

## Examples
Input photo
![alt text](screenshots/people_rest.jpg "Описание будет тут")
Output photo
![alt text](screenshots/people_rest_det.JPG "Описание будет тут")