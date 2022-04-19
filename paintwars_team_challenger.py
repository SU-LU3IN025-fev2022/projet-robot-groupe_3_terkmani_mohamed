# Projet "robotique" IA&Jeux 2021
#
# Binome:
#  Prénom Nom: Djamila Mohamed
#  Prénom Nom: Kamelia Terkmani
import random

def get_extended_sensors(sensors):
    for key in sensors:
        sensors[key]["distance_to_robot"] = 1.0
        sensors[key]["distance_to_wall"] = 1.0
        if sensors[key]["isRobot"] == True:
            sensors[key]["distance_to_robot"] = sensors[key]["distance"]
        else:
            sensors[key]["distance_to_wall"] = sensors[key]["distance"]
    return sensors

def get_team_name():
    return "groupe de travail" # à compléter (comme vous voulez)

def step(robotId, sensors):
    #sensors = get_extended_sensors(sensors)
    translation = 1 # vitesse de translation (entre -1 et +1)
    rotation = 0 #random.randint(-1,1) # vitesse de rotation (entre -1 et +1)

    #if sensors["sensor_front_left"]["distance"] < 1 or sensors["sensor_front"]["distance"] < 1:
    #    rotation = 0.5  # rotation vers la droite
    #elif sensors["sensor_front_right"]["distance"] < 1:
    #    rotation = -0.5  # rotation vers la gauche

    # sensor front
    if sensors["sensor_front"]["isRobot"] == True:
        if sensors["sensor_front"]["isSameTeam"] == False:
            enemy_detected_by_front_sensor = True # exemple de détection d'un robot de l'équipe adversaire (ne sert à rien)

            translation = 1 * sensors["sensor_front"]["distance"]
            rotation = (1) * sensors["sensor_front_left"]["distance"] + (-1) * sensors["sensor_front_right"]["distance"]

        else :
            translation = 1 * sensors["sensor_front"]["distance"]
            rotation = (-1) * sensors["sensor_front_left"]["distance"] + (1) * sensors["sensor_front_right"]["distance"]

    elif sensors["sensor_front"]["isRobot"] == False and sensors["sensor_front"]["distance"] < 1:

        translation = 1 * sensors["sensor_front"]["distance"]
        rotation = (-1) * sensors["sensor_front_left"]["distance"] + (1) * sensors["sensor_front_right"]["distance"]

    # sensor front left
    elif sensors["sensor_front_left"]["isRobot"] == True:
        if sensors["sensor_front_left"]["isSameTeam"] == False:
            enemy_detected_by_front_sensor = True

            translation = 1 * sensors["sensor_front"]["distance"]
            rotation = (1) * sensors["sensor_front_left"]["distance"] + (-1) * sensors["sensor_front_right"]["distance"]

        else :
            translation = 1 * sensors["sensor_front"]["distance"]
            rotation = (-1) * sensors["sensor_front_left"]["distance"] + (1) * sensors["sensor_front_right"]["distance"]

    elif sensors["sensor_front_left"]["isRobot"] == False and sensors["sensor_front_left"]["distance"] < 1:

        translation = 1 * sensors["sensor_front"]["distance"]
        rotation = (-1) * sensors["sensor_front_left"]["distance"] + (1) * sensors["sensor_front_right"]["distance"]

    # sensor front right
    elif sensors["sensor_front_right"]["isRobot"] == True:
        if sensors["sensor_front_right"]["isSameTeam"] == False:
            enemy_detected_by_front_sensor = True

            translation = 1 * sensors["sensor_front"]["distance"]
            rotation = (1) * sensors["sensor_front_left"]["distance"] + (-1) * sensors["sensor_front_right"]["distance"]

        else :
            translation = 1 * sensors["sensor_front"]["distance"]
            rotation = (-1) * sensors["sensor_front_left"]["distance"] + (1) * sensors["sensor_front_right"]["distance"]

    elif sensors["sensor_front_right"]["isRobot"] == False and sensors["sensor_front_right"]["distance"] < 1:

        translation = 1 * sensors["sensor_front"]["distance"]
        rotation = (-1) * sensors["sensor_front_left"]["distance"] + (1) * sensors["sensor_front_right"]["distance"]

    # sensor back
    if sensors["sensor_back"]["isRobot"] == True:
        if sensors["sensor_back"]["isSameTeam"] == False:
            enemy_detected_by_front_sensor = True # exemple de détection d'un robot de l'équipe adversaire (ne sert à rien)

            translation = 1 * sensors["sensor_back"]["distance"]
            rotation = (1) * sensors["sensor_back_left"]["distance"] + (-1) * sensors["sensor_back_right"]["distance"]

        else :
            translation = 1 * sensors["sensor_back"]["distance"]
            rotation = (-1) * sensors["sensor_back_left"]["distance"] + (1) * sensors["sensor_back_right"]["distance"]



    # sensor back left
    elif sensors["sensor_back_left"]["isRobot"] == True:
        if sensors["sensor_back_left"]["isSameTeam"] == False:
            enemy_detected_by_front_sensor = True

            translation = 1 * sensors["sensor_back"]["distance"]
            rotation = (1) * sensors["sensor_back_left"]["distance"] + (-1) * sensors["sensor_back_right"]["distance"]

        else :
            translation = 1 * sensors["sensor_back"]["distance"]
            rotation = (-1) * sensors["sensor_back_left"]["distance"] + (1) * sensors["sensor_back_right"]["distance"]



    # sensor back right
    elif sensors["sensor_back_right"]["isRobot"] == True:
        if sensors["sensor_back_right"]["isSameTeam"] == False:
            enemy_detected_by_front_sensor = True

            translation = 1 * sensors["sensor_back"]["distance"]
            rotation = (1) * sensors["sensor_back_left"]["distance"] + (-1) * sensors["sensor_back_right"]["distance"]

        else :
            translation = 1 * sensors["sensor_back"]["distance"]
            rotation = (-1) * sensors["sensor_back_left"]["distance"] + (1) * sensors["sensor_back_right"]["distance"]




    translation = max(-1, min(translation, 1))
    rotation = max(-1, min(rotation, 1))

    return translation, rotation
