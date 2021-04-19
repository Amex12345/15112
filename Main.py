import random
from ursina import *

#Global Variables
score=0
num=0
i=2
superi=1
dy=1
###################3


app=Ursina()
cmd=load_texture("Assets/images (2).jpeg")
serkan=load_texture('Assets/serkan.jpg')
jeff=load_texture('Assets/jeff.jpg')
Anis=load_texture('Assets/Anis.jpg')
Ausgusto=load_texture('Assets/Augusto.jpg')
download=load_texture('Assets/download.jpg')
dudley=load_texture('Assets/dudley.jpg')
farooqi=load_texture('Assets/Farooqi.jpg')
varoon=load_texture('Assets/varoon.jpg')
enemyPic=load_texture('Assets/images.png')
kira=load_texture('Assets/Kira.jpg')
Lauren=load_texture('Assets/lauren.jpg')
Oliver=load_texture('Assets/Oliver.jpg')
Patric=load_texture('Assets/patric.jpg')
reley=load_texture('Assets/reley.jpg')
coin1=load_texture('Assets/bitcoin.jpeg')
hole=load_texture('Assets/hole.jpeg')
brick=load_texture('Assets/brigde.jpg')
theSky=load_texture('Assets/download (1).jpeg')
enemy1=load_texture('Assets/enemy.png')
skyda=load_texture('Assets/sku.jpg')
enemyPlane=load_texture('Assets/alien.png')



mod=load_model("Assets/aircraft.obj")
enemy2=load_texture('Assets/airplane.png')
enemyFaces=[serkan,jeff,Anis,Ausgusto,download,dudley,farooqi,varoon,enemyPic,kira, Lauren, Oliver, Patric, reley]





#ball moves itself forward and rotates (somewhat like in vacume)
#AWSD are controllers 
#if you touch the boarder of tunnel it will make you jump a little bit
#if you touch obstacle game will not stop however, it will say GAME LOST


num=0

class theHero(Entity):
    def __init__(self, superAttack=False):
        self.superAttack=superAttack
        self.boardings=True
        self.supersonic=False
        self.isAlive=True
        
        super().__init__(
            
            model=mod,
            parent=scene,
            texture=enemy2,
            color=color.rgba(223, 35, 148),
            position=(0,4,0),
            origin_y=3,
            scale=0.005,
            collider='box',
            gravity=1,
            hit=False,
            speed=20,
            jumping=True,
            jump_height=2,
            jump_duration=0.5
            )


    def input(self, key):
        global num
        if key == 'space' or num>100:
            num=0
            self.boardings=False
            theHole=blackHole(position=Vec3(0, hero.y-2, hero.z+299))
            self.animate_z(self.z+300, duration=1)

            # theHole=blackHole(position=Vec3(0, hero.y-2, hero.z+299))

            

            
            self.boardings=True




    def update(self):
        global dy
        if self.isAlive:
            # if not self.supersonic:
            if held_keys['up arrow']: 
                self.y+=time.dt*5
                self.rotation_x-=time.dt*self.speed*2

            if held_keys['down arrow']: 
                self.y-=time.dt*5
                self.rotation_x+=time.dt*self.speed*2
                
            
                # if held_keys['w']:
                #     self.y+=time.dt*40
                    
                # self.rotation_x+=time.dt*180
            
            if held_keys["right arrow"]: 
                self.x+=time.dt*5
                self.rotation_z+=time.dt*self.speed*6

        
            if held_keys["left arrow"]: 
                    self.x-=time.dt*5
                    self.rotation_z-=time.dt*self.speed*6

            if held_keys['a']:
                self.rotation_z-=time.dt*self.speed*12
            if held_keys['d' ]:
                self.rotation_z+=time.dt*self.speed*12

            self.z+=time.dt*self.speed
        
        
            
        
        yValue=4
        if self.supersonic == True:
            yValue=-15
            # if  self.y>-17:
            #     self.y-=time.dt*dy
            #     dy+=1.5

            #     if 17-abs(self.y)<time.dt*dy:
            #         self.y=-17
            #         dy=1
                
            

        camera.position=Vec3(camera.x, yValue, self.z-30)













class ground(Entity):
    def __init__(self, position=(0,0,0)):
        super().__init__(
            parent=scene,
            position=position,
            model="cube",
            scale=Vec3(20,50,0.5),
            color=color.white,
            texture=brick,
            rotation=(90,0,0),
            collider='box',
        )
    def update(self):
        groundhit=self.intersects()
        # global dy
        # if hero.supersonic:
        #     if not groundhit.hit:
        #         hero.y-=time.dt*dy
        #         dy+=1
        #         if abs(self.y)-abs(hero.y)<time.dt*dy:
        #             hero.y=self.y



def supersonicBoard(n):
    for i in range(n, n+3):
        board=ground(position=Vec3(0,-21, 50*i))

# supersonicBoard(1)
    


''' regular tunnel'''


def createBoard(z):
    c1=Entity(model="cube", scale=Vec3(3,100,0.5), rotation=Vec3(90,0,0), texture=cmd, position=Vec3(0,0,z), collider='box', color=color.random_color())
    c2=Entity(model="cube", scale=Vec3(3,100,0.5), rotation=Vec3(-75,-90,90), texture=cmd, position=Vec3(2.3,0.3,z),collider='box',color=color.random_color() )
    c3=Entity(model="cube", scale=Vec3(3,100,0.5), rotation=Vec3(-28,-90,90), texture=cmd, position=Vec3(4,1.8,z), collider='box',color=color.random_color())
    c4=Entity(model="cube", scale=Vec3(3,100,0.5), rotation=Vec3(15,-90,90), texture=cmd, position=Vec3(4.2,3.8,z),collider='box',color=color.random_color())
    c5=Entity(model="cube", scale=Vec3(3,100,0.5), rotation=Vec3(58,-90,90), texture=cmd, position=Vec3(2.7,5.4,z),collider='box',color=color.random_color())
    c6=Entity(model="cube", scale=Vec3(3,100,0.5), rotation=Vec3(90,0,0), texture=cmd, position=Vec3(0,6.2,z),collider='box',color=color.random_color())
    c7=Entity(model="cube", scale=Vec3(3,100,0.5), rotation=Vec3(-58,-90,-90), texture=cmd, position=Vec3(-2.7,5.4,z),collider='box',color=color.random_color())
    c8=Entity(model="cube", scale=Vec3(3,100,0.5), rotation=Vec3(-15,-90,90), texture=cmd, position=Vec3(-4.2,3.8,z),collider='box',color=color.random_color())
    c9=Entity(model="cube", scale=Vec3(3,100,0.5), rotation=Vec3(28,-90,90), texture=cmd, position=Vec3(-4,1.8,z),collider='box',color=color.random_color())
    c10=Entity(model="cube", scale=Vec3(3,100,0.5), rotation=Vec3(75,-90,90), texture=cmd, position=Vec3(-2.3,0.3,z),collider='box',color=color.random_color())


def theBoard():
    for i in range(3):
        createBoard(100*i)


def makeBoard(z):
    createBoard(100*z) 

theBoard()



class enemies(Entity):
    def __init__(self, position=(1,1,3)):
        self.i=1
        self.isTrue=False
        self.num=0

        super().__init__(
            model='cube',
            scale=Vec3(1,1, random.randrange(1,5)),
            color=color.random_color(),
            position=position,
            collider='box',
            texture=random.choice(enemyFaces),
            destroy=False,
            
        )

    def Input(self,key):
        if key=='r':
            self.num+=1
    
    def update(self):

        if self.z<hero.z-20:
            destroy(self)
            self.i+1

    
        
        


class superEnemy(Entity):
    
    def __init__(self):
        super().__init__(
            model='sphere',
            scale=4,
            position=Vec3(hero.x-10, hero.y-10, hero.z-30),
            texture=enemy1)

    def call(self):
        self.animate_position(Vec3(hero.x, hero.y+4, hero.z+200))
        
    
    def update(self):
        if self.z-hero.z<100:
            destroy(self)

        
        
        

        


        

    





hero=theHero() 


class coin(Entity):
    def __init__(self):
        super().__init__(
            model="sphere",
            position=Vec3(random.randint(-2,2), random.randint(1,5), hero.z+20),
            scale=Vec3(0.5,0.5,0.5),
            color=color.gold,
            texture=coin1,
            collider='sphere'
        )
    def update(self):
        global score
        self.rotation_y+=time.dt*50
        hit=self.intersects()

        if hit.hit:
            score+=1
            destroy(self)
            print_on_screen(f'BitCoins Collected: {score}', duration=2, scale=2)
        
class thesky(Entity):
    def __init__(self):
        super().__init__(
            model="sphere",
            texture=skyda,
            
            scale=Vec3(100,100, 350),
            position=Vec3(0,0,0),
            double_sided=True
        )

    def update(self):
        self.z=hero.z+50
        self.rotation_z+=time.dt*2
        # self.rotation_y+=time.dt*10


background=thesky()


def putEne(n):
    for i in range(n):
        enemies(position=(random.randint(-3,3), random.randrange(1, 6), hero.z+30))
        
########################################################################3
#BlackHole

class blackHole(Entity):
    def __init__(self, position):
        super().__init__(
            model='cube',
            texture=hole,
            scale=4,
            double_sided=True,
            collider='box',
            position=position
        )
    def update(self):
        hit=self.intersects()
        if hit.hit:
            if hero.supersonic==False:
                hero.animate_position(Vec3(hero.x,-15, hero.z+40), delay=0)
                hero.supersonic=True
            elif hero.supersonic==True:
                hero.animate_position(Vec3(0, 4, hero.z+40), delay=0)
                hero.supersonic=False
                

            destroy(self)






############################################################################################

class theTexts(Text):
    global num
    def __init__(self):
        super().__init__(
            text=f'Sorry You lost the Game.\n The Score: {num}!', 
            color=color.red, 
            origin=(0,-8), 
            scale=1, 
            duration=1,
            appear=2)


    def update(self):
        if hero.isAlive or held_keys['r']:
            destroy(self)


class GuideLines(Text):
    def __init__(self):
        super().__init__(
            text=f'To Reload The Game Press "R"',
            color=color.green,
            origin=(0,-6),
            scale=1,
            duration=1,
            appear=2
        )

    def update(self):
        if hero.isAlive or held_keys['r']:
            destroy(self)





class supersonicEnemies(Entity):
    def __init__(self):
        super().__init__(
            model='quad',
            texture=enemyPlane,
            position=Vec3(random.randint(-3,3), random.randint(0,5), hero.z+150),
            scale=1,
            collider='box'
        )

    def call(self):


class bullets(entity):
    def __init__(self, position, color):
        self.dy=3
        super().__init__(
            model="cube",
            texture=laser,
            scale=Vec3(0.5,0.5,2),
            collider='box',
            color=color,
            position=position
        )

    def update(self):
        self.z-=time.dt*dy
        self.rotation_x+=time.dt*dy*4
        self.rotation_y+=time.dt*dy*4
        self.rotation_z+=time.dt*dy*4
        

        if self.z<hero.z:
            destroy(self)




#UPDATE FUNCTION

def update():
    global x, i, num, superi
 ##############################

    ##########################
    # if hero.supersonic and hero.isAlive:
    #     if hero.z>50*superi:
    #         supersonicBoard(superi)
    #         superi+=1

        

        
        

        

    
    ########################
    # if board.getZ()<hero.getZ()//2:
    # if i*int(board.z//2)==int(hero.z):
    #     createBoard(z=i*int(board.z))
    #     i+=1

    
        
    if hero.z>50*i and hero.boardings:
        if hero.supersonic==False:
            i+=1
            
            makeBoard(i)
            putEne(i%10)
            theCoin=coin()
            num+=i%10
        
            if i% 8 > 6:
                hero.speed+=2
            
    
    

    hit_info=hero.intersects()
    if hit_info.hit and hero.boardings:
        if not hero.supersonic:
            if hero.x>0:
                hero.x-=random.randint(1,3)
            if hero.x<0:
                hero.x+=random.randint(1,3)
            if hero.y>3: hero.y-=random.randint(1,3)
            if hero.y<3: hero.y+=random.randint(1,3)
            hero.isAlive=False
        
    


      
        
        
        
    
    

    if not hero.isAlive:
        # theText=theTexts()
        # reloadText=GuideLines()
        
        if held_keys['r']:
            hero.isAlive=True
            score=0
            hero.position=Vec3(0,4,0)
            
        
        

    
    
        

            

            

 






x=0

# origin=circles[m-1].z
EditorCamera()
   







app.run()
