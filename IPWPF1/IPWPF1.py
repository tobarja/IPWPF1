import wpf

from System.Windows import Application, Window
from System.Windows import MessageBox

class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'IPWPF1.xaml')
    
    def btnFirstButton_Click(self, sender, e):
        MessageBox.Show("Hello World")
    
    def btnSecondButton_Click(self, sender, e):
        self.Close()
    

if __name__ == '__main__':
    Application().Run(MyWindow())
