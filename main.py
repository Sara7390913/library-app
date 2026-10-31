#from view.menu import run_menu
#run_menu()
from view.library_gui import LibraryGUI
from tools.logger import Logger

#Logger.info("Library application started")
#Logger.error("This is a test error")
#Logger.debug("Application details")

if __name__ == "__main__":
    Logger.info("Library application started")

    app = LibraryGUI()
    app.run()