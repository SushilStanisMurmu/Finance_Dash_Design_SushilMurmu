import tkinter as tk
from tkinter import font
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


root=tk.Tk()

root.title("Company Finance Dashboard")
root.config(bg="#5859d2")

root.attributes("-fullscreen",True)
def exit_fullscreen(event=None):
    root.attributes('-fullscreen', False)
root.bind('<Escape>', exit_fullscreen)

s_width=root.winfo_screenwidth()
s_height=root.winfo_screenheight()
# root.geometry(f"{s_width}x{s_height-100}")
root.geometry("1000x1000")

# # function to resize the font size of the event when binding
# def resize_font(event,objectt,minimum_height):
#     # Calculate a new font size based on event height
#     # if(event.height)
#     new_size = max(minimum_height, int(event.height /2))  # You can tweak the divisor
#     objectt.configure(size=new_size)


lab_down_font=font.Font(family="Calibri",size=10,slant="italic")
lab_down=tk.Label(root,text="Designed by Sushil Murmu",bg="#d4d4d4",padx=10,fg="black",anchor="se",font=lab_down_font)
# # binding the la_down_font acccording to the lab_down height
# lab_down.bind("<Configure>",lambda event:resize_font(event,lab_down_font,minimum_height=4))
lab_down.place(relx=0,rely=0.95,relheight=0.05,relwidth=1)

root.update_idletasks()
root_width=root.winfo_width()
root_height=root.winfo_height()
# topmost frame named frame_top
frame_top=tk.Frame(root,bg="#1a1a1a",bd=0,relief="groove")
frame_top.pack_propagate(False)
frame_top.place(relx=0,rely=0,relwidth=1,relheight=0.11)


# frame containing buttons and content area       # this frame has same bg as root
frame_content=tk.Frame(root,bg="#5859d2")
frame_content.place(relx=0,rely=0.11,relwidth=1,relheight=1-0.11-0.05)

# frame containing buttons named frame_buttons
frame_buttons=tk.Frame(frame_content,bg="#608BC1",relief="groove",bd=0)
frame_buttons.pack_propagate(False)

frame_buttons.place(x=0.0+35,rely=0.0,relwidth=1,relheight=0.08)  #x=0.0 + width of menu button
#
#
# widgets in the first frame named frame_top
lab_CFD_font = font.Font(family="Calibri",size=30,weight="bold")
lab_CFD=tk.Label(frame_top,text="COMPANY FINANCE DASHBOARD",font=lab_CFD_font,bg="#1a1a1a",fg="#E9A319",anchor="sw",padx=10)

# # Bind the frame resize to update the font size
# lab_CFD.bind("<Configure>", lambda event: resize_font(event,lab_CFD_font,minimum_height=10))

lab_CFD.place(relx=0,rely=0.1,relwidth=0.42,relheight=0.5)
lab_CFD_more_font=font.Font(family="Calibri",size=10,weight="bold")
lab_CFD_more=tk.Label(frame_top,text="Innovated by TEAM 102",font=lab_CFD_more_font,bg="#1a1a1a",fg="#608BC1",anchor="nw",padx=11)
lab_CFD_more.place(relx=0.67,rely=0.0,relwidth=0.42,relheight=0.5)

# frame containing import file, delete data and label of time updated --->inside the frame top
frame_import_data=tk.Frame(frame_top,bg="#1a1a1a",relief="flat")
frame_import_data.place(relx=0.0015,rely=0.7,relwidth=0.25,relheight=0.27)
frame_import=tk.Frame(frame_import_data,bg="red",relief="flat")
frame_import.pack(side="left",expand=True,fill="both",pady=2,padx=2)
frame_reset=tk.Frame(frame_import_data,bg="green",relief="flat")
frame_reset.pack(side="right",expand=True,fill="both",padx=2,pady=2)
# import financial data button  
icon_import_data=tk.PhotoImage(file="import_data.png")
import_financial_data=tk.Button(frame_import,text="Import Financial data",image=icon_import_data,compound="right",cursor="hand2",relief="flat",bd=0,bg="whitesmoke",fg="black",font=("Calibri"))
import_financial_data.pack(expand="True",fill="both")


# reset dashboard button
icon_reset=tk.PhotoImage(file="reset.png")
reset_dashboard=tk.Button(frame_reset,text="Reset dashboard ",image=icon_reset,compound="right",cursor="hand2",relief="flat",bd=0,bg="whitesmoke",fg="black",font=("Calibri"))
reset_dashboard.pack(expand=True,fill="both")
# class to create tool tip for any widget hovered
class ToolTip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip_window = None
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event=None):
        x = self.widget.winfo_rootx() + 20
        y = self.widget.winfo_rooty() + 20

        self.tooltip_window = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(True)  # Remove window border
        tw.wm_geometry(f"+{x}+{y}")

        label = tk.Label(tw, text=self.text, background="#ffffe0", 
                         relief="solid", borderwidth=1,
                         font=("Arial", 9))
        label.pack(ipadx=5, ipady=2)

    def hide_tooltip(self, event=None):
        if self.tooltip_window:
            self.tooltip_window.destroy()
            self.tooltip_window = None

# adding tooltip for import and reset buttons
ToolTip(import_financial_data,"Only .xlsx file")
ToolTip(reset_dashboard,"Clears imported data")

#                           exit button
but_exit=tk.Button(frame_top,text="EXIT",fg="#FFFFFF",bg="#af3737",cursor="hand2",relief="flat",bd=0,command=lambda:root.destroy())
# confimation dialog box for EXIT
def confirm_exit():
    answer = tk.messagebox.askyesno("Exit", "Do you really want to exit?")
    if answer:
        root.destroy()
but_exit.place(relx=0.8,rely=0,relwidth=0.1,relheight=0.5)

# --------------------------------------- about us button----------------
var_about=tk.StringVar(value="0")
but_about=tk.Checkbutton(frame_top,indicatoron=False,onvalue="1",offvalue="0",selectcolor="#baafaf",variable=var_about,text="About Us",cursor="hand2",fg="#FFD700",bg="#1a1a1a",relief="flat",bd=0,command=lambda:but_about_clicked())
but_about.config(font=("Calibri",8,"bold"))

def but_about_clicked():

    reposition_but_about_and_but_help()
    
    frame_about.lift()
    but_menu.lift()
    but_menu.config(bg="#baafaf")
    var_help.set(0)
    var_about.set(1)
    var_but_menu.set(0)
    var_but_balance_sheet.set(0)
    var_but_cash_flow.set(0)
    var_but_graphs.set(0)
    var_but_product_profits.set(0)
    var_but_pl_statements.set(0)
    var_but_financial_ratios.set(0)
    var_but_sales_overview.set(0)
    var_but_forecast_budget.set(0) 

but_about.place(relx=0.9,rely=0.5,relwidth=0.1,relheight=0.5)
# function to re place the but_about button to its normal position
def reposition_but_about_and_but_help():
    but_about.place_configure(rely=0.5)
    but_help.place_configure(rely=0)

# ------------------------------------------------but_help---------------------------

var_help=tk.StringVar(value="0")
but_help=tk.Checkbutton(frame_top,indicatoron=False,onvalue="1",offvalue="0",selectcolor="#baafaf",variable=var_help,text="Help !",cursor="hand2",bg="#1a1a1a",fg="#FFD700",relief="flat",bd=0,command=lambda:but_help_clicked())
but_help.config(font=("Calibri",8,"bold"))
def but_help_clicked():
    frame_help.lift()
    but_menu.lift()
    but_menu.config(bg="#baafaf")

    # making but_help change position
    but_help.place_configure(rely=0.5)
    # making but_about change position
    but_about.place_configure(rely=0)
    var_help.set(1)
    var_about.set(0)
    var_but_menu.set(0)
    var_but_balance_sheet.set(0)
    var_but_cash_flow.set(0)
    var_but_product_profits.set(0)
    var_but_financial_ratios.set(0)
    var_but_sales_overview.set(0)

but_help.place(relx=0.9,rely=0,relwidth=0.1,relheight=0.5)
#
#
#
# all widgets in the second frame named frame_buttons
current_page=None

#        
# -------------------------MENU  button to show the buttons ---------------------
var_but_menu=tk.IntVar()
var_but_menu.set(1)
icon_menuShow=tk.PhotoImage(file="menuShow.png")
icon_menuHide=tk.PhotoImage(file="menuHide.png")
but_menu=tk.Checkbutton(frame_content,image=icon_menuHide,variable=var_but_menu,indicatoron=False,width=30,height=40,selectcolor="#d4d4d4",relief="flat",bd=0,cursor="hand2",command=lambda:but_menu_clicked())
but_menu.place(relx=0.0,rely=0.0,width=35,relheight=0.08)

def but_menu_clicked():
    if var_but_menu.get()==0:
        frame_buttons.place_forget()
        # changing icon to menu show
        but_menu.config(image=icon_menuShow,bg="#af3737")
    elif var_but_menu.get()==1:
        frame_buttons.place(x=0.0+35,rely=0.0,relwidth=1,relheight=0.08)  #x=0.0 + width of menu button
        frame_buttons.lift()
        # changing icon to menu hide
        but_menu.config(image=icon_menuHide)
    
    
#
#
#

# --------------------right navigator button ------
icon_nav_right=tk.PhotoImage(file="nav_right.png")
style=ttk.Style()
style.theme_use("clam")
style.configure("TButton1",
             background="#2e8b57",
             foreground="#ffffff",
             relief="flat",
             bd=0,
             focusthickness=0,
             focuscolor=style.configure(".")["background"]
             )
# Remove focus border from TButton
style.layout("TButton1",
    [('Button.padding',
      {'children': [('Button.label', {'side': 'left', 'expand': 1})],
       'sticky': 'nswe'})]
       )
style.map("TButton1",
          background=[("active","#3baf6d")],
          foreground=[("active","#ffffff")])

style.configure("TButton2",
             background="#1a1a1a",
             foreground="#FFD700",
             relief="flat",
             bd=0,
             focusthickness=0,
             focuscolor=style.configure(".")["background"]
             )
    # Remove focus border from TButton2
style.layout("TButton2",
                 [('Button.padding',
                    {'children': [('Button.label', {'side': 'left', 'expand': 1})],
                    'sticky': 'nswe'})])
style.map("TButton2",
          background=[("active","#AFDDFF")])
but_right=ttk.Button(frame_buttons,image=icon_nav_right,cursor="hand2",style="TButton1",command=lambda:but_right_clicked())
but_right.config(text="Next",compound="left")
def but_right_clicked():
    global current_page
    current_page=current_page
    if current_page==8: 
        but_balance_sheet_clicked()
    elif current_page==1:
        but_cash_flow_clicked()
    elif current_page==2:
        but_product_profits_clicked()
    elif current_page==3:
        but_financial_ratios_clicked()
    elif current_page==4:
        but_graphs_clicked()
    elif current_page==5:
        but_pl_statements_clicked()
    elif current_page==6:
        but_sales_overview_clicked()
    elif current_page==7:
        but_forecast_budget_clicked()
but_right.pack(side="left",fill="both",expand=True)

# --------------------------FONT for all the buttons
font_buttons=font.Font(family="Calibri",size=11)
lab_CFD_font.config(family="Calibri")
lab_CFD_more_font.config(family="Calibri")
# -------------------- balance sheet button--------------
var_but_balance_sheet=tk.IntVar(value=0)
but_balance_sheet=tk.Checkbutton(frame_buttons,text="BALANCE SHEET",variable=var_but_balance_sheet,command=lambda:but_balance_sheet_clicked(),indicatoron=False,selectcolor="#d4d4d4",cursor="hand2",bg="#608BC1",fg="#000000",relief="flat",bd=0,font=font_buttons)
but_balance_sheet.pack(side="left",fill="both",expand=True)
def but_balance_sheet_clicked():
    # frame_balance_sheet.lift()
    global current_page
    current_page=1
    frame_balance_sheet.lift()
    lift_important_widgets()
    var_about.set(0)
    var_help.set(0)
    var_but_balance_sheet.set(1)

    var_but_cash_flow.set(0)
    var_but_graphs.set(0)
    var_but_product_profits.set(0)
    var_but_pl_statements.set(0)
    var_but_financial_ratios.set(0)
    var_but_sales_overview.set(0)
    var_but_forecast_budget.set(0)
    
var_but_cash_flow=tk.IntVar(value=0)
but_cash_flow=tk.Checkbutton(frame_buttons,text="CASH FLOW",variable=var_but_cash_flow,command=lambda:but_cash_flow_clicked(),indicatoron=False,selectcolor="#d4d4d4",cursor="hand2",bg="#608BC1",fg="#000000",relief="flat",bd=0,font=font_buttons)
def but_cash_flow_clicked():
    # frame_cash_flow.lift()
    global current_page
    current_page=2
    frame_cash_flow.lift()
    lift_important_widgets()
    var_about.set(0)
    var_help.set(0)
    var_but_balance_sheet.set(0)
    var_but_cash_flow.set(1)
    var_but_graphs.set(0)
    var_but_product_profits.set(0)
    var_but_pl_statements.set(0)
    var_but_financial_ratios.set(0)
    var_but_sales_overview.set(0)
    var_but_forecast_budget.set(0)
    
but_cash_flow.pack(side="left",fill="both",expand=True)

var_but_product_profits=tk.IntVar(value=0)
but_product_profits=tk.Checkbutton(frame_buttons,text="PRODUCT PROFITS",variable=var_but_product_profits,command=lambda:but_product_profits_clicked(),indicatoron=False,selectcolor="#d4d4d4",cursor="hand2",bg="#608BC1",fg="#000000",relief="flat",bd=0,font=font_buttons)
def but_product_profits_clicked():
    # frame_cash_flow.lift()
    global current_page
    current_page=3
    frame_product_profits.lift()
    lift_important_widgets()
    var_about.set(0)
    var_help.set(0)
    var_but_balance_sheet.set(0)
    var_but_cash_flow.set(0)
    var_but_graphs.set(0)
    var_but_product_profits.set(1)
    var_but_pl_statements.set(0)
    var_but_financial_ratios.set(0)
    var_but_sales_overview.set(0)
    var_but_forecast_budget.set(0)
but_product_profits.pack(side="left",fill="both",expand=True)

var_but_financial_ratios=tk.IntVar(value=0)
but_financial_ratios=tk.Checkbutton(frame_buttons,text="FINANCIAL RATIOS",variable=var_but_financial_ratios,command=lambda:but_financial_ratios_clicked(),indicatoron=False,selectcolor="#d4d4d4",cursor="hand2",bg="#608BC1",fg="#000000",relief="flat",bd=0,font=font_buttons)
def but_financial_ratios_clicked():
    # frame_cash_flow.lift()
    global current_page
    current_page=4
    frame_financial_ratios.lift()
    lift_important_widgets()
    var_about.set(0)
    var_help.set(0)
    var_but_balance_sheet.set(0)
    var_but_cash_flow.set(0)
    var_but_graphs.set(0)
    var_but_product_profits.set(0)
    var_but_pl_statements.set(0)
    var_but_financial_ratios.set(1)
    var_but_sales_overview.set(0)
    var_but_forecast_budget.set(0)
but_financial_ratios.pack(side="left",fill="both",expand=True)

var_but_graphs=tk.IntVar(value=0)
but_graphs=tk.Checkbutton(frame_buttons,text="GRAPHS",variable=var_but_graphs,command=lambda:but_graphs_clicked(),indicatoron=False,selectcolor="#d4d4d4",cursor="hand2",bg="#608BC1",fg="#000000",relief="flat",bd=0,font=font_buttons)
def but_graphs_clicked():
    # frame_cash_flow.lift()
    global current_page
    current_page=5
    frame_graphs.lift()
    lift_important_widgets()
    var_about.set(0)
    var_help.set(0)
    var_but_balance_sheet.set(0)
    var_but_cash_flow.set(0)
    var_but_graphs.set(1)
    var_but_product_profits.set(0)
    var_but_pl_statements.set(0)
    var_but_financial_ratios.set(0)
    var_but_sales_overview.set(0)
    var_but_forecast_budget.set(0)
but_graphs.pack(side="left",fill="both",expand=True)

var_but_pl_statements=tk.IntVar(value=0)
but_pl_statements=tk.Checkbutton(frame_buttons,text="P & L STATEMENTS",variable=var_but_pl_statements,command=lambda:but_pl_statements_clicked(),indicatoron=False,selectcolor="#d4d4d4",cursor="hand2",bg="#608BC1",fg="#000000",relief="flat",bd=0,font=font_buttons)
def but_pl_statements_clicked():
    # frame_cash_flow.lift()
    global current_page
    current_page=6
    frame_p_l_statements.lift()
    lift_important_widgets()
    var_about.set(0)
    var_help.set(0)
    var_but_balance_sheet.set(0)
    var_but_cash_flow.set(0)
    var_but_graphs.set(0)
    var_but_product_profits.set(0)
    var_but_pl_statements.set(1)
    var_but_financial_ratios.set(0)
    var_but_sales_overview.set(0)
    var_but_forecast_budget.set(0)

but_pl_statements.pack(side="left",fill="both",expand=True)


var_but_sales_overview=tk.IntVar(value=0)
but_sales_overview=tk.Checkbutton(frame_buttons,text="SALES OVERVIEW",variable=var_but_sales_overview,command=lambda:but_sales_overview_clicked(),indicatoron=False,selectcolor="#d4d4d4",cursor="hand2",bg="#608BC1",fg="#000000",relief="flat",bd=0,font=font_buttons)
def but_sales_overview_clicked():
    # frame_cash_flow.lift()
    global current_page
    current_page=7
    frame_sales_overview.lift()
    lift_important_widgets()
    var_about.set(0)
    var_help.set(0)
    var_but_balance_sheet.set(0)
    var_but_cash_flow.set(0)
    var_but_graphs.set(0)
    var_but_product_profits.set(0)
    var_but_pl_statements.set(0)
    var_but_financial_ratios.set(0)
    var_but_sales_overview.set(1)
    var_but_forecast_budget.set(0)
but_sales_overview.pack(side="left",fill="both",expand=True)

var_but_forecast_budget=tk.IntVar(value=0)
but_forecast_budget=tk.Checkbutton(frame_buttons,text="FORECAST AND BUDGET    ",variable=var_but_forecast_budget,command=lambda:but_forecast_budget_clicked(),indicatoron=False,selectcolor="#d4d4d4",cursor="hand2",bg="#608BC1",fg="#000000",relief="flat",bd=0,font=font_buttons)
def but_forecast_budget_clicked():
    # frame_cash_flow.lift()
    global current_page
    frame_forecast_budget.lift()
    lift_important_widgets()
    current_page=8
    var_about.set(0)
    var_help.set(0)
    var_but_balance_sheet.set(0)
    var_but_cash_flow.set(0)
    var_but_graphs.set(0)
    var_but_product_profits.set(0)
    var_but_pl_statements.set(0)
    var_but_financial_ratios.set(0)
    var_but_sales_overview.set(0)
    var_but_forecast_budget.set(1)
but_forecast_budget.pack(side="left",fill="both",expand=True)


# -----------------------frame of balance sheet---------------------------
frame_balance_sheet=tk.Frame(frame_content,bg="#d4d4d4")
frame_balance_sheet.place(relx=0,rely=0,relwidth=1,relheight=1)


# --------------------- frame of cash flow--------------------------------
frame_cash_flow=tk.Frame(frame_content,bg="#d4d4d4")
frame_cash_flow.place(relx=0,rely=0,relwidth=1,relheight=1)


# ---------------------- frame of graphs -------------------------------
frame_graphs=tk.Frame(frame_content,bg="#d4d4d4")
frame_graphs.place(relx=0,rely=0,relwidth=1,relheight=1)

# under_dev

# ---------------------------- frame of product profits -------------------------
frame_product_profits=tk.Frame(frame_content,bg="#d4d4d4")
frame_product_profits.place(relx=0,rely=0,relwidth=1,relheight=1)



# ---------------------------- frame of P & L STATEMENTS -------------------------
frame_p_l_statements=tk.Frame(frame_content,bg="#d4d4d4")
frame_p_l_statements.place(relx=0,rely=0,relwidth=1,relheight=1)


# ---------------------------- frame of financial ratios -------------------------
frame_financial_ratios=tk.Frame(frame_content,bg="#d4d4d4")
frame_financial_ratios.place(relx=0,rely=0,relwidth=1,relheight=1)

# ---------------------------- frame of sales overview -------------------------
frame_sales_overview=tk.Frame(frame_content,bg="#d4d4d4")
frame_sales_overview.place(relx=0,rely=0,relwidth=1,relheight=1)


# ---------------------------- frame of forecast budget -------------------------
frame_forecast_budget=tk.Frame(frame_content,bg="#d4d4d4")
frame_forecast_budget.place(relx=0,rely=0,relwidth=1,relheight=1)


# ------------------------------ Help --------------------------------
frame_help=tk.Frame(frame_content,bg="#baafaf")
frame_help.place(relx=0,rely=0,relwidth=1,relheight=1)

def design_help():
    header_frame_help=tk.Label(frame_help,text="Help",font=("Calibri",12,"bold"),bg="#baafaf",anchor="center")
    header_frame_help.place(relx=0,rely=0,relwidth=1,relheight=0.1)
    frame_=tk.Frame(frame_help,bg="#134950",bd=1)
    frame_.place(relx=0.025,rely=0.095,relwidth=0.95,relheight=1-0.095)
    #label for note
    tk.Label(frame_,text="Help section's design will be available in the future work",anchor="center",bg="white",fg="#888888",
             font=("Calibri",10,"bold italic")).pack(expand=True,fill="both",padx=1,pady=1)

design_help()

# ------------------------------ About Us --------------------------------
frame_about=tk.Frame(frame_content,bg="#baafaf")
frame_about.place(relx=0,rely=0,relwidth=1,relheight=1)
def design_about():
    header_frame_about=tk.Label(frame_about,text="About Us",font=("Calibri",12,"bold"),bg="#baafaf",anchor="center")
    header_frame_about.place(relx=0,rely=0,relwidth=1,relheight=0.1)
    frame_=tk.Frame(frame_about,bg="#134950",bd=1)
    frame_.place(relx=0.025,rely=0.095,relwidth=0.95,relheight=1-0.095)
    #label for note
    tk.Label(frame_,text="About Us section's design will be available in the future work",anchor="center",bg="white",fg="#888888",
             font=("Calibri",10,"bold italic")).pack(expand=True,fill="both",padx=1,pady=1)

design_about()


# ---------------- work of frame of balance sheet---------
def design_balance_sheet():
    

    header_frame_balance_sheet=tk.Label(frame_balance_sheet,text="BALANCE SHEET",font=("Calibri",12,"bold"),bg="#d4d4d4",anchor="center")
    header_frame_balance_sheet.place(relx=0,rely=0,relwidth=1,relheight=0.1)

    
    frame_out=tk.Frame(frame_balance_sheet,border=2,relief="groove",bg="#134950")
    frame_out.place(relx=0.025,rely=0.1,relwidth=0.95,relheight=0.9)
    # frame.pack_propagate(False)
    frame_treeview=tk.Frame(frame_out,border=0,relief="groove",bg="RED")
    # frame_treeview.pack_propagate(False)
    frame_treeview.pack(side="top",expand=True,fill="both",padx=0,pady=0)
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview",
                    background="#ECEFCA",
                    fieldbackground="#ECEFCA",
                    font=("Calibri",10),
                    border=0,
                    rowheight=25,
                    )
    # style.map("Treeview",
    #           background=[("selected","#caf4f5")],
    #           foreground=[("selected","black")],
    #           )
    # style.configure("hoverrow",
    #                 background="#acaf8e"
    #                 )
    style.configure("Treeview.Heading",
                    font=("Calibri", 11, "bold"),
                    bd=0,
                    relief="flat",
                    background="#547792",
                    fieldbackground="#547792")
    

    # ---------- Treeview Table ----------
    columns = ("current", "last", "difference")

    tree = ttk.Treeview(frame_treeview, columns=columns, show="tree headings")
    tree.pack(side="top",fill="both",expand=True,padx=0,pady=0)
    
    tree.heading("#0", text="Category")
    tree.heading("current", text="Current Year")
    tree.heading("last", text="Last Year")
    tree.heading("difference", text="Difference")

    tree.column("#0", width=250)
    tree.column("current", anchor="center", width=120)
    tree.column("last", anchor="center", width=120)
    tree.column("difference", anchor="center", width=120)

    # ---------- Mock Data ----------
    # Assets
    tree.insert("", "end", "assets", text="Assets", open=True)
    tree.insert("assets", "end", text="Cash", values=("₹100,000", "₹80,000", "+₹20,000"))
    tree.insert("assets", "end", text="Accounts Receivable", values=("₹50,000", "₹60,000", "-₹10,000"))
    tree.insert("assets", "end", text="Inventory", values=("₹40,000", "₹35,000", "+₹5,000"))
    tree.insert("assets", "end", text="Prepaid Expenses", values=("₹10,000", "₹8,000", "+₹2,000"))

    # Liabilities
    tree.insert("", "end", "liabilities", text="Liabilities", open=True)
    tree.insert("liabilities", "end", text="Accounts Payable", values=("₹20,000", "₹25,000", "-₹5,000"))
    tree.insert("liabilities", "end", text="Short-term Loans", values=("₹10,000", "₹15,000", "-₹5,000"))

    # Equity
    tree.insert("", "end", "equity", text="Equity", open=True)
    tree.insert("equity", "end", text="Share Capital", values=("₹100,000", "₹100,000", "₹0"))
    tree.insert("equity", "end", text="Retained Earnings", values=("₹60,000", "₹35,000", "+₹25,000"))

    # ---------- Bottom Summary ----------
    summary = tk.Label(frame_out, text="Total Assets = Total Liabilities + Equity", font=("Calibri", 11),border=2,relief="groove", fg="black", bg="#fbe4d6")
    # frame.place(relx=0.025,rely=0.1,relwidth=0.95,relheight=0.9)
    # summary.place(relx=0.025,rely=0.9,relwidth=0.95,relheight=0.1)
    summary.pack(side="top",fill="x",padx=0,pady=0)
    
    # adding hovering effect to the treeview
    # using binding
    # using tags
    hover_state={"prev":None}
    def on_hover(event):
        row_id=tree.identify_row(event.y)
        # CLEARS old hover
        if hover_state["prev"] and hover_state["prev"]!= row_id:
            tree.item(hover_state["prev"],tags=())
        
        #add hover to current row
        if row_id and tree.parent(row_id):
            tree.item(row_id,tags=("hoverrow",))
            hover_state["prev"]=row_id
        else:
            hover_state["prev"]=None
    tree.tag_configure("hoverrow",background="white",foreground="black")
    tree.bind("<Motion>",on_hover)

design_balance_sheet()
# a paned window to contain both table and graphical visual of balance sheet

#---------------work of frame cash flow  
def design_cash_flow():
     
    header_frame_cash_flow=tk.Label(frame_cash_flow,text="CASH FLOW",font=("Calibri",12,"bold"),bg="#d4d4d4",anchor="center")
    header_frame_cash_flow.place(relx=0,rely=0,relwidth=1,relheight=0.1)
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview",
                    background="#ECEFCA",
                    fieldbackground="#ECEFCA",
                    font=("Calibri",10),
                    border=0,
                    rowheight=25
                  )
    


    style.map("Treeview",
              background=[("selected","#bfc29f")],
              foreground=[("selected","black")],
              )
    
    
    
    # a paned window to contain both table and graphical visual of cash flow
    style.configure("TPanedWindow",
                    border=2)
    paned_window = tk.PanedWindow(frame_cash_flow, orient=tk.HORIZONTAL,sashwidth=5,bg="#547792")  # Horizontal orientation
    # paned_window.pack(fill="both", expand=True)
    paned_window.place(relx=0.025,rely=0.095,relwidth=0.95,relheight=1-0.095)

    # --------------------- Frame ------------------
    frame_table = tk.Frame(paned_window)
    # frame_table.place(relx=0.03,rely=0.095,relwidth=0.95,relheight=0.95)
    frame_table.pack_propagate(False)
    frame_table.pack(side="top",expand=True,fill="both")
    frame_graph_paned_cash_flow=tk.Frame(paned_window,width=730,bg="#d4d4d4") #width decides minimum width of the frame to be opened in paned area
    frame_graph_paned_cash_flow.pack_propagate(False)
    frame_graph_paned_cash_flow.pack(expand=True,fill="both")

    # adding both frames to the paned window
    paned_window.add(frame_graph_paned_cash_flow)
    paned_window.add(frame_table)
    # by default, the second added frame is opened so i added the the frame_table secondly

    #-------------   ########################################################
    # --------------------------------TABLE DATA -----------------------
    columns = ("", "amount")
    tree = ttk.Treeview(frame_table, columns=columns, show="tree headings")
    tree.pack(side="top",fill="both",expand=True)

    

    # tree.column("#0", width=0, stretch=tk.NO)
    # tree.heading("#0", text="", anchor=tk.W)

    tree.heading("#0", text="Description")
    tree.heading("amount", text="Amount (₹)")
    
    tree.column("#0",anchor="w",width=250)
    tree.column("amount", anchor="center",width=120)

    ### -----mock data
    # ------------------ Insert Data ------------------
    tree.insert("", "end","OPERATING ACTIVITIES",text="OPERATING ACTIVITIES" ,open=True)
    tree.insert("OPERATING ACTIVITIES", "end", text="Net Income",values=("","75,000"))
    tree.insert("OPERATING ACTIVITIES", "end", text="Depreciation",values=("","10,000"))
    tree.insert("OPERATING ACTIVITIES", "end", text="Change in Working Capital",values=("","-5,000"))
    tree.insert("OPERATING ACTIVITIES", "end", text="Net Cash from Operating Activities",values=( "","80,000"), tags=("total"))

    

    tree.insert("", "end","INVESTING ACTIVITIES", text="INVESTING ACTIVITIES",open=True)
    tree.insert("INVESTING ACTIVITIES", "end",text="Purchase of Equipment", values=("","-30,000"))
    tree.insert("INVESTING ACTIVITIES", "end", text="Net Cash from Investing Activities",values=("","-30,000"), tags=("total",))


    tree.insert("", "end", "FINANCING ACTIVITIES",text="FINANCING ACTIVITIES", open=True)
    tree.insert("FINANCING ACTIVITIES", "end", text="Loan Received",values=( "","50,000"))
    tree.insert("FINANCING ACTIVITIES", "end", text="Dividends Paid", values=("","-10,000"))
    tree.insert("FINANCING ACTIVITIES", "end",text="Net Cash from Financing Activities", values=("", "40,000"), tags=("total",))


    tree.insert("", "end","Total", text="Net Change in Cash",values=("", "90,000"), tags=("summary",),open=True)
    tree.insert("Total", "end",text="Beginning Cash Balance", values=("","10,000"), tags=("summary",))
    tree.insert("Total", "end", text="Ending Cash Balance",values=("", "1,00,000"), tags=("summary",))

    # ------------------ Style Tags ------------------
    # tree.tag_configure("header", font=("Calibri", 10, "bold"), background="#F0F4FF")
    tree.tag_configure("total", font=("Calibri", 10, "bold"), background="#ECEFCA")
    tree.tag_configure("summary", font=("Calibri", 10, "bold"), background="#fbe4d6",foreground="black",anchor="w")

    # adding hovering effect to the treeview
    # using binding
    # using tags
    # not using custom style , because custom syle designs the complete widget
    # and here i want to make hover effect on current row
    # so tags is the best till now
    # tags is best for both parent-child tree as well as normal tree
    hover_state={"prev":None}
    def on_hover(event):
            row_id=tree.identify_row(event.y)
            #CLEARS old hover
            if hover_state["prev"] and hover_state["prev"]!=row_id:
                tree.item(hover_state["prev"],tags=())
            # add hover to current row
            if row_id and tree.parent(row_id):
                tree.item(row_id,tags=("hoverrow",))
                hover_state["prev"]=row_id
            else:
                hover_state["prev"]=None
    tree.tag_configure("hoverrow",background="white",foreground="black")
    tree.bind("<Motion>",on_hover)
    ########################################################
    ####################
    # ---------------       Graph of cash flow inside the paned window of the frame_cash_flow
    frame_chart=tk.Frame(frame_graph_paned_cash_flow,bg="#ECEFCA")
    frame_chart.pack(expand=True,fill="both")

    activities = ["Beginning Balance", "Operating", "Investing", "Financing", "Ending Balance"]
    values = [10000, 80000, -30000, 40000, 100000]
    # creating the figure
    fig,ax=plt.subplots(figsize=(6,4),dpi=100)
    ax.plot(activities,values,marker='o',linestyle='-',color="#134950",linewidth=2)

    #adding value labels on each points
    for i, value in enumerate(values):
        ax.text(i, value + 2000, f"₹{value:,}", ha='center', fontweight='bold')

    # design , style of the graph
    ax.set_facecolor('#ebe8db')  #  background for the chart/axes
    fig.patch.set_facecolor("#ffffff")
    ax.set_title("Cash Flow",fontsize=13,fontweight="bold",font="Calibri")
    ax.set_ylabel("Amount (Rs)",fontsize=13,fontweight="bold",font="Calibri")
    ax.grid(True)
    ax.spines[["top","right"]].set_visible(False)

    #Embeding the plot in tkinter
    canvas=FigureCanvasTkAgg(fig,master=frame_chart)
    canvas.draw()
    canvas.get_tk_widget().pack(expand=True,fill="both")

design_cash_flow()

#function to design the graphs section
def design_graphs():
    header_frame_graphs=tk.Label(frame_graphs,text="GRAPHS",font=("Calibri",12,"bold"),bg="#d4d4d4",anchor="center")
    header_frame_graphs.place(relx=0,rely=0,relwidth=1,relheight=0.1)
    frame_=tk.Frame(frame_graphs,bg="#134950",bd=1)
    frame_.place(relx=0.025,rely=0.095,relwidth=0.95,relheight=1-0.095)
    #label for note
    tk.Label(frame_,text="This section is reserved for optional data visualization features",anchor="center",bg="white",fg="#888888",
             font=("Calibri",10,"bold italic")).pack(expand=True,fill="both",padx=1,pady=1)

design_graphs()
# function to design the products profit section
def design_products_profit():
    header_frame_product_profits=tk.Label(frame_product_profits,text="PRODUCT PROFITS",font=("Calibri",12,"bold"),bg="#d4d4d4",anchor="center")
    header_frame_product_profits.place(relx=0,rely=0,relwidth=1,relheight=0.1) 
    
    # a paned window to contain both table and grahical visual of product profits
    paned_window=tk.PanedWindow(frame_product_profits,orient=tk.HORIZONTAL,sashwidth=5,bg="#134950")  #horizontal orientation
    paned_window.place(relx=0.025,rely=0.095,relwidth=0.95,relheight=1-0.095)

    #  ---------------- Frame
    frame_table=tk.Frame(paned_window,width=495)
    frame_table.pack_propagate(False)
    frame_table.pack(expand=True,fill="both")
    frame_graph_product_profits=tk.Frame(paned_window, bg="#134950",width=805)  #width decides minimum width of the frame to be opened in paned area
    frame_graph_product_profits.pack_propagate(False)
    frame_graph_product_profits.pack(expand=True,fill="both")

    
    # adding both frams to the paned window
    paned_window.add(frame_table)
    paned_window.add(frame_graph_product_profits)
    
    frame_treeview=tk.Frame(frame_table,bg="#d4d4d4")
    frame_treeview.place(relx=0,rely=0,relwidth=1,relheight=0.9)
    columns=("Product Name","Units Sold","Revenue","Cost Price","Profit")
    tree=ttk.Treeview(frame_treeview,columns=columns,show="tree headings")
    # adding a scrollbar to the treeview
    scrollbar=ttk.Scrollbar(frame_treeview,orient="vertical",command=tree.yview)
    scrollbar.pack(side="right",fill="y")
    tree.config(yscrollcommand=scrollbar.set)
    tree.pack(side="left",fill="both",expand=True)
    # this is imoprtant to make the ghost column disapper
    tree.column("#0", width=0, stretch=tk.NO)
    tree.heading("#0", text="", anchor=tk.W)

    tree.heading("Product Name",text="Product Name")
    tree.heading("Units Sold",text="Units sold")
    tree.heading("Revenue",text="Revenue (₹)")
    tree.heading("Cost Price",text="Cost Price (₹)")
    tree.heading("Profit",text="Profit (₹)")

    tree.column("Product Name",anchor="w",width=100)
    tree.column("Units Sold",anchor="center",width=100)
    tree.column("Revenue",anchor="center",width=100)
    tree.column("Cost Price",anchor="center",width=100)
    tree.column("Profit",anchor="center",width=100)

    # sample data
    sample_data=[
        ["Product A", 120, 480000,240000,240000],
        ["Product B", 100, 380000,160000,200000],
        ["Product C", 180, 320000,170000,150000],
        ["Product D", 70, 280000,130000,150000],
        ["Product E", 75, 320000, 120000, 200000],
        ["Product F", 60, 250000, 95000, 155000],
        ["Product G", 90, 370000, 140000, 230000],
        ["Product H", 55, 210000, 80000, 130000],
        ["Product I", 85, 340000, 135000, 205000],
        ["Product J", 50, 190000, 70000, 120000],
        ["Product K", 70, 300000, 110000, 190000],
        ["Product L", 65, 270000, 100000, 170000],
        ["Product M", 80, 350000, 125000, 225000],
        ["Product N", 45, 180000, 65000, 115000],
        ["Product O", 95, 390000, 145000, 245000],
        ["Product P", 58, 230000, 85000, 145000],
        ["Product Q", 63, 260000, 95000, 165000],
        ["Product R", 77, 310000, 115000, 195000],
        ["Product S", 80, 350000, 125000, 225000],
        ["Product T", 45, 180000, 65000, 115000],
        ["Product U", 95, 390000, 145000, 245000],
        ["Product V", 58, 230000, 85000, 145000],
        ["Product W", 63, 260000, 95000, 165000],
        ["Product X", 77, 310000, 115000, 195000],
        ["Product Y", 80, 350000, 125000, 225000],
        ["Product Z", 45, 180000, 65000, 115000]

    ]
    # inserting data to treeview name tree
    for data in sample_data:
        tree.insert(parent="",index="end",iid=None,text="",values=data)

    # adding hovering effect to the treeview
    # using binding
    # using tags
    # def on_hover(event):
    #     row_id=tree.identify_row(event.y)
    #     for row in tree.get_children():
    #         tree.item(row,tags=())    # clear previous tags
    #     if row_id:
    #         tree.item(row_id,tags=("hover",))
    # setting up hover tag style
    hover_state={"prev":None}
    def on_hover(event):
        row_id=tree.identify_row(event.y)
        # CLEARS old hover
        if hover_state["prev"] and hover_state["prev"]!= row_id:
            tree.item(hover_state["prev"],tags=())
        
        #add hover to current row
        if row_id:
            tree.item(row_id,tags=("hoverrow",))
            hover_state["prev"]=row_id
        else:
            hover_state["prev"]=None
    tree.tag_configure("hoverrow",background="white",foreground="black")
  
    # tree.tag_configure("hover",background="#acaf8e")
    tree.bind("<Motion>",on_hover)


    ##################################################################
    ###########   --------- GRAPH-----

    products=["Product A","Product B","Product C","Product D","Product E","Product F","Product G","Product H"]
    profits=[200000,240000,150000,100000,200000,155000,230000,130000]
    # giving colour to each profit bars in the graph
    colors=[]
    max_profit=max(profits)
    min_profit=min(profits)
    for p in profits:
        if p==max_profit : colors.append("#65a3bb") # highest profit with this color
        elif p==min_profit : colors.append("#9ebdc9")  # lowest profit 
        else : colors.append("#c9e8f5")
    # creating figure
    fig,ax=plt.subplots(figsize=(10,8))
    ax.barh(products,profits,color=colors,edgecolor="#134950")
    ax.set_facecolor('#ebe8db') #  background for the chart/axes
    fig.patch.set_facecolor("#ffffff")
    ax.set_xlabel("Profit (INR)",fontsize=12)
    ax.set_ylabel("Products",fontsize=12)
    ax.set_title("Profit by Product",fontsize=13)
    ax.grid(axis="x",linestyle=":",alpha=0.5,color="steelblue")

    # displaying the graph in the tkinter
    canvas=FigureCanvasTkAgg(fig,master=frame_graph_product_profits)
    canvas.get_tk_widget().pack()
    canvas.draw()





    # a frame to entry and search product
    # frame_search_product=tk.Frame(frame_table,bg="yellow")
    # frame_search_product.pack_propagate(False)
    # frame_search_product.pack(side="bottom",expand=True,fill="both")

    # label of search products
    frame_entry_and_searchButton=tk.Frame(frame_table,relief="raised",border=2,height=90,bg="#FBE4D6")
    frame_entry_and_searchButton.place(relx=0,rely=0.9,relwidth=1,relheight=0.1)
    label_search_product=tk.Label(frame_entry_and_searchButton,text="Search your Product",font=("Calibri",14),bg="#FBE4D6",anchor="center")
    label_search_product.pack(side="top",expand=True,fill="both")
    # frame to contain search entry and search button
    var_entry_product=tk.StringVar()
    var_entry_product.set("Enter product name")
    entry_search=tk.Entry(frame_entry_and_searchButton,textvariable=var_entry_product,bg="white",font=("Calibri",14),relief="flat",border=2)
    entry_search.pack(side="left",expand="True",fill="x",padx=4,pady=3)
    # entry_search.place(relx=0.1,rely=0.3,relwidth=0.6,relheight=0.5)
    button_search=tk.Button(frame_entry_and_searchButton,text="Search",width=10,bg="#2e8b57",fg="#FFFFFF",font=("Calibri",12),relief="raised",border=2)
    # button_search.place(relx=0.8,rely=0.3,relwidth=0.2,relheight=0.5)
    button_search.pack(side="right",expand="True",fill="x",padx=4,pady=3)

    # binding function widget when focused in
    def on_click(event):
        #making the entry product widget to work when clicked(focused in)
        if(event.widget==entry_search):
            if(var_entry_product.get()=="Enter product name"):
                var_entry_product.set("")
    # binding function widget when focused out
    def focus_out(event):
        #making the entry product widget to work when focused out
        if(event.widget==entry_search):
            if(var_entry_product.get()==""):
                var_entry_product.set("Enter product name")
    # calling binding funtion  
    entry_search.bind("<FocusIn>",on_click)
    entry_search.bind("<FocusOut>",focus_out)

design_products_profit()

# function to design the profit and loss statements section
def design_p_l_statements():
    
    header_frame_p_l_statements=tk.Label(frame_p_l_statements,text="P&L STATEMENTS",font=("Calibri",12,"bold"),bg="#d4d4d4",anchor="center")
    header_frame_p_l_statements.place(relx=0,rely=0,relwidth=1,relheight=0.1)
    frame_=tk.Frame(frame_p_l_statements,bg="#134950",bd=1)
    frame_.place(relx=0.025,rely=0.095,relwidth=0.95,relheight=1-0.095)
    #label for note
    tk.Label(frame_,text="This section is reserved for profit and loss statements (if included)",anchor="center",bg="white",fg="#888888",
             font=("Calibri",10,"bold italic")).pack(expand=True,fill="both",padx=1,pady=1)
design_p_l_statements()

def design_sales_overview():
    header_frame_sales_overview=tk.Label(frame_sales_overview,text="SALES OVERVIEW",font=("Calibri",12,"bold"),bg="#d4d4d4",anchor="center")
    header_frame_sales_overview.place(relx=0,rely=0,relwidth=1,relheight=0.1)
    frame_=tk.Frame(frame_sales_overview,bg="#134950",bd=1)
    frame_.place(relx=0.025,rely=0.095,relwidth=0.95,relheight=1-0.095)
    #label for note
    tk.Label(frame_,text="This section is reserved for sales trends and summarizes (if included)",anchor="center",bg="white",fg="#888888",
             font=("Calibri",10,"bold italic")).pack(expand=True,fill="both",padx=1,pady=1)

design_sales_overview()

def design_forecast_budget():
    
    header_frame_forecast_budget=tk.Label(frame_forecast_budget,text="FORECAST AND BUDGET",font=("Calibri",12,"bold"),bg="#d4d4d4",anchor="center")
    header_frame_forecast_budget.place(relx=0,rely=0,relwidth=1,relheight=0.1)

    frame_=tk.Frame(frame_forecast_budget,bg="#134950",bd=1)
    frame_.place(relx=0.025,rely=0.095,relwidth=0.95,relheight=1-0.095)
    #label for note
    tk.Label(frame_,text="This section is reserved for forecasts and budgets (if included)",anchor="center",bg="white",fg="#888888",
             font=("Calibri",10,"bold italic")).pack(expand=True,fill="both",padx=1,pady=1)

design_forecast_budget()
# function to design the financial rations section
def design_financial_ratios():
    header_frame_financial_ratios=tk.Label(frame_financial_ratios,text="FINANCIAL RATIOS",font=("Calibri",12,"bold"),bg="#d4d4d4",anchor="center")
    header_frame_financial_ratios.place(relx=0,rely=0,relwidth=1,relheight=0.1)
    frame_all_ratios=tk.Frame(frame_financial_ratios,bg="#134950",bd=2)
    frame_all_ratios.place(relx=0.025,rely=0.095,relwidth=0.95,relheight=1-0.095)
    # creating the progress bar with canvas for better UI
    def draw_progress_bar(canvas, value, max_value, width, height,myTrick):
        # Clear the canvas
        canvas.delete("all")

        # Calculate filled width
        fill_width = (value / max_value) * width

        # Draw background (full bar)
        canvas.create_rectangle(0, 0, width, height, fill="#ccc", outline="")

        # Draw progress (filled portion)
        canvas.create_rectangle(0, 0, fill_width, height, fill="#74d777", outline="")

        # Optional: draw text
        canvas.create_text(width // 2, height // 2, text=f"{value:.1f} {myTrick}", fill="white", font=("Calibri", 12))
    bar_width = 250    # of progress bar
    bar_height = 13    # of progress bar

    #  frame of leverage
    frame_leverage=tk.Frame(frame_all_ratios,bg="#f0f0f0",width=600,border=1,relief="groove")
    frame_leverage.pack_propagate(False)
    frame_leverage.pack(side="right",fill="y",padx=0,pady=0)
    tk.Label(frame_leverage,text="Leverage",bg="#547792",font=("Calibri",12,"bold"),anchor="w").pack(padx=3,pady=2,fill="x")

    # frame for first ratio inside the frame of leverage
    frame_DtE=tk.Frame(frame_leverage)
    frame_DtE.pack(expand=True,fill="both")
    la1=tk.Label(frame_DtE,text="Debt-to-Equity:",font=("Calibri",11))
    la1.pack(side="left",padx=6)
    canvas4=tk.Canvas(frame_DtE,width=bar_width,height=bar_height,bg="black",highlightthickness=0)
    canvas4.pack(side="left")
    draw_progress_bar(canvas4,value=0.8,max_value=5,width=bar_width,height=bar_height,myTrick="/5")
    # frame for second ratio inside the frame of leverage
    frame_IC=tk.Frame(frame_leverage)
    frame_IC.pack(expand=True,fill="both")
    la2=tk.Label(frame_IC,text="Interest Coverage:",font=("Calibri",11))
    la2.pack(side="left",padx=6)
    canvas5=tk.Canvas(frame_IC,width=bar_width,height=bar_height,bg="black",highlightthickness=0)
    canvas5.pack(side="left")
    draw_progress_bar(canvas5,value=3.5,max_value=10,width=bar_width,height=bar_height,myTrick="/5")
    # frame for the third ratio inside the frame of frame_leverage
    frame_Eq=tk.Frame(frame_leverage)
    frame_Eq.pack(expand=True,fill="both")
    la3=tk.Label(frame_Eq,text="Equity Ratio:",font=("Calibri",11),anchor="w")
    la3.pack(side="top",fill="both",expand=True,padx=6)
    # creating the figure
    fig=Figure(figsize=(3,3))
    ax=fig.add_subplot(111)
    fig.patch.set_facecolor("#f0f0f0")
    ax.set_facecolor('#f0f0f0') #  background for the chart/axes
    ax.pie([40,60],labels=['Equity','Debt'],colors=["#74d777","#d9655d"],
           autopct="%1.0f%%",startangle=90)
    ax.set_title("Capital Structure")
    ax.axis("equal")

    # embeding the pie chart in tkinter
    canvas6=FigureCanvasTkAgg(fig,master=frame_Eq)
    canvas6.draw()
    canvas6.get_tk_widget().pack()
    ####
    ##
    ##
    ###
    # frame of liquidity ratios
    frame_liquidity=tk.Frame(frame_all_ratios,bg="#f0f0f0",border=1,relief="groove")
    frame_liquidity.pack(side="top",fill="both",expand=True,padx=0,pady=0)
    # frame_liquidity.pack_propagate(False)
    tk.Label(frame_liquidity,text="Liquidity",anchor="w",font=("Calibri",12,"bold"),bg="#547792").pack(padx=3,pady=2,fill="x")
    # frame of first ratio
    frame_cr=tk.Frame(frame_liquidity)
    frame_cr.pack(expand=True,fill="both")
    la4=tk.Label(frame_cr,text="Current Ratio:",font=("Calibri",11))
    la4.pack(side="left",padx=6)
    # Create canvas for progress bar of cr
    
    canvas = tk.Canvas(frame_cr, width=bar_width, height=bar_height, bg="black", highlightthickness=0)
    canvas.pack(side="left")
    # Draw the progress bar with 2.1 out of 5
    draw_progress_bar(canvas, value=2.1, max_value=5, width=bar_width, height=bar_height,myTrick="/5")

    # frame for second ratio inside frame of liquidity
    frame_qr=tk.Frame(frame_liquidity)
    frame_qr.pack(expand=True,fill="both")
    la5=tk.Label(frame_qr,text="Quick Ratio:",font=("Calibri",11))
    la5.pack(side="left",padx=6)
    canvas2=tk.Canvas(frame_qr,width=bar_width,height=bar_height,bg="black",highlightthickness=0)
    canvas2.pack(side="left")
    draw_progress_bar(canvas2,value=1.7,max_value=5,width=bar_width,height=bar_height,myTrick="/5")

    # frame for third ration inside the frame of linquidity
    frame_crr=tk.Frame(frame_liquidity)
    frame_crr.pack(expand=True,fill="both")
    la6=tk.Label(frame_crr,text="Cash Ratio:",font=("Calibri",11))
    la6.pack(side="left",padx=6)
    canvas3=tk.Canvas(frame_crr,width=bar_width,height=bar_height,bg="black",highlightthickness=0)
    canvas3.pack(side="left")
    draw_progress_bar(canvas3,value=0.9,max_value=5,width=bar_width,height=bar_height,myTrick="/5")

    ####
    ###
    ##
    # frame of profitability
    frame_profitability=tk.Frame(frame_all_ratios,bg="#f0f0f0")
    # frame_profitability.pack_propagate(False)
    frame_profitability.pack(side="top",expand=True,fill="both",padx=0,pady=0)
    tk.Label(frame_profitability,text="Profitability",font=("Calibri",12,"bold"),bg="#547792",
             anchor="w").pack(padx=3,pady=2,fill="x")
    # frame for first ration inside the frame of profitability
    frame_npm=tk.Frame(frame_profitability)
    frame_npm.pack(expand=True,fill="both")
    la7=tk.Label(frame_npm,text="Net Profit Margin:",font=("Calibri",11))
    la7.pack(side="left",padx=6)
    canvas3=tk.Canvas(frame_npm,width=bar_width,height=bar_height,bg="black",highlightthickness=0)
    canvas3.pack(side="left")
    draw_progress_bar(canvas3,value=15,max_value=100,width=bar_width,height=bar_height,myTrick="%")
    # frame for second raio inside the frame of profitability
    frameROA=tk.Frame(frame_profitability)
    frameROA.pack(expand=True,fill="both")
    la8=tk.Label(frameROA,text="Return of Assets (ROA) : 8%",font=("Calibri",11),anchor="w" )
    la8.pack(expand=True,fill="both",padx=6)
    # frame for third ratio inside the frame frame_profitability
    frameROE=tk.Frame(frame_profitability)
    frameROE.pack(expand=True,fill="both")
    la9=tk.Label(frameROE,text="Return of Equity (ROE): 12%",font=("Calibri",11),anchor="w")
    la9.pack(expand=True,fill="both",padx=6)

    # frame of efficiency
    frame_efficiency=tk.Frame(frame_all_ratios,bg="#f0f0f0")
    frame_efficiency.pack(side="top",fill="both",expand=True,padx=0,pady=0)
    tk.Label(frame_efficiency,text="Efficiency",anchor="w",font=("Calibri",12,"bold"),bg="#547792").pack(padx=3,pady=2,fill="x")
    frameATurnover=tk.Frame(frame_efficiency)
    frameATurnover.pack(expand=True,fill="both")
    la10=tk.Label(frameATurnover,text="Asset Turnover: 1.2",font=("Calibri",11),anchor="w")
    la10.pack(expand=True,fill="both",padx=6)
    frameITurnover=tk.Frame(frame_efficiency)
    frameITurnover.pack(expand=True,fill="both")
    la11=tk.Label(frameITurnover,text="Inventory Turnover: 4.5",font=("Calibri",11),anchor="w")
    la11.pack(expand=True,fill="both",padx=6)
    frameRTurnOver=tk.Frame(frame_efficiency)
    frameRTurnOver.pack(expand=True,fill="both")
    la12=tk.Label(frameRTurnOver,text="Receivables Turnover: 6.3",font=("Calibri",11),anchor="w")
    la12.pack(expand=True,fill="both",padx=6)
    

    # function to make all specific labels to have tooltip--- by class Tooltip i have decleared earlier
    def add_tooltips_to_ratios_of_finance():
        ToolTip(la2,"Measures ability to pay")
    add_tooltips_to_ratios_of_finance()
        
design_financial_ratios()

# function to lift important widgets to the top
def lift_important_widgets():
    but_menu.lift()
    frame_buttons.lift()
# -----------------------------------------------------------------------
but_balance_sheet_clicked()
root.config(bd=3,relief="groove")
root.mainloop()
