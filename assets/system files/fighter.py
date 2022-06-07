import pygame
class Fighter():
    def __init__(self,x,y,data,spriteSheet,animationSteps):
        self.width = 288
        self.height = 128
        self.flip = False
        self.animationList = self.load_images(spriteSheet, animationSteps)
        self.rect = pygame.Rect((x, y, 80, 180))
        self.vel_y = 0
        self.jump = False
        self.attacking = False
        self.attack_type = 0
        self.health = 100
        
    def load_images(self,spriteSheet,animationSteps):
        #extract images
        animationList = []
        for y, animation in enumerate(animationSteps):
            tmp_img_list = []
            for x in range(animation):
                tmp_img = spriteSheet.subsurface( x * self.width, y * self.height, self.width, self.height)
                tmp_img_list.append(tmp_img)
            animationList.append(tmp_img_list)
        return animationList
    def move(self, width, height,surface,target):
        SPEED = 10
        GRAVITY = 2
        dx = 0 #delta x
        dy = 0 #delta y
        
        #keypress
        key = pygame.key.get_pressed()
        #non attack
        if self.attacking == False:
            #movement
            if key[pygame.K_a]:
                dx = -SPEED
            if key[pygame.K_d]:
                dx = SPEED
            #jump
            if key[pygame.K_w] and self.jump == False:
                self.vel_y = -30
                self.jump = True
            #attack
            if key[pygame.K_r] or key[pygame.K_t]:
                self.attack(surface, target)
                #determine which attack type was used
                if key[pygame.K_r]:
                    self.attack_type = 1
                if key[pygame.K_t]:
                    self.attack_type = 2
        #apply gravity
        self.vel_y += GRAVITY
        dy += self.vel_y
        #ensure player stays on screen
        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > width:
            dx = width - self.rect.right
        if self.rect.bottom + dy > height - 50: #adjust for floor value
            self.vel_y = 0
            self.jump = False
            dy = height - 50 - self.rect.bottom
        #ensure players face each other
        if target.rect.centerx > self.rect.centerx:
            self.flip = False
        else:
            self.flip = True
        #update
        self.rect.x += dx
        self.rect.y += dy
    def attack(self,surface, target):
        self.attacking = True
        attacking_rect = pygame.Rect(self.rect.centerx - (2*self.rect.width*self.flip), self.rect.y, 2*self.rect.width, self.rect.height)
        if attacking_rect.colliderect(target.rect):
            target.health -= 10
        pygame.draw.rect(surface, (0, 255,0), attacking_rect)
    def draw(self, surface):
        pygame.draw.rect(surface, (255,0,0), self.rect)