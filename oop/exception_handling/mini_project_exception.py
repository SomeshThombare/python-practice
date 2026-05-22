# class TooSmallAgeException(Exception):
#     def __init__(self, message):
#         super().__init__(message)

# class ToBigAgeException(Exception):
#     def __init__(self, message):
#         super().__init__(message)

class AgeException(Exception):
    def  __init__(self, message):
        super().__init__(message)

def play_car_racing_game(age):
    if age < 18 :
        raise AgeException("Your age is too samll to play game") #Exception object
    elif age > 50:
        raise AgeException('Your age is to big to play game')
    else:
        print('You can paly game...')

play_car_racing_game(8)
