from tkinter import*
from tkinter import ttk
import tkinter.messagebox
import pymysql
import random
import time
import mysql.connector
import pyodbc
from decimal import Decimal
from ataskaita import ataskaitos



conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=LAPTOP-EGR3M9P8\MSSQLSERVER01;"
    "Database=Knygynas;"
    "Trusted_Connection=yes;"
)

class DataEntryForm:
    def __init__(self, root):

        self.root = root
        self.root.title = ("Data Entry Form")
        self.root.geometry("1370x770+0+0")
        self.root.configure(background = 'gainsboro')

        Pirkejas_ID = IntVar()
        Vardas = StringVar()
        Pavarde = StringVar()
        Telefonas = StringVar()
        Kaina = DoubleVar()
        Kiekis = IntVar()
        Knygu_suma = DoubleVar()
        Pavadinimas = StringVar()
        Formatas = StringVar()
        Mokejimo_data = StringVar()
        Search = StringVar()
        DataDay = StringVar()
        Data_nuo = StringVar()
        Data_iki = StringVar()
        Kaina_nuo = DoubleVar()
        Kaina_iki = DoubleVar()

        MainFrame = Frame(self.root, bd = 10, width = 1350, height = 700, relief = RIDGE)
        MainFrame.grid()

        # TopFrame1 = Frame(MainFrame, bd = 5, width = 1340, height = 200, relief = RIDGE, bg ='cadet blue')
        # TopFrame1.grid(row = 0, column = 0)
        TopFrame2 = Frame(MainFrame, bd = 5, width = 1340, height = 50, relief = RIDGE, bg ='cadet blue')
        TopFrame2.grid(row = 1, column = 0)
        TopFrame3 = Frame(MainFrame, bd = 5, width = 1340, height = 300, relief = RIDGE, bg ='cadet blue')
        TopFrame3.grid(row = 2, column = 0)


        # InnerTopFrame1 = Frame(TopFrame1, bd = 5, width = 1330, height = 190, relief = RIDGE)
        # InnerTopFrame1.grid()
        InnerTopFrame2 = Frame(TopFrame2, bd = 5, width = 1330, height = 48, relief = RIDGE)
        InnerTopFrame2.grid()
        InnerTopFrame3 = Frame(TopFrame3, bd = 5, width = 1330, height = 280, relief = RIDGE)
        InnerTopFrame3.grid()
        InnerTopFrame4 = Frame(TopFrame2, bd = 5, width = 20, height = 40, relief = RIDGE)
        InnerTopFrame4.grid()


        #ataskaita

        

        # Mokejimo_data.set(time.strftime("%d/%m/%Y"))
        Mokejimo_data.set(time.strftime("%Y-%m-%d %H:%M:%S"))
        Data_nuo.set(time.strftime("2021-01-01"))
        Data_iki.set(time.strftime("%Y-%m-%d"))



        

        def Reset():

            Pirkejas_ID.set("")
            Vardas.set("")
            Pavarde.set("")
            Telefonas.set("")
            Kaina.set("")
            Kiekis.set("")
            Knygu_suma.set("")
            Pavadinimas.set("")
            Formatas.set("")
            Mokejimo_data.set("")
            Search.set("")
            DataDay.set("")
            Mokejimo_data.set("")
            Data_nuo.set("2021-01-01")
            Data_iki.set("")
            Kaina_nuo.set("")
            Kaina_iki.set("10000")
            

            Mokejimo_data.set(time.strftime("%Y-%m-%d %H:%M:%S"))
            #Data_nuo.set(time.strftime("%Y-%m-%d"))
            Data_iki.set(time.strftime("%Y-%m-%d"))

        def iExit():
            iExit = tkinter.messagebox.askyesno("Knygyno DB", "Patvirtinkite, kad norite uždaryti")
            if iExit > 0:
                root.destroy()
                return


        def prideti():
            if Pirkejas_ID.get() == 0 or Pirkejas_ID.get() == "":
                iExit = tkinter.messagebox.showerror("Knygyno DB", "ID Netinkamas!")
            elif Vardas.get() == "" or Pavarde.get() == "":
                iExit = tkinter.messagebox.showerror("Knygyno DB", "Vardas arba pavardė netinkami!")
            elif Telefonas.get() >= '37069999999' or Telefonas.get() <= '37060000000':
                iExit = tkinter.messagebox.showerror("Knygyno DB", "Neteisingai įvestas Telefono numeris!")
            elif Kaina.get() == 0 or Kaina.get() == "" or Kiekis.get() == 0 or Kiekis.get() == "" or Knygu_suma.get() == 0 or Knygu_suma.get() != (Kaina.get() * Kiekis.get()) or Knygu_suma.get() == "":
                iExit = tkinter.messagebox.showerror("Knygyno DB", "Kaina, kiekis arba knygų suma netinkami!")
            elif Pavadinimas.get() == "" or len(Formatas.get()) != 1:
                iExit = tkinter.messagebox.showerror("Knygyno DB", "Knygos pavadinimas arba formatas netinkami!")
            else:

                list = [Pirkejas_ID.get(), Vardas.get(), Pavarde.get(), Telefonas.get(), Kaina.get(), Kiekis.get(), Knygu_suma.get(), 
                  Pavadinimas.get(), Formatas.get(), Mokejimo_data.get()]
                tree_records.insert('', END, text='Listbox', values=list)
                tkinter.messagebox.showinfo("Knygyno DB", "Informacija pridėta!")

        def atsaukti():
            tkinter.messagebox.showinfo("Knygyno DB", "Įrašo pridėjimas atšauktas!")
            Reset()

        def addData():
            TopFrame1 = Frame(MainFrame, bd = 8, width = 1340, height = 200, relief = RIDGE, bg ='#000080')
            TopFrame1.grid(row = 0, column = 0)

            InnerTopFrame1 = Frame(TopFrame1, bd = 3, width = 1330, height = 190, relief = RIDGE)
            InnerTopFrame1.grid()

            lblClientID = Label(InnerTopFrame1, font = ('arial', 12, 'bold'), text = 'Pirkėjo ID', bd = 10)
            lblClientID.grid(row = 0, column = 0, sticky = W)
            txtlblClientID = Entry(InnerTopFrame1, font = ('arial', 12, 'bold'), bd = 5, width = 20, justify = 'left', textvariable = Pirkejas_ID)
            txtlblClientID.grid(row = 0, column = 1)

            lblLClientName = Label(InnerTopFrame1, font = ('arial', 12, 'bold'), text = 'Vardas', bd = 10)
            lblLClientName.grid(row = 1, column = 0, sticky = W)
            txtlblLClientName = Entry(InnerTopFrame1, font = ('arial', 12, 'bold'), bd = 5, width = 20, justify = 'left', textvariable = Vardas)
            txtlblLClientName.grid(row = 1, column = 1)

            lblClientLastName = Label(InnerTopFrame1, font = ('arial', 12, 'bold'), text = 'Pavardė', bd = 10)
            lblClientLastName.grid(row = 2, column = 0, sticky = W)
            txtlblClientLastName = Entry(InnerTopFrame1, font = ('arial', 12, 'bold'), bd = 5, width = 20, justify = 'left', textvariable = Pavarde)
            txtlblClientLastName.grid(row = 2, column = 1)

            lblClientTelephone = Label(InnerTopFrame1, font = ('arial', 12, 'bold'), text = 'Telefonas', bd = 10)
            lblClientTelephone.grid(row = 0, column = 2, sticky = W)
            txtlblClientTelephone = Entry(InnerTopFrame1, font = ('arial', 12, 'bold'), bd = 5, width = 20, justify = 'left', textvariable = Telefonas)
            txtlblClientTelephone.grid(row = 0, column = 3)

            lblBookPrice = Label(InnerTopFrame1, font = ('arial', 12, 'bold'), text = 'Kaina', bd = 10)
            lblBookPrice.grid(row = 2, column = 2, sticky = W)
            txtlblBookPrice = Entry(InnerTopFrame1, font = ('arial', 12, 'bold'), bd = 5, width = 20, justify = 'left', textvariable = Kaina)
            txtlblBookPrice.grid(row = 2, column = 3)

            lblBookAmount = Label(InnerTopFrame1, font = ('arial', 12, 'bold'), text = 'Kiekis', bd = 10)
            lblBookAmount.grid(row = 1, column = 2, sticky = W)
            self.cboBookAmount = ttk.Combobox(InnerTopFrame1, font = ('font', 12, 'bold'), width = 18, textvariable = Kiekis)
            self.cboBookAmount['value'] = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
            self.cboBookAmount.current(0)
            self.cboBookAmount.grid(row = 1, column = 3)

            # txtlblBookAmmount = Entry(InnerTopFrame1, font = ('arial', 12, 'bold'), bd = 5, width = 20, justify = 'left', textvariable = Kiekis)
            # txtlblBookAmmount.grid(row = 1, column = 3)

            lblFullPrice = Label(InnerTopFrame1, font = ('arial', 12, 'bold'), text = 'Knygų suma', bd = 10)
            lblFullPrice.grid(row = 0, column = 4, sticky = W)
            txtlblFullPrice = Entry(InnerTopFrame1, font = ('arial', 12, 'bold'), bd = 5, width = 20, justify = 'left', textvariable = Knygu_suma)
            txtlblFullPrice.grid(row = 0, column = 5)

            lblBookName = Label(InnerTopFrame1, font = ('arial', 12, 'bold'), text = 'Knygos pavadinimas', bd = 10)
            lblBookName.grid(row = 1, column = 4, sticky = W)
            txtlblBookName = Entry(InnerTopFrame1, font = ('arial', 12, 'bold'), bd = 5, width = 20, justify = 'left', textvariable = Pavadinimas)
            txtlblBookName.grid(row = 1, column = 5)

            lblBookFormat = Label(InnerTopFrame1, font = ('arial', 12, 'bold'), text = 'Formatas', bd = 10)
            lblBookFormat.grid(row = 2, column = 4, sticky = W)
            self.cboBookFormat = ttk.Combobox(InnerTopFrame1, font = ('font', 12, 'bold'), width = 18, textvariable = Formatas)
            self.cboBookFormat['value'] = ('', 'Spausdinta', 'Elektroninė')
            self.cboBookFormat.current(0)
            self.cboBookFormat.grid(row = 2, column = 5)

            lblPaymentDate = Label(InnerTopFrame1, font = ('arial', 12, 'bold'), text = 'Mokėjimo data', bd = 10)
            lblPaymentDate.grid(row = 0, column = 6, sticky = W)
            txtlblPaymentDate = Entry(InnerTopFrame1, font = ('arial', 12, 'bold'), bd = 5, width = 20, justify = 'left', textvariable = Mokejimo_data)
            txtlblPaymentDate.grid(row = 0, column = 7)

            # lblDateFrom = Label(InnerTopFrame1, font = ('arial', 12, 'bold'), text = 'Data nuo', bd = 10)
            # lblDateFrom.grid(row = 3, column = 0, sticky = W)
            # txtlblDateFrom = Entry(InnerTopFrame1, font = ('arial', 12, 'bold'), bd = 5, width = 10, justify = 'left', textvariable = Data_nuo)
            # txtlblDateFrom.grid(row = 3, column = 1)

            # lblDateTo = Label(InnerTopFrame1, font = ('arial', 12, 'bold'), text = 'iki', bd = 10)
            # lblDateTo.grid(row = 3, column = 2, sticky = E)
            # txtlblDateTo = Entry(InnerTopFrame1, font = ('arial', 12, 'bold'), bd = 5, width = 10, justify = 'left', textvariable = Data_iki)
            # txtlblDateTo.grid(row = 3, column = 3)

            # lblPriceFrom = Label(InnerTopFrame1, font = ('arial', 12, 'bold'), text = 'Kainų suma nuo', bd = 10)
            # lblPriceFrom.grid(row = 4, column = 0, sticky = W)
            # txtlblPriceFrom = Entry(InnerTopFrame1, font = ('arial', 12, 'bold'), bd = 5, width = 10, justify = 'left', textvariable = Kaina_nuo)
            # txtlblPriceFrom.grid(row = 4, column = 1)

            # lblPriceTo = Label(InnerTopFrame1, font = ('arial', 12, 'bold'), text = 'iki', bd = 10)
            # lblPriceTo.grid(row = 4, column = 2, sticky = E)
            # txtlblPriceTo = Entry(InnerTopFrame1, font = ('arial', 12, 'bold'), bd = 5, width = 10, justify = 'left', textvariable = Kaina_iki)
            # txtlblPriceTo.grid(row = 4, column = 3)

            # self.btnFilterDate = Button(InnerTopFrame1, pady = 1, bd = 1, font = ('arial', 8, 'bold'), width = 8, text = "Filtruoti", command = filterDate)
            # self.btnFilterDate.grid(row = 3, column = 4, padx = 2)

            # self.btnFilterSum = Button(InnerTopFrame1, pady = 1, bd = 1, font = ('arial', 8, 'bold'), width = 8, text = "Filtruoti", command = filterSum)
            # self.btnFilterSum.grid(row = 4, column = 4, padx = 2)

            self.btnAddYes = Button(InnerTopFrame1, pady = 1, bd = 1, font = ('arial', 8, 'bold'), width = 10, text = "Pridėti", bg = 'green', command = prideti)
            self.btnAddYes.grid(row = 4, column = 6, padx = 2)

            self.btnAddNo = Button(InnerTopFrame1, pady = 1, bd = 1, font = ('arial', 8, 'bold'), width = 10, text = "Atšaukti", bg = 'red', command = atsaukti)
            self.btnAddNo.grid(row = 4, column = 7, padx = 2)

            



            # if Pirkejas_ID.get() == 0 or Pirkejas_ID.get() == "":
            #     iExit = tkinter.messagebox.showerror("Knygyno DB", "ID Netinkamas!")
            # elif Vardas.get() == "" or Pavarde.get() == "":
            #     iExit = tkinter.messagebox.showerror("Knygyno DB", "Vardas arba pavardė netinkami!")
            # elif Telefonas.get() >= '37069999999' or Telefonas.get() <= '37060000000':
            #     iExit = tkinter.messagebox.showerror("Knygyno DB", "Neteisingai įvestas Telefono numeris!")
            # elif Kaina.get() == 0 or Kaina.get() == "" or Kiekis.get() == 0 or Kiekis.get() == "" or Knygu_suma.get() == 0 or Knygu_suma.get() != (Kaina.get() * Kiekis.get()) or Knygu_suma.get() == "":
            #     iExit = tkinter.messagebox.showerror("Knygyno DB", "Kaina, kiekis arba knygų suma netinkami!")
            # elif Pavadinimas.get() == "" or Formatas.get() != "S" or Formatas.get() == "E":
            #     iExit = tkinter.messagebox.showerror("Knygyno DB", "Knygos pavadinimas arba formatas netinkami!")
            # else:
            #     list = [Pirkejas_ID.get(), Vardas.get(), Pavarde.get(), Telefonas.get(), Kaina.get(), Kiekis.get(), Knygu_suma.get(), 
            #       Pavadinimas.get(), Formatas.get(), Mokejimo_data.get()]
            #     tree_records.insert('', END, text='Listbox', values=list)
            #     tkinter.messagebox.showinfo("Knygyno DB", "Informacija pridėta!")
            
        def LearnersInfo(ev):
            viewInfo = tree_records.focus()
            learnerData = tree_records.item(viewInfo)
            row = learnerData ['values']

            Pirkejas_ID.set(row[0])
            Vardas.set(row[1])
            Pavarde.set(row[2])
            Telefonas.set(row[3])
            Kaina.set(row[4])
            Kiekis.set(row[5])
            Knygu_suma.set(row[6])
            Pavadinimas.set(row[7])
            Formatas.set(row[8])
            Mokejimo_data.set(row[9])
            #Search.set(row[10])
            #DataDay.set(row[11])


        def changeY():
            list = [Pirkejas_ID.get(), Vardas.get(), Pavarde.get(), Telefonas.get(), Kaina.get(), Kiekis.get(), Knygu_suma.get(), 
                Pavadinimas.get(), Formatas.get(), Mokejimo_data.get()]

            selected_items = tree_records.selection()        
            for selected_item in selected_items:
                reallyUp = tkinter.messagebox.askyesno("Knygyno DB", "Patvirtinkite, kad norite pakeisti") 
            if reallyUp > 0:
                tree_records.delete(selected_item) # istrina
                tree_records.insert('', END, text='Listbox', values=list) #naujo pridejimas
                tkinter.messagebox.showinfo("Knygyno DB", "Informacija pakeista!")

        def changeN():
            tkinter.messagebox.showinfo("Knygyno DB", "Įrašo pridėjimas atšauktas!")
            Reset()

        def update():
            #---------------------------------------------------------------------
            TopFrame1 = Frame(MainFrame, bd = 8, width = 1340, height = 200, relief = RIDGE, bg ='#4B0082')
            TopFrame1.grid(row = 0, column = 0)

            InnerTopFrame1 = Frame(TopFrame1, bd = 3, width = 1330, height = 190, relief = RIDGE)
            InnerTopFrame1.grid()

            lblClientID = Label(InnerTopFrame1, font = ('arial', 12, 'bold'), text = 'Pirkėjo ID', bd = 10)
            lblClientID.grid(row = 0, column = 0, sticky = W)
            txtlblClientID = Entry(InnerTopFrame1, font = ('arial', 12, 'bold'), bd = 5, width = 20, justify = 'left', textvariable = Pirkejas_ID)
            txtlblClientID.grid(row = 0, column = 1)

            lblLClientName = Label(InnerTopFrame1, font = ('arial', 12, 'bold'), text = 'Vardas', bd = 10)
            lblLClientName.grid(row = 1, column = 0, sticky = W)
            txtlblLClientName = Entry(InnerTopFrame1, font = ('arial', 12, 'bold'), bd = 5, width = 20, justify = 'left', textvariable = Vardas)
            txtlblLClientName.grid(row = 1, column = 1)

            lblClientLastName = Label(InnerTopFrame1, font = ('arial', 12, 'bold'), text = 'Pavardė', bd = 10)
            lblClientLastName.grid(row = 2, column = 0, sticky = W)
            txtlblClientLastName = Entry(InnerTopFrame1, font = ('arial', 12, 'bold'), bd = 5, width = 20, justify = 'left', textvariable = Pavarde)
            txtlblClientLastName.grid(row = 2, column = 1)

            lblClientTelephone = Label(InnerTopFrame1, font = ('arial', 12, 'bold'), text = 'Telefonas', bd = 10)
            lblClientTelephone.grid(row = 0, column = 2, sticky = W)
            txtlblClientTelephone = Entry(InnerTopFrame1, font = ('arial', 12, 'bold'), bd = 5, width = 20, justify = 'left', textvariable = Telefonas)
            txtlblClientTelephone.grid(row = 0, column = 3)

            lblBookPrice = Label(InnerTopFrame1, font = ('arial', 12, 'bold'), text = 'Kaina', bd = 10)
            lblBookPrice.grid(row = 2, column = 2, sticky = W)
            txtlblBookPrice = Entry(InnerTopFrame1, font = ('arial', 12, 'bold'), bd = 5, width = 20, justify = 'left', textvariable = Kaina)
            txtlblBookPrice.grid(row = 2, column = 3)

            lblBookAmount = Label(InnerTopFrame1, font = ('arial', 12, 'bold'), text = 'Kiekis', bd = 10)
            lblBookAmount.grid(row = 1, column = 2, sticky = W)
            self.cboBookAmount = ttk.Combobox(InnerTopFrame1, font = ('font', 12, 'bold'), width = 18, textvariable = Kiekis)
            self.cboBookAmount['value'] = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
            self.cboBookAmount.current(0)
            self.cboBookAmount.grid(row = 1, column = 3)

            # txtlblBookAmmount = Entry(InnerTopFrame1, font = ('arial', 12, 'bold'), bd = 5, width = 20, justify = 'left', textvariable = Kiekis)
            # txtlblBookAmmount.grid(row = 1, column = 3)

            lblFullPrice = Label(InnerTopFrame1, font = ('arial', 12, 'bold'), text = 'Knygų suma', bd = 10)
            lblFullPrice.grid(row = 0, column = 4, sticky = W)
            txtlblFullPrice = Entry(InnerTopFrame1, font = ('arial', 12, 'bold'), bd = 5, width = 20, justify = 'left', textvariable = Knygu_suma)
            txtlblFullPrice.grid(row = 0, column = 5)

            lblBookName = Label(InnerTopFrame1, font = ('arial', 12, 'bold'), text = 'Knygos pavadinimas', bd = 10)
            lblBookName.grid(row = 1, column = 4, sticky = W)
            txtlblBookName = Entry(InnerTopFrame1, font = ('arial', 12, 'bold'), bd = 5, width = 20, justify = 'left', textvariable = Pavadinimas)
            txtlblBookName.grid(row = 1, column = 5)

            lblBookFormat = Label(InnerTopFrame1, font = ('arial', 12, 'bold'), text = 'Formatas', bd = 10)
            lblBookFormat.grid(row = 2, column = 4, sticky = W)
            self.cboBookFormat = ttk.Combobox(InnerTopFrame1, font = ('font', 12, 'bold'), width = 18, textvariable = Formatas)
            self.cboBookFormat['value'] = ('', 'Spasudinta', 'Elektroninė')
            self.cboBookFormat.current(0)
            self.cboBookFormat.grid(row = 2, column = 5)

            lblPaymentDate = Label(InnerTopFrame1, font = ('arial', 12, 'bold'), text = 'Mokėjimo data', bd = 10)
            lblPaymentDate.grid(row = 0, column = 6, sticky = W)
            txtlblPaymentDate = Entry(InnerTopFrame1, font = ('arial', 12, 'bold'), bd = 5, width = 20, justify = 'left', textvariable = Mokejimo_data)
            txtlblPaymentDate.grid(row = 0, column = 7)

            self.btnChangeYes = Button(InnerTopFrame1, pady = 1, bd = 1, font = ('arial', 8, 'bold'), width = 10, text = "Pakeisti", bg = 'green', command = changeY)
            self.btnChangeYes.grid(row = 4, column = 6, padx = 2)

            self.btnChangeNo = Button(InnerTopFrame1, pady = 1, bd = 1, font = ('arial', 8, 'bold'), width = 10, text = "Atšaukti", bg = 'red', command = changeN)
            self.btnChangeNo.grid(row = 4, column = 7, padx = 2)

            #---------------------------------------------------------------------

            list = [Pirkejas_ID.get(), Vardas.get(), Pavarde.get(), Telefonas.get(), Kaina.get(), Kiekis.get(), Knygu_suma.get(), 
                  Pavadinimas.get(), Formatas.get(), Mokejimo_data.get()]

            # selected_items = tree_records.selection()        
            # for selected_item in selected_items:
            #     reallyUp = tkinter.messagebox.askyesno("Knygyno DB", "Patvirtinkite, kad norite pakeisti") 
            # if reallyUp > 0:
            #     tree_records.delete(selected_item) # istrina
            #     tree_records.insert('', END, text='Listbox', values=list) #naujo pridejimas
            #     tkinter.messagebox.showinfo("Knygyno DB", "Informacija pakeista!")

        def delete():
            selected_items = tree_records.selection()
            print (tree_records.selection())        
            for selected_item in selected_items:          
                really = tkinter.messagebox.askyesno("Knygyno DB", "Patvirtinkite, kad norite ištrinti")
            if really > 0:
                tree_records.delete(selected_item)
                tkinter.messagebox.showinfo("Knygyno DB", "Informacija ištrinta!")

        def displayData():
            conn = pyodbc.connect(
                "Driver={SQL Server Native Client 11.0};"
                "Server=LAPTOP-EGR3M9P8\MSSQLSERVER01;"
                "Database=Knygynas;"
                "Trusted_Connection=yes;"
            )
            cur = conn.cursor()
            cur.execute("""SELECT cast(Pirkejas.Pirkejas_ID as int), Pirkejas.Vardas, Pirkejas.Pavarde, cast(Pirkejas.Telefonas as BIGINT), cast(Perka.Kaina as float), Perka.Kiekis, 
                            cast(Perka.Kaina * Perka.Kiekis as float) AS Knygu_suma, Kurinys.Pavadinimas, Knyga.Formatas, cast(Krepselis.Mokejimo_data AS smalldatetime)
                        FROM Pirkejas, Krepselis, Perka, Knyga, Leidinys, Kurinys
                        WHERE Pirkejas.Pirkejas_ID = Krepselis.Pirkejas_ID
                          AND Krepselis.Mokejimas_ID = Perka.Mokejimas_ID
                          AND Perka.Knyga_ID = Knyga.Knyga_ID
                          AND Knyga.Leidinys_ID = Leidinys.Leidinys_ID
                          AND Leidinys.Kurinys_ID = Kurinys.Kurinys_ID
                        ORDER BY Krepselis.Mokejimas_ID""")
            result = cur.fetchall()
            if len(result) != 0:
                for row in result:
                    list = [elem for elem in row]
                    tree_records.insert('', END, text='Listbox', values=list)
                    conn.commit()
                conn.close()
            #-----------------------------
            # i = 0
            # for row in result:
            #     for j in range(len(row)):
            #         tree_records = Entry(root, width=10, fg='blue')
            #         tree_records.insert(END, row[j])
            #         conn.commit()
            #     i += 1
            # root.mainloop()
            #-----------------------------
            # insertObject = []
            # columnNames = [column[0] for column in cur.description]
            
            # for row in result:
            #     tree_records.insert( dict( zip ( columnNames, row)), END, text='Listbox',)


        def ataskaita():
            ataskaitos()


        def filterDate():
            for child in tree_records.get_children():
                if not (Data_nuo.get() <= tree_records.item(child)["values"][9] <= Data_iki.get()):
                    tree_records.delete(child)
            
        def filterSum():
            for child in tree_records.get_children():
                if not (Kaina_nuo.get() <= float(tree_records.item(child)["values"][6]) <= Kaina_iki.get()):
                    tree_records.delete(child)

        def filterIt():

            InnerTopFrame6 = Frame(TopFrame2, bd = 5, width = 20, height = 40, relief = RIDGE)
            InnerTopFrame6.grid()

            lblDateFrom = Label(InnerTopFrame6, font = ('arial', 12, 'bold'), text = 'Data nuo', bd = 10)
            lblDateFrom.grid(row = 0, column = 4, sticky = W)
            txtlblDateFrom = Entry(InnerTopFrame6, font = ('arial', 12, 'bold'), bd = 5, width = 10, justify = 'left', textvariable = Data_nuo)
            txtlblDateFrom.grid(row = 0, column = 5)

            lblDateTo = Label(InnerTopFrame6, font = ('arial', 12, 'bold'), text = 'iki', bd = 10)
            lblDateTo.grid(row = 0, column = 6, sticky = E)
            txtlblDateTo = Entry(InnerTopFrame6, font = ('arial', 12, 'bold'), bd = 5, width = 10, justify = 'left', textvariable = Data_iki)
            txtlblDateTo.grid(row = 0, column = 7)

            lblPriceFrom = Label(InnerTopFrame6, font = ('arial', 12, 'bold'), text = 'Kainų suma nuo', bd = 10)
            lblPriceFrom.grid(row = 1, column = 4, sticky = W)
            txtlblPriceFrom = Entry(InnerTopFrame6, font = ('arial', 12, 'bold'), bd = 5, width = 10, justify = 'left', textvariable = Kaina_nuo)
            txtlblPriceFrom.grid(row = 1, column = 5)

            lblPriceTo = Label(InnerTopFrame6, font = ('arial', 12, 'bold'), text = 'iki', bd = 10)
            lblPriceTo.grid(row = 1, column = 6, sticky = E)
            txtlblPriceTo = Entry(InnerTopFrame6, font = ('arial', 12, 'bold'), bd = 5, width = 10, justify = 'left', textvariable = Kaina_iki)
            txtlblPriceTo.grid(row = 1, column = 7)

            self.btnFilterDate = Button(InnerTopFrame6, pady = 1, bd = 1, font = ('arial', 8, 'bold'), width = 8, text = "Filtruoti", command = filterDate)
            self.btnFilterDate.grid(row = 0, column = 8, padx = 2)

            self.btnFilterSum = Button(InnerTopFrame6, pady = 1, bd = 1, font = ('arial', 8, 'bold'), width = 8, text = "Filtruoti", command = filterSum)
            self.btnFilterSum.grid(row = 1, column = 8, padx = 2)



    #==================================================Widget==================================
        # lblClientID = Label(InnerTopFrame1, font = ('arial', 12, 'bold'), text = 'Pirkėjo ID', bd = 10)
        # lblClientID.grid(row = 0, column = 0, sticky = W)
        # txtlblClientID = Entry(InnerTopFrame1, font = ('arial', 12, 'bold'), bd = 5, width = 20, justify = 'left', textvariable = Pirkejas_ID)
        # txtlblClientID.grid(row = 0, column = 1)

        # lblLClientName = Label(InnerTopFrame1, font = ('arial', 12, 'bold'), text = 'Vardas', bd = 10)
        # lblLClientName.grid(row = 1, column = 0, sticky = W)
        # txtlblLClientName = Entry(InnerTopFrame1, font = ('arial', 12, 'bold'), bd = 5, width = 20, justify = 'left', textvariable = Vardas)
        # txtlblLClientName.grid(row = 1, column = 1)

        # lblClientLastName = Label(InnerTopFrame1, font = ('arial', 12, 'bold'), text = 'Pavardė', bd = 10)
        # lblClientLastName.grid(row = 2, column = 0, sticky = W)
        # txtlblClientLastName = Entry(InnerTopFrame1, font = ('arial', 12, 'bold'), bd = 5, width = 20, justify = 'left', textvariable = Pavarde)
        # txtlblClientLastName.grid(row = 2, column = 1)

        # lblClientTelephone = Label(InnerTopFrame1, font = ('arial', 12, 'bold'), text = 'Telefonas', bd = 10)
        # lblClientTelephone.grid(row = 0, column = 2, sticky = W)
        # txtlblClientTelephone = Entry(InnerTopFrame1, font = ('arial', 12, 'bold'), bd = 5, width = 20, justify = 'left', textvariable = Telefonas)
        # txtlblClientTelephone.grid(row = 0, column = 3)

        # lblBookPrice = Label(InnerTopFrame1, font = ('arial', 12, 'bold'), text = 'Kaina', bd = 10)
        # lblBookPrice.grid(row = 2, column = 2, sticky = W)
        # txtlblBookPrice = Entry(InnerTopFrame1, font = ('arial', 12, 'bold'), bd = 5, width = 20, justify = 'left', textvariable = Kaina)
        # txtlblBookPrice.grid(row = 2, column = 3)

        # lblBookAmount = Label(InnerTopFrame1, font = ('arial', 12, 'bold'), text = 'Kiekis', bd = 10)
        # lblBookAmount.grid(row = 1, column = 2, sticky = W)
        # self.cboBookAmount = ttk.Combobox(InnerTopFrame1, font = ('font', 12, 'bold'), width = 18, textvariable = Kiekis)
        # self.cboBookAmount['value'] = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
        # self.cboBookAmount.current(0)
        # self.cboBookAmount.grid(row = 1, column = 3)

        # # txtlblBookAmmount = Entry(InnerTopFrame1, font = ('arial', 12, 'bold'), bd = 5, width = 20, justify = 'left', textvariable = Kiekis)
        # # txtlblBookAmmount.grid(row = 1, column = 3)

        # lblFullPrice = Label(InnerTopFrame1, font = ('arial', 12, 'bold'), text = 'Knygų suma', bd = 10)
        # lblFullPrice.grid(row = 0, column = 4, sticky = W)
        # txtlblFullPrice = Entry(InnerTopFrame1, font = ('arial', 12, 'bold'), bd = 5, width = 20, justify = 'left', textvariable = Knygu_suma)
        # txtlblFullPrice.grid(row = 0, column = 5)

        # lblBookName = Label(InnerTopFrame1, font = ('arial', 12, 'bold'), text = 'Knygos pavadinimas', bd = 10)
        # lblBookName.grid(row = 1, column = 4, sticky = W)
        # txtlblBookName = Entry(InnerTopFrame1, font = ('arial', 12, 'bold'), bd = 5, width = 20, justify = 'left', textvariable = Pavadinimas)
        # txtlblBookName.grid(row = 1, column = 5)

        # lblBookFormat = Label(InnerTopFrame1, font = ('arial', 12, 'bold'), text = 'Formatas', bd = 10)
        # lblBookFormat.grid(row = 2, column = 4, sticky = W)
        # self.cboBookFormat = ttk.Combobox(InnerTopFrame1, font = ('font', 12, 'bold'), width = 18, textvariable = Formatas)
        # self.cboBookFormat['value'] = ('', 'S', 'E')
        # self.cboBookFormat.current(0)
        # self.cboBookFormat.grid(row = 2, column = 5)

        # lblPaymentDate = Label(InnerTopFrame1, font = ('arial', 12, 'bold'), text = 'Mokėjimo data', bd = 10)
        # lblPaymentDate.grid(row = 0, column = 6, sticky = W)
        # txtlblPaymentDate = Entry(InnerTopFrame1, font = ('arial', 12, 'bold'), bd = 5, width = 20, justify = 'left', textvariable = Mokejimo_data)
        # txtlblPaymentDate.grid(row = 0, column = 7)

        # lblDateFrom = Label(InnerTopFrame1, font = ('arial', 12, 'bold'), text = 'Data nuo', bd = 10)
        # lblDateFrom.grid(row = 3, column = 0, sticky = W)
        # txtlblDateFrom = Entry(InnerTopFrame1, font = ('arial', 12, 'bold'), bd = 5, width = 10, justify = 'left', textvariable = Data_nuo)
        # txtlblDateFrom.grid(row = 3, column = 1)

        # lblDateTo = Label(InnerTopFrame1, font = ('arial', 12, 'bold'), text = 'iki', bd = 10)
        # lblDateTo.grid(row = 3, column = 2, sticky = E)
        # txtlblDateTo = Entry(InnerTopFrame1, font = ('arial', 12, 'bold'), bd = 5, width = 10, justify = 'left', textvariable = Data_iki)
        # txtlblDateTo.grid(row = 3, column = 3)

        # lblPriceFrom = Label(InnerTopFrame1, font = ('arial', 12, 'bold'), text = 'Kainų suma nuo', bd = 10)
        # lblPriceFrom.grid(row = 4, column = 0, sticky = W)
        # txtlblPriceFrom = Entry(InnerTopFrame1, font = ('arial', 12, 'bold'), bd = 5, width = 10, justify = 'left', textvariable = Kaina_nuo)
        # txtlblPriceFrom.grid(row = 4, column = 1)

        # lblPriceTo = Label(InnerTopFrame1, font = ('arial', 12, 'bold'), text = 'iki', bd = 10)
        # lblPriceTo.grid(row = 4, column = 2, sticky = E)
        # txtlblPriceTo = Entry(InnerTopFrame1, font = ('arial', 12, 'bold'), bd = 5, width = 10, justify = 'left', textvariable = Kaina_iki)
        # txtlblPriceTo.grid(row = 4, column = 3)


        
#==========================================================================================================================================================

        scroll_x = Scrollbar(InnerTopFrame3, orient = HORIZONTAL)
        scroll_y = Scrollbar(InnerTopFrame3, orient = VERTICAL)

        scroll_x.pack(side = BOTTOM, fill = X)
        scroll_y.pack(side = RIGHT, fill = Y)

        #Tables

        tree_records = ttk.Treeview(InnerTopFrame3, height = 20, columns = ("Pirkejas.Pirkejas_ID", "Pirkejas.Vardas", "Pirkejas.Pavarde", "Pirkejas.Telefonas", 
        "Perka.Kaina", "Perka.Kiekis", "Knygu_suma", "Kurinys.Pavadinimas", "Knyga.Formatas", "Krepselis.Mokejimo_data"), xscrollcommand = scroll_x.set, yscrollcommand = scroll_y.set)



        tree_records.heading("Pirkejas.Pirkejas_ID", text = "P_ID")
        tree_records.heading("Pirkejas.Vardas", text = "P_vardas")
        tree_records.heading("Pirkejas.Pavarde", text = "P_pavardė")
        tree_records.heading("Pirkejas.Telefonas", text = "Tel. nr.")
        tree_records.heading("Perka.Kaina", text = "Kaina")
        tree_records.heading("Perka.Kiekis", text = "Kiekis")
        tree_records.heading("Knygu_suma", text = "Knygų suma")
        tree_records.heading("Kurinys.Pavadinimas", text = "Knygos pavadinimas")
        tree_records.heading("Knyga.Formatas", text = "Formatas")
        tree_records.heading("Krepselis.Mokejimo_data", text = "Mokėjimo data")

        tree_records['show'] = "headings"

        tree_records.column("Pirkejas.Pirkejas_ID", width = 40, anchor = tkinter.W)
        tree_records.column("Pirkejas.Vardas", width = 80, anchor = tkinter.W)
        tree_records.column("Pirkejas.Pavarde", width = 80, anchor = tkinter.W)
        tree_records.column("Pirkejas.Telefonas", width = 80, anchor = tkinter.CENTER)
        tree_records.column("Perka.Kaina", width = 80, anchor = tkinter.CENTER)
        tree_records.column("Perka.Kiekis", width = 60, anchor = tkinter.CENTER)
        tree_records.column("Knygu_suma", width = 100, anchor = tkinter.CENTER)
        tree_records.column("Kurinys.Pavadinimas", width = 200, anchor = tkinter.CENTER)
        tree_records.column("Knyga.Formatas", width = 100, anchor = tkinter.CENTER)
        tree_records.column("Krepselis.Mokejimo_data", width = 200, anchor = tkinter.CENTER)

        tree_records.pack(fill = BOTH, expand = 1)
        tree_records.bind("<ButtonRelease-1>", LearnersInfo)
        #tree_records.bind("<ButtonRelease-2", searchDB)
        


#==========================================================================================================================================================


        self.btnAddNew = Button(InnerTopFrame2, pady = 1, bd = 4, font = ('arial', 16, 'bold'), width = 13, text = "Pridėti naują", command = addData, foreground="#000080")
        self.btnAddNew.grid(row = 0, column = 0, padx = 3)

        self.btnDisplay = Button(InnerTopFrame2, pady = 1, bd = 4, font = ('arial', 16, 'bold'), width = 13, text = "Įrašų rodymas", command = displayData)
        self.btnDisplay.grid(row = 0, column = 1, padx = 3)

        self.btnUpdate = Button(InnerTopFrame2, pady = 1, bd = 4, font = ('arial', 16, 'bold'), width = 13, text = "Pakeisti", command = update, foreground="#4B0082")
        self.btnUpdate.grid(row = 0, column = 2, padx = 3)

        self.btnDelete = Button(InnerTopFrame2, pady = 1, bd = 4, font = ('arial', 16, 'bold'), width = 13, text = "Ištrinti", command = delete)
        self.btnDelete.grid(row = 0, column = 3, padx = 3)

        # self.btnReset = Button(InnerTopFrame2, pady = 1, bd = 4, font = ('arial', 16, 'bold'), width = 13, text = "Išvalyti formą", command = Reset)
        # self.btnReset.grid(row = 0, column = 4, padx = 3)

        self.btnAddExit = Button(InnerTopFrame2, pady = 1, bd = 4, font = ('arial', 16, 'bold'), width = 13, text = "Išeiti", command = iExit)
        self.btnAddExit.grid(row = 0, column = 5, padx = 3)

        self.btnSearch = Button(InnerTopFrame4, pady = 6, bd = 6, font = ('Times', 16, 'bold'), width = 13, text = "Ataskaita", command = ataskaita)
        self.btnSearch.grid(row = 0, column = 3, padx = 3)

        self.btnFilter = Button(InnerTopFrame2, pady = 1, bd = 4, font = ('arial', 16, 'bold'), width = 13, text = "Filtravimas", command = filterIt)
        self.btnFilter.grid(row = 0, column = 4, padx = 3)


        


if __name__ == '__main__':
    root = Tk(className='Knygynas')
    application = DataEntryForm(root)
    root.mainloop()