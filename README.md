This is a repository for testing out Github workflows.

There is a dummy Python package `pbtbx` which has a single trivial unit
test, plus the following workflows:

 - Python CI: runs linting and `pytest` on `push` and `pull-request` events
 - Create release: performs operations to make a new release when triggered
   manually.
