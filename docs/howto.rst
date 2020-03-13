HowTo Write The Docs
====================

Links
-----

Internal References
~~~~~~~~~~~~~~~~~~~

Rename the reference::

    :ref:`Weiterlesen... <elemente_inhaltsverzeichnis_overview>`

No renaming::

    :ref:`elemente_inhaltsverzeichnis_overview`

Amazon Ref Links
~~~~~~~~~~~~~~~~

Use the following pattern to mark links which will replaced in the
future by ref link generator to ease changing reflink-account without
changing the docs.

example::

    .. [#theissen2017_211] `Theissen:2017; Seite 211 <{amazon:theissen_2017}>`_.

Pattern
-------

Table
~~~~~

.. code-block:: rst

    .. list-table:: priority range categories for Sphinx transforms
       :widths: 20,80

       * - Priority
         - Main purpose in Sphinx
       * - 0-99
         - Fix invalid nodes by docutils. Translate a doctree.
       * - 100-299
         - Preparation
       * - 300-399
         - early
       * - 400-699
         - main
       * - 700-799
         - Post processing. Deadline to modify text and referencing.
       * - 800-899
         - Collect referencing and referenced nodes. Domain processing.
       * - 900-999
         - Finalize and clean up.
