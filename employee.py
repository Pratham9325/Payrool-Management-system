from tkinter import *
from tkinter import messagebox,ttk
import pymysql
import time
from datetime import datetime
import os
import tempfile
import subprocess
from fpdf import FPDF
from tkinter import filedialog

class EmployeeSystem:
    
    def __init__(self, root):
        global txt_netsalary
        self.root = root
        self.root.title("Employee Payroll Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
       
        title=Label(self.root,text="Employee Payroll Management System",font=('times new roman',30,'bold'),bg="#017cda",fg='white',anchor="w",padx=10).place(x=0,y=0,relwidth=1,height=60)
        btn_emp = Button(self.root, text="All Employee 's", command=self.employee_frame, font=('times new roman', 20), bg="#C58F4B", fg='black')
        btn_emp.place(x=1200, y=8, height=30, width=200)
    
        #==============freme1=====================#
         #==============variables=================#
        self.var_emp_code=StringVar()
        self.var_designation=StringVar()
        self.var_name=StringVar()
        self.var_age=StringVar()
        self.var_grnder=StringVar()
        self.var_email=StringVar()
        self.var_hr_location=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_proof_id=StringVar() #addhar card
        self.var_contact=StringVar()
        self.var_status=StringVar()
        self.var_exp=StringVar()
        
        self.Month_Days=30
        self.work_pay=0
        
        
        Frame1 = Frame(self.root, bd=5, relief=RIDGE, bg="white",)
        Frame1.place(x=10, y=70, width=750, height=670)
        
        
        
        
        title2 = Label(Frame1, text="Employee Details", font=('times new roman', 20,'bold'), bg="#778899", fg='#fff', padx=10)
        title2.place(x=0, y=0, relwidth=1,)
        
        lbi_code = Label(Frame1, text="Employee Code", font=('times new roman', 20), bg="white", fg='black')
        lbi_code.place(x=10, y=70)
        
        txt_code = Entry(Frame1, font=('times new roman', 15),textvariable=self.var_emp_code, bg="LIGHTYELLOW", fg='black').place(x=220, y=72,width=200)
        
        self.btn_search = Button(Frame1, text="Search", font=('times new roman', 20,'bold'), command=self.search, bg='black', fg='black')
        self.btn_search.place(x=480, y=70, width=100)
       
        
        #======================ROW1==============================
        lbi_designation = Label(Frame1, text="Designation ", font=('times new roman', 20), bg="white", fg='black')
        lbi_designation.place(x=10, y=120)
        
        txt_designation = Entry(Frame1, font=('times new roman', 15),textvariable=self.var_designation, bg="LIGHTYELLOW", fg='black')
        txt_designation.place(x=170, y=125)
        
        lbi_dob = Label(Frame1, text="D.O.B ", font=('times new roman', 20), bg="white", fg='black')
        lbi_dob.place(x=342, y=120, width=200, ) 
        
        txt_dob = Entry(Frame1, font=('times new roman', 15),textvariable=self.var_dob, bg="LIGHTYELLOW", fg='black')
        txt_dob.place(x=520, y=125)
        #===========X===X=======ROW1===X===========X==================
        
        
         #======================ROW2==============================
        lbi_Name = Label(Frame1, text="Name ", font=('times new roman', 20), bg="white", fg='black')
        lbi_Name.place(x=10, y=170)
        
        txt_Name= Entry(Frame1, font=('times new roman', 15),textvariable=self.var_name, bg="LIGHTYELLOW", fg='black')
        txt_Name.place(x=170, y=175)
        
        lbi_doj = Label(Frame1, text="D.O.J ", font=('times new roman', 20), bg="white", fg='black')
        lbi_doj.place(x=342, y=170, width=200, ) 
        
        txt_doj = Entry(Frame1, font=('times new roman', 15),textvariable=self.var_doj, bg="LIGHTYELLOW", fg='black')
        txt_doj.place(x=520, y=175)
        #===========X===X=======ROW2===X===========X==================
        
        
        #======================ROW3==============================
        lbi_Age = Label(Frame1, text="Age ", font=('times new roman', 20), bg="white", fg='black')
        lbi_Age.place(x=10, y=220)
        
        txt_Age = Entry(Frame1, font=('times new roman', 15),textvariable=self.var_age, bg="LIGHTYELLOW", fg='black')
        txt_Age.place(x=170, y=225)
        
        lbi_expe = Label(Frame1, text="Experience ", font=('times new roman', 20), bg="white", fg='black')
        lbi_expe.place(x=342, y=220, width=200, ) 
        
        txt_expe = Entry(Frame1, font=('times new roman', 15),textvariable=self.var_exp, bg="LIGHTYELLOW", fg='black')
        txt_expe.place(x=520, y=225)
        #===========X===X=======ROW3===X===========X==================
        
        
         #======================ROW4==============================
        lbi_gender= Label(Frame1, text="Gender ", font=('times new roman', 20), bg="white", fg='black')
        lbi_gender.place(x=10, y=270)
        
        # Gender options
        gender_options = [ 'Select','Male', 'Female', 'Others']
        
        # Gender combobox
        gender_combobox = ttk.Combobox(root, values=gender_options, font=('times new roman', 15),textvariable=self.var_grnder, background="LIGHTYELLOW", foreground='black')
        gender_combobox.place(x=185, y=350,width=175)
        
        # Set the default value to 'Select'
        gender_combobox.current(0) # Index of 'Select' in the list
        
        lbi_profil = Label(Frame1, text="Proof ID ", font=('times new roman', 20), bg="white", fg='black')
        lbi_profil.place(x=342, y=270, width=200, ) 
        
        txt_profil = Entry(Frame1, font=('times new roman', 15),textvariable=self.var_proof_id, bg="LIGHTYELLOW", fg='black')
        txt_profil.place(x=520, y=275)
        #===========X===X=======ROW4===X===========X==================
        
        
         #======================ROW5==============================
        lbi_email= Label(Frame1, text="Email ", font=('times new roman', 20), bg="white", fg='black')
        lbi_email.place(x=10, y=320)
        
        txt_email = Entry(Frame1, font=('times new roman', 15),textvariable=self.var_email, bg="LIGHTYELLOW", fg='black')
        txt_email.place(x=170, y=325)
        
        lbi_conte = Label(Frame1, text="Contact no ", font=('times new roman', 20), bg="white", fg='black')
        lbi_conte.place(x=342, y=320, width=200, ) 
        
        txt_conte = Entry(Frame1, font=('times new roman', 15),textvariable=self.var_contact, bg="LIGHTYELLOW", fg='black')
        txt_conte.place(x=520, y=325)
        #===========X===X=======ROW5===X===========X==================
        
        
           
         #======================ROW5==============================
        lbi_hired= Label(Frame1, text="Hired Location ", font=('times new roman', 20), bg="white", fg='black')
        lbi_hired.place(x=10, y=370)
        
        txt_hired = Entry(Frame1, font=('times new roman', 15),textvariable=self.var_hr_location, bg="LIGHTYELLOW", fg='black')
        txt_hired.place(x=170, y=375)
        
        lbi_status = Label(Frame1, text="Status ", font=('times new roman', 20), bg="white", fg='black')
        lbi_status.place(x=342, y=370, width=200, ) 
        
        txt_status= Entry(Frame1, font=('times new roman', 15),textvariable=self.var_status, bg="LIGHTYELLOW", fg='black')
        txt_status.place(x=520, y=375)
        #===========X===X=======ROW5===X===========X==================
        
        
        #======================ROW6==============================
        lbi_address= Label(Frame1, text="Address ", font=('times new roman', 20), bg="white", fg='black')
        lbi_address.place(x=10, y=420)
        
        self.txt_address = Text(Frame1, font=('times new roman', 15), bg="LIGHTYELLOW", fg='black')
        self.txt_address.place(x=170, y=425,width=550,height=170)
        
        
        
        
        
        
        
        
        #==============freme2=====================#
        
        self.var_month=StringVar()
        self.var_year=StringVar()
        self.var_salary=StringVar()
        self.var_t_days=StringVar() 
        self.var_apsent=StringVar()
        self.var_medical=StringVar()
        self.var_pf=StringVar()
        self.var_convence=StringVar() 
        self.var_net_salary=StringVar() 
        
        
        
        Frame2=Frame(self.root,bd=3,relief=RIDGE,bg="white")
        Frame2.place(x=770,y=70, width=650,height=350)
        
        
        title3 = Label(Frame2, text="Employee Salary Details", font=('times new roman', 20,'bold'), bg="#778899", fg='#fff', padx=10)
        title3.place(x=0, y=0, relwidth=1)
        
        lbi_month = Label(Frame2, text="Month", font=('times new roman', 18), bg="white", fg='black').place(x=10, y=60)
        
        txt_month = Entry(Frame2, font=('times new roman', 15),textvariable=self.var_month, bg="LIGHTYELLOW", fg='black').place(x=100, y=60,width=100)
        
        lbi_year = Label(Frame2, text="Year", font=('times new roman', 18), bg="white", fg='black').place(x=230, y=60)
        
        txt_year = Entry(Frame2, font=('times new roman', 15), bg="LIGHTYELLOW", fg='black',textvariable=self.var_year).place(x=300, y=60,width=100)
        
        lbi_salary = Label(Frame2, text="Salary", font=('times new roman', 18), bg="white", fg='black')
        lbi_salary.place(x=430, y=60)
        
        txt_salary = Entry(Frame2, font=('times new roman', 15), bg="LIGHTYELLOW", fg='black',textvariable=self.var_salary).place(x=500, y=60,width=100)
        
        
        #======================ROW1==============================
        lbi_days = Label(Frame2, text="Total Days", font=('times new roman', 18), bg="white", fg='black',)
        lbi_days.place(x=10, y=120,)
        
        txt_days= Entry(Frame2, font=('times new roman', 15),textvariable=self.var_t_days, bg="LIGHTYELLOW", fg='black')
        txt_days.place(x=110, y=120,width=120)
        
        lbi_absent = Label(Frame2, text="Absents", font=('times new roman', 18), bg="white", fg='black')
        lbi_absent.place(x=280, y=120,  ) 
        
        txt_absent = Entry(Frame2, font=('times new roman', 15),textvariable=self.var_apsent, bg="LIGHTYELLOW", fg='black')
        txt_absent.place(x=370, y=120,width=120)
        #===========X===X=======ROW1===X===========X==================
        
         #======================ROW2==============================
        lbi_medical = Label(Frame2, text="Medical", font=('times new roman', 18), bg="white", fg='black')
        lbi_medical.place(x=10, y=160,)
        
        txt_medical= Entry(Frame2, font=('times new roman', 15),textvariable=self.var_medical, bg="LIGHTYELLOW", fg='black')
        txt_medical.place(x=110, y=160,width=120)
        
        lbi_pf = Label(Frame2, text="Pf", font=('times new roman', 18), bg="white", fg='black')
        lbi_pf.place(x=280, y=160,  ) 
        
        txt_pf = Entry(Frame2, font=('times new roman', 15),textvariable=self.var_pf, bg="LIGHTYELLOW", fg='black')
        txt_pf.place(x=370, y=160,width=120)
        #===========X===X=======ROW2===X===========X==================
        
        
           #======================ROW3==============================
        lbi_convence = Label(Frame2, text="Convence", font=('times new roman', 18), bg="white", fg='black')
        lbi_convence.place(x=10, y=200,)
        
        txt_convence= Entry(Frame2, font=('times new roman', 15),textvariable=self.var_convence, bg="LIGHTYELLOW", fg='black')
        txt_convence.place(x=110, y=200,width=120)
       # Display net salary automatically
        lbi_netsalary = Label(Frame2, text="Net Salary", font=('times new roman', 18), bg="white", fg='black')
        lbi_netsalary.place(x=260, y=200,)
        
        self.txt_netsalary= Entry(Frame2, font=('times new roman', 15),state=DISABLED,textvariable=self.var_net_salary, bg="LIGHTYELLOW", fg='black')
        self.txt_netsalary.place(x=370, y=200,width=120)
        
        
        self. btn_calculate = Button(Frame2, text="Calculate", command=self.calculate,font=('times new roman', 20,'bold'), bg="#C58F4B", fg='#008B8B')
        self.btn_calculate.place(x=120, y=235, height=30, width=120)
        # Create and place the Save button
        self.btn_save = Button(Frame2, text="Save", command=self.add, font=('times new roman', 20,'bold'), bg="#C58F4B", fg='#017cda')
        self.btn_save.place(x=260, y=235, height=30, width=120)

        self. btn_clear = Button(Frame2, text="Clear",command=self.clear_fields, font=('times new roman', 20,'bold'), bg="#C58F4B", fg='#008080')
        self.btn_clear.place(x=400, y=235, height=30, width=120)
        # btn_print = Button(Frame2, text="Print", font=('times new roman', 20), bg="gray", fg='black').place(x=460, y=70 ) 
        
        self. btn_update = Button(Frame2, text="Update", command=self.update_data,font=('times new roman', 20,'bold'),state=DISABLED, bg="#C58F4B", fg='Green')
        self.btn_update.place(x=120, y=270, height=30, width=180)
        # Create and place the Save button
        self.btn_delete = Button(Frame2, text="Delete", command=lambda: self.delete_and_clear(self.var_emp_code),state=DISABLED, font=('times new roman', 20,'bold'), bg="#C58F4B", fg='red')
        self.btn_delete.place(x=340, y=270, height=30, width=180)
        # #===========X===X=======ROW3===X===========X==================
       
        
        
        
        
        #==============freme3=====================#
        Frame3=Frame(self.root,bd=3,relief=RIDGE,bg="white")
        Frame3.place(x=770,y=380, width=650,height=360)
        #==============calculator Freame=========
        self.var_txt=StringVar()
        self.var_operator=''
        def btn_clear(num):
            self.var_operator=self.var_operator+str(num)
            self.var_txt.set(self.var_operator)
    
        
        Cal_Frame=Frame(Frame3,bg='white',bd=2,relief=RIDGE,)
        Cal_Frame.place(x=4,y=4,width=247,height=297)  
        
        #=================Row1===========================
        txt_Result=Entry(Cal_Frame,bg='lightyellow', textvariable=self.var_txt ,justify=RIGHT,fg='black',font=('times new roman',20,'bold') ).place(x=0,y=0,relwidth=1,height=40)  
        btn_7=Button(Cal_Frame,text='7', command=lambda:btn_clear(7),font=('time new roman',15,'bold')).place(x=0,y=42,width=60,height=65) 
        btn_8=Button(Cal_Frame,text='8',font=('time new roman',15,'bold')).place(x=61,y=42,width=60,height=65)    
        btn_9=Button(Cal_Frame,text='9',font=('time new roman',15,'bold')).place(x=122,y=42,width=60,height=65)    
        btn_div=Button(Cal_Frame,text='/',font=('time new roman',15,'bold')).place(x=183,y=42,width=60,height=65)    
           
         #=================Row2===========================
        tet_Result=Entry(Cal_Frame,bg='lightyellow',font=('times new roman',20,'bold')).place(x=0,y=0,relwidth=1,height=40)  
        btn_4=Button(Cal_Frame,text='4',font=('time new roman',15,'bold')).place(x=0,y=104,width=60,height=65) 
        btn_5=Button(Cal_Frame,text='5',font=('time new roman',15,'bold')).place(x=61,y=104,width=60,height=65)    
        btn_6=Button(Cal_Frame,text='6',font=('time new roman',15,'bold')).place(x=122,y=104,width=60,height=65)    
        btn_str=Button(Cal_Frame,text='*',font=('time new roman',15,'bold')).place(x=183,y=104,width=60,height=65)    
        
        
         #=================Row3===========================
        tet_Result=Entry(Cal_Frame,bg='lightyellow',font=('times new roman',20,'bold')).place(x=0,y=0,relwidth=1,height=40)  
        btn_1=Button(Cal_Frame,text='1',font=('time new roman',15,'bold')).place(x=0,y=166,width=60,height=65) 
        btn_2=Button(Cal_Frame,text='2',font=('time new roman',15,'bold')).place(x=61,y=166,width=60,height=65)    
        btn_3=Button(Cal_Frame,text='3',font=('time new roman',15,'bold')).place(x=122,y=166,width=60,height=65)    
        btn_sub=Button(Cal_Frame,text='-',font=('time new roman',15,'bold')).place(x=183,y=166,width=60,height=65)    
        
        
        
         #=================Row4===========================
        tet_Result=Entry(Cal_Frame,bg='lightyellow',font=('times new roman',20,'bold')).place(x=0,y=0,relwidth=1,height=40)  
        btn_0=Button(Cal_Frame,text='0',font=('time new roman',15,'bold')).place(x=0,y=224,width=60,height=65) 
        btn_dot=Button(Cal_Frame,text='.',font=('time new roman',15,'bold')).place(x=61,y=224,width=60,height=65)    
        btn_plus=Button(Cal_Frame,text='+',font=('time new roman',15,'bold')).place(x=122,y=224,width=60,height=65)    
        btn_eual=Button(Cal_Frame,text='=',font=('time new roman',15,'bold')).place(x=183,y=224,width=60,height=65)    
                    
        #============================salary fream============================
        
        sal_Frame=Frame(Frame3,bg='white',bd=2,relief=RIDGE,)
        sal_Frame.place(x=270,y=4,width=360,height=297)  
        title_sal = Label(sal_Frame, text="Salary Reciept", font=('times new roman', 20), bg="lightgray", fg='black', padx=10)
        title_sal.place(x=0, y=0, relwidth=1)
        
        
        
        
        title = Label(self.root, text="Copyright @ 2024 Employee Payroll Management System  develop by system consultant Tech.", font=('times new roman', 20, 'bold'),
              bg="SystemButtonFace", fg='#000', pady=25).place(x=0, y=750, relwidth=1, height=100)
        sal_Frame2=Frame(sal_Frame,bg='white',bd=2,relief=RIDGE)
        sal_Frame2.place(x=0,y=30,relwidth=1,height=230)
        sample=f'''\tCompany Name:system consultant Tech.\n\tAddress:Jalgaon
----------------------------------------------------------------------
        Employee ID\t\t: 
        Salary of\t\t:  Mon-YYYY
        Generated On\t\t: DD-MM-YYYY
----------------------------------------------------------------------
        Total Days\t\t: DD
        Total Present\t\t: DD
        Total Absent\t\t: DD
        Convence\t\t: Rs.---
        Medical\t\t: Rs.---
        PF\t\t: Rs.---
        Gross Payment\t\t: Rs.---
        Net Salary\t\t" : Rs.---
---------------------------------------------------------------------
        this is computer generator sleep, not 
        require any signature
---------------------------------------------------------------------
        '''    
        
        scroll_y=Scrollbar(sal_Frame2,orient=VERTICAL)
        scroll_y.pack(fill=Y,side=RIGHT)
        
        self.txt_salary_receipt = Text(sal_Frame2, font=('times new roman', 14), bg='lightyellow',
                               yscrollcommand=scroll_y.set)
        self.txt_salary_receipt.pack(fill=BOTH, expand=True)
        
        scroll_y.config(command=self.txt_salary_receipt.yview)
        self.txt_salary_receipt.insert(END,sample)
        
        self.btn_print = Button(sal_Frame, text="Print", font=('times new roman', 20,'bold'),state=DISABLED,command=self.print_salary, bg="lightblue", fg='#F2852C')
        self. btn_print.place(x=200, y=262, height=30, width=120)
        
        self.check_connection()
        
        ########## Search start#######################
        
    def search(self):
        try:
           con = pymysql.connect(host='localhost', user='root', passwd='', db='EMS')
           cur = con.cursor()
           cur.execute("SELECT * FROM amp_salary WHERE e_id=%s", (self.var_emp_code.get(),))
           rows = cur.fetchall()  # Fetch all rows that match the given employee ID

           if rows:
            # Employee ID found
              self.var_emp_code.set(rows[0][0])
              self.var_designation.set(rows[0][1])
              self.var_name.set(rows[0][2])
              self.var_age.set(rows[0][3])
              self.var_grnder.set(rows[0][4])  # Corrected variable name here
              self.var_email.set(rows[0][5])
              self.var_hr_location.set(rows[0][6])
              self.var_doj.set(rows[0][7])
              self.var_dob.set(rows[0][8])
              self.var_exp.set(rows[0][9])
              self.var_proof_id.set(rows[0][10])
              self.var_contact.set(rows[0][11])
              self.var_status.set(rows[0][12])
              self.txt_address.delete('1.0', END)
              self.txt_address.insert(END, rows[0][13])
  
              self.var_month.set(rows[0][14])
              self.var_year.set(rows[0][15])
              self.var_salary.set(rows[0][16])
              self.var_t_days.set(rows[0][17])
              self.var_apsent.set(rows[0][18])
              self.var_medical.set(rows[0][19])
              self.var_convence.set(rows[0][20])

              self.var_net_salary.set(rows[0][21])
              self.var_pf.set(rows[0][22])

            # Open the salary receipt file and display its content in the text box
              with open('Salary_reciept/' + str(rows[0][23]), 'r') as file:
                self.txt_salary_receipt.delete('1.0', END)
                for line in file:
                    self.txt_salary_receipt.insert(END, line)
            # Show the update, delete, and clear buttons
              self.btn_update.config(state=NORMAL)
              self.btn_delete.config(state=NORMAL)
              self.btn_clear.config(state=NORMAL)
              self.btn_print.config(state=NORMAL)
              self.btn_save.config(state=DISABLED)
           else:
            # Employee ID not found
            messagebox.showerror("Error", "Employee ID not found", parent=self.root)
            self.btn_update.config(state=DISABLED)
            self.btn_delete.config(state=DISABLED)
            self.btn_clear.config(state=DISABLED)
            
            
        except Exception as ex:
            messagebox.showerror("Error", f'Error due to: {str(ex)}')
             ########## Search start end   #######################
    def add(self):    
  
        if self.var_emp_code.get()=='' or self.var_net_salary.get()==''or self.var_name.get()=='Elsa':
         
              messagebox.showerror('Error',"Employee ID must be requirement")
        else:      
         try:
            con = pymysql.connect(host='localhost', user='root', passwd='', db='EMS')
            cur = con.cursor()
            cur.execute("SELECT * FROM amp_salary WHERE e_id=%s", (self.var_emp_code.get(),))
            rows = cur.fetchall()  # Corrected to include () to call the fetchall method
        #    print(rows)  # Now prints the actual result set
           # Close the connection when done
            if rows:
               messagebox.showerror("Error", "This Employee ID is already available in our records", parent=self.root)
            else:
                
                cur.execute('INSERT INTO amp_salary VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                (
                     self.var_emp_code.get(),
                     self.var_designation.get(),
                     self.var_name.get(),
                     self.var_age.get(),
                     self.var_grnder.get(), # Corrected variable name here
                     self.var_email.get(),
                     self.var_hr_location.get(),
                     self.var_doj.get(),
                     self.var_dob.get(),
                     self.var_exp.get(),
                     self.var_proof_id.get(),
                     self.var_contact.get(),
                     self.var_status.get(),
                     self.txt_address.get('1.0', END),
      
                    self.var_month.get(),
                    self.var_year.get(),
                    self.var_salary.get(),
                    self.var_t_days.get(),
                    self.var_apsent.get(),
                    self.var_medical.get(),
                    self.var_convence.get(),
                    
 
                    self.var_net_salary.get(),
                    
                    self.var_pf.get(),
                    self.var_emp_code.get()+".txt"
                )
                )   
                
                
                con.commit()
                con.close()
                file=open('Salary_reciept/'+str(self.var_emp_code.get())+".txt",'w')
                file.write(self.txt_salary_receipt.get('1.0',END))
                file.close()
                messagebox.showinfo("success","Record Added Successfully")
                self.clear_fields()
                
         except  Exception as ex:
                messagebox.showerror("Error", f'Error due to: {str(ex)}')
    def check_connection(self):  
        try:
          con = pymysql.connect(host='localhost', user='root', passwd='', db='EMS')
          cur = con.cursor()
          cur.execute("SELECT * FROM amp_salary")
          rows = cur.fetchone()  # Corrected to include () to call the fetchall method
          print(rows)  # Now prints the actual result set
          con.close()  # Close the connection when done
        except Exception as ex:
            messagebox.showerror("Error", f'Error due to: {str(ex)}')
     
    def shwo(self):
        try:
            con = pymysql.connect(host='localhost', user='root', passwd='', db='EMS')
            cur = con.cursor()
            cur.execute("SELECT * FROM amp_salary")
            rows = cur.fetchall()  # Corrected to fetch all rows

            self.employee_tree.delete(*self.employee_tree.get_children())
            for row in rows:
                self.employee_tree.insert('', END, values=row)
            con.close()

        except Exception as ex:
            messagebox.showerror("Error", f'Error due to: {str(ex)}')
        
    
    def calculate(self):
        print("calculate")

    # Check if all fields are filled
        if (self.var_month.get() == '' or self.var_year.get() == '' or self.var_salary.get() == '' or 
        self.var_t_days.get() == '' or self.var_apsent.get() == '' or self.var_pf.get() == '' or 
        self.var_medical.get() == '' or self.var_convence.get() == ''):
          messagebox.showerror('Error', 'All fields are required')
        else:
            try:
            # Convert relevant variables to floats
               per_day_salary = float(self.var_salary.get()) / float(self.Month_Days)
               total_salary = per_day_salary * float(self.var_t_days.get())
               pf_deduction = float(self.var_pf.get())
               medical_allowance = float(self.var_medical.get())
               conveyance_allowance = float(self.var_convence.get())
               absents = float(self.var_apsent.get())

            # Calculate net salary
               net_salary = total_salary - (pf_deduction + medical_allowance + conveyance_allowance) * (1 - absents / float(self.Month_Days))

            # Update the net salary variable
               self.var_net_salary.set(str(round(net_salary, 2)))

            # Prepare the receipt text
               receipt_text = f'''\tCompany Name:system consultant Tech.\n\tAddress:Jalgaon
----------------------------------------------------------------------
Employee ID\t\t: {self.var_emp_code.get()}
Salary of\t\t:  {self.var_month.get()}--{self.var_year.get()}
Generated On\t\t: {datetime.now().strftime("%d-%m-%Y")}
----------------------------------------------------------------------
Total Days\t\t: {self.var_t_days.get()}
Total Present\t\t: {int(self.var_t_days.get()) - int(self.var_apsent.get())}
Total Absent\t\t: {self.var_apsent.get()}
Convence\t\t: Rs.{self.var_convence.get()}
Medical\t\t: Rs.{self.var_medical.get()}
PF\t\t: Rs.{self.var_pf.get()}
Gross Payment\t\t: Rs.{self.var_salary.get()}
Net Salary\t\t: Rs.{net_salary}
---------------------------------------------------------------------
This is a computer-generated slip, not 
require any signature
---------------------------------------------------------------------'''

               print("Receipt Text:")
               print(receipt_text)  # Debugging: Print the receipt text
               

            # Update the receipt text in the txt_salary_receipt widget
               self.txt_salary_receipt.delete('1.0', END)
               self.txt_salary_receipt.insert(END, receipt_text)
               self.btn_print.config(state=NORMAL)
               self.txt_netsalary.config(state=NORMAL)
            except ValueError:
                messagebox.showerror('Error', 'Invalid input. Please enter valid numeric values for salary, PF, medical, convence, total days, and absents')
    
    def employee_frame(self):
        self.root2 = Toplevel(self.root)
        self.root2.title("Employee Payroll Management System")
        self.root2.geometry("1000x500+120+60")
        self.root2.config(bg="white")
        title=Label(self.root2,text="All Employee Details ",font=('times new roman',30,'bold'),bg="#017cda",fg='white',anchor="w",padx=10).pack(side=TOP,fill=X)
        self.root2.focus_force()
        
  
       
        
        
        Scrolly=Scrollbar(self.root2,orient=VERTICAL)
        ScrollX=Scrollbar(self.root2,orient=HORIZONTAL)
        ScrollX.pack(side=BOTTOM,fill=X)
        Scrolly.pack(side=RIGHT,fill=Y)
        self.employee_tree=ttk.Treeview(self.root2,columns=('e_id', 'designation', 'name', 'age', 'gender', 'email', 'hr_location', 'dog', 'dob', 
                                                            'experience', 'proof_id', 'contact', 'status', 'address', 'month', 'year',
                                                            'basic_salary', 't_days', 'absent_days', 
                                                            'medical', 'convenient', 'net_salary', 'pf', 'salary_receipt'),yscrollcommand=Scrolly.set,xscrollcommand=ScrollX.set)
        self.employee_tree.heading('e_id',text='Emp_id')
        self.employee_tree.heading('designation',text='designation')
        self.employee_tree.heading('name',text='Name')
        self.employee_tree.heading('age',text='age')
        self.employee_tree.heading('gender',text='gender')
        self.employee_tree.heading('email',text='email')
        self.employee_tree.heading('hr_location',text='hr_location')
        self.employee_tree.heading('dog',text='dog')
        self.employee_tree.heading('dob',text='dob')
        self.employee_tree.heading('experience',text='experience')
        self.employee_tree.heading('proof_id',text='proof_id')
        self.employee_tree.heading('contact',text='contact')
        self.employee_tree.heading('status',text='status')
        self.employee_tree.heading('address',text='address')
        self.employee_tree.heading('month',text='month')
        self.employee_tree.heading('year',text='year')
        self.employee_tree.heading('basic_salary',text='basic_salary')
        self.employee_tree.heading('t_days',text='tolel days')
        self.employee_tree.heading('absent_days',text='absent_days')
        self.employee_tree.heading('medical',text='medical')
        self.employee_tree.heading('convenient',text='convenient')
        self.employee_tree.heading('net_salary',text='net_salary')
        self.employee_tree.heading('pf',text='pf')
        self.employee_tree.heading('salary_receipt',text='salary_receipt')
    
        self.employee_tree['show'] = 'headings'
      
        # Set the width for all columns
        self.employee_tree.column('e_id', width=50)
        self.employee_tree.column('designation', width=150)
        self.employee_tree.column('name', width=150)
        self.employee_tree.column('age', width=50)
        self.employee_tree.column('gender', width=100)
        self.employee_tree.column('email', width=200)
        self.employee_tree.column('hr_location', width=200)
        self.employee_tree.column('dog', width=100)
        self.employee_tree.column('dob', width=100)
        self.employee_tree.column('experience', width=100)
        self.employee_tree.column('proof_id', width=200)
        self.employee_tree.column('contact', width=200)
        self.employee_tree.column('status', width=100)
        self.employee_tree.column('address', width=200)
        self.employee_tree.column('month', width=200)
        self.employee_tree.column('year', width=100)
        self.employee_tree.column('basic_salary', width=200)
        self.employee_tree.column('t_days', width=100)
        self.employee_tree.column('absent_days', width=100)
        self.employee_tree.column('medical', width=100)
        self.employee_tree.column('convenient', width=100)
        self.employee_tree.column('net_salary', width=200)
        self.employee_tree.column('pf', width=150)
        self.employee_tree.column('salary_receipt', width=50)
        ScrollX.config(command=self.employee_tree.xview)
        Scrolly.config(command=self.employee_tree.yview)
        self.employee_tree.pack(fill=BOTH, expand=1, side=TOP)
        self.shwo()
        self.root2.mainloop()
    
             
             
    def update_data(self):
        try:
        # Retrieve the updated data from input fields
            emp_code = self.var_emp_code.get()
            designation = self.var_designation.get()
            name = self.var_name.get()
            age = self.var_age.get()
            gender = self.var_grnder.get()  # Corrected variable name here
            email = self.var_email.get()
            hr_location = self.var_hr_location.get()
            doj = self.var_doj.get()
            dob = self.var_dob.get()
            exp = self.var_exp.get()
            proof_id = self.var_proof_id.get()
            contact = self.var_contact.get()
            status = self.var_status.get()
            address = self.txt_address.get('1.0', 'end-1c')  # Retrieve address from Text widget
            month = self.var_month.get()
            year = self.var_year.get()
            salary = self.var_salary.get()
            t_days = self.var_t_days.get()
            absent_days = self.var_apsent.get()
            medical = self.var_medical.get()
            convence = self.var_convence.get()  # Corrected variable name here
            net_salary = self.var_net_salary.get()
            pf = self.var_pf.get()

        # Connect to the database
            con = pymysql.connect(host='localhost', user='root', passwd='', db='EMS')
            cur = con.cursor()
    
            # Execute SQL UPDATE query to update the record in the database
            cur.execute("""UPDATE amp_salary SET 
                           designation=%s, name=%s, age=%s, gender=%s, email=%s, 
                           hr_location=%s, dog=%s, dob=%s, experience=%s, proof_id=%s, 
                           contact=%s, status=%s, address=%s, month=%s, year=%s, 
                           basic_salary=%s, t_days=%s, absent_days=%s, medical=%s, 
                           convenient=%s, net_salary=%s, pf=%s 
                           WHERE e_id=%s""", 
                        (designation, name, age, gender, email, hr_location, doj, dob, exp, proof_id,
                         contact, status, address, month, year, salary, t_days, absent_days, medical,
                         convence, net_salary, pf, emp_code))
    
            # Commit the changes to the database
            con.commit()

        # Close the database connection
            con.close()

        # Display success message
            messagebox.showinfo("Success", "Data updated successfully")
            self.clear_fields()
            self.btn_calculate.config(state=NORMAL)
            self.btn_clear.config(state=NORMAL)
            self.btn_delete.config(state=DISABLED)
            self.btn_save.config(state=NORMAL)   
            self.btn_update.config(state=DISABLED)
            self.btn_print.config(state=DISABLED)
            
        except Exception as ex:
        # Handle errors
          messagebox.showerror("Error", f'Error during data update: {str(ex)}')
          
          
          
    def delete_and_clear(self, var_emp_code):
        try:
            # Connect to the database
            con = pymysql.connect(host='localhost', user='root', passwd='', db='EMS')
            cur = con.cursor()
        
            # Execute SQL DELETE query to delete all data for the given primary key ID
            cur.execute("DELETE FROM amp_salary WHERE e_id=%s", (var_emp_code.get(),))
        
            # Commit the changes to the database
            con.commit()
        
            # Close the database connection
            con.close()
        
            # Display success message
            messagebox.showinfo("Success", "Data deleted successfully")
            
            # Clear all fields after deletion
            self.clear_fields()
            self.btn_calculate.config(state=NORMAL)
            self.btn_clear.config(state=NORMAL)
            self.btn_delete.config(state=DISABLED)
            self.btn_save.config(state=NORMAL)   
            self.btn_update.config(state=DISABLED)
            self.btn_print.config(state=DISABLED)
        
        except Exception as ex:
            # Handle errors
            messagebox.showerror("Error", f'Error during data deletion: {str(ex)}')
     
    def clear_fields(self):
    # Clear all input fields
         self.var_emp_code.set('')
         self.var_designation.set('')
         self.var_name.set('')
         self.var_age.set('')
         self.var_grnder.set('Select')
         self.var_email.set('')
         self.var_hr_location.set('')
         self.var_doj.set('')
         self.var_dob.set('')
         self.var_exp.set('')
         self.var_proof_id.set('')
         self.var_contact.set('')
         self.var_status.set('')
         self.txt_address.delete('1.0', 'end')
         self.var_month.set('')
         self.var_year.set('')
         self.var_salary.set('')
         self.var_t_days.set('')
         self.var_apsent.set('')
         self.var_medical.set('')
         self.var_convence.set('')
         self.var_net_salary.set('')
         self.var_pf.set('')
         self.txt_salary_receipt.delete('1.0', END)

    # Reset the sample text
         sample = '''\tCompany Name:system consultant Tech.\n\tAddress:Jalgaon
----------------------------------------------------------------------
Employee ID\t\t: 
Salary of\t\t:  Mon-YYYY
Generated On\t\t: DD-MM-YYYY
----------------------------------------------------------------------
Total Days\t\t: DD
Total Present\t\t: DD
Total Absent\t\t: DD
Convence\t\t: Rs.---
Medical\t\t: Rs.---
PF\t\t: Rs.---
Gross Payment\t\t: Rs.---
Net Salary\t\t" : Rs.---
---------------------------------------------------------------------
this is computer generator sleep, not 
require any signature
---------------------------------------------------------------------
'''
         self.txt_salary_receipt.insert(END, sample)
         self.btn_calculate.config(state=NORMAL)
         self.btn_clear.config(state=NORMAL)
         self.btn_delete.config(state=DISABLED)
         self.btn_save.config(state=NORMAL)   
         self.btn_update.config(state=DISABLED)
   
     
     
     
     
    def print_salary(self):
        try:
            # Prepare the receipt text
            receipt_text = f'''\tCompany Name:system consultant Tech.\n\tAddress:Jalgaon

    ----------------------------------------------------------------------
    Employee ID\t\t: {self.var_emp_code.get()}
    Salary of\t\t:  {self.var_month.get()}--{self.var_year.get()}
    Generated On\t\t: {datetime.now().strftime("%d-%m-%Y")}
    ----------------------------------------------------------------------
    Total Days\t\t: {self.var_t_days.get()}
    Total Present\t\t: {int(self.var_t_days.get()) - int(self.var_apsent.get())}
    Total Absent\t\t: {self.var_apsent.get()}
    Convence\t\t: Rs.{self.var_convence.get()}
    Medical\t\t: Rs.{self.var_medical.get()}
    PF\t\t: Rs.{self.var_pf.get()}
    Gross Payment\t\t: Rs.{self.var_salary.get()}
    Net Salary\t\t: Rs.{self.var_net_salary.get()}
    ---------------------------------------------------------------------
    This is a computer-generated slip, not 
    require any signature
    ---------------------------------------------------------------------'''

            # Prompt the user to choose a location to save the PDF file
            pdf_path = filedialog.asksaveasfilename(defaultextension=".pdf")
            if pdf_path:
                # Create PDF object
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", size=12)
                
                # Add receipt text to PDF
                pdf.multi_cell(0, 10, txt=receipt_text)
                
                # Save PDF to the selected location
                pdf.output(pdf_path)
                messagebox.showinfo("Success", "Receipt saved as PDF successfully!")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
     
     
     
  

root  = Tk()
obj = EmployeeSystem(root)
root.mainloop()
