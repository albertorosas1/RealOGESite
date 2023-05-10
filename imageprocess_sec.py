import cv2
import os


video_path = /videos
def save_frame_sec(video_path, sec, result_path, imgName):
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        return
    
    result_path = /images
    
    os.makedirs(os.path.dirname(result_path), exist_ok=True)
    
    fps = cap.get(cv2.CAP_PROP_FPS)
    
    cap.set(cv2.CAP_PROP_POS_FRAMES, round(fps * sec))
    
    ret, frame = cap.read()
    
    if ret:
        cv2.imwrite(result_path, frame, imgName)

)
