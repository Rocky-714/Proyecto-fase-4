SoftwareFJ - Reservation Management System
This project is a robust reservation management system developed using Object-Oriented Programming (POO). The software handles reservations for specialized services (rooms, equipment, and consulting) with a strong emphasis on data integrity, advanced exception handling, and persistent event logging.

Technical Specifications
Architecture: Modular design utilizing abstract base classes, inheritance, and polymorphism to ensure scalability.

Exception Handling: Custom exception definitions and strategic recovery flows (try/except/else/finally) to maintain system stability.

Data Integrity: Strict validation layers at the entity level to ensure consistent system state.

Persistence: Real-time event auditing and error tracking through a centralized logging system.

Environment: Standalone Python application developed without external dependencies.

Project Structure
Plaintext
SoftwareFJ/
│
├── main.py              # Main entry point for console simulations
├── main_interfaz.py     # Main entry point for GUI application
├── logs.txt             # Centralized event and error log
├── README.md            # Project documentation
│
├── interfaz/            # GUI module
│   ├── __init__.py
│   └── ventana_principal.py
│
├── modelos/             # Business logic (POO implementation)
│   ├── __init__.py
│   ├── cliente.py
│   ├── entidad.py
│   ├── excepciones.py
│   ├── reserva.py
│   ├── servicio.py      # Abstract base class definition
│   └── servicios_especializados.py
│
├── pruebas/             # Test cases and simulation logic
│   ├── __init__.py
│   └── simulaciones.py
│
└── utils/               # System utilities
    ├── __init__.py
    └── logger.py        # Auditing module
Execution Requirements
Python: Version 3.12 or higher.

Environment: VS Code or PyCharm.

Deployment:

Clone the repository.

Execute the console simulation via: python main.py

Execute the Graphical User Interface via: python main_interfaz.py

Project Objectives
This system is engineered to meet rigorous robustness standards, ensuring that in the event of operational anomalies (such as invalid data inputs or resource conflicts), the application captures the incident, logs the context, and continues its execution without crashing.
