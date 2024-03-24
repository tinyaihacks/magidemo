import wx
from os.path import join
from transformers import AutoModelForCausalLM, AutoTokenizer 
class MainFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Load Model', size=(900, 600))

        self.model = None
        self.tokenizer = None
        
        panel = wx.Panel(self)
        
        btn = wx.Button(panel, label='Load Model')
        self.result_textctrl=result_textctrl = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.HSCROLL)

        self.Bind(wx.EVT_BUTTON, self.OnButtonClick, btn)
        
        sizer = wx.BoxSizer()
        sizer.Add(btn, 0, wx.ALL|wx.CENTER, 5)
        sizer.Add(result_textctrl, 1, wx.EXPAND | wx.ALL, 5)
        panel.SetSizer(sizer)
        
    def OnButtonClick(self, event):
        
        if self.model is None: # Load model the first time only
            print("Loading model...")
            
            

            try:
            
                if 0:
                    # Replace 'milkowski/Magicoder-S-DS-6.7B-GGUF' with your model name on HuggingFace Model Hub
                    self.model = AutoModelForCausalLM.from_pretrained(join('models','milkowski','Magicoder-S-DS-6.7B-GGUF') )
                    
                    # Replace 'magicoder-s-ds-6.7b' with your tokenizer name on HuggingFace Model Hub
                    self.tokenizer = AutoTokenizer.from_pretrained('magicoder-s-ds-6.7b') 
                if 1:
                    model = AutoModelForCausalLM.from_pretrained(join('models','milkowski','Magicoder-S-DS-6.7B-GGUF', 'magicoder-s-ds-6.7b.f16.gguf')) 
                     # Here you can add your text generation task using the model loaded above        
            except Exception as error:
                self.result_textctrl.SetValue(str(error))  
                return
        
        print("Model loaded!")
        
app = wx.App()
frame = MainFrame(None, -1)
frame.Show()
app.MainLoop()