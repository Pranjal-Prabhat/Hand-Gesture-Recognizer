import cv2
import mediapipe as mp
import time

def recog(cam_no=0, cam_not_open_error=True, precision_values=[45, 48.4, 50,8,3.5], out_of_range_error=False, make_win=True,close_key=27, show_fps=True, show_out=True, show_x=False, show_y=False, show_z=True ):
    diff_x = diff_y = diff_z = avj_z = t_diff = fps = output = prev_time = curr_time = hand = 0
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
                tip_x = hand_landmarks.landmark[8].x * 100
                base_x = hand_landmarks.landmark[5].x * 100
                tip_y = hand_landmarks.landmark[8].y * 100
                base_y = hand_landmarks.landmark[5].y * 100
                tip_z = ((hand_landmarks.landmark[8].z + 1) / 2) * 100
                base_z = ((hand_landmarks.landmark[5].z + 1) / 2) * 100

                avj_z = (tip_z + base_z) / 2
                diff_x = abs(tip_x - base_x)
                diff_y = abs(tip_y - base_y)
                diff_z = abs(tip_z - base_z)
                t_diff = (diff_y**2 + diff_x**2)**0.5

                if precision_values[0] < avj_z < precision_values[1]:
                    if t_diff < precision_values[3] or tip_y > base_y:
                        output = 1
                    else:
                        output = 0
                elif precision_values[1] < avj_z < precision_values[2]:
                    if t_diff < precision_values[4] or tip_y > base_y:
                        output = 1
                    else:
                        output = 0
                elif avj_z < precision_values[0] or avj_z > precision_values[2]:
                    if out_of_range_error:
                        raise RuntimeError("Out of range error.")

            curr_time = time.time()
            fps = 1 / (curr_time - prev_time)
            prev_time = curr_time

            if show_fps:
                cv2.putText(image, f'FPS: {float(fps)}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
            if show_out:
                cv2.putText(image, f'OUTPUT: {int(output)}', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
            if show_z:
                cv2.putText(image, f'Z: {float(avj_z)}', (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
            if show_x:
                cv2.putText(image, f'X: {int(diff_x)}', (10, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
            if show_y:
                cv2.putText(image, f'Y: {int(diff_y)}', (10, 180), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        else:
            output= fps= diff_x= diff_y= avj_z= t_diff=hand =0
        if make_win:
            cv2.imshow('Hand Tracking', image)
            if cv2.waitKey(5) & 0xFF == close_key:
                break

                cap.release()
                cv2.destroyAllWindows()
        data = [hand,output, fps, diff_x, diff_y, avj_z, t_diff]

recog(0,True,[45, 48.4, 50,8,3.5],False,True,27,True,True,False,False,True)
