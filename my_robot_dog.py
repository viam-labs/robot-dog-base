# Custom base implementation for quadruped robot dog

import time
from typing import Any, Dict, Optional
from viam.components.base import Base, Vector3
import socket
import sys

sys.path.append("/home/fido/.local/lib/python3.9/site-packages")


class RobotDog(Base):
    # Subclass the Viam base component and implement the required functions
    def __init__(self, name: str):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(("10.0.0.144", 5001))
        # Per the Freenove code, 5001 is for sending/receiving instructions. Port 8001 is used for video.
        super().__init__(name)

    def send_data(self, data):
        try:
            self.client_socket.send(data.encode("utf-8"))
        except Exception as e:
            print(e)

    async def set_power(self, linear: Vector3, angular: Vector3, extra: Optional[Dict[str, Any]] = None, **kwargs):
        self.linear_pwr = linear
        self.angular_pwr = angular

        # Convert from power percentage (0-1) to what to send to robot dog.
        conversion_factor_a = 30
        conversion_factor_l = 20
        ang_vel = int(angular.z * conversion_factor_a)
        lin_vel = int(linear.y * conversion_factor_l)

        if ang_vel > 0:
            command = "CMD_TURN_LEFT#" + str(ang_vel) + "\n"

        if ang_vel < 0:
            ang_vel = abs(ang_vel)
            command = "CMD_TURN_RIGHT#" + str(ang_vel) + "\n"

        if ang_vel != 0:
            self.send_data(command)

        if lin_vel > 0:
            command = "CMD_MOVE_FORWARD#" + str(lin_vel) + "\n"

        if lin_vel < 0:
            lin_vel = abs(lin_vel)
            command = "CMD_MOVE_BACKWARD#" + str(lin_vel) + "\n"

        if lin_vel != 0:
            self.send_data(command)

    async def stop(self, extra: Optional[Dict[str, Any]] = None, **kwargs):
        self.is_stopped = True

        command = "CMD_MOVE_STOP#8\n"
        self.send_data(command)

    async def is_moving(self):
        # return not self.is_stopped
        return False

    async def do(self, command: Dict[str, Any]):
        angle = str(command.get("head_tilt"))
        command = "CMD_HEAD#" + angle + "\n"

        self.send_data(command)
