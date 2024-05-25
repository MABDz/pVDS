
# pVDS

The Phlebotomist's Vein Detection System (pVDS) is a biomedical device designed to improve the accuracy of peripheral vein access procedures by helping locate and visualize the superficial vein structure in epidermal tissue.



## System Components

####  Vein Finder Wand

<img src="https://i.imgur.com/o2DipfS.jpeg" alt="Wand" width="300"/>

This is the hardware component of pVDS. It primarily consists of an array of IR-Illuminators, IR-Sensitive Camera, and a narrow-band-pass IR-filter. This allows for low-noise, realtime image acquisition. The Wand draws power and communicates to a PC through a single USB connection. 

#### pVDS Software

This program runs in tandem with the Vein Finder Wand to process the images captured by the IR-Sensitive camera. The program does so by parsing the raw output from the Wand and performing a series of adjustments to make vein structures clearly visible. This is achieved by processing the input first through a grayscale filter to improve perfomance in later steps. Content Limited Adaptive Histogram Equalization (CLAHE) is then performed, and finally the image is run through a sharpening filter. The intensity of each of these steps can be manually adjusted to optimize the output for different patients and skin tones.



## Use Cases
1. Training of medical staff, in particular Phlebotomists
2. Emergency situations where Venipuncture must be performed by an untrained individual
3. Identifying medical conditions such as Thrombosis and venous embolism


