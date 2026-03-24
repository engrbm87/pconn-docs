Workstations
============

Add, remove and configure workstations from this page.

.. note::

  Adding/editing/removing a workstation can only be done from a workstation with ``Admin`` or ``Super Admin`` role.


Adding a workstation
--------------------

- Click the ``ADD`` button next to the search field to add a new workstation.
- Fill in the workstation details:
  
  1. **Name**: Provide a friendly name for the workstation (e.g. "Office PC")
  2. **IP Address**: Enter the IP address of the workstation. This must be reachable from the server.
  3. **Role**: Set the workstation role. Refer to the Roles section below for more details.
  4. **Password**: Set a password for this workstation (required for ``editor`` and ``admin`` roles). This password will be used when navigating to the Settings page from this workstation.
   
  .. note::

    For new installation, the first workstation must be added from the ``Super Admin`` workstation.

Editing a workstation
---------------------

- Click the ``CONFIGURE`` button next to the workstation name.
- Modify the desired fields (name, IP address, role, password).
- Click ``SUBMIT`` to save the changes.

Disabling a workstation
-----------------------

- Click the three dots menu next to the workstation name.
- Select ``DISABLE``.

This will disable all plugin entries that are associated with this workstation. 
You can re-enable the workstation later which will re-enable the associated plugin entries as well.

Removing a workstation
----------------------

.. note::

    You can only remove other workstations. At least one workstation with ``admin`` role must be configured.

- Click the three dots menu next to the workstation name.
- Select ``DELETE``.
- Confirm the deletion in the dialog.

This will remove all plugin entries that are associated with this workstation. If you want to keep the plugin entries, make sure to assign them to a different workstation before deleting.

Roles
-----

- **Admin**: This role has full access to the system, including managing workstations, plugins, and system settings.
- **Editor**: This role can manage plugins and view other system details but cannot manage workstations or modify system settings.
- **User**: This role has access to the dashboard only and cannot make any changes to the system.

  .. note::

    **Super Admin** role is only assigned to the localhost workstation created by default. It has full access to the system and cannot be deleted or modified.
    When upgrading from a pre **2026.3.x** version, if there is a workstation configured with ip **127.0.0.1**, it will be assigned the `Super Admin` role (and renamed to "Super Admin").
    
    If there is no workstation with ip **127.0.0.1**, a new workstation with that ip will be created and assigned the `Super Admin` role. The system will run in recovery mode until the password is set by navigating to the localhost workstation and completing the onboarding process.

Password reset
--------------

A workstation with ``Admin`` role of higher can assign a new password to any registered workstation using the ``CONFIGURE`` button. If there is only 1 ``Admin`` workstation and its password is lost, the user can set a new password for that workstation from the ``Super Admin`` workstation. 

To reset the ``Super Admin`` password (for any reason) the system must be set into recovery mode. This can be done by inserting `"recovery_mode": true` inside the `core.config` file located in the configuration directory (default: `C:\ProgramData\Platform Connectors\config\.storage\core.config`). Then restarting the application using the ``restart`` button inside the system settings page.

When the system is in recovery mode, only the ``Super Admin`` workstation can access the web UI. By navigating to `http(s)://localhost:8000` from that machine, the user will be prompted to set a new password. After that, the system will exit recovery mode and return to normal operation.