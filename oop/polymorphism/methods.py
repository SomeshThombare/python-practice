class TV:
    def on(self):
        print('start TV')

class Projector:
    def on(self):
        print('start Projector')

class AC:
    def on(self):
        print('Start AC...')

def remote(obj):
    obj.on()

tv = TV()
remote(tv)

pr = Projector()
remote(pr)

ac = AC()
remote(ac)