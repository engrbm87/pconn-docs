Gallagher REST
==============

Overview
--------

This platform handles the communication with Gallagher Command Center via its REST API.

Configuration
-------------

Start by adding a plugin that uses this platform

Connecting to Gallagher Command Center locally:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Host (Required): Server ip address or hostname
- Port (Required): REST API server port (default 8904)
- API Key (Required): API Key generated from Gallagher Command Center
- Integration Token (Optional): Integration Token if required by the plugin (this will be provided by Gallagher)
- Use Certificate Thumbprint: If enforced in Gallagher Command Center, copy the displayed Thumbprint into the REST item in Gallagher Command Center and enable it here.

Connecting to Gallagher Command Center via a Gateway:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Cloud Gateway (Required): Select the gateway that is used by your Command Center configured cloud item.
- API Key (Required): API Key generated from Gallagher Command Center
- Integration Token (Optional): Integration Token if required by the plugin (this will be provided by Gallagher)
- Use Certificate Thumbprint: If enforced in Gallagher Command Center, copy the displayed Thumbprint into the REST item in Gallagher Command Center and enable it here. 

