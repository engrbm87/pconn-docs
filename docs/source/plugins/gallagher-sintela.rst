Gallagher Sintela Plugin
================================

Overview
--------

This plugin exposes pushed detections triggered by Sintela Onyx devices to Gallagher Command Center. Detections are associated with zones that are represented in Command Center using Virtual Outputs. 

Licensing
---------

- The license should include "gallagher_sintela" under the "plugins" section.
- This plugin has a limit on the number of zones that can be monitored.

Platform requirements
---------------------

- Gallagher Command Center 9.00+ with RESTCreateEvents=1, RESTStatus=1 & RESTOverrides=1 included in the Command Center license file.
- A custom Event type called `Onyx Detection` must be created in Command Center. Refer to the Gallagher platform page for more details (:doc:`/platforms/gallagher-rest`).

Configuration
-------------

1. Navigate to Settings → Plugin Entries
2. Click on "Add Plugin" button
3. Select "Gallagher Sintela" from the list
4. Configure the connection to Gallagher Command Center. Refer to (:doc:`/platforms/gallagher-rest`)
5. Configure the Sintela integration. Refer to (:doc:`/platforms/sintela`)
6. The configuration is done and the plugin is loaded.

Options
-------

This plugin options allow you set the following:

- **Zone Name Prefix**: The plugin will look for Virtual Outputs created in Command Center with this prefixed value. This is useful to avoid name conflicts with existing outputs in Command Center.
- **Zone detection timeout**: The timeout after which a zone with no detections is considered normal. This timeout value is configurable in seconds.


Dashboard
---------

The plugin dashboard displays a waterfall chart of the detections received from Sintela Onyx devices. The chart is updated in real-time as detections are received. This should be used for checking if new detections are picked up by the plugin. For better experience, it is recommended to use Sintela Dashboard web interface.


Functionality
-------------
- The plugin requires zones to be configured in Sintela. Each zone is represented by a virtual output in Gallagher Command Center.
- The virtual output can be customized to have a custom icon set (i.e. Command Center fence icons can be used if we are monitoring a fence.).
- The custom event created should be associated with Output type. This allows the operator to set a custom action plan for this event inside the virtual output properties (or in the associated Alarm zone event defaults).
- When a detection is received from Sintela Onyx devices, the plugin will look for a Virtual Output in Command Center with the name `<Zone Name Prefix> <Zone Name>`. If found, the plugin will set the Virtual Output to active. If not found, the plugin will log a warning message.
- The event message format is `<Detection Classification> detected at zone <Zone Name>`.
- If the detection is at a distance from the zone, the event message will reflect that indicating the distance and direction form that zone.
- If the same detected object (identified by the detection id) has moved to another zone, the event message will append `previously at zone <Previous Zone Name>`. This allows the operator to know that the same object has moved from one zone to another.
- The event details will include the following data retrieved from Sintela:
  - Detection ID
  - Severity
  - Start time
  - Position
- The plugin keeps track of detections and their current zone. If a zone no longer has any associated detections and the configured timeout has elapsed. The virtual output will be set to inactive.