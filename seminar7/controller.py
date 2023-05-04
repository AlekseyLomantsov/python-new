import gui
import database
import check
def start():
    database.save_info(gui.get_input())
    data = database.get_info()
    result = check.check(data)
    gui.send_info(result)