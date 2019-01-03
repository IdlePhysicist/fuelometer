TODO List

- [x] Add db insert functionality
- [x] Clear fields after row is inserted into db
- [x] Add db viewer
  - [ ] Make the table display data!
  - [ ] Would it be smart to rewrite the db connection to use the QT connector as opposed to the Python one?
  - [ ] **MAJOR** db viewer needs to be a window and not a dialog, because the latter has no buttons to close the window!
- [ ] Add setup script!
- [x] Add configuration file
  - [x] Add table name to window from config file
  - [x] Add table name to db connector from config file
    * Pass table name from mainWindow.\_\_init\_\_ to MileageWorker.db_fetchrows()
