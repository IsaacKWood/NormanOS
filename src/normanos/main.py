import threading

from normanos.message_bus import MessageBus
from normanos.system_state import SystemState

from normanos.intent import IntentEngine
from normanos.brain import BrainModule
from normanos.planner import PlanningEngine

from normanos.task_manager import TaskManager
from normanos.runtime import RobotRuntime

from normanos.command_engine import CommandEngine
from normanos.interface import NormanInterface


def boot_banner():
    print("\n" + "=" * 30)
    print("        NormanOS v0.1")
    print("   AI Engineering Assistant")
    print("=" * 30 + "\n")


def main():
    boot_banner()

    state = SystemState()
    bus = MessageBus()

    planner = PlanningEngine()

    task_manager = TaskManager(bus, state)

    runtime = RobotRuntime(task_manager)
    threading.Thread(target=runtime.start, daemon=True).start()

    IntentEngine(bus)
    BrainModule(bus, planner)

    command_engine = CommandEngine(bus, state, task_manager)
    interface = NormanInterface(bus, command_engine)

    print("\n🤖 Norman is ready.\n")

    interface.start()


if __name__ == "__main__":
    main()