Gallagher Availo Plugin
=======================

Overview
--------

This plugin connects to Gallagher Command Center using it's REST API and retrieves the entry and exit records for all cardholders. It identifies the first entry and last exist for each cardholder on a given day and pushes them as transactions to Availo cloud using its API. 

Licensing
---------

- The license should include "gallagher_availo" under the "plugins" section.
- This plugin has a limit on the number of instances that can be created.

Configuration
-------------

1. Navigate to Settings → Plugin Entries
2. Click on "Add Plugin" button
3. Select "Gallagher Availo" from the list
4. Configure the connection to Gallagher Command Center. Refer to (:doc:`/platforms/gallagher-rest`)
5. Configure the connection to Availo cloud. Refer to (:doc:`/platforms/availo`)
6. The configuration is done and the plugin is loaded.

Options
-------

This plugin includes the following options:

- **Gallagher Unique Personal Field**: Select the cardholder **unique** personal field that includes the **Employee Number** value assigned to each employee in Availo.
- **Gallagher Doors to Monitor**: Select the doors that will be monitored for entry/exit events.
- **Daily Sync Time**: The time of the day when the plugin will sync the transactions to Availo cloud. The plugin will fetch the entry and exit events for the previouse day. This task will be repeated daily unless it's paused from the plugin dashboard. Clearing this field will stop the scheduled syncing as well.
- **Time Zone in Availo**: Select the time zone that should be used when pushing the transactions to Availo.


Dashboard
---------

The plugin dashboard displays the list of sync attempts including the attempt time and the sync date. Clicking on a sync attempt will display the details of the attempt including the number of success and failed employee transactions. It will also display additional details about the sync.

.. note::

    A Download report button is provided to download the sync details as a json file for further troubleshooting.
    In case of errors raised during the sync, the error logs can be retrieved from the application logs (:doc:`/settings/logs`).

Managing Sync:
^^^^^^^^^^^^^^

The plugin provides a section to manage sync. This includes:

- Pausing and Resuming sync (available if **SYNC TIME** is configured)
- Manual Sync: This allows to manually trigger a sync for a specific date.
- A field to show the number of sync attempts since the plugin was loaded (resets on plugin reload or application restart).
- A button to clear sync history (this only clears the history displayed in the plugin dashboard, it does not affect the actual data pushed to Availo).


