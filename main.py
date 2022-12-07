def padel_court_cost(court_type):
 if court_type == "indoor":
       return 30 
 if court_type == 'outdoor':
   return 20

def rackets_cost(racket_brand):
    if racket_brand == "Bullpadel":
     return 100
    if racket_brand == "Nox":
        return 140
    if racket_brand == "Siux":
        return 200
def padel_balls_cost(ball_boxes):
    if ball_boxes == "1":
     return 2
    if ball_boxes =="2":
        return 3.5
    if ball_boxes =="3":
        return 5
# print(padel_balls_cost('box'))
def padel_game_cost():
    hours = input('hours : ')
    court_type = input("the court type : ")
    racket_brand = input('racket brand : ')
    ball_boxes = input('number of ball boxes: ')
    court =  padel_court_cost(court_type)
    racket= rackets_cost(racket_brand)
    ball = padel_balls_cost(ball_boxes)
    print(court + racket + ball)
padel_game_cost()


# print(padel_game_cost())