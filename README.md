# Hand-Index-Finger_down-Recogniser
![WhatsApp Image 2024-09-27 at 23 13 37_98fa1de8](https://github.com/user-attachments/assets/6b31ebf1-32f9-4e7a-8a8b-1239933a22cf)
![WhatsApp Image 2024-09-27 at 23 14 04_e3f08d64](https://github.com/user-attachments/assets/166cd51e-0db8-4b27-bf93-8491999b7639)


---
Author: Pranjal Prabhat 👨‍🔬
---

## What's Diffrent 👀
-Easy acces to recognisation.

-High level optimization for commercial uses.

## Overview 🖐
Hand-Index-Finger_down-Recogniser can be used to recognise wether the index finger tip is close to the base of index finger.

## How to Use 👀
### Direct
#### Run these is cmd to run the file directly:
```cmd
cd %HOMEPATH%\Downloads
git clone https://github.com/Pranjal-Prabhat/Hand-Index-Finger_down-Recognizer.git
cd Hand-Index-Finger_down-Recognizer
pip install -r requirements.txt
python index_finger_gesture.py
cd Hand-Index-Finger_down-Recognizer
```
### Indirect
1. Install (mediapipe,opencv) using pip.
2. Clone the repo.
3. Unzip the repo.
4. Run the python file that is present in the repo.

#### Note: Use 'esc' key to close window.

## Customizations
### At last the file have a function called recog in it:
#### 1st argument: Which camera to use (default 0)(computers inbuild camera).

#### 2nd argument: Is that if you want error when camera not opens (default True).

#### 3rd argument: What should be the diffrent values for diffrent distance ranges (default [45, 48.4, 50,8,3.5]).

#### 4th argument: Is that if you want error when hand is too close or far , i.e out of range (default False).

#### 5th argument: Is that if you want a window to be open to see the results or want to run processes in backround (default True).

#### 6th argument: Is set which key to use to close the window(of opencv) (default 27 or esc key).

#### 7th argument: Is that if you want fps to be shown on the window (default True). 

#### 8th argument: Is that if you want output to be shown on window (default True)(Shown as 1 or 0).

#### 9th, 10th and 11th argument:It is that if you want to show the x , y and z values on window. Only z is set to true.
