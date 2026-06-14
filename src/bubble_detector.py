import cv2

def detect_bubble(video_path):
    video = cv2.VideoCapture(video_path)

    ret, frame1 = video.read()
    ret, frame2 = video.read()

    while ret:

        diff = cv2.absdiff(frame1, frame2)

        gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

        _, thresh = cv2.threshold(
            gray,
            25,
            255,
            cv2.THRESH_BINARY
        )

        contours, _ = cv2.findContours(
            thresh,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        for c in contours:

            if cv2.contourArea(c) < 50:
                continue

            x, y, w, h = cv2.boundingRect(c)

            cv2.rectangle(
                frame1,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

        cv2.imshow("Bubble Detection", frame1)

        frame1 = frame2
        ret, frame2 = video.read()

        if cv2.waitKey(30) == 27:
            break

    video.release()
    cv2.destroyAllWindows()
