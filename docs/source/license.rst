License
=======

You must have a valid license file before you can start using Platform Connectors. The application will not operate without one.

License scope and rules
-----------------------

The license file governs multiple aspects of usage:

1. Application Version
   - The license explicitly lists the highest application version you are entitled to run.
   - Upgrading the application beyond that version requires obtaining an updated license first.
2. Expiry
   - Demo licenses: limited, short‑term expiry (e.g. 30 days).
   - Standard licenses: 1 year expiry (renew annually).
3. Workstation Limit
   - The license includes a maximum number of workstation machines that can be registered.
   - Additional workstation capacity can be purchased per workstation and supplied via an updated license file.
4. Plugin Enablement
   - Only plugins listed in the license are enabled in the UI.
   - Individual plugins may include: (a) max instance count, (b) limits on items, connections, or transactions.
   - See each plugin’s page for its specific limits.

License types
-------------

- Demo: Short evaluation period, reduced limits, often limited plugins.
- Standard: Full plugin access per purchase, renewable yearly.

Obtaining a license
-------------------

- Contact sales/support with required details (organization, desired plugins, workstation count).
- Receive a signed license file (e.g. ``pconn.lic``).

Applying a license (UI)
-----------------------

First-time activation happens immediately after you browse to the application for the first time.

1. Open ``http://localhost:8000`` (or your configured host/port).
2. A modal dialog appears prompting you to upload the license file (--file  ``.lic``).
3. Click **Upload** and select the file.
4. Once the onboarding is completed, you can check the license details by navigating to Settings.

.. image:: _static/license/license-dialog.png
   :alt: License activation dialog
   :width: 450
   :align: center


Applying a updated license (after initial activation):

1. Navigate to Settings → Licensing.
2. Click **Update License**.
3. Upload the new license file (for version upgrade or added capacity).
4. The page refreshes showing updated version entitlement, expiry, workstation quota, and plugin limits.

.. image:: _static/license/license-details.png
    :alt: License details page
    :width: 450
    :align: center

Workstation registration
------------------------

When a workstation first connects/registers, it consumes one slot from the license. To free a slot (for decommissioned machines), deregister the workstation from the Settings page.


Plugin limits
-------------

Plugin pages document their specific limit semantics. Examples:

- "Instance limit": Maximum number of active plugin instances.
- "Item limit": Cap on items processed (records, devices, connections, etc.).


Next steps
----------

After activation, proceed to plugin installation and configuration: :doc:`plugins/index`.
