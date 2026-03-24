BACnet Emulator
===============

Overview
--------

This platform emulates a BACnet device with configurable points.

Configuration
-------------

Start by adding a plugin that uses this platform


- Host (Required): The hostname or IP address of the BACnet emulator.
- Port (Required): The port on which the BACnet emulator is listening (default: 47808).
- Device ID (Required): The identifier for the BACnet device (default: 89089).
- BBMD address: The IP address of the BACnet Broadcast Management Device (BBMD) if used in a BACnet/IP network.


Functionality
-------------

This platform provides an ObjectBase class that can be used for the following types:

- Binary Input
- Binary Output
- Multi State Value

Each object will have the following properties:

- Present value: The current value of the object.
- Reliability: The reliability status of the object.
- Out of service: A flag that is set by disabling the object from the plugin.
- State values: A list of state values for multi-state objects.

For Binary Output objects, a callback can be passed which will be called when the present value is changed by a BACnet client.
