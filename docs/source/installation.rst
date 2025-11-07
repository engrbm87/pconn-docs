Installation
============

Platform Connectors is available as a windows installer that sets up a Windows service hosting the web server. It can be installed on any machine that can connect to the systems it needs to communicate with. Refer to each plugin documentation for specific connectivity requirements.

Prerequisites
-------------

- Windows 10/11 or Windows Server 2019+
- Administrator permissions to install software and manage Windows services
- Optional: Allow inbound traffic on the HTTP port you plan to use (default ``8000``)

Installation
--------------------

1. Run the setup installer as an administrator and follow the prompts.
2. When installation completes, a Windows service is installed and configured to start automatically.


Default web address
-------------------

After installation the web server runs as a Windows service and is reachable at:

``http://localhost:8000``

If you changed the host/port (see below), use the updated address.

Configuration (host, port, directories)
---------------------------------------

Configuration lives in:

``C:\Program Files (x86)\Platform Connectors\appsettings.json``

Relevant section:

.. code-block:: json

   {
     "PconnSettings": {
       "HostIp": "0.0.0.0",
       "Port": 8000,
       "ConfigDir": "C:\\ProgramData\\Platform Connectors\\config"
     }
   }

What these do:

- ``HostIp``: IP address the server binds to (use ``0.0.0.0`` to listen on all interfaces, or ``127.0.0.1`` for local-only)
- ``Port``: HTTP port (default ``8000``)
- ``ConfigDir``: Path to the configuration directory used by the application/plugins

To change settings:

1. Stop the service using Windows Services or PowerShell:
   
   .. code-block:: powershell

      Stop-Service -Name "Platform Connectors"

2. Edit ``appsettings.json`` as an administrator (files under ``Program Files (x86)`` require elevation)
3. Save your changes
4. Start the service again:

   .. code-block:: powershell

      Start-Service -Name "Platform Connectors"

5. If you changed the port or host, update any firewall rules accordingly

Verify installation
-------------------

1. Open a browser on the host and navigate to ``http://localhost:8000``
2. Confirm the service is running (by checking Windows Services or via PowerShell):

   .. code-block:: powershell

      Get-Service -Name "Platform Connectors"

3. Apply your license (see :doc:`license`) and install/configure plugins (see :doc:`plugins/index`)

Update
------

- Run the newer installer and follow the prompts. The service will be updated in-place. If prompted, stop the service before updating.

Uninstall
---------

- Use “Apps & features” (Windows 10/11) or “Programs and Features” to uninstall “Platform Connectors”.

