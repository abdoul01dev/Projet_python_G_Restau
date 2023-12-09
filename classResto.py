import tkinter as tk
from tkinter import ttk
import sqlite3 
from datetime import datetime
from tkinter import PhotoImage



class Requete(object):
    def __init__(self) :
        """initialisation"""
        self.donnees=[]
        self.datecomS="10/10/2022"

    def creationDB(self):
        conn=sqlite3.connect("dbRestaut.db")
        cur=conn.cursor()
        cur. execute("PRAGMA foreign_keys = ON")
        cur.execute("create table if not exists mets(id_mets integer primary key autoincrement unique,nom_mets text not null,mPrix integer not null)")
        cur.execute("create table if not exists client(idClient integer primary key autoincrement unique,nomClient text not null,prenomClient text not null,numClient integer not null)")
        cur.execute("""create table if not exists commande(id_com integer primary key autoincrement unique,id_mets integer not null,idClient integer not null,dateCom text,
                    qte integer not null,
                    foreign key(id_mets) references mets(id_mets) ON DELETE CASCADE,
                    foreign key(idClient) references Cient(idClient) ON DELETE CASCADE)""")
        conn.commit()
        conn.close()

    def enregitrementsClient(self):
        conn=sqlite3.connect("dbRestaut.db")
        cur=conn.cursor()
        self.donnees=cur.execute("""SELECT * FROM client""")
        conn.commit()
        conn.close()
        
    
    def insertClient(self,nom,prenom,numero):
        conn=sqlite3.connect("dbRestaut.db")
        cur=conn.cursor()
        cur.execute("""INSERT INTO client(nomClient,prenomClient,numClient) values(?,?,?)""",(nom,prenom,numero))
        conn.commit()
        conn.close()
        
    def suprimerClient(self,ID_client):
        conn=sqlite3.connect("dbRestaut.db")
        cur=conn.cursor()
        cur.execute("""delete from client where idClient=?""",ID_client)
        conn.commit()
        conn.close()
    
    def modifierClient(self,ID_client,nom,prenom,numero):
        conn=sqlite3.connect("dbRestaut.db")
        cur=conn.cursor()
        cur.execute("""update client set nomClient=?,PrenomClient=?,numClient=? where idClient=?""",(nom,prenom,numero,ID_client))
        conn.commit()
        conn.close()

    def insertMets(self,plat,prix):
        conn=sqlite3.connect("dbRestaut.db")
        cur=conn.cursor()
        cur.execute("""INSERT INTO mets(nom_mets,mPrix) values(?,?)""",(plat,prix))
        conn.commit()
        conn.close()
        
    def suprimerMets(self,ID_client):
        conn=sqlite3.connect("dbRestaut.db")
        cur=conn.cursor()
        cur.execute("""delete from mets where id_mets=?""",ID_client)
        conn.commit()
        conn.close()
    
    def modifierMets(self,ID_client,plat,prix):
        conn=sqlite3.connect("dbRestaut.db")
        cur=conn.cursor()
        cur.execute("""update mets set nom_mets=?,mPrix=? where id_mets=?""",(plat,prix,ID_client))
        conn.commit()
        conn.close()

    def insertCommande(self,id_mets,id_client,dateCom,qte):
        conn=sqlite3.connect("dbRestaut.db")
        cur=conn.cursor()
        cur.execute("""INSERT INTO commande(id_mets,idClient,dateCom,qte) values(?,?,?,?)""",(id_mets,id_client,dateCom,qte))
        conn.commit()
        conn.close()
        
    def suprimerCommande(self,ID_com):
        conn=sqlite3.connect("dbRestaut.db")
        cur=conn.cursor()
        cur.execute("""delete from commande where id_com=?""",ID_com)
        self.dateCommandeSupprime(ID_com)
        conn.commit()
        conn.close()
    def dateCommandeSupprime(self,param):
        conn=sqlite3.connect("dbRestaut.db")
        cur=conn.cursor()
        R=cur.execute("select distinct commande.dateCom from commande where id_com=?",param)
        for r in R:
            self.datecomS=r[0]
            #print(self.datecomS)
        conn.commit()
        conn.close()
        
    
    def modifierCommande(self,id_mets,id_client,dateCom,qte,iD_com):
        conn=sqlite3.connect("dbRestaut.db")
        cur=conn.cursor()
        cur.execute("""update commande set id_mets=?,idClient=?,dateCom=?,qte=? where id_com=?""",(id_mets,id_client,dateCom,qte,iD_com))
        conn.commit()
        conn.close()


def show_page(page_number):
    # Cache toutes les pages
    for frame in frames.values():
        frame.grid_remove()

    # Affiche la page spécifiée
    frames[page_number].grid(row=0, column=0, sticky="nsew")
    if page_number==0:
        print("ok")
    elif page_number==1:
        Clients.afficher_enregistrements()
    elif page_number==2:
        Mets.afficher_enregistrements()
    else:
        conn=sqlite3.connect("dbRestaut.db")
        cur=conn.cursor()
        cur.execute("select dateCom from commande where id_com=?",(cur.lastrowid,))
        Commande.afficher_enregistrements(Commande.selecDate())
        conn.commit
        conn.close()

class Accueil(object):
    def __init__(self):
        self.can=[]
        
    def create_page_Accueil(self,container):
        self.con1=tk.Frame(container,width=1600,height=720,bg="#B6540A",highlightbackground="#AF7204")
        self.con1.place(x=100,y=20)
        photo = PhotoImage(file="gar.png")
        label = tk.Label(self.con1, image=photo,bg="#B6540A")
        label.image = photo  # To prevent garbage collection
        label.place(x=100, y=10,)
        label_1 = tk.Label(self.con1, text="          Heureux de vous retrouver, gerer efficacement votre restaurant en toute confiance!!          ",bg="darkgreen",fg="white",bd=1,font=("Arial 20 bold"),)
        label_1.place(x=40,y=640)
        label_2 = tk.Label(self.con1, text="BIENVENUE!!",bg="#B6540A",fg="white",bd=1,font=("Arial 40 bold"),)
        label_2.place(x=250,y=180)
        
        


class Client(object):
    def __init__(self) :
        self.set=[]
        self.can=[]
        self.interfaceDB=Requete()
        self.donnees= []
        self.img=[]
        
    def create_page_client(self,container):
        #global donneesClients
        self.con1=tk.Frame(container,width=1600,height=570,bg="#B6540A")
        self.con1.place(x=100,y=110)
        
        photo = PhotoImage(file="salade.png")
        label = tk.Label(self.con1, image=photo,bg="#B6540A")
        label.image = photo 
        label.place(x=890, y=63)
        
        
        cl=tk.Label(container,text="Liste des clients",fg="#B6540A",bg="black",font="TrembuchetMs 20 bold ")
        cl.place(x=-150,y=70,width=1580,height=50)
        res=tk.Label(root,text="RESTAURANT EgateGroup",bg="darkgreen",fg="white",font="Arial 20 bold")
        res.place(x=480,y=10,width=400)
        motif=tk.Label(root,text="_"*200,bg="#4D100A",fg="white",pady=2,font="arial 12 bold")
        motif.place(x=0,y=10,width=500)
        motif2=tk.Label(root,text="_"*250,bg="#4D100A",fg="white",pady=2,font="arial 12 bold")
        motif2.place(x=880,y=10,width=500)


        #les boutons de gestion des clients
        bnc1=tk.Button(self.con1,text="Nouveau",bg="darkgreen",fg="white",font="TrembuchetMs 12 ",activebackground="darkgreen",padx=2,pady=2,command=self.ouvrir_fenetre_ajout)
        bnc2=tk.Button(self.con1,text="Modifier",bg="#4D100A",fg="white",font="TrembuchetMs 12 ",activebackground="#4D100A",command=self.ouvrir_fenetre_modification)
        bnc3=tk.Button(self.con1,text="Supprimer",bg="darkred",fg="white",font="TrembuchetMs 12 ",activebackground="darkred",command=self.supprimer_enregistrement)
        bnc1.place(x=895,y=65,width=85)
        bnc2.place(x=895,y=105,width=85)
        bnc3.place(x=895,y=145,width=85)

        self.set = ttk.Treeview(self.con1)
        self.set.place(x=50,y=50,width=840,height=460)

        self.set['columns']= ('id', 'Nom','Prenom','Telephone')
        self.set.column("#0", width=0,  stretch="NO")
        self.set.column("id",anchor="center", width=80)
        self.set.column("Nom",anchor="center", width=80)
        self.set.column("Prenom",anchor="center", width=80)
        self.set.column("Telephone",anchor="center", width=80)

        self.set.heading("#0",text="",anchor="center")
        self.set.heading("id",text="ID",anchor="center")
        self.set.heading("Nom",text="Nom",anchor="center")
        self.set.heading("Prenom",text="Prénom",anchor="center")
        self.set.heading("Telephone",text="Télephone",anchor="center")
        return (self.set,self.con1)
    

    def afficher_enregistrements(self):
        conn=sqlite3.connect("dbRestaut.db")
        cur=conn.cursor()
        data=cur.execute("""SELECT * FROM client""")
        self.donnees=data
        # Effacer les anciennes données
        for row in self.set.get_children():
            self.set.delete(row)

        # Ajouter les enregistrements à la Treeview
        for enregistrement in data:
            self.set.insert("", "end", values=enregistrement)

    def ouvrir_fenetre_ajout(self):
        #fen=tk.Tk()
        fenetre_ajout = tk.Toplevel(bg="#4D100A")
        fenetre_ajout.title("Ajouter un client")
        fenetre_ajout.geometry("600x300")


        # Entrées pour saisir les détails
        nom_entry = tk.Entry(fenetre_ajout)
        nom_label = tk.Label(fenetre_ajout, text="Nom:", bg="#4D100A",fg='white',font="Arial 12 bold")
        nom_label.place(x=170,y=65)
        nom_entry.place(x=265,y=65)

        prenom_entry = tk.Entry(fenetre_ajout)
        prenom_label = tk.Label(fenetre_ajout, text="Prénom:", bg="#4D100A",fg='white',font="Arial 12 bold")
        prenom_label.place(x=170,y=110)
        prenom_entry.place(x=265,y=110)

        tel_entry = tk.Entry(fenetre_ajout)
        tel_label = tk.Label(fenetre_ajout, text="Téléphone:", bg="#4D100A",fg='white',font="Arial 12 bold")
        tel_label.place(x=170,y=155)
        tel_entry.place(x=265,y=155)

        ajouter_btn = tk.Button(fenetre_ajout, text="Valider",bg="darkgreen",fg="white",bd=1 ,font="Arial 12 bold",command=lambda: self.ajouter_enregistrement_fenetre_ajout(nom_entry.get(), prenom_entry.get(),tel_entry.get(), fenetre_ajout))
        ajouter_btn.place(x=275,y=200)
        print("ok")
        fenetre_ajout.mainloop()

    def ajouter_enregistrement_fenetre_ajout(self,nom, prenom,telephone, fenetre):
        if nom and prenom:
            #nouvel_id = self.donnees.append((len(self.donnees)+1,nom,prenom, telephone))
            self.interfaceDB.insertClient(nom,prenom,telephone)
            self.afficher_enregistrements()
           # print(f"Enregistrement ajouté avec l'ID: {nouvel_id}")
            fenetre.destroy()
        else:
            print("Veuillez remplir tous les champs.")

    def ouvrir_fenetre_modification(self):
        conn=sqlite3.connect("dbRestaut.db")
        cur=conn.cursor()
        selection = self.set.selection()
        if selection:
            identifiant = int(self.set.item(selection, "values")[0])
            #enregistrement = self.trouver_enregistrement_par_id(identifiant)
            data=cur.execute("""SELECT * FROM client """)
            fenetre_modification = tk.Toplevel(bg="#4D100A")
            fenetre_modification.title("Modifier un client")
            fenetre_modification.geometry("600x300")
            for result in data:
                if result[0]==identifiant:
                    v1=result[1]
                    v2=result[2]
                    v3=result[3]
            # Entrées pré-remplies avec les données actuelles
            nom_var = tk.StringVar(fenetre_modification, value=v1)
            nom_entry = tk.Entry(fenetre_modification, textvariable=nom_var)
            nom_label = tk.Label(fenetre_modification, text="Nom:", bg="#4D100A",fg='white',font="Arial 12 bold")
            nom_label.place(x=170,y=65)
            nom_entry.place(x=265,y=65)

            prenom_var = tk.StringVar(fenetre_modification, value=v2)
            prenom_entry = tk.Entry(fenetre_modification, textvariable=prenom_var)
            prenom_label = tk.Label(fenetre_modification, text="Prénom:", bg="#4D100A",fg='white',font="Arial 12 bold")
            prenom_label.place(x=170,y=115)
            prenom_entry.place(x=265,y=115)

            tel_var = tk.StringVar(fenetre_modification, value=v3)
            tel_entry = tk.Entry(fenetre_modification, textvariable=tel_var)
            tel_label = tk.Label(fenetre_modification, text="Téléphone:", bg="#4D100A",fg='white',font="Arial 12 bold")
            tel_label.place(x=170,y=175)
            tel_entry.place(x=265,y=175)
            modifier_btn = tk.Button(fenetre_modification, text="Valider",bg="darkgreen",fg="white",bd=1 ,font="Arial 12 bold", command=lambda: self.modifier_enregistrement_fenetre_modification(identifiant, nom_var.get(),prenom_var.get(), tel_var.get(), fenetre_modification))
            modifier_btn.place(x=275,y=240)
        else:
            print("Sélectionnez un enregistrement à modifier.")

   

    def modifier_enregistrement_fenetre_modification(self, identifiant, nom,prenom, tel,fenetre):
        if nom and prenom:
            self.interfaceDB.modifierClient(identifiant, nom,prenom, tel)
            #self.donnees[identifiant-1]=(identifiant, nom, prenom,tel)
            self.afficher_enregistrements()
            print(f"Enregistrement modifié avec l'ID: {identifiant}")
            fenetre.destroy()
        else:
            print("Veuillez remplir tous les champs.")

    def supprimer_enregistrement(self):
        selection = self.set.selection()
        if selection:
            identifiant = int(self.set.item(selection, "values")[0])
            #del self.donnees[identifiant-1]
            self.interfaceDB.suprimerClient((identifiant,))
            self.afficher_enregistrements()
            print(f"Enregistrement supprimé avec l'ID: {identifiant}")
        else:
            print("Sélectionnez un enregistrement à supprimer.")
    

class Mets(object):
    def __init__(self) :
        self.set=[]
        self.can=[]
        self.interfaceDB=Requete()
        self.donnees=[]
        #[(1,"Tô",600),(2,"Riz gras",800)]
        #self.nbrClient=len(self.donnees)+1
    def create_page_mets(self,container):
        con1=tk.Frame(container,width=1600,height=570,bg="#B6540A")
        con1.place(x=100,y=110)
        
        
        photo = PhotoImage(file="png (3).png")
        label = tk.Label(con1, image=photo,bg="#B6540A")
        label.image = photo 
        label.place(x=890, y=50)
        
        
        cl=tk.Label(container,text="Liste des mets",fg="#B6540A",bg="black",font="TrembuchetMs 20 bold ")
        cl.place(x=-150,y=70,width=1580,height=50)
        res=tk.Label(root,text="RESTAURANT EgateGroup",bg="darkgreen",fg="white",font="Arial 20 bold")
        res.place(x=480,y=10,width=400)
        motif=tk.Label(root,text="_"*200,bg="#4D100A",fg="white",pady=2,font="arial 12 bold")
        motif.place(x=0,y=10,width=480)
        motif2=tk.Label(root,text="_"*200,bg="#4D100A",fg="white",pady=2,font="arial 12 bold")
        motif2.place(x=880,y=10,width=480)


        #les boutons de gestion des mets
        bnc1=tk.Button(con1,text="Nouveau",bg="darkgreen",fg="white",font="TrembuchetMs 12 ",activebackground="darkgreen",activeforeground="white",padx=2,pady=2,command=self.ouvrir_fenetre_ajout)
        bnc2=tk.Button(con1,text="Modifier",bg="#4D100A",fg="white",font="TrembuchetMs 12 ",activebackground="#4D100A",activeforeground="white",command=self.ouvrir_fenetre_modification)
        bnc3=tk.Button(con1,text="Supprimer",bg="darkred",fg="white",font="TrembuchetMs 12 ",activebackground="darkred",activeforeground="white",command=self.supprimer_enregistrement)
        bnc1.place(x=895,y=65,width=85)
        bnc2.place(x=895,y=105,width=85)
        bnc3.place(x=895,y=145,width=85)

        self.set = ttk.Treeview(con1)
        self.set.place(x=50,y=50,width=840,height=460)

        self.set['columns']= ('id', 'plat','prix',)
        self.set.column("#0", width=0,  stretch="NO")
        self.set.column("id",anchor="center", width=80)
        self.set.column("plat",anchor="center", width=80)
        self.set.column("prix",anchor="center", width=80)

        self.set.heading("#0",text="",anchor="center")
        self.set.heading("id",text="ID",anchor="center")
        self.set.heading("plat",text="Plat",anchor="center")
        self.set.heading("prix",text="Prix",anchor="center")
        return (set,con1)

    
    def afficher_enregistrements(self):
        conn=sqlite3.connect("dbRestaut.db")
        cur=conn.cursor()
        data=cur.execute("""SELECT * FROM mets""")
        self.donnees=data
        # Effacer les anciennes données
        for row in self.set.get_children():
            self.set.delete(row)

        # Ajouter les enregistrements à la Treeview
        for enregistrement in data:
            self.set.insert("", "end", values=enregistrement)

    def ouvrir_fenetre_ajout(self):
        #fen=tk.Tk()
        fenetre_ajout = tk.Toplevel(bg="#4D100A")
        fenetre_ajout.title("Ajouter un mets")
        fenetre_ajout.geometry("600x300")


        # Entrées pour saisir les détails
        plat_entry = tk.Entry(fenetre_ajout)
        plat_label = tk.Label(fenetre_ajout, text="Plat:",bg="#4D100A",fg="white",font="Arial 12 bold",activebackground="#4D100A")
        plat_label.place(x=190,y=65)
        plat_entry.place(x=245,y=65)

        prix_entry = tk.Entry(fenetre_ajout)
        prix_label = tk.Label(fenetre_ajout, text="Prix:",bg="#4D100A",fg="white",font="Arial 12 bold",activebackground="#4D100A")
        prix_label.place(x=190,y=115)
        prix_entry.place(x=245,y=115)

        ajouter_btn = tk.Button(fenetre_ajout, text="Valider",bg="darkgreen",fg="white",bd=1,font="Arial 12 bold",activebackground="darkgreen", command=lambda: self.ajouter_enregistrement_fenetre_ajout(plat_entry.get(), prix_entry.get(), fenetre_ajout))
        ajouter_btn.place(x=250,y=170)
        print("ok")
        fenetre_ajout.mainloop()

    def ajouter_enregistrement_fenetre_ajout(self,plat, prix, fenetre):
        if plat and prix:
            #nouvel_id = self.donnees.append((len(self.donnees)+1,plat,prix))
            self.interfaceDB.insertMets(plat,prix)
            self.afficher_enregistrements()
            #print(f"Enregistrement ajouté avec l'ID: {nouvel_id}")
            fenetre.destroy()
        else:
            print("Veuillez remplir tous les champs.")

    def ouvrir_fenetre_modification(self):
        conn=sqlite3.connect("dbRestaut.db")
        cur=conn.cursor()
        selection = self.set.selection()
        if selection:
            identifiant = int(self.set.item(selection, "values")[0])
            data=cur.execute("""SELECT * FROM mets """)
            #enregistrement = self.trouver_enregistrement_par_id(identifiant)

            fenetre_modification = tk.Toplevel(bg="#4D100A")
            fenetre_modification.title("Modifier un mets")
            fenetre_modification.geometry("600x300")
            for result in data:
                if result[0]==identifiant:
                    v1=result[1]
                    v2=result[2]

            # Entrées pré-remplies avec les données actuelles
            plat_var = tk.StringVar(fenetre_modification, value=v1)
            plat_entry = tk.Entry(fenetre_modification, textvariable=plat_var)
            plat_label = tk.Label(fenetre_modification, text="Plat:",bg="#4D100A",fg="white",font="Arial 12 bold",activebackground="#4D100A",activeforeground="white")
            plat_label.place(x=180,y=65)
            plat_entry.place(x=245,y=65)

            prix_var = tk.StringVar(fenetre_modification, value=v2)
            prix_entry = tk.Entry(fenetre_modification, textvariable=prix_var)
            prix_label = tk.Label(fenetre_modification, text="Prix:",bg="#4D100A",fg="white",font="Arial 12 bold",activebackground="#4D100A",activeforeground="white")
            prix_label.place(x=180,y=115)
            prix_entry.place(x=245,y=115)

            modifier_btn = tk.Button(fenetre_modification, text="Valider",bg="darkgreen",fg="white",bd=1,font="Arial 12 bold",activebackground="darkgreen",activeforeground="white", command=lambda: self.modifier_enregistrement_fenetre_modification(identifiant, plat_var.get(),prix_var.get(), fenetre_modification))
            modifier_btn.place(x=250,y=170)
        else:
            print("Sélectionnez un enregistrement à modifier.")

    

    def modifier_enregistrement_fenetre_modification(self, identifiant, plat,prix,fenetre):
        if plat and prix:
            #self.donnees[identifiant-1]=(identifiant,plat, prix)
            self.interfaceDB.modifierMets(identifiant, plat,prix)
            self.afficher_enregistrements()
            print(f"Enregistrement modifié avec l'ID: {identifiant}")
            fenetre.destroy()
        else:
            print("Veuillez remplir tous les champs.")

    def supprimer_enregistrement(self):
        selection = self.set.selection()
        if selection:
            identifiant = int(self.set.item(selection, "values")[0])
            self.interfaceDB.suprimerMets((identifiant,))
            self.afficher_enregistrements()
            print(f"Enregistrement supprimé avec l'ID: {identifiant}")
        else:
            print("Sélectionnez un enregistrement à supprimer.")


class Commande(object):
    def __init__(self) :
        self.set=[]
        self.can=[]
        self.interfaceDB=Requete()
        self.donnees=[]
        self.texte="10000"
        self.en_date=ttk.Combobox(values=['10/10/23','15/10/23'],height=50)
    def create_page_commandes(self,container):
        con1=tk.Frame(container,width=1600,height=570,bg="#B6540A")
        con1.place(x=100,y=110)

        photo = PhotoImage(file="commande.PNG")
        label = tk.Label(con1, image=photo,bg="#B6540A")
        label.image = photo 
        label.place(x=900, y=180)

        cl=tk.Label(container,text="Liste des commandes",fg="#B6540A",bg="black",font="TrembuchetMs 20 bold ")
        cl.place(x=-150,y=70,width=1580,height=50)
        res=tk.Label(root,text="RESTAURANT EgateGroup",bg="darkgreen",fg="white",font="Arial 20 bold")
        res.place(x=480,y=10,width=400)
        motif=tk.Label(root,text="_"*200,bg="#4D100A",fg="white",pady=2,font="arial 12 bold")
        motif.place(x=0,y=10,width=480)
        motif2=tk.Label(root,text="_"*200,bg="#4D100A",fg="white",pady=2,font="arial 12 bold")
        motif2.place(x=880,y=10,width=480)
        
        self.texte=tk.StringVar()
        self.texte.initialize(4000)
        total=tk.Label(con1, text="Total :",bg="#B6540A",fg="white",bd=5,width=80,font="arial 16 bold")
        total.place(x=-350,y=490)

        #les boutons de gestion des commandes
        bnc1=tk.Button(con1,text="Nouveau",bg="darkgreen",fg="white",font="TrembuchetMs 12 ",activebackground="darkgreen",padx=2,pady=2, command=self.ouvrir_fenetre_ajout)
        bnc2=tk.Button(con1,text="Modifier",bg="#4D100A",fg="white",font="TrembuchetMs 12 ",activebackground="#4D100A",command=self.ouvrir_fenetre_modification)
        bnc3=tk.Button(con1,text="Supprimer",bg="darkred",fg="white",font="TrembuchetMs 12 ",activebackground="darkred",command=self.supprimer_enregistrement)
        bnc4=tk.Button(con1,text="Facture",bg="darkorange",fg="white",font="TrembuchetMs 12 ",activebackground="#B6540A",command=self.generer_facture)
        bnc1.place(x=895,y=65,width=85)
        bnc2.place(x=895,y=105,width=85)
        bnc3.place(x=895,y=145,width=85)
        bnc4.place(x=895,y=185,width=85)
        self.con=con1

        ok=tk.Button(con1,text="ok",command=self.selecDate,bg="#B6540A",activebackground="blue",fg="white")
        ok.place(x=330,y=17)
        tout=tk.Button(con1,text="Afficher tous",command=self.afficherTout,bg="#B6540A",activebackground="blue",fg="white")
        tout.place(x=530,y=17)
        lab_date=tk.Label(con1,text="choisir une date: ",bg="#B6540A",fg="white",font="arial 12 bold")
        lab_date.place(x=50,y=17)

        set = ttk.Treeview(con1)
        set.place(x=50,y=50,width=840,height=440)

        set['columns']= ('id', 'NomPrenom','Telephone','plat','qte','mnt')
        set.column("#0", width=0,  stretch="NO")
        set.column("id",anchor="center", width=80)
        set.column("NomPrenom",anchor="center", width=80)
        set.column("Telephone",anchor="center", width=80)
        set.column("plat",anchor="center", width=80)
        set.column("qte",anchor="center", width=80)
        set.column("mnt",anchor="center", width=80)

        set.heading("#0",text="",anchor="center")
        set.heading("id",text="ID",anchor="center")
        set.heading("NomPrenom",text="Nom et Prénom",anchor="center")
        set.heading("Telephone",text="Télephone",anchor="center")
        set.heading("plat",text="Plat",anchor="center")
        set.heading("qte",text="Quantité",anchor="center")
        set.heading("mnt",text="Montant",anchor="center")
        self.set=set
        return (set,con1)   
    
    
    def  dateC(self):
        conn=sqlite3.connect("dbRestaut.db")
        cur=conn.cursor()
        data2=cur.execute("""SELECT distinct commande.dateCom from commande order by dateCom asc""")
        val=[]
        for v in data2:
            val.append(v[0])
        conn.commit()
        conn.close()
        return val

    def selecDate(self):
        #return self.en_date.get()
        self.afficher_enregistrements(self.en_date.get())

    def afficherTout(self):
        conn=sqlite3.connect("dbRestaut.db")
        cur=conn.cursor()
        req="""SELECT client.nomClient,client.prenomClient,client.numClient,
         mets.nom_mets, commande.qte,mets.mPrix,commande.id_com,commande.dateCom
        FROM client 
        JOIN commande ON commande.idClient=client.idClient
        JOIN mets ON mets.id_mets=commande.id_mets
        WHERE commande.dateCom IN ({})
        """.format(','.join('?' for _ in self.dateC()))
        data=cur.execute(req,self.dateC())
        #self.donnees=data
        table=[]
        for row in data:
            table.append((row[6],row[0]+" "+row[1],row[2],row[3],row[4],row[5]*row[4]))
        # Effacer les anciennes données
        for row in self.set.get_children():
            self.set.delete(row)

        # Ajouter les enregistrements à la Treeview
        somme=0
        for enregistrement in table:
            self.set.insert("", "end", values=enregistrement)
            somme+=int(enregistrement[5])
        self.Somme=tk.Label(self.con, text=str(somme)+" FCFA",bg="#B6540A",fg="white",bd=5,width=80,font="arial 16 bold")
        self.Somme.place(x=300,y=490)

    
    def afficher_enregistrements(self,param):
        conn=sqlite3.connect("dbRestaut.db")
        cur=conn.cursor()
        data=cur.execute("""SELECT client.nomClient,client.prenomClient,client.numClient,
                         mets.nom_mets, commande.qte,mets.mPrix,commande.id_com
                         FROM client 
                         JOIN commande ON commande.idClient=client.idClient
                         JOIN mets ON mets.id_mets=commande.id_mets
                         WHERE commande.dateCom=?;
                         """,(param,))
        self.donnees=data
        table=[]
        for row in data:
            table.append((row[6],row[0]+" "+row[1],row[2],row[3],row[4],row[5]*row[4]))
        # Effacer les anciennes données
        for row in self.set.get_children():
            self.set.delete(row)

        # Ajouter les enregistrements à la Treeview
        somme=0
        for enregistrement in table:
            self.set.insert("", "end", values=enregistrement)
            somme+=int(enregistrement[5])
        self.Somme=tk.Label(self.con, text=str(somme)+" FCFA",bg="#B6540A",fg="white",bd=5,width=80,font="arial 16 bold")
        self.Somme.place(x=300,y=490)
        self.en_date=ttk.Combobox(self.con,values=self.dateC())
        self.en_date.place(x=185,y=20)
    
    def ouvrir_fenetre_ajout(self):
        conn=sqlite3.connect("dbRestaut.db")
        cur=conn.cursor()
        fenetre_ajout = tk.Toplevel(bg="#4D100A")
        fenetre_ajout.title("Prise de commande")
        fenetre_ajout.geometry("600x300")
        client=cur.execute("""SELECT * FROM client """)
        listeNomPrenom=[]
        listeID=[]
        for c in client:
            listeID.append(c[0])
            listeNomPrenom.append(c[1]+" "+c[2]+"("+str(c[3])+")")
        
        plat=cur.execute("""SELECT * FROM mets """)
        listePlat=[]
        listeID2=[]
        for p in plat:
            listeID2.append(p[0])
            listePlat.append(p[1])

        # Entrées pour saisir les détails
        selection = tk.StringVar()
        self.nom_entry = ttk.Combobox(fenetre_ajout,values=listeNomPrenom,textvar=selection)
        nom_label = ttk.Label(fenetre_ajout, text="Client:",background="#4D100A",foreground="white",font="Arial 12 bold")
        nom_label.place(x=170,y=65)
        self.nom_entry.place(x=245,y=65)

        self.plat_entry = ttk.Combobox(fenetre_ajout,values=listePlat)
        plat_label = ttk.Label(fenetre_ajout, text="Plat:",background="#4D100A",foreground="white",font="Arial 12 bold")
        plat_label.place(x=170,y=115)
        self.plat_entry.place(x=245,y=115)

        qte_entry = ttk.Combobox(fenetre_ajout,values=list(range(1,31)))
        qte_label = ttk.Label(fenetre_ajout, text="Quantité:",background="#4D100A",foreground="white",font="Arial 12 bold")
        qte_label.place(x=170,y=175)
        qte_entry.place(x=245,y=175)
        ajouter_btn = tk.Button(fenetre_ajout, text="Valider",bg="darkgreen",fg="white",bd=1,font="Arial 12 bold",activebackground="darkgreen", command=lambda: self.ajouter_enregistrement_fenetre_ajout(listeID2[listePlat.index(self.plat_entry.get())],listeID[listeNomPrenom.index(self.nom_entry.get())],datetime.now().date(), qte_entry.get(), fenetre_ajout))
        ajouter_btn.place(x=245,y=220)
        fenetre_ajout.mainloop()

    def ajouter_enregistrement_fenetre_ajout(self,id_mets,idClient,dateCom,qte,fenetre):
        if id_mets and idClient and qte:
            conn=sqlite3.connect("dbRestaut.db")
            cur=conn.cursor()
            self.interfaceDB.insertCommande(id_mets,idClient,dateCom,qte)
            #nouvel_id = self.donnees.append((len(self.donnees)+1,nomPrenom, telephone,plat,qte,prix))
            self.afficher_enregistrements(dateCom)
            #print(f"Enregistrement ajouté avec l'ID: {nouvel_id}")
            fenetre.destroy()
        else:
            print("Veuillez remplir tous les champs.")

    def ouvrir_fenetre_modification(self):
        conn=sqlite3.connect("dbRestaut.db")
        cur=conn.cursor()
        selection = self.set.selection()
        if selection:
            identifiant = int(self.set.item(selection, "values")[0])
            nomP = str(self.set.item(selection, "values")[1])
            num=str(self.set.item(selection, "values")[2])
            pl = str(self.set.item(selection, "values")[3])
            qte = int(self.set.item(selection, "values")[4])
            
            fenetre_modification = tk.Toplevel(bg="#4D100A")
            fenetre_modification.title("Modifier une commande")
            fenetre_modification.geometry("600x300")

            client=cur.execute("""SELECT * FROM client """)
            listeNomPrenom=[]
            listeID=[]
            for c in client:
                listeID.append(c[0])
                listeNomPrenom.append(c[1]+" "+c[2]+"("+str(c[3])+")")
            
            plat=cur.execute("""SELECT * FROM mets """)
            listePlat=[]
            listeID2=[]
            for p in plat:
                listeID2.append(p[0])
                listePlat.append(p[1])
        
            # Entrées pré-remplies avec les données actuelles
            selection = tk.StringVar()
            self.nom_entry = ttk.Combobox(fenetre_modification,values=listeNomPrenom)
            nom_label = ttk.Label(fenetre_modification, text="Client:",background="#4D100A",foreground="white",font="Arial 12 bold")
            self.nom_entry.set(nomP+"("+num+")")
            nom_label.place(x=170,y=65)
            self.nom_entry.place(x=245,y=65)

            self.plat_entry = ttk.Combobox(fenetre_modification,values=listePlat)
            plat_label = ttk.Label(fenetre_modification, text="Plat:",background="#4D100A",foreground="white",font="Arial 12 bold")
            self.plat_entry.set(pl)
            plat_label.place(x=170,y=115)
            self.plat_entry.place(x=245,y=115)

            qte_entry = ttk.Combobox(fenetre_modification,values=list(range(1,31)))
            qte_label = ttk.Label(fenetre_modification, text="Quantité:",background="#4D100A",foreground="white",font="Arial 12 bold")
            qte_entry.set(qte)
            qte_label.place(x=170,y=175)
            qte_entry.place(x=245,y=175)


            modifier_btn = tk.Button(fenetre_modification, text="Valider",bg="darkgreen",fg="white",font="Arial 12 bold",activebackground="darkgreen", command=lambda: self.modifier_enregistrement_fenetre_modification(identifiant, listeID2[listePlat.index(self.plat_entry.get())],listeID[listeNomPrenom.index(self.nom_entry.get())],datetime.now().date(), qte_entry.get(), fenetre_modification))
            modifier_btn.place(x=245,y=220)
        else:
            print("Sélectionnez un enregistrement à modifier.")

    def modifier_enregistrement_fenetre_modification(self, identifiant, id_mets, id_client,date,qte,fenetre):
        if id_mets and id_client and qte:
            #self.donnees[identifiant-1]=(identifiant, nomPrenom,tel,plat,qte,prix)
            self.interfaceDB.modifierCommande(id_mets, id_client,date,qte,identifiant)
            self.afficher_enregistrements(date)
            print(f"Enregistrement modifié avec l'ID: {identifiant}")
            fenetre.destroy()
        else:
            print("Veuillez remplir tous les champs.")

    def supprimer_enregistrement(self):
        selection = self.set.selection()
        if selection:
            identifiant = int(self.set.item(selection, "values")[0])
            self.interfaceDB.suprimerCommande((identifiant,))
            self.interfaceDB.dateCommandeSupprime((identifiant,))
            
            self.afficher_enregistrements(self.interfaceDB.datecomS)
            print(f"Enregistrement supprimé avec l'ID: {identifiant}")
            print(self.interfaceDB.datecomS)
        else:
            print("Sélectionnez un enregistrement à supprimer.")
    
    def generer_facture(self):
        selection = self.set.selection()
        if selection:
            identifiant = int(self.set.item(selection, "values")[0])
            nom_prenom = str(self.set.item(selection, "values")[1])
            numero = str(self.set.item(selection, "values")[2])
            nom_met = str(self.set.item(selection, "values")[3])
            quantite = int(self.set.item(selection, "values")[4])  # Indice pour la quantité dans la Treeview
            montant = float(self.set.item(selection, "values")[5])  # Indice pour le montant unitaire dans la Treeview

            # Calcul du total de la commande
            total_commande =  montant

            # Création de la fenêtre de la facture
            fenetre_facture = tk.Toplevel(bg="white",bd=2)
            fenetre_facture.title(f"Facture pour la commande {identifiant}")
            fenetre_facture.geometry("300x400")

            # Affichage des informations dans la fenêtre de la facture
            label_num = tk.Label(fenetre_facture, text=f"Client N°: {identifiant}",bg="white", font="Arial 12 bold")
            label_num.pack()
            
            label_client = tk.Label(fenetre_facture, text=f"Nom du Client : {nom_prenom}",bg="white", font="Arial 10 bold")
            label_client.pack()
            label_client.place(x=40,y=50)

            label_numero = tk.Label(fenetre_facture, text=f"Numéro de téléphone : {numero}",bg="white", font="Arial 10 bold")
            label_numero.pack()
            label_numero.place(x=40,y=90)

            label_plat = tk.Label(fenetre_facture, text=f"plat : {nom_met}",bg="white",font="Arial 10 bold")
            label_plat.pack()
            label_plat.place(x=40,y=130)

            label_quantite = tk.Label(fenetre_facture, text=f"Quantité : {quantite}",bg="white", font="Arial 10 bold")
            label_quantite.pack()
            label_quantite.place(x=40,y=180)

            label_total_commande = tk.Label(fenetre_facture, text=f"Total de la commande : {total_commande}",bg="white", font="Arial 11 bold")
            label_total_commande.pack()
            label_total_commande.place(x=40,y=220)

            label_remercie = tk.Label(fenetre_facture, text=f"meci pour la confiance et bon appétit",bg="darkgreen",fg="white",bd=1,font=("Arial 12 bold"))
            label_remercie.pack()
            label_remercie.place(x=5,y=350)
        else:
            print("Sélectionnez une commande pour générer la facture.")

root = tk.Tk()
root.wm_title("EgateGroup")
root.geometry("1400x768")
baseDeDonnees=Requete()
baseDeDonnees.creationDB()
accueil=Accueil()
Clients=Client()

Mets=Mets()
Commande=Commande()
# Créer un conteneur pour les pages
container = tk.Frame(root,width=600,height=1000,bg="#4D100A")
#container.pack(side="left", fill="both")
container.pack(side="left", fill="both", expand=True)
container.grid_rowconfigure(0, weight=1)
container.grid_columnconfigure(0, weight=1)
barM = tk.Frame(root,width=140,height=1000,bg="#4D100A")
barM.place(x=0,y=20)
Button = tk.Button(barM, text="ACCUEIL",bg="darkgreen",fg="white",font="TrembuchetMs 12 ",activebackground="darkgreen", command=lambda: show_page(0))
Button.place(x=5,y=30,width=130)
Button1 = tk.Button(barM, text="CLIENTS",bg="darkgreen",fg="white",font="TrembuchetMs 12 ",activebackground="darkgreen", command=lambda: show_page(1))
Button1.place(x=5,y=65,width=130)
Button2 = tk.Button(barM, text="METS",bg="darkgreen",fg="white",font="TrembuchetMs 12 ",activebackground="darkgreen", command=lambda: show_page(2))
Button2.place(x=5,y=100,width=130)
Button3 = tk.Button(barM, text="COMMANDES",bg="darkgreen",fg="white",font="TrembuchetMs 12 ",activebackground="darkgreen", command=lambda: show_page(3))
Button3.place(x=5,y=135,width=130)
Button3 = tk.Button(barM, text="QUITTER",bg="darkred",fg="white",font="TrembuchetMs 12 ",activebackground="darkred", command=quit)
Button3.place(x=5,y=170,width=130)

# Créer un dictionnaire pour stocker les pages
frames = {}
frames[0]=ttk.Frame(container)
frames[1] = ttk.Frame(container)
frames[2] = ttk.Frame(container)
frames[3] = ttk.Frame(container)
accueil.create_page_Accueil(frames[0])
Clients.create_page_client(frames[1])
Mets.create_page_mets(frames[2])
Commande.create_page_commandes(frames[3])
show_page(0)
root.mainloop()
