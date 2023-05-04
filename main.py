from distutils.version import Version
import stat
from textwrap import fill
from turtle import bgcolor
import baseDeDatos
import os
import tkinter as tk
from tkinter import BOTH, LEFT, font,ttk
from datetime import datetime
from datetime import date
from tkinter import messagebox
#Creacion de base de datos, si exite no la crea
def borrar():
    if Tabla.selection():
        if messagebox.askyesno(message="¿Desea Borrar elemento?", title="Borrar elemento"):
            for item in Tabla.selection():
                print(Tabla.item(item,"values"))
                Nombre=Tabla.item(item,"values")[0]
                Modelo=Tabla.item(item,"values")[1]
                Version=Tabla.item(item,"values")[2]
                Precio=Tabla.item(item,"values")[3]
                Fcha=Tabla.item(item,"values")[4]
                Total=Tabla.item(item,"values")[5]
                Estado=Tabla.item(item,"values")[6]

            baseDeDatos.deleteRow(Nombre)
            Buscar()
    else:
        messagebox.showwarning(message="Debe seleccionar un elemento de la tabla para editar",title="Editar elemento")
def editar2():
    if Tabla.selection():
        for item in Tabla.selection():
            print(Tabla.item(item,"values"))
            Nombre=Tabla.item(item,"values")[0]
            Modelo=Tabla.item(item,"values")[1]
            Version=Tabla.item(item,"values")[2]
            Precio=Tabla.item(item,"values")[3]
            Fcha=Tabla.item(item,"values")[4]
            Total=Tabla.item(item,"values")[5]
            Estado=Tabla.item(item,"values")[6]

        RaizCargar2=tk.Toplevel(RaizPrincipal)
        RaizCargar2.resizable(0,0)
        FrameCargar2=ttk.Frame(RaizCargar2)
        FrameCargar2.grid(column=0,row=0,padx=10,pady=10)
        #Labels de carga
        Nombre2Label=tk.Label(FrameCargar2,text="Nombre",font=font.Font(family="Times",size=14,weight=font.BOLD))
        
        Nombre2Label.grid(row=0,column=0)
        Mode2Label=tk.Label(FrameCargar2,text="Modelo",font=font.Font(family="Times",size=14,weight=font.BOLD))
        Mode2Label.grid(row=1,column=0)
        Version2Label=tk.Label(FrameCargar2,text="Version",font=font.Font(family="Times",size=14,weight=font.BOLD))
        Version2Label.grid(row=2,column=0)
        Precio2Label=tk.Label(FrameCargar2,text="Precio",font=font.Font(family="Times",size=14,weight=font.BOLD))
        Precio2Label.grid(row=3,column=0)
        Fecha2Label=tk.Label(FrameCargar2,text="Fecha",font=font.Font(family="Times",size=14,weight=font.BOLD))
        Fecha2Label.grid(row=4,column=0)
        Total2Label=tk.Label(FrameCargar2,text="Total",font=font.Font(family="Times",size=14,weight=font.BOLD))
        Total2Label.grid(row=5,column=0)
        Estado2Label=tk.Label(FrameCargar2,text="Estado",font=font.Font(family="Times",size=14,weight=font.BOLD))
        Estado2Label.grid(row=6,column=0)
        #Entry de carga
        Nombre2Entry=tk.Entry(FrameCargar2,font=font.Font(family="Times",size=14))
        Nombre2Entry.insert(0,Nombre)
        
        Nombre2Entry.grid(row=0,column=1,padx=5)
        Mode2Entry=tk.Entry(FrameCargar2,font=font.Font(family="Times",size=14))
        Mode2Entry.insert(0,Modelo)
        
        Mode2Entry.grid(row=1,column=1,padx=5)
        Version2Entry=tk.Entry(FrameCargar2,font=font.Font(family="Times",size=14))
        Version2Entry.grid(row=2,column=1,padx=5)
        Version2Entry.insert(0,Version)
        Precio2Entry=tk.Entry(FrameCargar2,font=font.Font(family="Times",size=14))
        Precio2Entry.grid(row=3,column=1,padx=5)
        Precio2Entry.insert(0,Precio)
        Fecha2Entry=tk.Entry(FrameCargar2,font=font.Font(family="Times",size=14))
        Fecha2Entry.insert(0,Fecha)
        
        Fecha2Entry.grid(row=4,column=1,padx=5)

        Total2Entry=tk.Entry(FrameCargar2,font=font.Font(family="Times",size=14))
        Total2Entry.grid(row=5,column=1,padx=5)
        Total2Entry.insert(0,Total)
        Estado2Entry=tk.Entry(FrameCargar2,font=font.Font(family="Times",size=14))
        Estado2Entry.insert(0,Estado)
        Estado2Entry.grid(row=6,column=1,padx=5)
        Boton2Cargar=tk.Button(FrameCargar2,text="Editar",font=font.Font(family="Times",size=14),width=30,bg="#E3B1F2",borderwidth=5,command=lambda:actualizar())
        Boton2Cargar.grid(row=7,column=0,columnspan=2,pady=10)
        def actualizar():
            baseDeDatos.updateFields("Nombre",Nombre,Nombre2Entry.get())
            baseDeDatos.updateFields("Modelo",Nombre,Mode2Entry.get())
            baseDeDatos.updateFields("Versión",Nombre,Version2Entry.get())
            baseDeDatos.updateFields("Precio",Nombre,Precio2Entry.get())
            baseDeDatos.updateFields("Fecha",Nombre,Fecha2Entry.get())
            baseDeDatos.updateFields("Total",Nombre,Total2Entry.get())
            baseDeDatos.updateFields("Estado",Nombre,Estado2Entry.get())
            
            RaizCargar2.destroy()
            Buscar()
    else:
        messagebox.showwarning(message="Debe seleccionar un elemento de la tabla para editar",title="Editar elemento") 
def editar(event):
    
    for item in Tabla.selection():
        print(Tabla.item(item,"values"))
        Nombre=Tabla.item(item,"values")[0]
        Modelo=Tabla.item(item,"values")[1]
        Version=Tabla.item(item,"values")[2]
        Precio=Tabla.item(item,"values")[3]
        Fcha=Tabla.item(item,"values")[4]
        Total=Tabla.item(item,"values")[5]
        Estado=Tabla.item(item,"values")[6]

    RaizCargar2=tk.Toplevel(RaizPrincipal)
    RaizCargar2.resizable(0,0)
    FrameCargar2=ttk.Frame(RaizCargar2)
    FrameCargar2.grid(column=0,row=0,padx=10,pady=10)
    #Labels de carga
    Nombre2Label=tk.Label(FrameCargar2,text="Nombre",font=font.Font(family="Times",size=14,weight=font.BOLD))
    
    Nombre2Label.grid(row=0,column=0)
    Mode2Label=tk.Label(FrameCargar2,text="Modelo",font=font.Font(family="Times",size=14,weight=font.BOLD))
    Mode2Label.grid(row=1,column=0)
    Version2Label=tk.Label(FrameCargar2,text="Version",font=font.Font(family="Times",size=14,weight=font.BOLD))
    Version2Label.grid(row=2,column=0)
    Precio2Label=tk.Label(FrameCargar2,text="Precio",font=font.Font(family="Times",size=14,weight=font.BOLD))
    Precio2Label.grid(row=3,column=0)
    Fecha2Label=tk.Label(FrameCargar2,text="Fecha",font=font.Font(family="Times",size=14,weight=font.BOLD))
    Fecha2Label.grid(row=4,column=0)
    Total2Label=tk.Label(FrameCargar2,text="Total",font=font.Font(family="Times",size=14,weight=font.BOLD))
    Total2Label.grid(row=5,column=0)
    Estado2Label=tk.Label(FrameCargar2,text="Estado",font=font.Font(family="Times",size=14,weight=font.BOLD))
    Estado2Label.grid(row=6,column=0)
    #Entry de carga
    Nombre2Entry=tk.Entry(FrameCargar2,font=font.Font(family="Times",size=14))
    Nombre2Entry.insert(0,Nombre)
    Nombre2Entry.config(state="disable")
    Nombre2Entry.grid(row=0,column=1,padx=5)
    Mode2Entry=tk.Entry(FrameCargar2,font=font.Font(family="Times",size=14))
    Mode2Entry.insert(0,Modelo)
    Mode2Entry.config(state="disable")
    Mode2Entry.grid(row=1,column=1,padx=5)
    Version2Entry=tk.Entry(FrameCargar2,font=font.Font(family="Times",size=14),state="disable")
    Version2Entry.grid(row=2,column=1,padx=5)
    Precio2Entry=tk.Entry(FrameCargar2,font=font.Font(family="Times",size=14),state="disable")
    Precio2Entry.grid(row=3,column=1,padx=5)
    Fecha2Entry=tk.Entry(FrameCargar2,font=font.Font(family="Times",size=14))
    Fecha2Entry.insert(0,Fecha)
    Fecha2Entry.config(state="disable")
    Fecha2Entry.grid(row=4,column=1,padx=5)
    Total2Entry=tk.Entry(FrameCargar2,font=font.Font(family="Times",size=14),state="disable")
    Total2Entry.grid(row=5,column=1,padx=5)
    Estado2Entry=tk.Entry(FrameCargar2,font=font.Font(family="Times",size=14))
    Estado2Entry.insert(0,Estado)
    Estado2Entry.grid(row=6,column=1,padx=5)
    Boton2Cargar=tk.Button(FrameCargar2,text="Actualizar",font=font.Font(family="Times",size=14),width=30,bg="#5EC8C4",fg="#FFFFFF",borderwidth=5,command=lambda:actualizar())
    Boton2Cargar.grid(row=7,column=0,columnspan=2,pady=10)
    def actualizar():
        baseDeDatos.updateField(Nombre,Estado2Entry.get())
        RaizCargar2.destroy()
if os.path.exists('StockPlacas.db'):
    pass
else:
    
    baseDeDatos.crearDb()
    baseDeDatos.createTabla()
color=("red","green")
F= datetime.now()
Fecha=str(F.day)+"-"+str(F.month)+"-"+str(F.year)
print(Fecha)
RaizPrincipal = tk.Tk()
RaizPrincipal.title("Control de placas")
RaizPrincipal.resizable(0,0)
#Contenedor de Boton y texto de busqueda
FramePrincipal=ttk.Frame(RaizPrincipal, width=1200,height=100)
FramePrincipal.pack()
LabelModelo=tk.Label(FramePrincipal,font=font.Font(family="Times",size=18),text="Modelo:")
LabelModelo.grid(row=0,column=0)
EntryBusqueda=ttk.Entry(FramePrincipal, font=font.Font(family="Times",size=20))
EntryBusqueda.grid(row=0,column=1,padx=20)
BotonBusqueda=tk.Button(FramePrincipal,text="Buscar",bg="#5ACD8C",width=20,fg="#FFFFFF",font=font.Font(family="Times",size=14,weight=font.BOLD),borderwidth=5,command=lambda:Buscar())
BotonBusqueda.grid(row=0,column=2,padx=100,pady=10)
BotonCarga=tk.Button(FramePrincipal,text="+",width=3,font=font.Font(family="Times",size=14,weight=font.BOLD),borderwidth=5,command=lambda:Cargar(),fg="#FFFFFF",bg="Darkblue")
BotonCarga.grid(row=0,column=3)
BotonEditar=tk.Button(FramePrincipal,text="E",width=3,font=font.Font(family="Times",size=14,weight=font.BOLD),borderwidth=5,command=lambda:editar2(),bg="#E3B1F2")
BotonEditar.grid(row=0,column=4,padx=10)
BotonBorrar=tk.Button(FramePrincipal,text="-",width=3,font=font.Font(family="Times",size=14,weight=font.BOLD),borderwidth=5,command=lambda:borrar(),bg="#F96262")
BotonBorrar.grid(row=0,column=5)
#Contenedor de Tabla 
FrameTabla=ttk.Frame(RaizPrincipal,width=1200,height=600)
FrameTabla.pack()
columnas=("Nombre","Modelo","Version","Precio","Fecha","Total","Estado")
Tabla=ttk.Treeview(FrameTabla,height=18,show="headings",columns=columnas)
Tabla.column("Nombre", width=200,anchor="center")
Tabla.column("Modelo", width=300,anchor="center")
Tabla.column("Version", width=100,anchor="center")
Tabla.column("Precio", width=100,anchor="center")
Tabla.column("Fecha", width=100,anchor="center")
Tabla.column("Total", width=100,anchor="center")
Tabla.column("Estado", width=100,anchor="center")

Tabla.heading("Nombre",text="Nombre")
Tabla.heading("Modelo",text="Modelo")
Tabla.heading("Version",text="Version")
Tabla.heading("Precio",text="Precio")
Tabla.heading("Fecha",text="Fecha")
Tabla.heading("Total",text="Total")
Tabla.heading("Estado",text="Estado")

Tabla.pack(side=LEFT,fill=BOTH,pady=10,padx=20)
Tabla.bind('<Double-1>', editar)

def Cargar():
    RaizCargar=tk.Toplevel(RaizPrincipal)
    RaizCargar.resizable(0,0)
    FrameCargar=ttk.Frame(RaizCargar)
    FrameCargar.grid(column=0,row=0,padx=10,pady=10)
    #Labels de carga
    NombreLabel=tk.Label(FrameCargar,text="Nombre",font=font.Font(family="Times",size=14,weight=font.BOLD))
    NombreLabel.grid(row=0,column=0)
    ModeLabel=tk.Label(FrameCargar,text="Modelo",font=font.Font(family="Times",size=14,weight=font.BOLD))
    ModeLabel.grid(row=1,column=0)
    VersionLabel=tk.Label(FrameCargar,text="Version",font=font.Font(family="Times",size=14,weight=font.BOLD))
    VersionLabel.grid(row=2,column=0)
    PrecioLabel=tk.Label(FrameCargar,text="Precio",font=font.Font(family="Times",size=14,weight=font.BOLD))
    PrecioLabel.grid(row=3,column=0)
    FechaLabel=tk.Label(FrameCargar,text="Fecha",font=font.Font(family="Times",size=14,weight=font.BOLD))
    FechaLabel.grid(row=4,column=0)
    TotalLabel=tk.Label(FrameCargar,text="Total",font=font.Font(family="Times",size=14,weight=font.BOLD))
    TotalLabel.grid(row=5,column=0)
    EstadoLabel=tk.Label(FrameCargar,text="Estado",font=font.Font(family="Times",size=14,weight=font.BOLD))
    EstadoLabel.grid(row=6,column=0)
    #Entry de carga
    NombreEntry=tk.Entry(FrameCargar,font=font.Font(family="Times",size=14))
    NombreEntry.grid(row=0,column=1,padx=5)
    ModeEntry=tk.Entry(FrameCargar,font=font.Font(family="Times",size=14))
    ModeEntry.grid(row=1,column=1,padx=5)
    VersionEntry=tk.Entry(FrameCargar,font=font.Font(family="Times",size=14))
    VersionEntry.grid(row=2,column=1,padx=5)
    PrecioEntry=tk.Entry(FrameCargar,font=font.Font(family="Times",size=14))
    PrecioEntry.grid(row=3,column=1,padx=5)
    FechaEntry=tk.Entry(FrameCargar,font=font.Font(family="Times",size=14))
    FechaEntry.insert(0,Fecha)
    FechaEntry.grid(row=4,column=1,padx=5)
    TotalEntry=tk.Entry(FrameCargar,font=font.Font(family="Times",size=14))
    TotalEntry.grid(row=5,column=1,padx=5)
    EstadoEntry=tk.Entry(FrameCargar,font=font.Font(family="Times",size=14))
    EstadoEntry.grid(row=6,column=1,padx=5)
    BotonCargar=tk.Button(FrameCargar,text="Cargar",font=font.Font(family="Times",size=14),width=30,bg="darkblue",fg="#FFFFFF",borderwidth=5,command=lambda:Carga())
    BotonCargar.grid(row=7,column=0,columnspan=2,pady=10)


    def Carga():
        Nombre=NombreEntry.get()
        Modelo=ModeEntry.get()
        Version=VersionEntry.get()
        Precio=PrecioEntry.get()
        Fech=FechaEntry.get()
        Total=TotalEntry.get()
        Estado=EstadoEntry.get()
        if len(Nombre)>0:
            if(len(Modelo)>0):
                if(len(Version)>0):
                    if(len(Precio)>0):
                        if(len(Fech)>0):
                            if(len(Total)>0):
                                if len(Estado)>0:
                                    baseDeDatos.insertRow(Nombre,Modelo,Version,Precio,Fech,Total,Estado)
                                    messagebox.showinfo(message="Se añadio con exito: "+Nombre,title="Tabla")
                                else:
                                    messagebox.showerror(message="Debe completar todos los campos",title="Tabla")
                            else:
                                messagebox.showerror(message="Debe completar todos los campos",title="Tabla")
                        else:
                            messagebox.showerror(message="Debe completar todos los campos",title="Tabla")
                    else:
                        messagebox.showerror(message="Debe completar todos los campos",title="Tabla")
                else:
                    messagebox.showerror(message="Debe completar todos los campos",title="Tabla")
            else:
                messagebox.showerror(message="Debe completar todos los campos",title="Tabla")                                    
        else:
            messagebox.showerror(message="Debe completar todos los campos",title="Tabla")

        NombreEntry.delete(0,tk.END)
        ModeEntry.delete(0,tk.END)
        VersionEntry.delete(0,tk.END)
        PrecioEntry.delete(0,tk.END)
        
        TotalEntry.delete(0,tk.END)
        EstadoEntry.delete(0,tk.END)
        RaizCargar.destroy()
def Buscar():
    Items=Tabla.get_children()
    print(Items)
    if(len(Items)>0):
        Tabla.delete(Items)
        
    if(EntryBusqueda.get()=="*"):
        datos=baseDeDatos.searchAll()
        for i in datos:
            print (i)
            nombre=i[0]
            modelo=i[1]
            Precio=i[3]
            Version=i[2]
            Fecha=i[4]
            Total=i[5]
            Estado=i[6]
        
        
            Tabla.insert('',tk.END,tag=(color[0]),values=(nombre,modelo,Version,Precio,Fecha,Total,Estado))
    else:
        if len(EntryBusqueda.get())>0:    
            datos=baseDeDatos.search(EntryBusqueda.get())
            for i in datos:
                print (i)
                nombre=i[0]
                modelo=i[1]
                Precio=i[3]
                Version=i[2]
                Fecha=i[4]
                Total=i[5]
                Estado=i[6]
            
            
                Tabla.insert('',tk.END,tag=('fuente',),values=(nombre,modelo,Version,Precio,Fecha,Total,Estado))
        else:
            messagebox.showwarning(message="Esta buscando un campo vacio",title="Busqueda")


RaizPrincipal.mainloop()









