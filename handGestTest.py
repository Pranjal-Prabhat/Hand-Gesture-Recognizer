import cv2
import mediapipe as mp
import time

def isFinDown(finBaseX,finBaseY,finTipX,finTipY,finAvgZ,wristY,precisionValues=[45,48.4,50,8,3.5]):
    out1=0
    tdiff = (abs(finBaseX-finTipX)**2 + abs(finTipY-finBaseY)**2)**(0.5)
    
    if ((precisionValues[0] < finAvgZ < precisionValues[1]) and finTipY<wristY):
        if tdiff < precisionValues[3] or finTipY > finBaseY:
            out1 = 1
        else:
            out1 = 0
    elif ((precisionValues[1] < finAvgZ < precisionValues[2]) and finTipY<wristY):
        if tdiff < precisionValues[4] or finTipY > finBaseY:
            out1 = 1
        else:
            out1 = 0
    elif (finAvgZ < precisionValues[0] or finAvgZ > precisionValues[2]):
        out1=0
    
    return out1

def isFinClose(point1X,point1Y,point2X,point2Y,finAvgZ,precisionValues=[45,48.4,50,8,3.5]):
    out2=0
    tdiff2 = (abs(point1X-point2X)**2 + abs(point2Y-point1Y)**2)**(0.5)
    
    if ((precisionValues[0] < finAvgZ < precisionValues[1])):
        if tdiff2 < precisionValues[3]:
            out2 = 1
        else:
            out2 = 0
    elif ((precisionValues[1] < finAvgZ < precisionValues[2])):
        if tdiff2 < precisionValues[4]:
            out2 = 1
        else:
            out2 = 0
    elif (finAvgZ < precisionValues[0] or finAvgZ > precisionValues[2]):
        out2=0

    return out2




def recog(cam_no=0, cam_not_open_error=True, precisionValues=[45, 48.4, 50,8,3.5], out_of_range_error=False, make_win=True,close_key=27, show_fps=True, show_out=True,printing=True):
    fps = output = prev_time = curr_time = finded = 0

    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5)
    mp_drawing = mp.solutions.drawing_utils

    cap = cv2.VideoCapture(cam_no)

    while cap.isOpened():
        success, image = cap.read()
        if not success:
            if cam_not_open_error:
                raise RuntimeError("Camera number specified in recog function was either not working or was not able to open.")
            else:
                continue

        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image_rgb)

        if results.multi_hand_landmarks:
            hand=1
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                indexTipX = hand_landmarks.landmark[8].x * 100
                indexTipY = hand_landmarks.landmark[8].y * 100
                indexBaseX = hand_landmarks.landmark[5].x * 100
                indexBaseY = hand_landmarks.landmark[5].y * 100
                indexTipZ = ((hand_landmarks.landmark[8].z + 1)/2)*100
                indexBaseZ = ((hand_landmarks.landmark[5].z + 1)/2)*100

                middleTipX = hand_landmarks.landmark[12].x * 100
                middleTipY = hand_landmarks.landmark[12].y * 100
                middleBaseX = hand_landmarks.landmark[9].x * 100
                middleBaseY = hand_landmarks.landmark[9].y * 100
                middleTipZ = ((hand_landmarks.landmark[12].z + 1)/2)*100
                middleBaseZ = ((hand_landmarks.landmark[9].z + 1)/2)*100

                ringTipX = hand_landmarks.landmark[16].x * 100
                ringTipY = hand_landmarks.landmark[16].y * 100
                ringBaseX = hand_landmarks.landmark[13].x * 100
                ringBaseY = hand_landmarks.landmark[13].y * 100
                ringTipZ = ((hand_landmarks.landmark[16].z + 1)/2)*100
                ringBaseZ = ((hand_landmarks.landmark[13].z + 1)/2)*100

                pinkyTipX = hand_landmarks.landmark[20].x * 100
                pinkyTipY = hand_landmarks.landmark[20].y * 100
                pinkyBaseX = hand_landmarks.landmark[17].x * 100
                pinkyBaseY = hand_landmarks.landmark[17].y * 100
                pinkyTipZ = ((hand_landmarks.landmark[20].z + 1)/2)*100
                pinkyBaseZ = ((hand_landmarks.landmark[17].z + 1)/2)*100

                ringTipX = hand_landmarks.landmark[16].x * 100
                ringTipY = hand_landmarks.landmark[16].y * 100
                ringBaseX = hand_landmarks.landmark[13].x * 100
                ringBaseY = hand_landmarks.landmark[13].y * 100
                ringTipZ = ((hand_landmarks.landmark[16].z + 1)/2)*100
                ringBaseZ = ((hand_landmarks.landmark[13].z + 1)/2)*100

                thumbTipX = hand_landmarks.landmark[4].x * 100
                thumbTipY = hand_landmarks.landmark[4].y * 100
                thumbBaseX = hand_landmarks.landmark[1].x * 100
                thumbBaseY = hand_landmarks.landmark[1].y * 100
                thumbTipZ = ((hand_landmarks.landmark[4].z + 1)/2)*100
                thumbBaseZ = ((hand_landmarks.landmark[1].z + 1)/2)*100

                indexAvgZ = (indexTipZ + indexBaseZ) / 2
                middleAvgZ = (middleTipZ + middleBaseZ) / 2
                ringAvgZ = (ringTipZ + ringBaseZ) / 2
                pinkyAvgZ = (pinkyTipZ + pinkyBaseZ) / 2
                thumbAvgZ = (thumbTipZ + thumbBaseZ) / 2

                wristX= hand_landmarks.landmark[0].x * 100
                wristY= hand_landmarks.landmark[0].y * 100 
                wristZ= ((hand_landmarks.landmark[0].z + 1)/2)*100

                
            indexOut = isFinDown(indexBaseX,indexBaseY,indexTipX,indexTipY,indexAvgZ,wristY)
            middleOut = isFinDown(middleBaseX,middleBaseY,middleTipX,middleTipY,middleAvgZ,wristY)
            ringOut = isFinDown(ringBaseX,ringBaseY,ringTipX,ringTipY,ringAvgZ,wristY)
            pinkyOut = isFinDown(pinkyBaseX,pinkyBaseY,pinkyTipX,pinkyTipY,pinkyAvgZ,wristY)
            thumbOut = isFinDown(thumbBaseX,thumbBaseY,thumbTipX,thumbTipY,thumbAvgZ,wristY)



            finded =0
                    
            if (indexOut == 1 and (middleOut+ringOut+pinkyOut)==0 and finded == 0 ):
                output = 1
                finded = 1

            if (middleOut == 1 and (indexOut+ringOut+pinkyOut)==0 and finded == 0 ):
                output = 2
                finded = 1

            if (middleOut == 0 and (isFinDown(indexBaseX,indexBaseY,indexTipX,indexTipY,indexAvgZ,wristY,[45,48.4,50,9,4.5])+isFinDown(ringBaseX,ringBaseY,ringTipX,ringTipY,ringAvgZ,wristY,[45,48.4,50,9,4.5])+isFinDown(pinkyBaseX,pinkyBaseY,pinkyTipX,pinkyTipY,pinkyAvgZ,wristY,[45,48.4,50,9,4.5]))==3 and finded == 0 ):
                output = 3
                finded = 1

            if (ringOut == 0 and (indexOut+middleOut+pinkyOut)==3 and finded == 0 ):
                output = 4
                finded = 1

            if ((ringOut+middleOut)==2 and (indexOut+thumbOut+pinkyOut)==0):
                output = 5
                finded = 1

            if ((ringOut+middleOut)==0 and (indexOut+pinkyOut)==2):
                output = 6
                finded = 1

            if ((indexOut+ringOut)==2 and (middleOut+pinkyOut)==0):
                output = 7
                finded = 1            

            if (isFinClose(indexTipX,indexTipY,middleTipX,middleTipY,wristZ,[45, 48.4, 50,10,6]) + isFinClose(pinkyTipX,pinkyTipY,ringTipX,ringTipY,wristZ,[45, 48.4, 50,10,6])+ isFinClose(ringTipX,ringTipY,middleTipX,middleTipY,wristZ,[45, 48.4, 50,10,6])==3 and isFinClose(thumbBaseX,thumbBaseY,thumbTipX,thumbBaseY,wristZ,[45, 48.4, 50, 13, 7]) == 0 and finded == 0):
                output= 8
                finded = 1

            if (isFinClose(pinkyTipX,pinkyTipY,thumbTipX,thumbTipY,middleAvgZ,[45, 48.4, 50,10,6])==1 and finded == 0):
                output = 9
                finded = 1

            if (isFinClose(middleTipX,middleTipY,thumbTipX,thumbTipY,pinkyAvgZ,[45, 48.4, 50,10,6])==1 and finded == 0):
                output = 10
                finded = 1

            if (finded == 0):
                output = 0

            curr_time = time.time()
            fps = 1 / (curr_time - prev_time)
            prev_time = curr_time

            if show_fps:
                cv2.putText(image, f'FPS: {int(fps)}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
            if show_out:
                cv2.putText(image, f'OUTPUT: {(output)}', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

        else:
            output= fps= indexDiffX= indexDiffY= indexAvgZ= indexDiffT=hand =None

        if printing:
            print(f"Hand:{hand} Output:{output} FPS:{fps}")

        if make_win:
            cv2.imshow('Hand Tracking', image)
            if cv2.waitKey(5) & 0xFF == close_key:
                break

                cap.release()
                cv2.destroyAllWindows()

        yield [hand,output,fps]

recog(0,True,[45, 48.4, 50,8,3.5],False,True,27,True,True,False)

for result in recog():
    pass
    # hand, output, fps= result
    # print(f"{hand},{output},{fps}")
