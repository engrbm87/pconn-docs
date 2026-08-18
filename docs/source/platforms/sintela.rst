Sintela
=======

Overview
--------

This platform handles the communication with Sintela Onyx devices.

Configuration
-------------

.. note::

    Refer to Sintela documentation for generating a Bearer Token.
    If Secure connection is selected, a server certificate needs to be exported and uploaded when setting up the platform.

Connecting to Sintela Onyx devices:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Host** (Required): Onyx device ip address
- **Port** (Required): Onyx API port (default 8181)
- **Bearer Token** (Required): Bearer Token generated from OnyxApi setting tab.
- **Verify SSL** (Optional): Validate server certificate.
- **Server PEM Certificate** (Optional): If a server certificate is used in OnyxAPi settings, the pem file should be uploaded here.

