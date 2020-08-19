import random


class GenerateTrackingNumber():

    alpha = ['A', 'B', 'Q', 'W', 'E', 'R', 'Y', 'U', 'P', 'S', 'D', 'F', 'H', 'L', 'V', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    trackingNumber = ''

    def generate(self):
        GenerateTrackingNumber.resettrackingnumber(GenerateTrackingNumber)
        self.startcount = 1
        while self.startcount < 9:
            self.rand = random.choice(self.alpha)
            self.trackingNumber = self.rand + self.trackingNumber
            self.startcount += 1
        return self.trackingNumber

    def gettracknumber(self):
        self.trackingNumber = GenerateTrackingNumber.generate(GenerateTrackingNumber)
        return self.trackingNumber

    def resettrackingnumber(self):
        self.trackingNumber = ''
        return self.trackingNumber