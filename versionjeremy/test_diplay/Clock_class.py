import datetime,time
import display


#datetime/time librairie venant d'internet permet de travailler date et heures/time pour gerer les pauses et attendre une seconde pour mettre à jour l'horloge
#display fichier importe du projet faite manuellement : il sert à afficher des infos utilisateurs pour afficher heures et entrees des données utilisateurs

"""
class objet clock
"""

class Clock:

    
    """
    input : tuple, int, str, bool
    represente une horloge pour afficher heure manuellement ou automatiquement
    """

    def __init__(self, clock, ampm_hour, format, mode):

        """
        initialisation de la class constructeur clock
        """

        self.clock = clock # horloge au format tuple(h,m,s)
        self.ampm_hour = ampm_hour#heure au format 12h
        self.format = format # AM/PM ou 24h
        self.mode = mode # True pour le mode 12h, False pour le mode 24h

    """
    def: 
    input: datetime
    """
    def clock_ticking(self, clock_datetime):
        #mise à jour de l'heure
        clock_datetime = clock_datetime + datetime.timedelta(seconds=1) #ajout 1s
        self.clock = (clock_datetime.strftime('%H'), clock_datetime.strftime('%M'), clock_datetime.strftime('%S'))#strftime formate le tuple en chaine de caractere
        
        # %I = hour in 12h format   formate l'heure en am/pm
        self.ampm_hour = clock_datetime.strftime('%I') 
        # %p = AM/PM recupere le format
        self.format = clock_datetime.strftime('%p') 

    def display_clock(self, event):
        #affichage de l'heure en continu
        while True:
            event.wait() #attend que mon even se déclenche
            clock_datetime = datetime.datetime(1970, 1, 1, int(self.clock[0]), int(self.clock[1]), int(self.clock[2])) #convention en informatique de prendre en base 1/1/1970
                            #conversion en type datetime 
            #format d'affichage qui dépend de mode
            if self.mode == False:
                display.clock_24h(self)
            else:
                display.clock_12h(self)
                
            self.clock_ticking(clock_datetime)

            time.sleep(1) #temps d'attente 1s

    def change_clock(self):
        #configuration heure horloge
        while True:
            clock_config = display.input_clock_config() #input sur display
            # Demande à l'utilisateur s'il veut une configuration automatique ou manuelle

            if clock_config == "automatique" or clock_config == "auto" or clock_config == "a":
                current_time = datetime.datetime.now() # Récupère l'heure actuelle
                self.clock = (current_time.strftime("%H"), current_time.strftime("%M"), current_time.strftime("%S"))
                return
            
            elif clock_config == "manuel" or clock_config == "m":
                while True:
                    user_clock = display.input_user_clock() #input display
                    # Demande à l'utilisateur de saisir l'heure manuellement

                        
                    #Verify if it's a number
                    try:
                        test = int(user_clock)
                    except Exception:
                        display.error_NaN()
                        continue

                    #Verify if it's a valid hour with datetime error directly
                    try:
                        # [0,1,2,3,4,5]
                        # [:2]= [0,1]
                        # [:4] =[0,1,2,3]
                        # [2:4] =  [2,3]
                        # [4:] = [4,5]
                        test = datetime.datetime(1970, 1, 1, int(user_clock[:2]), int(user_clock[2:4]), int(user_clock[4:]))
                    except Exception:
                        display.error_invalid_time()
                        continue

                    #Verify if the input contain exactly 6 numbers
                    if len(user_clock) != 6:
                        display.error_number_length()
                        continue

                    if self.mode == True:  # Vérifie si l'entrée contient uniquement des chiffres
                        user_format = display.input_user_format(user_clock)
                        
                        if user_format != "AM" and user_format != "PM": 
                            display.error_format()# Affiche une erreur si le format est invalide
                            continue

                        self.format = user_format
                        #A = ante et P = post
                        if user_format == "PM" and user_clock[:2] != "12":
                            user_clock = str(int(user_clock[:2])+12) + user_clock[2:]
                        elif user_format == "AM" and user_clock[:2] == "12":
                            user_clock[:2] = "00"

                    display.message_clock_valid() # Confirme que l'heure a été modifiée
                    
                    self.clock = (user_clock[:2], user_clock[2:4], user_clock[4:]) # Met à jour l'heure
                    return    
            
            else:
                continue