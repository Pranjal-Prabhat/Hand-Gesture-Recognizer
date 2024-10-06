# Hand-Gesture-Recogniser

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
git clone https://github.com/Pranjal-Prabhat/Hand-Gesture-Recogniser.git
cd Hand-Gesture-Recogniser
pip install -r requirements.txt
python handGestTest.py
```
### Indirect
1. Install (mediapipe,opencv) in pip.
2. Clone the repo.
3. Unzip the repo.
4. Run the test python file in the repo.

Note: Use 'esc' key to close window.

## Customizations
### At last the file have a function called recog in it:
#### 1st argument: Which camera to use (default 0)(computers inbuild camera).

#### 2nd argument: Is that is you want error is camera not open (default True).

#### 3rd argument: What should be the diffrent values for diffrent distance ranges (default [45, 48.4, 50,8,3.5]).

#### 4th argument: Is that is you want error when hand too close or far , i.e out of range (default False).

#### 5th argument: Is that if you want a window to open to see the results or want to run in backround (default True).

#### 6th argument: Is to which key to use to close the window(of opencv) (default 27 or esc key).

#### 7th argument: Is that is you want fps shown on window (default True). 

#### 8th argument: Is that is you want output shown on window (default True).

#### 9th, 10th and 11th argument:It is that if you want to show the x , y and z values on window. Only z is set to true.
