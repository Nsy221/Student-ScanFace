import streamlit as st
import face_rec
#from Main import face_rec
from streamlit_webrtc import webrtc_streamer
import av
import time
import threading


def scanFace():

    st.header('Please scan your face to record your attendance')
    
    # Retrieve the Data from Redis Database
    with st.spinner('Retrieving Data from Redis DB ...'):
        redis_face_db = face_rec.retrieve_data(name='academy:register')
        

    st.success("Data Successfully retrieve from Redis")

    waitTime = 20 #time in seconds
    setTime = time.time()
    realTimepred = face_rec.RealTimepred() #real time pred class
   
    #callback function
    def video_frame_callback(frame):
        
        img = frame.to_ndarray(format="bgr24") #3 dimension numpy array
        # operation that can perform on the array
        pred_img= realTimepred.face_prediction(img, redis_face_db,
                                            'facial_features', ['Name', 'Role'], thresh=0.5)

        return av.VideoFrame.from_ndarray(pred_img, format="bgr24")


    def save_data_periodically():
        while True:
            time.sleep(waitTime)
            realTimepred.saveLogs_redis()
            print('Saved data to Redis database')

    # Create a thread for saving data periodically
    save_thread = threading.Thread(target=save_data_periodically)
    save_thread.daemon = True  # Set the thread as a daemon so it exits when the main program exits
    save_thread.start()
    
    webrtc_streamer(key="realtimePrediction", video_frame_callback=video_frame_callback)


if __name__ == "__main__":
    scanFace()