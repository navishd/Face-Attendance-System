import cv2
import os
import pandas as pd
from datetime import datetime
from deepface import DeepFace

DB_PATH = "database"
CSV_FILE = "Attendance.csv"

cap = cv2.VideoCapture(0)

marked_today = set()

while True:

    ret, frame = cap.read()

    if not ret:
        break

    try:

        result = DeepFace.find(
            img_path=frame,
            db_path=DB_PATH,
            enforce_detection=False,
            silent=True
        )

        if len(result) > 0 and len(result[0]) > 0:

            identity = result[0].iloc[0]["identity"]

            name = os.path.basename(identity)
            name = os.path.splitext(name)[0].upper()

            # Face coordinates
            x = int(result[0].iloc[0]["source_x"])
            y = int(result[0].iloc[0]["source_y"])
            w = int(result[0].iloc[0]["source_w"])
            h = int(result[0].iloc[0]["source_h"])

            # Green face box
            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

            # Name background box
            cv2.rectangle(
                frame,
                (x, y + h - 35),
                (x + w, y + h),
                (0, 255, 0),
                -1
            )

            # Name text
            cv2.putText(
                frame,
                name,
                (x + 10, y + h - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255, 255, 255),
                2
            )

            today = datetime.now().strftime("%Y-%m-%d")
            key = f"{name}_{today}"

            if key not in marked_today:

                now = datetime.now()

                row = {
                    "Name": name,
                    "Time": now.strftime("%H:%M:%S"),
                    "Date": now.strftime("%Y-%m-%d")
                }

                df = pd.read_csv(CSV_FILE)

                df.loc[len(df)] = row

                df.to_csv(
                    CSV_FILE,
                    index=False
                )

                marked_today.add(key)

                print(f"{name} Attendance Marked")

        else:

            # Red warning banner
            cv2.rectangle(
                frame,
                (20, 20),
                (550, 90),
                (0, 0, 255),
                -1
            )

            cv2.putText(
                frame,
                "UNKNOWN PERSON DETECTED",
                (30, 65),
                cv2.FONT_HERSHEY_DUPLEX,
                0.9,
                (255, 255, 255),
                2
            )

    except Exception as e:
        print("Error:", e)

    cv2.imshow(
        "Face Attendance System",
        frame
    )

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()