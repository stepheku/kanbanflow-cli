import os
from kanbanflow_cli.kanban_board import KanbanBoard
from kanbanflow_cli.kanban_task_list import KanbanTask, KanbanTaskList
from kanbanflow_cli.kanban_subtask import KanbanSubTask
import kanbanflow_cli.kanbanflow_menu as kanbanflow_menu

print(
r"""
    __ __            __                ________                  ________    ____
   / //_/___ _____  / /_  ____ _____  / ____/ /___ _      __    / ____/ /   /  _/
  / ,< / __ `/ __ \/ __ \/ __ `/ __ \/ /_  / / __ \ | /| / /   / /   / /    / /  
 / /| / /_/ / / / / /_/ / /_/ / / / / __/ / / /_/ / |/ |/ /   / /___/ /____/ /   
/_/ |_\__,_/_/ /_/_.___/\__,_/_/ /_/_/   /_/\____/|__/|__/____\____/_____/___/   
                                                        /_____/                  
""")

if not os.environ.get('KBFLOW_API'):
    print('''Environment variable $KBFLOW_API has not been set. 
    Set this with the command: export KBFLOW_API="API Key"''')
    exit()

print('Connecting to KanbanFlow board...')
board = KanbanBoard()
task_list = KanbanTaskList()
print('Connected to KanbanFlow board: {}'.format(board.board_name))

for key, val in kanbanflow_menu.menu_dict.items():
    print('{}. {}'.format(key, val))

while True:
    option_choice = input('Select a menu option: ')
    try:
        option_choice = int(option_choice)
        if option_choice in kanbanflow_menu.menu_dict.keys():
            break
    except ValueError:
        pass

if option_choice == 1:
    for idx, col_name in enumerate(board.get_board_columns_names(), 1):
        print('{}. {}'.format(idx, col_name))
    while True:
        col_option_choice = input('Select a column option: ')
        try:
            col_option_choice = int(col_option_choice)
            if col_option_choice <= len(board.get_board_columns_names()):
                break
        except ValueError:
            pass
    for idx, task_name in enumerate(task_list.get_task_list_by_column_index(col_option_choice-1)[:10]):
        print('{}. {}'.format(idx, task_name))

if __name__ == "__main__":
    pass
