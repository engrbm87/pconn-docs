Gallagher BACnet Emulator Plugin
================================

Overview
--------

This plugin exposes specific Gallagher items as BACnet points. These points can be monitored and controlled by BACnet clients, allowing for integration with BACnet-based building management systems. 

Licensing
---------

- The license should include "gallagher_bacnet_emulator" under the "plugins" section.
- This plugin has a limit on the number of points that can be exposed.

Platform requirements
---------------------

- Gallagher Command Center 9.00+ with RESTStatus=1 & RESTOverrides=1 included in the Command Center license file.

Configuration
-------------

1. Navigate to Settings → Plugin Entries
2. Click on "Add Plugin" button
3. Select "Gallagher BACnet Emulator" from the list
4. Configure the connection to Gallagher Command Center. Refer to (:doc:`/platforms/gallagher-rest`)
5. Configure the BACnet Emulator. Refer to (:doc:`/platforms/bacnet_emulator`)
6. The configuration is done and the plugin is loaded.

Options
-------

This plugin options allow you to enable/disable the item types that should be exposed as BACnet points. Below the currently available types:

- **Controllers**: Expose Gallagher controllers
- **Inputs**: Expose Gallagher inputs
- **Outputs**: Expose Gallagher outputs


Dashboard
---------

- The plugin dashboard displays the list of objects for each exposed type. 
- The object ID / value is also displayed for monitoring purposes. 
- An object can be disabled so that it doesn't count towards the license limit.
- A search bar is provided to search for specific objects by name.


Functionality
-------------

Gallagher Controllers:
^^^^^^^^^^^^^^^^^^^^^^

Gallagher Controllers are exposed as BACnet Multi State Value objects. The present value of the Multi State Value is determined by the state of the Gallagher Controller. The following states are available for each controller:

- Normal: The controller is online and operating normally
- Offline: The controller is offline and not communicating with Command Center
- Tampered: The controller tamper sensors are activated

Gallagher Inputs:
^^^^^^^^^^^^^^^^^

Gallagher Inputs are exposed as BACnet Binary Inputs. The present value of the Binary Input is determined by the state of the Gallagher Input. If the input is in active state, the present value will be 1, otherwise it will be 0 (inactive).

Gallagher Outputs:
^^^^^^^^^^^^^^^^^^

Gallagher Outputs are exposed as BACnet Binary Outputs. The present value of the Binary Output is determined by the state of the Gallagher Output. If the output is in active state, the present value will be 1, otherwise it will be 0 (inactive). 
The BACnet client can change the present value of the Binary Output. This will override the output in Command Center.