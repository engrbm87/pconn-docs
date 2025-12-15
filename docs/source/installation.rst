Installation
============

Platform Connectors is available as a windows installer that sets up a Windows service hosting the web server. It can be installed on any machine that can connect to the systems it needs to communicate with. Refer to each plugin documentation for specific connectivity requirements.

Prerequisites
-------------

- Windows 10/11 or Windows Server 2016+
- Administrator permissions to install software and manage Windows services
- Optional: Allow inbound traffic on the HTTP(s) port you plan to use (default ``8000``)

Installation
--------------------

1. Run the setup installer as an administrator and follow the prompts.
2. When installation completes, a Windows service is installed and configured to start automatically.


Default web address
-------------------

After installation the web server runs as a Windows service and is reachable at:

``http://localhost:8000``

If you changed the host/port (see below), use the updated address.

Using SSL
---------

A folder called ``default-ssl`` is provided alongside the installation in ``C:\Program Files (x86)\Platform Connectors``. This folder contains a self-signed certificate that you can use for ssl communication.

To enable brwosing using https, rename ``default-ssl`` to ``ssl`` so the service loads the bundled certificate, or create a new ``ssl`` folder and place your own certificate and private key there. The files must be named ``cert.pem`` and ``key.pem``.

After updating the certificate files, restart the windows service so the server picks up the change.

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

1. Stop the service using windows Services
2. Edit ``appsettings.json`` as an administrator (files under ``Program Files (x86)`` require elevation)
3. Save your changes
4. Start the service again
5. If you changed the port or host, update any firewall rules accordingly


Onboarding flow
---------------

1. Start the Windows service (already installed during setup).
2. Visit ``http://localhost:8000`` (or your configured host/port).
3. Apply the license in the modal dialog that appears so the system becomes operational.
4. Register the very first workstation that will communicate with Platform Connectors (:doc:`workstation`).
5. After the initial workstation is registered, proceed to configure your plugins/navigation/options.

.. _install-upgrade:

Upgrade
-------

- Run the newer installer and follow the prompts
- Navigate to the host url. The license dialog will show.
- Upload the new license file that has the new version to continue using the application.

Uninstall
---------

- Use “Apps & features” (Windows 10/11) or “Programs and Features” to uninstall “Platform Connectors”.

