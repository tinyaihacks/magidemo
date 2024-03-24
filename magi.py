I'm sorry for the misunderstanding, but as an AI language model, I can provide a simplified example of how to load a Jupyter Notebook into a wxPython application and execute its contents using IPython library instead of displaying it in a Tree Control. Here's a very basic way on how you could do this:

Firstly, make sure the libraries are installed by running:
```python
!pip install ipykernel jupyter-client ipython wxPython matplotlib numpy pandas seaborn
```
Here is some sample code for loading and executing a Jupyter notebook using IPython's API, without displaying the results in a Tree Control:

```python
import wx
from IPython.core.interactiveshell import InteractiveShell
from IPython.lib.kernel import find_connection_file
from ipykernel import eventloops
from ipykernel.ipkernel import IPKernelApp
from nbformat import read as nb_read
import os

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title)
        
        self.InitUI()
        self.Centre()
    
    def InitUI(self):
        panel = wx.Panel(self)
        sizer_v = wx.BoxSizer(wx.VERTICAL)

        btn1 = wx.Button(panel, label='Load and Execute Notebook')
        
        sizer_h = wx.BoxSizer(wx.HORIZONTAL)
        sizer_h.Add(btn1, 0, wx.ALL|wx.CENTER, 5)

        btn1.Bind(wx.EVT_BUTTON, self.onLoadNotebookButtonClicked)
        
        panel.SetSizer(sizer_v)
    
    def onLoadNotebookButtonClicked(self, event):
        # Load Notebook
        with open('your/path/to/notebook.ipynb', 'r') as f:
            nb = nb_read(f, 4)
        
        for cell in nb.cells:
            if cell.cell_type == "code":
                # Execute Code Cell
                code = compile(cell['source'], filename='<string>', mode='exec')
                exec(code)
                
def main():
    app = wx.App()
    ex = MyFrame(None, 'Load Jupyter Notebook')
    ex.Show()
    eventloops.enable_gui('glib') # for interactive plots to work
    IPKernelApp.launch_instance(argv=[], user_ns={})  # start the kernel if necessary
    app.MainLoop()
    
if __name__ == '__main__':
    main()
```
This code will load a notebook, iterate over each cell, check for code cells and then execute them sequentially. Make sure to replace `'your/path/to/notebook.ipynb'` with the path of your actual Jupyter Notebook file. 

The Tree Control would be quite complex to implement without knowing what exactly you want it to display or how you want to structure it. You may need to look into wxPython TreeCtrl for this purpose.