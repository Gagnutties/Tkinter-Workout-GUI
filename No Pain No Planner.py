# -*- coding: utf-8 -*-
"""
Created on Tue May 10 10:24:14 2022
Planner Application
@author: Dylan
"""
#SECRET HASH TO DIFFERENTIATE FILES IS: 7pQXk5jXt3 for playlists
#SECRET HASH TO DIFFERENTIATE TIME FILES IS: p223ET8Q22
##########################################IMPORTS AND SETUP####################
import os
import os.path
import pickle
import tkinter as tk
from datetime import date
import datetime
root = tk.Tk()
root.geometry('1000x600')
root.title('Planner')
root.configure(bg='#FEE440')
#############################################FUNCTIONS##############################

###########################################################################################CALENDAR PAGE###################################
def Calendar():
    for widget in frame.winfo_children():
        widget.destroy()
    btn = tk.Button(root, text="CCCCCCCCCCCCCCCCCCCCCC", bg='#00BBF9', activebackground="#00F5D4")
    btn.config(height=2, width=25)
    btn.place(x=715, y=20)
    
    btn = tk.Button(root, text="The Last 7 Days Displayed Below", bg='#00BBF9', activebackground="#00F5D4")
    btn.config(height=2, width=25)
    btn.place(x=510, y=20)
    
    btn = tk.Button(root, text="CCCCCCCCCCCCCCCCCCCCCC", bg='#00BBF9', activebackground="#00F5D4")
    btn.config(height=2, width=25)
    btn.place(x=300, y=20)
    
    Today = date.today()
    LoadToday = Today.strftime("%d-%m-%Y") 

##########################################################################################################DAYS IN LAST 7############################
    Day1 = tk.Frame(frame, padx=0, pady=15, bg="#00BBF9")
    Day1.place(width=80, height=450, x=-10, y=0)
    
    d = datetime.datetime.strptime(LoadToday, '%d-%m-%Y')
    if os.path.exists(str(d.strftime('%d-%m-%Y'))+"p223ET8Q22") == True:
        LblD1 = tk.Label(Day1, text=d.strftime('%d-%m'), bg="#00BBF9", fg="#000000")
        LblD1.pack()
        
        Load = open(str(d.strftime('%d-%m-%Y'))+"p223ET8Q22", 'rb')
        LoadedPlaylist = pickle.load(Load)

        for i in LoadedPlaylist:
            if(i == "Endurance"):

                EndurancePhoto = tk.PhotoImage(file = "Endurance.png")
                EnLabel = tk.Label(Day1, image = EndurancePhoto, bg="#FEE440")
                EnLabel.pack()
                EnLabel.keepimage = EndurancePhoto
            elif(i == "Strength"):

                StrengthPhoto = tk.PhotoImage(file = "Strength.png")
                StLabel = tk.Label(Day1, image = StrengthPhoto, bg="#FEE440")
                StLabel.pack()
                StLabel.keepimage = StrengthPhoto
            else:

                BalancePhoto = tk.PhotoImage(file = "Balance.png")
                BaLabel = tk.Label(Day1, image = BalancePhoto, bg="#FEE440")
                BaLabel.pack()
                BaLabel.keepimage = BalancePhoto
                
                
                
                
                
                
    else:
        LblD1 = tk.Label(Day1, text=d.strftime('%d-%m'), bg="#00BBF9", fg="#000000")
        LblD1.pack()
        pass
    
##############################################################################################DAY 2
    Day2 = tk.Frame(frame, padx=15, pady=15, bg="#00BBF9")
    Day2.place(width=80, height=450, x=75, y=0)
    
    d = datetime.datetime.strptime(LoadToday, '%d-%m-%Y') - datetime.timedelta(days=1)
    
    if os.path.exists(str(d.strftime('%d-%m-%Y'))+"p223ET8Q22") == True:
        LblD2 = tk.Label(Day2, text=d.strftime('%d-%m'), bg="#00BBF9", fg="#000000")
        LblD2.pack()
        
        Load = open(str(d.strftime('%d-%m-%Y'))+"p223ET8Q22", 'rb')
        LoadedPlaylist = pickle.load(Load)
        
        for i in LoadedPlaylist:
            if(i == "Endurance"):

                EndurancePhoto = tk.PhotoImage(file = "Endurance.png")
                EnLabel = tk.Label(Day2, image = EndurancePhoto, bg="#FEE440")
                EnLabel.pack()
                EnLabel.keepimage = EndurancePhoto
            elif(i == "Strength"):

                StrengthPhoto = tk.PhotoImage(file = "Strength.png")
                StLabel = tk.Label(Day2, image = StrengthPhoto, bg="#FEE440")
                StLabel.pack()
                StLabel.keepimage = StrengthPhoto
            else:

                BalancePhoto = tk.PhotoImage(file = "Balance.png")
                BaLabel = tk.Label(Day2, image = BalancePhoto, bg="#FEE440")
                BaLabel.pack()
                BaLabel.keepimage = BalancePhoto
        
    else:
        LblD2 = tk.Label(Day2, text=d.strftime('%d-%m'), bg="#00BBF9", fg="#000000")
        LblD2.pack()
        pass

##############################################################################################DAY 3
    Day3 = tk.Frame(frame, padx=15, pady=15, bg="#00BBF9")
    Day3.place(width=80, height=450, x=160, y=0)
    
    d = datetime.datetime.strptime(LoadToday, '%d-%m-%Y') - datetime.timedelta(days=2)
    
    if os.path.exists(str(d.strftime('%d-%m-%Y'))+"p223ET8Q22") == True:
        LblD3 = tk.Label(Day3, text=d.strftime('%d-%m'), bg="#00BBF9", fg="#000000")
        LblD3.pack()
        
        Load = open(str(d.strftime('%d-%m-%Y'))+"p223ET8Q22", 'rb')
        LoadedPlaylist = pickle.load(Load)
        
        for i in LoadedPlaylist:
            if(i == "Endurance"):

                EndurancePhoto = tk.PhotoImage(file = "Endurance.png")
                EnLabel = tk.Label(Day3, image = EndurancePhoto, bg="#FEE440")
                EnLabel.pack()
                EnLabel.keepimage = EndurancePhoto
            elif(i == "Strength"):

                StrengthPhoto = tk.PhotoImage(file = "Strength.png")
                StLabel = tk.Label(Day3, image = StrengthPhoto, bg="#FEE440")
                StLabel.pack()
                StLabel.keepimage = StrengthPhoto
            else:

                BalancePhoto = tk.PhotoImage(file = "Balance.png")
                BaLabel = tk.Label(Day3, image = BalancePhoto, bg="#FEE440")
                BaLabel.pack()
                BaLabel.keepimage = BalancePhoto
    else:
        LblD3 = tk.Label(Day3, text=d.strftime('%d-%m'), bg="#00BBF9", fg="#000000")
        LblD3.pack()
        pass



##############################################################################################DAY 4
    Day4 = tk.Frame(frame, padx=15, pady=15, bg="#00BBF9")
    Day4.place(width=80, height=450, x=245, y=0)
    
    d = datetime.datetime.strptime(LoadToday, '%d-%m-%Y') - datetime.timedelta(days=3)
    
    if os.path.exists(str(d.strftime('%d-%m-%Y'))+"p223ET8Q22") == True:
        LblD4 = tk.Label(Day4, text=d.strftime('%d-%m'), bg="#00BBF9", fg="#000000")
        LblD4.pack()
        
        Load = open(str(d.strftime('%d-%m-%Y'))+"p223ET8Q22", 'rb')
        LoadedPlaylist = pickle.load(Load)
        
        for i in LoadedPlaylist:
            if(i == "Endurance"):

                EndurancePhoto = tk.PhotoImage(file = "Endurance.png")
                EnLabel = tk.Label(Day4, image = EndurancePhoto, bg="#FEE440")
                EnLabel.pack()
                EnLabel.keepimage = EndurancePhoto
            elif(i == "Strength"):

                StrengthPhoto = tk.PhotoImage(file = "Strength.png")
                StLabel = tk.Label(Day4, image = StrengthPhoto, bg="#FEE440")
                StLabel.pack()
                StLabel.keepimage = StrengthPhoto
            else:

                BalancePhoto = tk.PhotoImage(file = "Balance.png")
                BaLabel = tk.Label(Day4, image = BalancePhoto, bg="#FEE440")
                BaLabel.pack()
                BaLabel.keepimage = BalancePhoto
    else:
        LblD4 = tk.Label(Day4, text=d.strftime('%d-%m'), bg="#00BBF9", fg="#000000")
        LblD4.pack()
        pass



##############################################################################################DAY 5
    Day5 = tk.Frame(frame, padx=15, pady=15, bg="#00BBF9")
    Day5.place(width=80, height=450, x=330, y=0)
    
    d = datetime.datetime.strptime(LoadToday, '%d-%m-%Y') - datetime.timedelta(days=4)
    
    if os.path.exists(str(d.strftime('%d-%m-%Y'))+"p223ET8Q22") == True:
        LblD5 = tk.Label(Day5, text=d.strftime('%d-%m'), bg="#00BBF9", fg="#000000")
        LblD5.pack()
        
        Load = open(str(d.strftime('%d-%m-%Y'))+"p223ET8Q22", 'rb')
        LoadedPlaylist = pickle.load(Load)
        
        for i in LoadedPlaylist:
            if(i == "Endurance"):

                EndurancePhoto = tk.PhotoImage(file = "Endurance.png")
                EnLabel = tk.Label(Day5, image = EndurancePhoto, bg="#FEE440")
                EnLabel.pack()
                EnLabel.keepimage = EndurancePhoto
            elif(i == "Strength"):

                StrengthPhoto = tk.PhotoImage(file = "Strength.png")
                StLabel = tk.Label(Day5, image = StrengthPhoto, bg="#FEE440")
                StLabel.pack()
                StLabel.keepimage = StrengthPhoto
            else:

                BalancePhoto = tk.PhotoImage(file = "Balance.png")
                BaLabel = tk.Label(Day5, image = BalancePhoto, bg="#FEE440")
                BaLabel.pack()
                BaLabel.keepimage = BalancePhoto
    else:
        LblD5 = tk.Label(Day5, text=d.strftime('%d-%m'), bg="#00BBF9", fg="#000000")
        LblD5.pack()
        pass


##############################################################################################DAY 6
    Day6 = tk.Frame(frame, padx=15, pady=15, bg="#00BBF9")
    Day6.place(width=80, height=450, x=415, y=0)
    
    d = datetime.datetime.strptime(LoadToday, '%d-%m-%Y') - datetime.timedelta(days=5)
    
    if os.path.exists(str(d.strftime('%d-%m-%Y'))+"p223ET8Q22") == True:
        LblD6 = tk.Label(Day6, text=d.strftime('%d-%m'), bg="#00BBF9", fg="#000000")
        LblD6.pack()
        
        Load = open(str(d.strftime('%d-%m-%Y'))+"p223ET8Q22", 'rb')
        LoadedPlaylist = pickle.load(Load)
        
        for i in LoadedPlaylist:
            if(i == "Endurance"):

                EndurancePhoto = tk.PhotoImage(file = "Endurance.png")
                EnLabel = tk.Label(Day6, image = EndurancePhoto, bg="#FEE440")
                EnLabel.pack()
                EnLabel.keepimage = EndurancePhoto
            elif(i == "Strength"):

                StrengthPhoto = tk.PhotoImage(file = "Strength.png")
                StLabel = tk.Label(Day6, image = StrengthPhoto, bg="#FEE440")
                StLabel.pack()
                StLabel.keepimage = StrengthPhoto
            else:

                BalancePhoto = tk.PhotoImage(file = "Balance.png")
                BaLabel = tk.Label(Day6, image = BalancePhoto, bg="#FEE440")
                BaLabel.pack()
                BaLabel.keepimage = BalancePhoto
    else:
        LblD6 = tk.Label(Day6, text=d.strftime('%d-%m'), bg="#00BBF9", fg="#000000")
        LblD6.pack()
        pass



##############################################################################################DAY 7
    Day7 = tk.Frame(frame, padx=15, pady=15, bg="#00BBF9")
    Day7.place(width=80, height=450, x=500, y=0)
    
    d = datetime.datetime.strptime(LoadToday, '%d-%m-%Y') - datetime.timedelta(days=6)
    
    if os.path.exists(str(d.strftime('%d-%m-%Y'))+"p223ET8Q22") == True:
        LblD7 = tk.Label(Day7, text=d.strftime('%d-%m'), bg="#00BBF9", fg="#000000")
        LblD7.pack()
        
        Load = open(str(d.strftime('%d-%m-%Y'))+"p223ET8Q22", 'rb')
        LoadedPlaylist = pickle.load(Load)
        
        for i in LoadedPlaylist:
            if(i == "Endurance"):

                EndurancePhoto = tk.PhotoImage(file = "Endurance.png")
                EnLabel = tk.Label(Day7, image = EndurancePhoto, bg="#FEE440")
                EnLabel.pack()
                EnLabel.keepimage = EndurancePhoto
            elif(i == "Strength"):

                StrengthPhoto = tk.PhotoImage(file = "Strength.png")
                StLabel = tk.Label(Day7, image = StrengthPhoto, bg="#FEE440")
                StLabel.pack()
                StLabel.keepimage = StrengthPhoto
            else:

                BalancePhoto = tk.PhotoImage(file = "Balance.png")
                BaLabel = tk.Label(Day7, image = BalancePhoto, bg="#FEE440")
                BaLabel.pack()
                BaLabel.keepimage = BalancePhoto
    else:
        LblD7 = tk.Label(Day7, text=d.strftime('%d-%m'), bg="#00BBF9", fg="#000000")
        LblD7.pack()
        pass

    
    
    
    def ViewDay():
        for widget in frame.winfo_children():
            widget.destroy()
        SorryLabel = tk.Label(frame, text="This Feature \nNot Yet Available", font=('Helvatical bold',20), bg="#000000", fg="#ffffff")
        SorryLabel.pack()
    
    def ViewWeek():
        for widget in frame.winfo_children():
            widget.destroy()
        SorryLabel = tk.Label(frame, text="This Feature \nNot Yet Available", font=('Helvatical bold',20), bg="#000000", fg="#ffffff")
        SorryLabel.pack()
    
    def ViewMonth():
        for widget in frame.winfo_children():
            widget.destroy()
        SorryLabel = tk.Label(frame, text="This Feature \nNot Yet Available", font=('Helvatical bold',20), bg="#000000", fg="#ffffff")
        SorryLabel.pack()

#############################################################################################GOALS PAGE
def Goals():
    for widget in frame.winfo_children():
        widget.destroy()
    btn = tk.Button(root, text="Add Goal", bg='#00BBF9', activebackground="#00F5D4")
    btn.config(height=2, width=25)
    btn.place(x=715, y=20)
    
    btn = tk.Button(root, text="Edit Goals", bg='#00BBF9', activebackground="#00F5D4")
    btn.config(height=2, width=25)
    btn.place(x=510, y=20)
    
    btn = tk.Button(root, text="Goals %Completed", bg='#00BBF9', activebackground="#00F5D4")
    btn.config(height=2, width=25)
    btn.place(x=300, y=20)
    
    SorryLabel = tk.Label(frame, text="This Feature \nNot Yet Available", font=('Helvatical bold',20), bg="#000000", fg="#ffffff")
    SorryLabel.pack()

#######################################################################################################################WORKOUTS PAGE##################################
def Workouts():
    for widget in frame.winfo_children():
        widget.destroy()
    btn = tk.Button(root, text="View Playlists", bg='#00BBF9', activebackground="#00F5D4")
    btn.config(height=2, width=25)
    btn.place(x=715, y=20)
    btn.bind("<Button>", lambda e: ViewPlaylists(root, 1))
    
    btn = tk.Button(root, text="Create Playlist", bg='#00BBF9', activebackground="#00F5D4")
    btn.config(height=2, width=25)
    btn.place(x=510, y=20)
    btn.bind("<Button>", lambda e: CreatePlaylist())
    
    btn = tk.Button(root, text="Edit Playlists", bg='#00BBF9', activebackground="#00F5D4")
    btn.config(height=2, width=25)
    btn.place(x=300, y=20)
    btn.bind("<Button>", lambda e: EditPlaylists())
    
def EditPlaylists():
    for widget in frame.winfo_children():
        widget.destroy()
    SorryLabel = tk.Label(frame, text="This Feature \nNot Yet Available", font=('Helvatical bold',20), bg="#000000", fg="#ffffff")
    SorryLabel.pack()
    
    
def CreatePlaylist():
    def TransferWorkout():
        if StrengthWorkout.curselection() != None:
            for i in StrengthWorkout.curselection():
                NewWorkList.insert('end', StrengthWorkout.get(i))
                
        if EnduranceWorkout.curselection() !=None:
            for i in EnduranceWorkout.curselection():
                NewWorkList.insert('end', EnduranceWorkout.get(i))
                
        if BalanceWorkout.curselection() !=None:
            for i in BalanceWorkout.curselection():
                NewWorkList.insert('end', BalanceWorkout.get(i))
    def DeleteSelection():
            NewWorkList.delete('active')
            
    def SavePlaylist():
        Playlist = NewWorkList.get(0, 'end')
        Saved = open(str(PlaylistTitle.get())+"7pQXk5jXt3", 'wb')
        pickle.dump(Playlist, Saved)
        Saved.close()
        LoadPlaylist()
    def LoadPlaylist(): #HOW TO LOAD A TUPLE IS RIGHT HERE##########################################TUPLE LOAD 
        Load = open(str(PlaylistTitle.get())+"7pQXk5jXt3", 'rb')
        LoadedPlaylist = pickle.load(Load)

        
        
    
    for widget in frame.winfo_children():
        widget.destroy()
    EnduranceWorkout = tk.Listbox(frame, height=7, bg='#FEE440')
    EnduranceWorkout.place(x=70, y=40)
    EnduranceWorkout.insert('end', "Plank")
    EnduranceWorkout.insert('end', "High Knees")
    EnduranceWorkout.insert('end', "Jumping Jacks")
    
    
    StrengthWorkout = tk.Listbox(frame, height=7, bg='#FEE440')
    StrengthWorkout.place(x=70, y=170)
    StrengthWorkout.insert('end', "Push Ups")
    StrengthWorkout.insert('end', "Squats")
    StrengthWorkout.insert('end', "Sit Ups")
    
    BalanceWorkout = tk.Listbox(frame, height=7, bg='#FEE440')
    BalanceWorkout.place(x=70, y=300)
    BalanceWorkout.insert('end', "Downward Dog")
    BalanceWorkout.insert('end', "Upward Dog")
    BalanceWorkout.insert('end', "Child's Pose")
    
    
    btn = tk.Button(frame, text="Add To Playlist", bg='#00BBF9', activebackground="#00F5D4", command= TransferWorkout)
    btn.config(height=2, width=15)
    btn.place(x=215, y=210)
    
    btn = tk.Button(frame, text="Delete Selection", bg='#00BBF9', activebackground="#00F5D4", command= DeleteSelection)
    btn.config(height=1, width=12)
    btn.place(x=365, y=120)
    
    btn = tk.Button(frame, text="Save Playlist", bg='#00BBF9', activebackground="#00F5D4", command= SavePlaylist)
    btn.config(height=2, width=15)
    btn.place(x=355, y=320)

    NewWorkList = tk.Listbox(frame, height=10, bg= '#FEE440', relief= 'raised')
    NewWorkList.place(x=350, y=150)

    TitleL = tk.Label(frame, text='Title Playlist:', fg='#FEE440', bg='#9B5DE5')
    TitleL.place(x=350, y=70)
    PlaylistTitle = tk.Entry(frame, bg='#00BBF9')
    PlaylistTitle.place(x=350, y=90)

class ViewPlaylists:
    def __init__(self, root, w):
        self.root = root
        self.w = w
        self.Wnum = 0
        
        self.frame = tk.Frame(self.root, padx=15, pady=15, bg="#9B5DE5")
        self.frame.place(width=600, height=500, x=300, y=75)
        
        for widget in self.frame.winfo_children():
            widget.destroy()
        
        self.Label = tk.Label(self.frame, text="Choose Playist: ", fg='#FEE440', bg='#9B5DE5')
        self.Label.place(x=10, y=0)
    
        self.Playlistbox = tk.Listbox(self.frame, height=15, bg='#FEE440')
        self.Playlistbox.place(x=10, y=20)
        
        self.btn = tk.Button(self.frame, text='Begin Workout Playlist', bg='#00BBF9', activebackground="#00F5D4", command=self.StartWorkout)
        self.btn.config(height=12, width=17)
        self.btn.place(x=8, y=270)
        
        self.Warning = tk.Label(self.frame, text="MUST HIT BUTTON TO CLOSE SECTION", fg='#FEE440', bg='#9B5DE5')
        self.Warning.place(x=350, y=25)
        
        self.btnQ = tk.Button(self.frame, text='QUIT', bg='#00BBF9', activebackground='#00F5D4', command=self.QuitClass)
        self.btnQ.config(height=1, width=4)
        self.btnQ.place(x=520, y=0)
        for file in os.listdir():
            if "7pQXk5jXt3" in file:
                self.Playlistbox.insert('end', file.replace("7pQXk5jXt3", ""))
    def QuitClass(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        self.frame.destroy()
        Workouts()
        
    
    def StartWorkout(self): 
        for i in self.Playlistbox.curselection():
            self.Picked = self.Playlistbox.get(i)
        
        self.Load = open(str(self.Picked)+"7pQXk5jXt3", 'rb')
        self.LoadedPlaylist = pickle.load(self.Load)

        
        self.LblWN = tk.Label(self.frame, text=self.LoadedPlaylist[self.Wnum], width=10, bg="#9B5DE5", fg="#FEE440", font=("Helvetica", 30))
        self.LblWN.place(y=100, x=150)
        
        self.LblT = tk.Label(self.frame, width=self.w, bg="#00BBF9", relief='raised')
        self.LblT.place(y=300, x=150)
        
        self.WTypes = []
        self.root.after(100, self.WorkoutTimer)
    
    def DestroyLabel(self):
        self.LblT.destroy()
    def WorkoutTimer(self):
        self.LblWN.configure(text=self.LoadedPlaylist[self.Wnum])
        self.LblT.configure(width=self.w)

        self.w += 1
        if self.w > 60:
#$$$$$$$$$$$$$$$$$$$$# write a file and track the workout to a day######$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

            
            if self.LoadedPlaylist[self.Wnum] == "Jumping Jacks" or self.LoadedPlaylist[self.Wnum] == "Plank" or self.LoadedPlaylist[self.Wnum] == "High Knees":
                self.WTypes.append("Endurance")
            elif self.LoadedPlaylist[self.Wnum] == "Push Ups" or self.LoadedPlaylist[self.Wnum] == "Squats" or self.LoadedPlaylist[self.Wnum] == "Sit Ups":
                self.WTypes.append("Strength")
            else:
                self.WTypes.append("Balance")

            
            self.Wnum += 1
            if self.Wnum >= (len(self.LoadedPlaylist)):
                self.today = date.today()
                self.SaveToday = self.today.strftime("%d-%m-%Y")       
                self.DayFile = open(str(self.SaveToday)+"p223ET8Q22", 'wb')
                pickle.dump(self.WTypes, self.DayFile)
                self.DayFile.close()

                self.Load = open(str(self.SaveToday)+"p223ET8Q22", 'rb')
                self.LoadedPlaylist = pickle.load(self.Load)

                
                return
            self.w = 1
            self.root.after(1000, self.WorkoutTimer)
        self.root.after(3000, self.WorkoutTimer)
        
################################################SIDE BUTTONS###########################################################SIDE BUTTONS###########
btn = tk.Button(root, text="Visual Calendar", bg='#00BBF9', activebackground="#00F5D4", command=Calendar)
btn.config(height=10, width=30)
btn.grid(row=0, column=0, padx=10, pady=20)

btn = tk.Button(root, text="Goals", bg='#00BBF9', activebackground="#00F5D4")
btn.config(height=10, width=30)
btn.grid(row=1, column=0, padx=10, pady=20)
btn.bind("<Button>", lambda e: Goals())

btn = tk.Button(root, text="Workout Playlists", bg='#00BBF9', activebackground="#00F5D4")
btn.config(height=10, width=30)
btn.grid(row=2, column=0, padx=10, pady=20)
btn.bind("<Button>", lambda e: Workouts())

btn = tk.Button(root, text="CCCCCCCCCCCCCCCCCCCCCC", bg='#00BBF9', activebackground="#00F5D4")
btn.config(height=2, width=25)
btn.place(x=715, y=20)

btn = tk.Button(root, text="CCCCCCCCCCCCCCCCCCCCCC", bg='#00BBF9', activebackground="#00F5D4")
btn.config(height=2, width=25)
btn.place(x=510, y=20)

btn = tk.Button(root, text="CCCCCCCCCCCCCCCCCCCCCC", bg='#00BBF9', activebackground="#00F5D4")
btn.config(height=2, width=25)
btn.place(x=300, y=20)

###############################################################################################################################FRAMEWITHINFRAME#############################
frame = tk.Frame(root, padx=15, pady=15, bg="#9B5DE5")
frame.place(width=600, height=500, x=300, y=75)

root.mainloop()