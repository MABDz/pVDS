from ctypes import resize
import PySimpleGUI as sg
import cv2
import numpy as np
from skimage import io, filters, feature
from skimage.color import rgb2gray
from skimage.filters import meijering, sato, frangi, hessian
import pyi_splash

def multi_clahe(img, num):
    
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    for i in range(int(num)):
        img = cv2.createCLAHE(clipLimit=10, tileGridSize=(4+i*2,4+i*2)).apply(img)
    return img

def multi_sharp(img, num):
    
    kernel = np.array([[0, -1, 0], [-1, 5,-1], [0, -1, 0]])
    for i in range(int(num)):
        img = cv2.filter2D(src=img, ddepth=-1, kernel=kernel)
    return img

pyi_splash.update_text('UI Loaded ...')
pyi_splash.close()

def main():
    
    sg.theme("LightBlue6")
    
    col1 = [ [sg.Image(filename="", key="-IMAGE-")]]
    
    bstatus = True

    col2 = [[sg.Image(filename="Logo50.png", size=(500,210))],
            
            [sg.Text('Cameras:'),
             sg.Radio("Cam1", "Radio", visible = bstatus, size=(10, 1), key="-C1-"),
             sg.Radio("Cam2", "Radio", visible = bstatus, size=(10, 1), key="-C2-"),
             sg.Radio("Cam3", "Radio", visible = bstatus, size=(10, 1), key="-C3-")],
            [sg.Text(" ")],
            [sg.Checkbox("Use Multi-Pass filters", size=(20, 1), key="-MANUAL-")], 

            [sg.Text('Multi-Clahe passes:'),
                sg.Slider(
                            (0, 15),
                            0,
                            1,
                            orientation="h",
                            size=(40, 15),
                            key="-THRESH SLIDER-")],
            
            [sg.Text("Multi-Sharpen passes:"),
                        sg.Slider(
                            (0, 3),
                            0,
                            1,
                            orientation="h",
                            size=(40, 15),
                            key="-SHARP SLIDER-",
                        ),
                    ],
            
            [sg.Text(" ")],


            
            [sg.Radio("Sato Filter", "Radio", size=(10, 1), key="-SATO-"),
             sg.Radio("Meijering Filter", "Radio", size=(10, 1), key="-MEIJERING-"),
             sg.Radio("Hessian Filter", "Radio", size=(10, 1), key="-HESSIAN-")],
            [sg.Text(" ")],
            
            [sg.Button("Exit", size=(10, 1))]]
    
    
    
    layout = [ [sg.Column(col2, element_justification="c"), sg.Column(col1)] ]

    window = sg.Window("pVDS Image Processor", layout, resizable=True)
    
    capd = "none"
    
    while capd == "none":
        
            event, values = window.read(timeout=20)
            
            if values["-C1-"]:
                bstatus = False
                capd = 0
                
            elif values["-C2-"]:
                bstatus = False
                capd = 1
                
            elif values["-C3-"]:
                bstatus = False
                capd = 2
                

    cap = cv2.VideoCapture(capd)

    while True:
            event, values = window.read(timeout=20)
            if event == "Exit" or event == sg.WIN_CLOSED:
                break
            
            ret, frame = cap.read()

            if values["-MANUAL-"]:
    
                frame = multi_sharp(frame, values["-SHARP SLIDER-"])
                frame = multi_clahe(frame, values["-THRESH SLIDER-"])
                
       
            if values["-MEIJERING-"]:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame = rgb2gray(frame)
                frame = meijering(frame)
                frame = cv2.putText(frame,"Press Q to Exit", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 50, 0))
                cv2.imshow('Project VDD', frame)
                if cv2.waitKey(1) == ord('q'):
                    break
                
            if values["-HESSIAN-"]:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame = rgb2gray(frame)
                frame = hessian(frame)
                frame = cv2.putText(frame,"Press Q to Exit", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 50, 0))
                cv2.imshow('Project VDD', frame)
                if cv2.waitKey(1) == ord('q'):
                    break
                
            if values["-SATO-"]:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame = rgb2gray(frame)
                frame = sato(frame)
                frame = cv2.putText(frame,"Press Q to Exit", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 50, 0))
                cv2.imshow('Project VDD', frame)
                if cv2.waitKey(1) == ord('q'):
                    break
                    
                #frame = cv2.addWeighted(frame, 2, np.zeros(frame.shape, frame.dtype), 0, 50)
            

            imgbytes = cv2.imencode(".png", frame)[1].tobytes()
            window["-IMAGE-"].update(data=imgbytes)

    window.close()

main()
