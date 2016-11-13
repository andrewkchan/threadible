from jupyter_client import *

_manager = MultiKernelManager()
_workspaces = {}
_cells = {}
_workspace_count = 0

class Workspace:

    def __init__(self, name):
        global _workspace_count
        self.name = name
        self.cell_count = 0
        self.workspace_id = _workspace_count
        _workspace_count = _workspace_count + 1
        _workspaces[self.workspace_id] = self
        _manager.start_kernel(kernel_id=self.workspace_id)
        self.client = _manager.get_kernel(self.workspace_id).client()
        self.client.start_channels(stdin=False);

    def add_cell(self, cell):
        cell_id = self.workspace_id + ":" + str(self.cell_count)
        self.cell_count = self.cell_count + 1
        _cells[cell_id] = cell
        return cell_id

    def execute_code(self, code):
        return self.client.execute(code)

class Cell:
    def __init__(self, workspace_id):
        self.code = ''
        self.workspace_id = workspace_id
        self.cell_id = get_workspace(workspace_id).add_cell(self)

    def execute(self):
        return get_workspace(self.workspace_id).execute_code(self.code)

def get_workspace(workspace_id):
    return _workspaces[workspace_id]

def edit_cell_content(workspace_id, cell_id, code):
    if cell_id == -1:
        cell = Cell(workspace_id)
    else:
        cell = get_cell(cell_id)
    cell.code = code
    return cell.execute()

def get_cell(cell_id):
    return _cells[cell_id]