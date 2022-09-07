##################   Sprites
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("download.png")
        self.surf = pygame.Surface((50, 100))
        self.rect = self.surf.get_rect()

        
                            1) Rect objects
#determine whether Sprite A is in contact with Sprite B：
            self.rect.colliderect(sprite.rect)
# It returns True if the rectangles of the two objects overlap in anyway way, otherwise returns False.

                            2).Sprite Collision Functions

                            1.spritecollideany(sprite, group)
#  it will detect whether or whether not the sprite is in collision with any of the sprites within the group.检测与另一个Group的任何一个精灵是否有碰撞:

                            2.groupcollide()
                        pygame.sprite.groupcollide()
'''
it occurs between two groups, which it takes as the first and second parameter.
This function can also take third and fourth (optional) parameters called dokill1 and dokill2, 
    which take True or False values. If dokill1 is True, the colliding sprites from group1 will be removed using the kill method. 
    And if dokill2 is True, sprites from group2 will be removed.

