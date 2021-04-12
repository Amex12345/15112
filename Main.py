from ursina import *

app=Ursina()

#Press "V" to create obsticles 
#ball moves itself forward and rotates (somewhat like in vacume)
#AWSD are controllers 
#if you touch the boarder of tunnel it will make you jump a little bit
#if you touch obstacle game will not stop however, it will say GAME LOST

class theHero(Entity):
    def __init__(self, superAttack=False):
        self.superAttack=superAttack
        
        super().__init__(
            
            model='sphere',
            parent=ground,
            texture="noise",
            color=color.blue,
            position=(0,4,0),
            origin_y=3,
            scale=1,
            collider='sphere',
            gravity=1,
            hit=False,
            speed=40,
            jumping=True,
            jump_height=2,
            jump_duration=0.5
            )
    
    def getZ(self):
        return self.position.z


    def update(self):
        
    
        if held_keys['w']: hero.y+=time.dt*10
        
        if held_keys["a"]: hero.x-=time.dt*10
        if held_keys["d"]: hero.x+=time.dt*10
        if held_keys['s']: hero.y-=time.dt*10


        hero.z+=time.dt*20
        hero.rotation_z+=time.dt*self.speed
        hero.rotation_x+=time.dt*self.speed
        hero.rotation_y+=time.dt*self.speed/2
        
        global speed
        # if self.position.y>-0.5:
        #     self.y-=time.dt*speed
        #     speed+=0.1
        #     if abs(0-self.position.y)<speed*time.dt:
        #         self.position.y=0
        #         speed=0
        
        # hero.z+=time.dt*4

        camera.position=Vec3(camera.x,4, hero.z-40)

        if held_keys['o']: camera.x-=time.dt*10
        if held_keys['p']: camera.x+=time.dt*10



        




class ground(Entity):
    def __init__(self, position=(0,0,0)):
        super().__init__(
            parent=scene,
            origin_y=2,
            position=position,
            model="cube",
            scale=Vec3(9,50,0.5),
            color=color.rgba(123,123,123, 200),
            texture='white_cube',
            rotation=(90,0,0),
            collider='box',
        )


cmd=load_texture("images (2).jpeg")
#test 
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



enemyPic=load_texture('images.png')

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
            texture=enemyPic,
            destroy=False,
            
        )

    def Input(self,key):
        if key=='r':
            self.num+=1
    
    def update(self):

        if self.z<hero.z-20:
            destroy(self)
            self.i+1


class onTopEnemy(Entity):
    
    def __init__(self):
        self.inters=False
        super().__init__(
            model='quad',
            scale=enemies.scale,
            color=color.red,
            texture='noise',
            position=enemies.position,
            collider="box",
            collision=True
        )

    def update(self):
        self.inters=False
        if self.intersects(hero):
            self.inters=True


        

    
background=Sky(texture='sky_default')

# def createBoard(z):
#     ground(position=Vec3(0,-3,2*z))


hero=theHero() 


# obstacle=enemies(position=(random.randint(-3,3),random.randint(-3,3), hero.z+15))

def putEne():
    enemies(position=(random.randint(-3,3), random.randrange(1, 6), hero.z+15))
        


i=2
def update():
    global x, speed, i
##############################
    # camera.z=hero.z-30
    ##########################
    if held_keys['left_mouse_down']:
        obstacle=enemies(position=(random.randint(-3,3),random.randint(-3,3), hero.z+15))
        
    ########################
    # if board.getZ()<hero.getZ()//2:
    # if i*int(board.z//2)==int(hero.z):
    #     createBoard(z=i*int(board.z))
    #     i+=1

    if held_keys['v']:
        putEne()
        
    if hero.z>25*i:
        i+=1
        makeBoard(i)
        
        
        
        

    # thehit=hero.intersects(traverse_target=)
    hit=hero.intersects()
    if hit.hit:
        vos=Text(text='You lost', color=color.red, scale=4)
        hero.speed=hero.speed*-1
        if hero.x>0:
            hero.x-=random.randint(1,3)
        if hero.x<0:
            hero.x+=random.randint(1,3)
        if hero.y>3: hero.y-=random.randint(1,3)
        if hero.y<3: hero.y+=random.randint(1,3)

           

 






x=0
speed=0.2
# origin=circles[m-1].z
EditorCamera()
   







app.run()