import cv2

class VideoCamera:
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        self.tracker = None
        self.bbox = None
        self.init_tracking = False

    def __del__(self):
        self.video.release()

    def set_bbox(self, x, y, w, h):
        self.bbox = (x, y, w, h)
        self.init_tracking = True

    def get_frame(self):
        success, frame = self.video.read()
        if not success:
            return None

        if self.init_tracking and self.bbox:
            self.tracker = cv2.TrackerCSRT_create()
            print("Received bbox:", self.bbox)
            print("Type:", type(self.bbox), "Content:", self.bbox)

            if frame is None:
              print("❌ ERROR: Frame is None!")
              return None

            self.tracker.init(frame, self.bbox)
            self.init_tracking = False

        if self.tracker:
            success, box = self.tracker.update(frame)
            if success:
                (x, y, w, h) = [int(v) for v in box]
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        _, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()
