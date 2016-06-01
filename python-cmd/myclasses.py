# myclasses.py
# Kevin Kredit

class Projectile:

    def __init__(self,angle,velocity,height):
        '''Create a projectile object with given launch angle(degrees),
        velocity, and height.'''
        from math import pi,sin,cos
        self.xpos = 0.0
        self.ypos = height
        self.alt = height
        self.xvel = velocity*cos(angle*pi/180.0)
        self.yvel = velocity*sin(angle*pi/180.0)
        self.hang = 0.0

    def update(self,time):
        '''Update the position of the proj. object base on elapsed time.'''
        self.xpos += time*self.xvel
        self.yvel -= time*4.9
        self.ypos += time*self.yvel
        self.yvel -= time*4.9
        self.hang += time
        if self.ypos > self.alt: self.alt = self.ypos
        #return self.xpos,self.ypos

    def getY(self):
        '''Returns Y position of object'''
        return self.ypos

    def getX(self):
        '''Returns X position of object'''
        return self.xpos

    def maxalt(self):
        '''Returns the maximum height of object'''
        return self.alt

    def hangtime(self):
        '''Returns the air time of object'''
        return self.hang
