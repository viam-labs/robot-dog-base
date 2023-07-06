# DEPRECATED; we now recommend using robotdog.py, configured as a modular resource,
# rather than using this server implementation.
# Python SDK server for the custom base component
import sys
import time
import asyncio
from viam.rpc.server import Server

from my_robot_dog import RobotDog

# Add another directory where Python will look when importing modules
sys.path.append(<path to where you installed python3.9/site-packages>)
# For example sys.path.append(/home/fido/.local/lib/python3.9/site-packages)


async def main():
    time.sleep(5)  # Give the dog server time to start up
    srv = Server([RobotDog("my-robot-dog")])
    await srv.serve()


if __name__ == "__main__":
    asyncio.run(main())
