from PyQt5.QtCore import Qt, QTimer, pyqtSignal
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QCheckBox
from abstract_layer import KeyCaptureLineEdit_PAGE
from file_resource_management import FileResources
from gesture_recognition_camera import gestureRecognitionCamera, main
import multiprocessing as mp
from shortcut_layer import shortcut
from translate_layer import TranslatedButton as QPushButton, TranslatedLabel as QLabel, TranslatedCheckBox as QCheckBox


class GestureControlUI(QWidget):
    switch_page_signal = pyqtSignal(int)
    def __init__(self):
        super().__init__()
        self.setStyleSheet(FileResources.load_gesture_control_qss())
        self.set_background()
        self.set_ui()
        self.set_callbacks()

    def set_background(self):
        self.gestureRecognitionCamera = gestureRecognitionCamera
        self.gestureRecognitionCamera_output_queue = mp.Queue(maxsize=1)
        self.show_image = mp.Value('b', False)
        self.gestureRecognitionCamera_process = None
        self.gestureRecognitionCamera_start_event = mp.Event()
        self.gestureRecognitionCamera_stop_event = mp.Event()

        self.check_queue_timer = QTimer()
        self.check_queue_timer.timeout.connect(self.check_queue)
        self.check_queue_timer.start(100)

    def set_widgets(self):
        self.status_label = QLabel()
        self.status_label.setObjectName("statusLabel")
        self.gesture_label = QLabel()
        self.gesture_label.setObjectName("gestureLabel")
        self.camera_display_checkbox = QCheckBox()
        self.camera_display_checkbox.setObjectName("cameraDisplayCheckbox")
        self.start_button = QPushButton()
        self.start_button.setObjectName("startButton")
        self.stop_button = QPushButton()
        self.stop_button.setObjectName("stopButton")
        self.next_page = QPushButton()


    def set_all_texts(self):
        self.status_label.setText("NotStarted")
        self.gesture_label.setText("CurrentGesture")
        self.camera_display_checkbox.setText("ShowCamera")
        self.start_button.setText("Start")
        self.stop_button.setText("Stop")
        self.next_page.setText("Settings")

    def set_layouts(self):
        h_layout1 = QHBoxLayout()
        h_layout2 = QHBoxLayout()
        layout = QVBoxLayout()

        h_layout1.addWidget(self.status_label, 1)
        h_layout1.addWidget(self.gesture_label, 2)
        h_layout1.setSpacing(20)

        layout.addLayout(h_layout1)
        layout.addWidget(self.camera_display_checkbox)
        layout.addSpacing(10)

        h_layout2.addWidget(self.start_button)
        h_layout2.addWidget(self.stop_button)
        h_layout2.addWidget(self.next_page)
        h_layout2.setSpacing(10)

        layout.addLayout(h_layout2)
        layout.addStretch()

        self.setLayout(layout)

    def set_ui(self):
        self.set_widgets()
        self.set_all_texts()
        self.set_layouts()

    def set_callbacks(self):
        self.next_page.clicked.connect(self.settings_callback)
        self.start_button.clicked.connect(self.start_gesture_recognition)
        self.stop_button.clicked.connect(self.stop_gesture_recognition)
        self.camera_display_checkbox.stateChanged.connect(self.toggle_camera_display)

    def settings_callback(self):
        self.switch_page_signal.emit(KeyCaptureLineEdit_PAGE)

    def check_queue(self):
        if self.gestureRecognitionCamera_process is not None:
            if not self.gestureRecognitionCamera_output_queue.empty():
                gesture = self.gestureRecognitionCamera_output_queue.get()
                self.gesture_label.setText("Current_Gesture", second=gesture)
                shortcut.trigger_shortcut(gesture)
        else:
            self.gesture_label.setText("Current_Gesture_None")

    def start_gesture_recognition(self):
        if self.gestureRecognitionCamera_process is None:
            self.gestureRecognitionCamera_process = mp.Process(
                target=main,
                args=(
                    self.gestureRecognitionCamera_start_event,
                    self.gestureRecognitionCamera_stop_event,
                    self.gestureRecognitionCamera_output_queue,
                    self.show_image,
                )
            )
            self.gestureRecognitionCamera_process.start()
        self.gestureRecognitionCamera_start_event.set()
        self.status_label.setText("Start")

    def stop_gesture_recognition(self):
        if self.gestureRecognitionCamera_process is not None:
            self.gestureRecognitionCamera_start_event.clear()
            self.gestureRecognitionCamera_stop_event.set()
            self.gestureRecognitionCamera_process.join()
            self.gestureRecognitionCamera_process = None
        self.status_label.setText("Stop")

    def toggle_camera_display(self, state):
        if state == Qt.Checked:
            self.show_image = True
        else:
            self.show_image = False


# if __name__ == "__main__":
#     app = QApplication([])
#     window = GestureControlUI()
#     window.show()
#     app.exec_()
