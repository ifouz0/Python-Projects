import random
import os

NUM_CUBES = 6                   # Número total de cubos disponibles

competitor_name = ""            # Nombre del participante
initial_quantity = 0            # Cantidad de dinero inicial del participante
current_quantity = 0            # Cantidad de dinero actual del participante
current_bet = 0                 # Apuesta actual del participante
total_games = 0                 # Número total de partidas jugadas
win_games = 0                   # Cantidad de partidas ganadas por el participante
loses_games = 0                 # Cantidad de partidas perdidas por el participante
current_cube = 0                # Cubo en el que se encuentra la bola
selected_cube = 0               # Cubo seleccionado por el participante

os.system("clear")

print("*" * 150)
print("*" * 150)
print(f"{'P Y T H O N   S H E L L F I S H   V 1.0':^150}")
print("*" * 150)
print("*" * 150)

competitor_name = input(">¿Cuál es tu nombre amigo? ")
print(f"¡Bienvenido, {competitor_name}!. Te informo que hay {NUM_CUBES} cubos en juego :)")

correct_quantity = False
while not correct_quantity:
    try: 
        initial_quantity = int(input(f">¿Cuánto dinero quieres jugar, {competitor_name}? "))   
        if initial_quantity <= 0:
            print(F"ERROR: Por favor, no puedes jugar con {initial_quantity} euros. Elige una cantidad de dinero positiva.")       
            continue
        correct_quantity = True
        current_quantity = initial_quantity
    
    except ValueError as ex:
        print(F"ERROR: Por favor, debes elegir un valor numérico positivo como cantidad de dinero.")       

play_game = True
while play_game:
    print()
    print(F"{'##':^25}" * NUM_CUBES)
    print(F"{'####':^25}" * NUM_CUBES)
    print(F"{'######':^25}" * NUM_CUBES)
    print(F"{'########':^25}" * NUM_CUBES)
    for i in range(1, NUM_CUBES + 1): 
        print(f"{i:^25}", end = "")
    
    print()
    print("\n¿Donde está la pelota? ¿aquí o allí? ¿Donde está la pelota? ¿aquí o allí?")
    print("Venga hagan sus apuestas... que me quitan el dinero de las manos.\n")
    
    # Incrementamos el número de partidas en 1
    total_games += 1
    
    # Seleccionamos el cubo donde guardamos la bola
    current_cube = random.randint(1, NUM_CUBES)
    
    # Solicitamos la cantidad a apostar
    correct_bet = False
    while not correct_bet:
        try:
            print("-" * 150)
            current_bet = int(input(f">Te quedan {current_quantity} euros. ¿Cuánto dinero quieres apostar {competitor_name}? "))
            print("-" * 150)  
            if (current_bet < 1 or current_bet > current_quantity):
                print(F"Jaja..no me lo pongas tán fácil. Has elegido apostar {current_bet}. Por favor vuelve a elegir!!")
                continue    

            correct_bet = True
            print(F"{competitor_name}, has decidido apostar {current_bet} euros. A ver si los ganas o los pierdes")
        
        except ValueError as ex:
            print(F"ERROR: Por favor, debes elegir un valor numérico positivo como cantidad de dinero.")       
        
    # Preguntamos el cubo donde cree que esta la pelota
    correct_cube = False
    while not correct_cube:
        try:
            print("-" * 150)
            selected_cube = int(input(f">¿En que cubo está la pelota {competitor_name}? (1-{NUM_CUBES}) "))
            print("-" * 150)
            
            if (selected_cube < 1 or selected_cube > NUM_CUBES):
                print(F"ERROR: Jaja..no me lo pongas tán fácil. Has elegido el cubo {selected_cube} que no existe. Por favor vuelve a elegir!!")
                continue
            
            correct_cube = True
            print(F"{competitor_name}, has elegido el curso {selected_cube}. Vamos a ver si hay suerte")

        except ValueError as ex:
            print(F"ERROR: Por favor, debes elegir un valor numérico positivo como cantidad de dinero.")       


    # Determinamos si ha ganado o no
    if (current_cube == selected_cube) :
        current_quantity += current_bet # Actualizamos la cantidad disponible del concursante
        win_games +=1                   # Actualizamos el número de partidas ganadas
        print(F"Enhorabuena {competitor_name}, has acertado!!!La pelotita se encontraba en el cubo C{current_cube}.\n")
    else:
        current_quantity -= current_bet  #Actualizamos la cantidad disponible del concursante
        loses_games +=1                  #Actualizamos el número de partidas perdidas
        print(F"Lo siento mucho {competitor_name}, has fallado!!!. La pelotita se encontraba en el cubo C{current_cube} y tu elegiste el cubo C{selected_cube}\n")


    # Mostramos estadísticas
    print("-" * 150)
    print(f"---> Cantidad inicial: {initial_quantity} euros")
    print(f"---> Cantidad actual: {current_quantity} euros")
    print(f"---> Beneficios/Perdidas: {current_quantity - initial_quantity} euros")
    print(f"---> Partidas jugadas: {total_games} partidas")
    print(f"---> Partidas ganadas: {win_games} victorias ({win_games/total_games:.2%} victorias)")
    print(f"---> Partidas perdidas: {loses_games} derrotas ({loses_games/total_games:.2%} derrotas)")
    print("-" * 150)
    
    if current_quantity == 0 :
        print(f"\n\n----->Lo siento mucho {competitor_name} te has quedado sin dinero!!!!!!!!. Debes abandonar la mesa de juego.")
        play_game = False
        exit()

    
    finish = input(f"¿Deseas abandonar la partida {competitor_name}? (S/N) ")
    if (finish.upper() == "S"): play_game = False
    
    os.system("clear")

else:
    print("-" * 150)
    print(f"Gracias {competitor_name} por haber jugado con nosotros. Esperamos volverte a ver pronto!!")
    print("-" * 150)
       