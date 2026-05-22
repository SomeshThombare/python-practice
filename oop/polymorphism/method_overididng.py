class whatsapp:
    def status(self):
        print('Vertical ')

class NewWhatsapp(whatsapp):
    def status(self):   # method overrideed.......
        # super().status()
        print('Horizontal')

obj = NewWhatsapp()
obj.status()