from normanos.message_bus import MessageBus

from normanos.intent import IntentEngine
from normanos.brain import BrainModule
from normanos.motion import MotionModule
from normanos.task_manager import TaskManager
from normanos.runtime import RobotRuntime
from normanos.interface import NormanInterface

import threading

# --------------------
# System setup
# --------------------
bus = MessageBus()

intent = IntentEngine(bus)
brain = BrainModule(bus)
motion = MotionModule(bus)
tasks = TaskManager(bus)

runtime = RobotRuntime(tasks)
interface = NormanInterface(bus)

# --------------------
# Start robot runtime (background thread)
# --------------------
threading.Thread(target=runtime.start, daemon=True).start()

# --------------------
# Start user interface (main thread)
# --------------------
interface.start()