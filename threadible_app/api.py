from jupyter_client import *

manager = MultiKernelManager()
workspaces = {}
cells = {}

class Workspace:
    def __init__(self, workspace_id):
        self.cell_count = 0
        self.workspace_id = workspace_id
        workspaces[workspace_id] = self
        if workspace_id in manager.list_kernel_ids():
            manager.remove_kernel(workspace_id)
        manager.start_kernel(kernel_id=workspace_id)
    
    def add_cell(self, cell):
        cell.cell_id = self.workspace_id + ":" + str(self.cell_count)
        self.cell_count = self.cell_count + 1
        cells[cell.cell_id] = cell

class Cell:
    def __init__(self, workspace_id):
        content = ''
        get_workspace(workspace_id).add_cell(self)

def get_workspace(workspace_id):
    return workspaces[workspace_id]

def edit_cell_content(cell_id, code):
    cells[cell_id].content = code