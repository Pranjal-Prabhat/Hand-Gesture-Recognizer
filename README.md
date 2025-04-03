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
### Automatic
#### Run these is cmd to run the file directly:
##### Linux
```terminal
#!/bin/bash

INSTALL_DIR="$HOME/.local/share/hand-gesture"
mkdir -p "$INSTALL_DIR"
python3 -m venv "$INSTALL_DIR/venv"
source "$INSTALL_DIR/venv/bin/activate"
pip3 install hand-gest-recog-example-by-pranjal

echo '#!/bin/bash' > "$INSTALL_DIR/hand-gest-test-by-pranjal.sh"
echo "source \"$INSTALL_DIR/venv/bin/activate\" && python3 -c 'import hand_gest_example'" >> "$INSTALL_DIR/hand-gest-test-by-pranjal.sh"
chmod +x "$INSTALL_DIR/hand-gest-test-by-pranjal.sh"

mkdir -p "$HOME/.local/bin"
ln -sf "$INSTALL_DIR/hand-gest-test-by-pranjal.sh" "$HOME/.local/bin/hand-gest-test-by-pranjal"

DESKTOP_FILE="$HOME/Desktop/hand-gest-test-by-pranjal.desktop"
echo "[Desktop Entry]
Type=Application
Name=Hand Gest Test by Pranjal
Exec=$INSTALL_DIR/hand-gest-test-by-pranjal.sh
Icon=utilities-terminal
Terminal=true" > "$DESKTOP_FILE"
chmod +x "$DESKTOP_FILE"

export PATH="$HOME/.local/bin:$PATH"
echo "Setup complete. Run 'hand-gest-test-by-pranjal' in terminal or use the Desktop shortcut."
bash
```

##### Windows
```terminal
pip install --user hand-gest-recog-example-by-pranjal && (
echo @echo off
echo python -c "import hand_gest_example"
) > "%USERPROFILE%\Desktop\handgest.bat" && setx PATH "%PATH%;%USERPROFILE%\Desktop" && powershell "$s=(New-Object -COM WScript.Shell).CreateShortcut('%USERPROFILE%\Desktop\hand-gest-test-by-pranjal.lnk'); $s.TargetPath='%COMSPEC%'; $s.Arguments='/k handgest'; $s.Save()"
```
### Note: Bigger script in linux doesn't means windows is better! 

### Running the script:
##### Open cmd in windows or Terminal for linux then run this command:
```terminal
hand-gest-test-by-pranjal
```

#### Note: You can directly run the app from desktop

### Indirect

1. Get a stable python3 version (3.11.8 recommonded)
2. Make a python3 Envoirment
3. In the envoirment install mediapipe and opencv
4. clone the repo inside envoirment
5. run the HandGestTest.py code inside the envoirment
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
