import sys
import psutil
import os
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QFrame
from PyQt6.QtCore import Qt, QTimer, QPoint

os.environ["QT_QPA_PLATFORM"] = "xcb"

def bar(value, max_value=100, size=12):
    filled = int((value / max_value) * size)
    return "█" * filled + "░" * (size - filled)

class Overlay(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("photon")

        # Ventana overlay total con Bypass para X11 (Forzar siempre encima)
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint | 
            Qt.WindowType.WindowStaysOnTopHint | 
            Qt.WindowType.Tool |
            Qt.WindowType.X11BypassWindowManagerHint
        )

        # Transparencia real
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setGeometry(50, 50, 300, 180)
        
        # Variable para controlar el arrastre
        self.drag_position = QPoint()

        # Layout exterior
        outer_layout = QVBoxLayout(self)

        # Panel interior
        panel = QFrame()
        panel.setStyleSheet("""
            QFrame {
                background-color: rgba(10, 10, 10, 150);
                border-radius: 18px;
                padding: 12px;

            }
            QLabel {
                color: #E6E6E6;
                font-size: 14px;
                background-color: transparent;
            }
        """)

        layout = QVBoxLayout()

        # Labels
        self.title = QLabel("Estadisticas")
        self.cpu_label = QLabel()
        self.ram_label = QLabel()
        self.net_label = QLabel()
        self.temp_label = QLabel()
        

        self.title.setStyleSheet("""
            font-size: 18px;
            font-weight: bold;
            color: #7CFF6B;
        """)
        self.cpu_label.setStyleSheet("color: #7CFF6B;")
        self.ram_label.setStyleSheet("color: #7CFF6B;")
        self.net_label.setStyleSheet("color: #7CFF6B;")
        self.temp_label.setStyleSheet("color: #7CFF6B;")

        layout.addWidget(self.title)
        layout.addSpacing(10)
        layout.addWidget(self.cpu_label)
        layout.addWidget(self.ram_label)
        layout.addWidget(self.net_label)
        layout.addWidget(self.temp_label)

        panel.setLayout(layout)
        outer_layout.addWidget(panel)

        # Inicialización de red
        self.old_net = psutil.net_io_counters()

        # Timer actualización
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_stats)
        self.timer.start(1000)

        self.update_stats()

    def get_temp(self):
        try:
            temps = psutil.sensors_temperatures()
            for name in temps:
                return temps[name][0].current
        except:
            return None
    
    def update_stats(self):
        cpu = psutil.cpu_percent()
        ram = psutil.virtual_memory().percent

        new_net = psutil.net_io_counters()

        down = (new_net.bytes_recv - self.old_net.bytes_recv) / 1024
        up = (new_net.bytes_sent - self.old_net.bytes_sent) / 1024

        self.cpu_label.setText(f"CPU   {bar(cpu)} {cpu:.0f}%")
        self.ram_label.setText(f"RAM  {bar(ram)} {ram:.0f}%")
        self.net_label.setText(f"RED   ↓ {down:.1f} KB/s  ↑ {up:.1f} KB/s")

        temp = self.get_temp()
        self.temp_label.setText(
            f"TEMP: {temp:.1f}°C" if temp else "TEMP: N/A"
        )

        self.old_net = new_net

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            # Calculamos la distancia entre el puntero del ratón y la esquina superior izquierda de la ventana
            self.drag_position = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton:
            # Movemos la ventana restando la distancia calculada en el click inicial
            self.move(event.globalPosition().toPoint() - self.drag_position)
            event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    overlay = Overlay()
    overlay.show()
    sys.exit(app.exec())