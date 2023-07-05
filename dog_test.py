# dog_test.py is for testing the connection

import socket, time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("PASTE DOG IP ADDRESS HERE", 5001))

cmd = "CMD_MOVE_FORWARD#50"
s.send(cmd.encode("utf-8"))
time.sleep(3)
cmd = "CMD_MOVE_FORWARD#80"
s.send(cmd.encode("utf-8"))
time.sleep(3)
cmd = "CMD_MOVE_FORWARD#25"
s.send(cmd.encode("utf-8"))
time.sleep(3)
cmd = "CMD_MOVE_FORWARD#35"
s.send(cmd.encode("utf-8"))
time.sleep(3)
