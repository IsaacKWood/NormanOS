<<<<<<< HEAD
# NormanOS

> **NormanOS** is an event-driven robotics operating system that powers **Norman**, an AI Engineering Assistant designed to understand natural language, reason about tasks, and eventually interact with the physical world.

---

# Project Vision

Norman is a long-term engineering project focused on building a modular AI-powered robotics platform from the ground up.

The ultimate goal is to create an assistant capable of:

- Understanding natural language
- Planning multi-step tasks
- Learning from previous interactions
- Monitoring its own system state
- Integrating with sensors and hardware
- Controlling a physical robot
- Assisting with engineering design and problem solving

Rather than relying on one large script, Norman is built using independent modules that communicate through a central Message Bus, making the system scalable, maintainable, and easy to expand.

---

# Current Features (v0.1)

✅ Event-driven Message Bus

✅ Command Line Interface

✅ Intent Engine

✅ Brain Module

✅ Task Manager

✅ Motion Module

✅ Robot Runtime

✅ Shared System State

✅ Memory Module

✅ Command Engine

---

# Current Commands

## System

```text
status
help
shutdown
```

## Movement

```text
move forward
stop
move forward then stop
```

---

# System Architecture

```text
                  User
                    │
                    ▼
          Norman Interface
                    │
                    ▼
           Command Engine
          ┌─────────┴─────────┐
          │                   │
          ▼                   ▼
   System Commands      AI Pipeline
                              │
                              ▼
                      Intent Engine
                              │
                              ▼
                       Brain Module
                              │
                              ▼
                       Task Manager
                              │
                              ▼
                       Motion Module

Shared Services

• Message Bus
• System State
• Robot Runtime
• Memory Module
```

---

# Project Structure

```text
NormanOS/
│
├── docs/
│   ├── architecture.md
│   ├── roadmap.md
│   ├── commands.md
│   ├── changelog.md
│   └── vision.md
│
├── src/
│   └── normanos/
│
├── tests/
│
├── README.md
├── pyproject.toml
├── requirements.txt
└── .gitignore
```

---

# Design Philosophy

Norman is built around five core principles.

### Modular

Each subsystem performs one responsibility.

### Event Driven

Modules communicate using published events instead of direct dependencies.

### Expandable

New capabilities should be added without rewriting existing modules.

### Hardware Independent

The software should run without requiring physical hardware during development.

### Engineering Focused

Norman is designed to become an engineering assistant capable of solving technical problems and controlling robotic systems.

---

# Future Goals

- Persistent long-term memory
- Computer vision
- Voice conversation
- Engineering calculations
- CAD integration
- Internet research
- Robot navigation
- Autonomous task planning
- Hardware control
- Cloud synchronization

---

# Example Session

```text
=====================================
           NormanOS v0.1
      AI Engineering Assistant
=====================================

NormanOS starting...

🤖 Norman is online.

You: move forward then stop

🧠 Intent analyzing: move forward then stop

🧠 Brain → task: move_forward
📌 Task added: {'action': 'move_forward'}
🤖 Motion: moving forward

🧠 Brain → task: stop
📌 Task added: {'action': 'stop'}
🛑 Motion: stopped
```

---

# Author

Isaac Wood

Mechanical / Electrical Engineering Student

University of Wyoming

Project Norman is a long-term engineering project exploring artificial intelligence, robotics, and autonomous systems.

---

# License

Currently private.

Future license to be determined.
=======
# NormanOS
>>>>>>> 20ac8a7e395db6c143f95066a8a588649453df03
