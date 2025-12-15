Workstations
============

Add, remove and configure workstations from this page.


Adding a workstation
--------------------

- Click the **ADD** button next to the search field to add a new workstation.
- Fill in the workstation details:
  
  1. Name: Provide a friendly name for the workstation (e.g. "Office PC")
  2. IP Address: Enter the IP address of the workstation. This must be reachable from the server.
  3. Set as Admin: Check this box if you want this workstation to have admin privileges.
  4. Password: Set a password for this workstation (required for admin workstation). This password will be used when navigating to the Settings page from this workstation.

Editing a workstation
---------------------

- Click the **CONFIGURE** button next to the workstation name.
- Modify the desired fields (name, IP address, admin status, password).
- Click **SUBMIT** to save the changes.

Disabling a workstation
-----------------------

- Click the three dots menu next to the workstation name.
- Select **DISABLE**.

This will disable all plugin entries that are associated with this workstation. 
You can re-enable the workstation later which will re-enable the associated plugin entries as well.

Removing a workstation
----------------------

.. note::

    You can only remove other workstations. At least one admin workstation must be configured.

- Click the three dots menu next to the workstation name.
- Select **DELETE**.
- Confirm the deletion in the dialog.

This will remove all plugin entries that are associated with this workstation. If you want to keep the plugin entries, make sure to assign them to a different workstation before deleting.
