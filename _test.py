import wx
from IPython.core.display import display, HTML, Javascript
from traitlets.config import Config
from ipykernel.kernelapp import IPKernelApp
from jupyter_client.manager import start_new_kernel
import os

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title='Notebook Viewer', size=(800,600))
        
        self.nb = wx.html2.WebView.New(self)
        self.sizer = wx.BoxSizer()
        self.sizer.Add(self.nb, 1, wx.EXPAND | wx.ALL)
        self.SetSizer(self.sizer)
        
class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame()
        frame.Show()
        return True

def load_notebook(nb, path='path/to/your/notebook.ipynb'):
    with open(path) as f:
        html = nb._publish_html(f.read())[0]
    
    return html

frame.nb.LoadURL('data:text/html;charset=utf-8,' + load_notebook(frame.nb))
```
4. To make the notebook interactive, you need to create a kernel for it and start executing cells one by one:
```python
config = Config()
config.InteractiveShellApp.exec_lines = ["%gui wx"]
kernel_manager = IPKernelApp.instance().kernel_manager
kernel_manager.start_kernel(argv=['python3', '--gui=wx'], config=config)  # Creating kernel for Jupyter notebook
```
5. You can execute cells by iterating over them in your code, but this might be a little complex to do so and may not provide the desired result as the `notebook` doesn't have built-in functionality to handle execution of each cell. There is an open issue on GitHub asking for such feature: https://github.com/jupyter/nbconvert/issues/847
6. The other approach would be using Javascript to execute cells one by one, but this method might not work if the notebook contains some specific types of cells that are not supported in wxPython's WebView control.
   
This is a very general description and may not be practical for complex notebooks with lots of different cell types or dependencies. You will need to tweak it according to your requirements, but this should give you an idea how to approach such task.