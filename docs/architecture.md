# NormanOS Architecture

## Current Architecture

User
│
▼
Norman Interface
│
▼
Command Engine
│
├── System Commands
│      ├── status
│      ├── help
│      └── shutdown
│
└── AI Pipeline
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

Shared Components

• Message Bus
• System State
• Robot Runtime
• Memory Module

---

## Core Design Principles

- Modular design
- Event-driven communication
- Single responsibility per module
- Easily expandable
- Hardware independent