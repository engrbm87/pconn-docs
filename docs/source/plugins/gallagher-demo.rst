Gallagher Cardholder Viewer
===========================

Overview
--------

This is a demo plugin that connects to Gallagher Command Center and displays the list of configured cardholders with their personal fields. The user can update these fields and the new values are pushed to Command Center using REST API.

Licensing
---------

- The license should include "gallagher_demo" under the "plugins" section.
- This plugin has a limit on the number of instances that can be created.

Configuration
-------------

1. Navigate to Settings → Plugin Entries
2. Click on "Add Plugin" button
3. Select "Gallagher Cardholder Viewer" from the list
4. Configure the connection to Gallagher Command Center. Refer to (:doc:`/platforms/gallagher-rest`)
5. The configuration is done and the plugin is loaded.

Options
-------

This plugin includes the following options:

- **Profile Image**: Select the cardholder personal field of type `image` that will used as profile image.
