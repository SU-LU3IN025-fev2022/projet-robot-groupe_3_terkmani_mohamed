# Projet "robotique" IA&Jeux 2021
#
# Binome:
#  Prénom Nom: Djamila Mohamed
#  Prénom Nom: Kamelia Terkmani

def get_team_name():
    return "groupe de travail" # à compléter (comme vous voulez)

def step(robotId, sensors):

    translation = 1 * sensors["sensor_front"]["distance_to_wall"]
    rotation = (-1) * sensors["sensor_front_left"]["distance_to_wall"] + (1) * sensors["sensor_front_right"]["distance_to_wall"]

    if sensors["sensor_front"]["isRobot"] == True and sensors["sensor_front"]["isSameTeam"] == False:
        enemy_detected_by_front_sensor = True # exemple de détection d'un robot de l'équipe adversaire (ne sert à rien)

    return translation, rotation
