from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang.builder import Builder
import pymysql
from kivy import Config
Config.set('graphics', 'multisamples', '0')


conn=pymysql.connect(host="localhost",user="root",password='',db="py_db")
Builder.load_string("""
    

<homePage>:
    
    canvas.before:
        Color:
            rgb: 1, 1, 1
        Rectangle:
            size: self.size
    
    BoxLayout:
        color:(1,0,1,2)
        orientation: "vertical"
        Label:
            color:(1,0,1,2)
            text: "Home Page"
           
        
        Button:
            color:(1,1,1,2)
            text: "Logout"
            size_hint_y:None
            height:50
            on_press: root.out()

<MainScreen>:
    
    
    canvas.before:
        Color:
            rgb: 1, 1, 1
        Rectangle:
            size: self.size
    
    GridLayout:
        color:(1,0,1,2)
        size_hint: (.5, .5)
        pos_hint: {"center_x": .5, "center_y": .6}
        cols: 2
        padding: 20
        
        

        Label:
            color:(1,0,1,2)
            size_hint: (4, 2)
            text: "User Name"
            font_size: 30
            text_size: self.size
            valign: "middle"

        TextInput:
            id: username
            size_hint: (4, 2)
            cursor_blink: True
            font_size: 20
            multiline: False

        Label:
            color:(1,0,1,2)
            size_hint: (4, 2)
            text:"Pin:"
            font_size: 30
            text_size: self.size
            valign: "middle"

        TextInput:
            id: pin
            size_hint: (4, 2)
            cursor_blink: True
            font_size: 20
            multiline: False
            password: True

        

        Button:
            color:(1,1,1,1)
            size_hint_y: None
            height: 50
            text:'Login'
            on_release: root.login(username.text, pin.text)
        Label:
            color:(1,0,1,2)
            id: success
            size_hint:(4,2)
            #color: (0,0,0,1)
            font_size: 20
            text_size: self.size
            valign: "middle"
            text: "please login"
""")



#class ScreenManagement(ScreenManager):

    
       
    

 
class MainScreen(Screen):

    def login(self,uname_txt,pin_txt):
        f=open("C:\\Users\\User\\Desktop\\cmd.text","r")
        s=f.read()
        if s=="login":
            #Clock.schedule_once(self._myprintfunction, 1/60)
            print("okk")
            
            self.parent.current='homepage'
        
        

        conn=pymysql.connect(host="localhost",user="root",password='',db="py_db")
        mycur=conn.cursor()
        #if username_text == "root" and password_text == "123":
        if uname_txt=="" or pin_txt=="":
            label = self.ids.success
            label.text="Please enter the required field"
        elif uname_txt!="" or pin_txt!="":
            mycur.execute("select * from user_info where user_name='%s' and user_password ='%s'"%(uname_txt,pin_txt))
            
            data=mycur.fetchone()
            
            
            if data is not None:
                f=open("C:\\Users\\User\\Desktop\\cmd.text","w")
                f.write("login")
                self.parent.current = 'homepage' 
                
            else:
                label = self.ids.success
                label.text="login fake"  
       
               


class HomePage(Screen):
    '''def __init__(self,**kwargs):
        
        
        f=open("C:\\Users\\Talha Training\\Desktop\\cmd.txt","r")
        s=f.read()
        if s=="login":
            #Clock.schedule_once(self._myprintfunction, 1/60)
            #print("okk")
            self.parent.current='homepage'
        super(Screen,self).__init__(**kwargs) ''' 
    def log(self):
        f=open("C:\\Users\\User\\Desktop\\cmd.text","r")
        s=f.read()
        if s=="login":
            #Clock.schedule_once(self._myprintfunction, 1/60)
            print("okk")
            self.parent.current='homepage'
           
    def out(self):
        
        f=open("C:\\Users\\User\\Desktop\\cmd.text","w")
        f.truncate() 

sm = ScreenManager()

f=open("C:\\Users\\User\\Desktop\\cmd.text","r")
s=f.read()
if s=="login":
    sm.add_widget(HomePage(name='homepage'))   

sm.add_widget(MainScreen(name='main')) 
sm.add_widget(HomePage(name='homepage'))


class ss(App):
    
    def build(self):
         
      
        return sm
        
       
    
if __name__ == "__main__":
    ss().run()