import os
from kanbanflow_cli.kanban_board import KanbanBoard
from kanbanflow_cli.kanban_task_list import KanbanTask, KanbanTaskList
from kanbanflow_cli.kanban_subtask import KanbanSubTask
from kanbanflow_cli.kanbanflow_menu import menu_dict
from PyInquirer import style_from_dict, Token, prompt, Separator
from pprint import pprint

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

questions = [
    {
        'type': 'list',
        'name': 'theme',
        'message':'What size do you need?',
        'choices': [val for val in menu_dict.values()],
        'filter': lambda val: val.lower(),
    },
]

answers = prompt(questions)

pprint(answers)

if __name__ == "__main__":
    pass
