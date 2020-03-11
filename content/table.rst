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
