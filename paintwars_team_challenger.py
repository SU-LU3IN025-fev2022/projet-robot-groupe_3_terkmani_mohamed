# Projet "robotique" IA&Jeux 2021
#
# Binome:
#  Prénom Nom: Kamelia Terkmani
#  Prénom Nom: Djamila Mohamed
import random




def get_team_name():
    return "Fairy Tail" # à compléter (comme vous voulez)

# Pour recuperer distance_to_robot et distance_to_wall
def get_extended_sensors(sensors):
    for key in sensors:
        sensors[key]["distance_to_robot"] = 1.0
        sensors[key]["distance_to_wall"] = 1.0
        if sensors[key]["isRobot"] == True:
            sensors[key]["distance_to_robot"] = sensors[key]["distance"]
        else:
            sensors[key]["distance_to_wall"] = sensors[key]["distance"]
    return sensors


#Taches : longer les murs et suivre les ennemis 
def longer_murs(translation,rotation,sensors):

    sensors = get_extended_sensors(sensors)
    #Si obstacle du coté droit tourner à gauche d'un angle 90° (rotation = -0.5)
    if sensors["sensor_front_right"]["distance"] < 1:
        rotation = -0.5  # rotation vers la gauche
        return translation,rotation

	#Si ennemi repéré le suivre en utilisant loveBot
    if (sensors["sensor_front"]["isRobot"] == True and sensors["sensor_front"]["isSameTeam"] == False) or (sensors["sensor_front_left"]["isRobot"] == True and sensors["sensor_front_left"]["isSameTeam"] == False) or (sensors["sensor_front_right"]["isRobot"] == True and sensors["sensor_front_right"]["isSameTeam"] == False) :
        translation = 1
        rotation = ((1) * sensors["sensor_front_left"]["distance_to_robot"]) + ((-1) * sensors["sensor_front_right"]["distance_to_robot"]) #+ (1 * sensors["sensor_front"]["distance_to_robot"])
        return translation, rotation
	#s'il est suivi il s'arrete afin de bloquer l'ennemi
    if(sensors["sensor_back"]["isRobot"] and not sensors["sensor_back"]["isSameTeam"]):
    	return 0,0
	
	#Si mur en face
    if (sensors["sensor_front"]["distance_to_wall"] < 1):
        # Si obstacle à gauche tourner à droite de 90°
    	if(sensors["sensor_left"]["distance"] < 1):
    		return 1, 0.5
        # Si obstacle à droite tourner à gauche de 90°
    	if(sensors["sensor_right"]["distance"] < 1):
    		return 1, -0.5
	
	#Si couloir continuer tout droit
    if(sensors["sensor_right"]["distance_to_wall"] == 1 and sensors["sensor_left"]["distance_to_wall"] == 1 and sensors["sensor_front"]["distance_to_wall"] == 1) and (sensors["sensor_front_left"]["distance_to_wall"] < 1 and sensors["sensor_front_right"]["distance_to_wall"] < 1):
    	return 1,0
	
	#Si on est dans un couloir
    if(sensors["sensor_right"]["distance_to_wall"] < 1 and sensors["sensor_left"]["distance_to_wall"] < 1) or (sensors["sensor_front_left"]["distance_to_wall"] < 1 and sensors["sensor_front_right"]["distance_to_wall"] < 1):
        translation = 1
        rotation = 0
        # Si obstacle à gauche tourner à droite
        if sensors["sensor_front_left"]["distance_to_wall"] < 1 or sensors["sensor_front"]["distance_to_wall"] < 1:
    	    rotation = 0.5 
        # Si obstacle à droite tourner à gauche
        elif sensors["sensor_front_right"]["distance"] < 1:
    	    rotation = -0.5  
        return translation, rotation

	#Cas où il y a un trou sur la gauche
    if(sensors["sensor_back_left"]["distance_to_wall"] < 1 and sensors["sensor_left"]["distance_to_wall"] == 1):
    	return 1,-1
	
	#Cas où il y a un mur en face 
    if(sensors["sensor_front"]["distance_to_wall"] < 1):
    	return 0,1
	
	# comportement hatewall
    if (sensors["sensor_left"]["distance_to_wall"] < 0.5) or (sensors["sensor_right"]["distance_to_wall"] < 0.5) or (sensors["sensor_front_right"]["distance_to_wall"] < 0.5) or (sensors["sensor_front_left"]["distance_to_wall"] < 0.5):
        translation = 1
        rotation = ((-1) * sensors["sensor_front_left"]["distance_to_wall"]) + ((-1) * sensors["sensor_back_left"]["distance_to_wall"]) + ((1) * sensors["sensor_back_right"]["distance_to_wall"]) + ((1) * sensors["sensor_front_right"]["distance"])
        return translation,rotation


	#comportement lovewall
    if (sensors["sensor_front_left"]["distance_to_wall"] < 1) or (sensors["sensor_front_right"]["distance_to_wall"] < 1):
        translation = 1
        rotation = ((1) * sensors["sensor_front_left"]["distance_to_robot"]) + ((-1) * sensors["sensor_front_right"]["distance_to_robot"]) 
        return translation, rotation
    if sensors["sensor_right"]["distance_to_wall"]<1:
    	return 1, 0.5
    if sensors["sensor_left"]["distance_to_wall"]<1:
    	return 1, -0.5
    return 1,0





def step(robotId, sensors):
  # Comportement de base Breitenberg
  # 1- Si le robot est un allié : Le fuir
  # 2 - Si le robot est un ennemi : Le suivre
  # 3- Eviter les murs
    
    translation = 1 * sensors["sensor_front"]["distance"]
    rotation = (1) * sensors["sensor_front_left"]["distance"] + (-1) * sensors["sensor_front_right"]["distance"]
 

    if  robotId==0 :

     
        """
            l'ordre de priorité:
                1- EVITER LES MUR
                2- SUIVRE LES ENNEMIES
                3- NE PAS BLOQUER MES AMIS
            
        """

        translation = 1
        rotation = 0
        if (sensors["sensor_front"]["distance"] < 1):
            if (sensors["sensor_front"]["isRobot"] == False):  # mur
                rotation = 1 - sensors["sensor_front"]["distance"]
            else:#robot
                if (sensors["sensor_front"]["isSameTeam"]==False): #robot ennemi
                    rotation = 0
                else:#robot ami
                    rotation = 1 - sensors["sensor_front"]["distance"]           

        elif (sensors["sensor_front_left"]["distance"] < 1):
            if (sensors["sensor_front_left"]["isRobot"] == False):  # mur
                rotation = 0.5-sensors["sensor_front_left"]["distance"]
            else:#robot
                if (sensors["sensor_front_left"]["isSameTeam"]==False): #robot ennemi
                    translation = 1 
                    rotation = (-1 + sensors["sensor_front_left"]["distance"])
                else:#robot ami
                    rotation = -(-1 + sensors["sensor_front_left"]["distance"])
                    #rotation = random.choice([-1, 1]) 


        elif (sensors["sensor_front_right"]["distance"] < 1):
            if (sensors["sensor_front_right"]["isRobot"] == False):  # mur
                rotation = -(0.5-sensors["sensor_front_left"]["distance"])
            else:#robot
                if (sensors["sensor_front_right"]["isSameTeam"]==False): #robot ennemi
                    translation = 1 
                    rotation = (1 - sensors["sensor_front_right"]["distance"])
                else:#robot ami
                    rotation = -(1 - sensors["sensor_front_right"]["distance"])

            
        return translation, rotation
    
    """
            Robot 1 et 5 longent les murs
    """


    if (robotId == 1 or robotId==5):
        longer_murs(translation,rotation,sensors)

    """
            l'ordre de priorité:
                1- NE PAS BLOQUER MES AMIS
                2- SUIVRE LES ENNEMIES
                3- EVITER LES MUR
                
                
            
    """

    #Enemies
    # sensor front 
    if sensors["sensor_front"]["isRobot"] == True and sensors["sensor_front"]["isSameTeam"] == False:
        translation = 1
        rotation = 0
        return translation,rotation
    # sensor front left
    elif sensors["sensor_front_left"]["isRobot"] == True and sensors["sensor_front_left"]["isSameTeam"] == False:
        translation = 1 
        rotation = -(1- sensors["sensor_front_left"]["distance"])
        return translation,rotation

    # sensor front right
    elif sensors["sensor_front_right"]["isRobot"] == True and sensors["sensor_front_right"]["isSameTeam"] == False:
        translation = 1 
        rotation = 1- sensors["sensor_front_right"]["distance"]
        return translation,rotation
    
    # sensor back
    elif sensors["sensor_back"]["isRobot"] == True and sensors["sensor_back"]["isSameTeam"] == False:
        translation = 0
        rotation = 0
        return translation,rotation
    # sensor back left
    elif sensors["sensor_back_left"]["isRobot"] == True and sensors["sensor_back_left"]["isSameTeam"] == False:
        translation = -1
        rotation = -(1- sensors["sensor_back_left"]["distance"])
        return translation,rotation
    # sensor back right
    elif sensors["sensor_back_right"]["isRobot"] == True and sensors["sensor_back_right"]["isSameTeam"] == False:
        translation = -1
        rotation = 1- sensors["sensor_back_right"]["distance"]
        return translation,rotation
    
    #Alliés
    # sensor front 
    elif sensors["sensor_front"]["isRobot"] == True and sensors["sensor_front"]["isSameTeam"] == True:
        translation = 1
        rotation = 0
        if sensors["sensor_front"]["distance"] < 1:
            rotation =1 - sensors["sensor_front"]["distance"]
            return translation,rotation
    

    # sensor front left
    
    elif sensors["sensor_front_left"]["isRobot"] == True and sensors["sensor_front_left"]["isSameTeam"] == True:
        translation = 1
        if sensors["sensor_front_left"]["distance"] < 1 :
            rotation = 1- sensors["sensor_front_left"]["distance"]
        return translation,rotation
    # sensor front right
    elif sensors["sensor_front_right"]["isRobot"] == True and sensors["sensor_front_right"]["isSameTeam"] == True:
        translation = 1
        if sensors["sensor_front_right"]["distance"] < 1:
            rotation = -(1 - sensors["sensor_front_right"]["distance"])
        return translation,rotation
    # sensor right
    elif sensors["sensor_right"]["isRobot"] == True and sensors["sensor_right"]["isSameTeam"] == True:
        translation = 1
        if sensors["sensor_right"]["distance"] < 1:
            rotation = -(1 - sensors["sensor_right"]["distance"])
        return translation,rotation
    # sensor left
    elif sensors["sensor_left"]["isRobot"] == True and sensors["sensor_left"]["isSameTeam"] == True:
        translation = 1
        if sensors["sensor_left"]["distance"] < 1:
            rotation = 1 - sensors["sensor_left"]["distance"]
        return translation,rotation
    
       #Murs 
    else :
        	#cas où il y a un mur en face
        if (sensors["sensor_front"]["distance"] < 1):
    	    if(sensors["sensor_left"]["distance"] < 1):
    		    return 1, 0.5
    	    if(sensors["sensor_right"]["distance"] < 1):
    		    return 1, -0.5
	
	    # Si couloir
        if(sensors["sensor_right"]["distance"] == 1 and sensors["sensor_left"]["distance"] == 1 and sensors["sensor_front"]["distance"] == 1) and (sensors["sensor_front_left"]["distance"] < 1 and sensors["sensor_front_right"]["distance"] < 1):
    	    return 1,0
        
        if(sensors["sensor_back_left"]["distance"] < 1 and sensors["sensor_left"]["distance"] == 1):
    	    return 1,-1
    
        elif (sensors["sensor_front_right"]["distance"]<1 or sensors["sensor_front_left"]["distance"]<1 or sensors["sensor_front"]["distance"]<1):#un mur
          

                
            if sensors["sensor_front"]["distance"]<1:#un mur in front 
                rotation =1 - sensors["sensor_front"]["distance"]*random.choice([-1, 1])

            if sensors["sensor_front_left"]["distance"]<1:#un mur à gauche
                rotation = (1 - sensors["sensor_front_left"]["distance"])

            else:
                if sensors["sensor_front_right"]["distance"]<1:#un mur à droite
                    rotation = -(1 - sensors["sensor_front_right"]["distance"])
                



        

  
        
    translation = max(-1,min(translation,1))
    rotation = max(-1, min(rotation, 1))
        
      
           

    

    return translation, rotation
