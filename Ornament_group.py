def game(number, s, name):
    if number == '1':
        import pygame
        import os
        import sys
        pygame.init()
        sc = pygame.display.set_mode((1500, 800))
        sc.fill((0, 0, 0))
        surf = pygame.image.load(s).convert()
        surf.set_colorkey((255, 255, 255))
        rect = surf.get_rect(bottomright=(1500, 800))
        x2 = rect.width
        y2 = rect.height
        x = 1500 + x2
        y = 800
        pygame.display.update()

        while True:
                    if ((x-x2<0)) and ((y-y2)<0):
                        pygame.image.save(sc, 'static/'+str(name)+'.jpg')
                        return 0
                    elif (x-x2)<0:
                        x = x2+1500
                        y = y-y2
                    x = x-x2
                    rect = surf.get_rect(bottomright=(x, y))
                    sc.blit(surf, rect)
                    pygame.display.update()
    elif number == '2':
        import pygame
        import sys
        pygame.init()
        sc = pygame.display.set_mode((1500, 800))
        sc.fill((0, 0, 0))
        surf = pygame.image.load(s).convert()
        surf.set_colorkey((255, 255, 255))
        rect = surf.get_rect(bottomright=(1500, 800))
        x2 = rect.width
        y2 = rect.height
        x = 1500+x2
        y = 800
        copy_surf = surf
        elem = 0
        pygame.display.update()

        while True:
                        elem +=1
                        if ((x-x2<0)) and ((y-y2)<0):
                            pygame.image.save(sc, 'static/'+str(name)+'.jpg')
                            return 0
                        elif (x-x2)<0:
                            y=y-y2
                            x=x2+1500
                            elem = 0
                        elif elem%2==1:
                            x = x - x2
                            surf = pygame.transform.flip(copy_surf, 1, 0)
                            surf = pygame.transform.flip(surf, 0, 1)
                            rect = surf.get_rect(bottomright=(x, y))
                            sc.blit(surf, rect)
                            pygame.display.update()
                        else:
                            x = x - x2
                            surf = copy_surf
                            rect = surf.get_rect(bottomright=(x, y))
                            sc.blit(surf, rect)
                            pygame.display.update()
    elif number == '3':
        import pygame
        import sys
        pygame.init()
        sc = pygame.display.set_mode((1500, 800))
        sc.fill((0, 0, 0))
        surf = pygame.image.load(s).convert() 
        surf.set_colorkey((255, 255, 255))
        rect = surf.get_rect(bottomright=(1500, 800))
        x2 = rect.width
        y2 = rect.height
        x = 1500+x2
        y = 800
        copy_surf = surf
        elem = 0
        pygame.display.update() 
        while True:
                    elem +=1
                    if ((x-x2<0)) and ((y-y2)<0):
                        pygame.image.save(sc, 'static/'+str(name)+'.jpg')
                        return 0
                    if (x-x2)<0:
                        elem = 1
                        y=y-y2
                        x=x2+1500
                    if elem%2==1:
                        x = x-x2
                        surf = copy_surf
                        rect = surf.get_rect(bottomright=(x, y))
                        sc.blit(surf, rect)

                        centerr = rect.center

                        surf = pygame.transform.flip(copy_surf, 0, 1)
                        rect = surf.get_rect(center=centerr)
                        sc.blit(surf, rect)

                        pygame.display.update()
                    else:
                        x = x - x2
    elif number == '4':
        import pygame
        import sys
        pygame.init()
        sc = pygame.display.set_mode((1500, 800))
        sc.fill((0, 0, 0))
        surf = pygame.image.load(s).convert()
        surf.set_colorkey((255, 255, 255))
        rect = surf.get_rect(bottomright=(1500, 800))
        x2 = rect.width
        y2 = rect.height
        x = 1500 + x2
        y = 800
        pygame.display.update()
        elem = 0
        stroka = 1
        while True:
                    elem=elem+1
                    if ((x-x2<0)) and ((y-y2)<0):
                        pygame.image.save(sc, 'static/'+str(name)+'.jpg')
                        return 0
                    elif (x-x2)<0:
                        stroka+=1
                        elem=1
                        surf = pygame.transform.flip(surf, 0, 1)
                        x=x2+1500
                        y=y-y2
                    x=x-x2
                    if elem%2==1 and stroka%2==1:
                        rect = surf.get_rect(bottomright=(x, y))
                        sc.blit(surf, rect)
                        pygame.display.update()
                    elif elem%2==0 and stroka%2==0:
                        rect = surf.get_rect(bottomright=(x, y))
                        sc.blit(surf, rect)
                        pygame.display.update()
    elif number == '5':
        import pygame
        import sys
        pygame.init()
        sc = pygame.display.set_mode((1500, 800))
        sc.fill((0, 0, 0))
        surf = pygame.image.load(s).convert()
        surf.set_colorkey((255, 255, 255))
        surf = pygame.transform.flip(surf, 1, 0)
        rect = surf.get_rect(bottomright=(1500, 800))
        x2 = rect.width
        y2 = rect.height
        x = 1500 + x2
        y = 800
        pygame.display.update()
        while True:
                    if ((x-x2<0)) and ((y-y2)<0):
                        pygame.image.save(sc, 'static/'+str(name)+'.jpg')
                        return 0
                    elif (x-x2)<0:
                        surf = pygame.transform.flip(surf, 0, 1)
                        x=x2+1500
                        y=y-y2
                    surf = pygame.transform.flip(surf, 1, 0)
                    x = x-x2
                    rect = surf.get_rect(bottomright=(x, y))
                    sc.blit(surf, rect)
                    pygame.display.update()
    elif number == '6':
        import pygame
        import sys
        pygame.init()
        sc = pygame.display.set_mode((1500, 800))
        sc.fill((0, 0, 0))
        surf = pygame.image.load(s).convert()
        surf.set_colorkey((255, 255, 255))
        rect = surf.get_rect(bottomright=(1500, 800))
        x2 = rect.width
        y2 = rect.height
        x = 1500+x2
        y = 800
        pygame.display.update()
        save_surf = surf
        elem = 0
        stroka = 1
        while True:
                    elem = elem +1
                    if ((x-x2<0)) and ((y-y2)<0):
                        pygame.image.save(sc, 'static/'+str(name)+'.jpg')
                        return 0
                    elif (x-x2)<0:
                        elem = 0
                        stroka+=1
                        el=0
                        surf = pygame.transform.flip(surf, 0, 1)
                        x=x2+1500
                        y=y-y2
                    elif stroka%2==1 and elem%2==1:
                        x=x-x2
                        surf = save_surf
                        rect = save_surf.get_rect(bottomright=(x, y))
                        sc.blit(surf, rect)
                        
                        centerr=rect.center
                        surf = pygame.transform.flip(surf, 0, 1)
                        
                        rect = surf.get_rect(center=centerr)
                        sc.blit(surf, rect)
                        pygame.display.update()
                    elif stroka%2==0 and elem%2==0:
                        x=x-x2
                        surf = pygame.transform.flip(save_surf, 1, 0)
                        rect = surf.get_rect(bottomright = (x,y))
                        sc.blit(surf, rect)

                        centerr=rect.center
                        
                        surf = pygame.transform.flip(surf, 0, 1)
                        
                        rect = surf.get_rect(center=centerr)
                        sc.blit(surf, rect)
                        pygame.display.update()
                    else:
                        x = x - x2
    elif number == '7':
        import pygame
        import sys
        pygame.init()
        sc = pygame.display.set_mode((1500, 800))
        sc.fill((0, 0, 0))
        surf = pygame.image.load(s).convert()
        surf.set_colorkey((255, 255, 255))
        save_surf = surf
        surf = pygame.transform.flip(surf, 0, 1)
        rect = surf.get_rect(bottomright=(1500, 800))
        x2 = rect.width
        y2 = rect.height
        x = 1500 + x2 
        y = 800
        pygame.display.update()
        while True:
                    if ((x-x2<0)) and ((y-y2)<0):
                        pygame.image.save(sc, 'static/'+str(name)+'.jpg')
                        return 0
                    elif (x-x2)<0:
                        surf = pygame.transform.flip(save_surf, 1, 0)
                        save_surf = surf
                        x = x2+1500
                        y = y-y2
                    else:
                        surf = pygame.transform.flip(surf, 0, 1)
                    x = x-x2
                    rect = surf.get_rect(bottomright=(x, y))
                    sc.blit(surf, rect)
                    pygame.display.update()
    elif number == '8':
        import pygame
        import sys
        pygame.init()
        sc = pygame.display.set_mode((1500, 800))
        sc.fill((0, 0, 0))
        surf = pygame.image.load(s).convert()
        surf.set_colorkey((255, 255, 255))
        rect = surf.get_rect(bottomright=(1500, 800))
        x2 = rect.width
        y2 = rect.height
        x = 1500+x2
        y = 800
        save_surf = surf
        stroka = 1
        elem = 0
        pygame.display.update()
        while True:
                    elem += 1
                    if ((x-x2<0)) and ((y-y2)<0):
                        pygame.image.save(sc, 'static/'+str(name)+'.jpg')
                        return 0
                    elif (x-x2)<0:
                        stroka +=1
                        elem = 1
                        surf = save_surf
                        x = 1500+x2
                        y = y - y2
                        
                    if stroka%4==1 and elem%2==1:
                        x = x - x2
                        surf = save_surf
                        rect = surf.get_rect(bottomright=(x, y))
                        sc.blit(surf, rect)
                    elif stroka%4==2 and elem%2==0:
                        x = x - x2
                        surf =  pygame.transform.flip(save_surf, 0, 1)
                        rect = surf.get_rect(bottomright=(x, y))
                        sc.blit(surf, rect)
                    elif stroka%4==3 and elem%2==0:
                        x = x - x2
                        surf = save_surf
                        rect = surf.get_rect(bottomright=(x, y))
                        sc.blit(surf, rect)
                    elif stroka%4==0 and elem%2==1:
                        x = x - x2
                        surf =  pygame.transform.flip(save_surf, 0, 1)
                        rect = surf.get_rect(bottomright=(x, y))
                        sc.blit(surf, rect)
                    else:
                        x = x - x2
                    pygame.display.update()
    elif number == '9':
        import pygame
        import sys
        pygame.init()
        sc = pygame.display.set_mode((1500, 800))
        sc.fill((0, 0, 0))
        surf = pygame.image.load(s).convert()
        surf.set_colorkey((255, 255, 255))
        save_surf = surf
        surf = pygame.transform.flip(surf, 1, 0)
        rect = surf.get_rect(bottomright=(1500, 800))
        x2 = rect.width
        y2 = rect.height
        x = 1500 + x2
        y = 800
        pygame.display.update()
        el = 0
        st = 1
        while True:
                    el = el+1
                    if ((x-x2<0)) and ((y-y2)<0):
                        pygame.image.save(sc, 'static/'+str(name)+'.jpg')
                        return 0
                    elif (x-x2)<0:
                        el = 1
                        st += 1
                        x = x2+1500
                        y = y-y2
                    x = x-x2
                    if st%4 == 1:
                        if el%4 == 1:
                            surf = save_surf
                            rect = save_surf.get_rect(bottomright=(x, y))
                            sc.blit(surf, rect)
                            pygame.display.update()
                        elif el%4 == 2:
                            surf = pygame.transform.flip(surf, 1, 0)
                            rect = surf.get_rect(bottomright=(x, y))
                            sc.blit(surf, rect)
                            pygame.display.update()
                    elif st%4 == 2:
                        if el%4 == 3:
                            surf = pygame.transform.flip(save_surf, 0, 1)
                            rect = surf.get_rect(bottomright=(x, y))
                            sc.blit(surf, rect)
                            pygame.display.update()
                        elif el%4 == 0:
                            surf = pygame.transform.flip(surf, 1, 0)
                            rect = surf.get_rect(bottomright=(x, y))
                            sc.blit(surf, rect)
                            pygame.display.update()
                    elif st%4 == 3:
                        if el%4 == 3:
                            surf = save_surf
                            rect = save_surf.get_rect(bottomright=(x, y))
                            sc.blit(surf, rect)
                            pygame.display.update()
                        elif el%4 == 0:
                            surf = pygame.transform.flip(surf, 1, 0)
                            rect = surf.get_rect(bottomright=(x, y))
                            sc.blit(surf, rect)
                            pygame.display.update()
                    else:
                        if el%4 == 1:
                            surf = pygame.transform.flip(save_surf, 0, 1)
                            rect = surf.get_rect(bottomright=(x, y))
                            sc.blit(surf, rect)
                            pygame.display.update()
                        elif el%4 == 2:
                            surf = pygame.transform.flip(surf, 1, 0)
                            rect = surf.get_rect(bottomright=(x, y))
                            sc.blit(surf, rect)
                            pygame.display.update()
    elif number == '10':
        import pygame
        import sys
        pygame.init()
        sc = pygame.display.set_mode((1500, 800))
        sc.fill((0, 0, 0))
        surf = pygame.image.load(s).convert()
        surf.set_colorkey((255, 255, 255))
        save_surf = surf
        rect = surf.get_rect(bottomright=(1500, 800))
        x2 = rect.width
        y2 = rect.height
        x = 1500 + x2
        y = 800
        pygame.display.update()
        while True:
                    if ((x-x2<0)) and ((y-y2)<0):
                        pygame.image.save(sc, 'static/'+str(name)+'.jpg')
                        return 0
                    elif (x-x2)<0:
                        x = 1500 + x2
                        y = y - y2
                    x = x - x2
                    surf = save_surf
                    rect = surf.get_rect(bottomright=(x, y))
                    sc.blit(surf, rect)

                    centerr = rect.center

                    surf = pygame.transform.rotate(save_surf, 90)
                    rect = surf.get_rect(center = centerr)
                    sc.blit(surf, rect)

                    surf = pygame.transform.rotate(save_surf, 180)
                    rect = surf.get_rect(center = centerr)
                    sc.blit(surf, rect)

                    surf = pygame.transform.rotate(save_surf, 270)
                    rect = surf.get_rect(center = centerr)
                    sc.blit(surf, rect)
                    pygame.display.update()
    elif number == '11':
        import pygame
        import sys
        pygame.init()
        sc = pygame.display.set_mode((1500, 800))
        sc.fill((0, 0, 0))
        surf = pygame.image.load(s).convert()
        surf.set_colorkey((255, 255, 255))
        rect = surf.get_rect(bottomright=(1500, 800))
        x2 = rect.width
        y2 = rect.height
        x = 1500+x2
        y = 800
        save_surf = surf
        stroka = 1
        elem = 0
        pygame.display.update()
        while True:
                    elem+=1
                    if ((x-x2<0)) and ((y-y2)<0):
                        pygame.image.save(sc, 'static/'+str(name)+'.jpg')
                        return 0
                    if (x-x2)<0:
                        stroka += 1
                        elem = 1
                        surf = pygame.transform.flip(save_surf, 0, 1)
                        x = 1500 + x2
                        y = y - y2
                    if stroka%2==1 and elem%2==1:
                        x = x - x2
                        surf = pygame.transform.flip(save_surf,1, 0)
                        rect = surf.get_rect(bottomright=(x,y))
                        sc.blit(surf, rect)
                        pygame.display.update(rect)

                        centerr = rect.center

                        surf = pygame.transform.flip (surf, 0, 1)
                        surf = pygame.transform.rotate(surf, -90)
                        rect = surf.get_rect(center = centerr)
                        sc.blit(surf, rect)
                        pygame.display.update(rect)
                        
                    elif stroka%2==1 and elem%2==0:
                        x = x - x2
                        surf = save_surf
                        rect = surf.get_rect(bottomright=(x,y))
                        sc.blit(surf, rect)
                        pygame.display.update(rect)

                        centerr = rect.center

                        surf = pygame.transform.flip ( surf, 1, 0)
                        surf = pygame.transform.rotate( surf, -90)
                        rect = surf.get_rect(center = centerr)
                        sc.blit(surf, rect)
                        pygame.display.update(rect)
                    elif stroka%2==0 and elem%2==1:
                        x = x - x2
                        surf = pygame.transform.flip(save_surf,1, 0)
                        surf = pygame.transform.flip (surf, 0, 1)
                        rect = surf.get_rect(bottomright=(x,y))
                        sc.blit(surf, rect)
                        pygame.display.update(rect)

                        centerr = rect.center

                        surf = pygame.transform.flip (save_surf, 1, 0)
                        surf = pygame.transform.rotate(surf,90)
                        rect = surf.get_rect(center = centerr)
                        sc.blit(surf, rect)
                        pygame.display.update(rect)
                    elif stroka%2==0 and elem%2==0:
                        x = x - x2
                        surf = pygame.transform.flip(save_surf, 0, 1)
                        rect = surf.get_rect(bottomright=(x,y))
                        sc.blit(surf, rect)
                        pygame.display.update(rect)

                        centerr = rect.center

                        surf = pygame.transform.flip (surf, 1, 0)
                        surf = pygame.transform.rotate(surf, 90)
                        rect = surf.get_rect(center = centerr)
                        sc.blit(surf, rect)
                        pygame.display.update(rect)
                    
                    else:
                        x = x - x2
                        pygame.display.update(rect)
    elif number == '12':
        import pygame
        import sys
        pygame.init()
        sc = pygame.display.set_mode((1500, 800))
        sc.fill((0, 0, 0))
        surf = pygame.image.load(s).convert()
        surf.set_colorkey((255, 255, 255))
        rect = surf.get_rect(bottomright=(1500, 800))
        save_surf = surf
        save_rect = rect

        x2 = rect.width
        y2 = rect.height
        x = 1500 + x2
        y = 800

        elem = 0
        string = 1
        pygame.display.update()

        while True:
                    elem+=1
                    if ((x-x2<0)) and ((y-y2)<0):
                        pygame.image.save(sc, 'static/'+str(name)+'.jpg')
                        return 0
                    elif (x-x2)<0:
                        string+=1
                        elem = 0
                        y = y - y2
                        x = 1500+x2
                    
                    elif string%2==1 and elem%2==1:
                        x = x-x2
                        surf = save_surf
                        rect = surf.get_rect(bottomright=(x, y))
                        sc.blit(surf, rect)

                        surf = pygame.transform.rotate(save_surf, -90)
                        surf = pygame.transform.flip(surf,1,0)
                        rect = surf.get_rect(bottomright=(x, y))
                        sc.blit(surf, rect)
                    elif string%2==1 and elem%2==0:
                        x = x-x2
                        surf = pygame.transform.flip(save_surf,0,1)
                        rect = surf.get_rect(bottomright=(x, y))
                        sc.blit(surf, rect)

                        surf = pygame.transform.rotate(save_surf, 90)
                        rect = surf.get_rect(bottomright=(x, y))
                        sc.blit(surf, rect)
                    elif string%2==0 and elem%2==1:
                        x = x - x2
                        surf = pygame.transform.flip(save_surf,1,0)
                        rect = surf.get_rect(bottomright=(x, y))
                        sc.blit(surf, rect)
                        
                        surf = pygame.transform.rotate(save_surf, -90)
                        rect = surf.get_rect(bottomright=(x, y))
                        sc.blit(surf, rect)
                    elif string%2==0 and elem%2==0:
                        x = x-x2
                        surf = pygame.transform.flip(save_surf,0,1)
                        surf = pygame.transform.flip(surf,1,0)
                        rect = surf.get_rect(bottomright=(x, y))
                        sc.blit(surf, rect)

                        surf = pygame.transform.flip(save_surf,1,0)
                        surf = pygame.transform.rotate(surf, -90)
                        rect = surf.get_rect(bottomright=(x, y))
                        sc.blit(surf, rect)                    
                    pygame.display.update()
    elif number == '13':
        import pygame
        import sys
        pygame.init()
        sc = pygame.display.set_mode((1500, 800))
        sc.fill((0, 0, 0))
        surf = pygame.image.load(s).convert()
        surf.set_colorkey((255, 255, 255))
        rect = surf.get_rect(bottomright=(1500, 800))
        save_surf = surf

        x = 1500
        y = 800
        x2 = rect.width
        y2 = rect.height
        x = x+x2
        pygame.display.update()
        stroka = 1
        while True:
                    if ((x-x2<0)) and ((y-y2)<0):
                        pygame.image.save(sc, 'static/'+str(name)+'.jpg')
                        return 0
                    elif (x-x2)<0:
                        stroka +=1
                        if stroka%2 == 0:
                            x = 1500 + 1.5*x2
                            y = y - y2
                        else:
                            x = 1500+x2
                            y = y - y2
                    x = x-x2
                    surf = save_surf
                    rect = surf.get_rect(bottomright=(x, y))
                    sc.blit(surf, rect)

                    centerr = rect.center
                        
                    surf = pygame.transform.rotate(save_surf, 120)
                    rect = surf.get_rect(center = centerr)
                    sc.blit(surf, rect)

                    surf = pygame.transform.rotate(save_surf, 240)
                    rect = surf.get_rect(center = centerr)
                    sc.blit(surf, rect)

                    pygame.display.update()
    elif number == '14':
        import pygame
        import sys
        pygame.init()
        sc = pygame.display.set_mode((1500, 800))
        sc.fill((0, 0, 0))
        surf = pygame.image.load(s).convert()
        surf.set_colorkey((255, 255, 255))
        rect = surf.get_rect(bottomright=(1500, 800))
        save_surf = surf
        coordinate = 0

        x2 = rect.width
        y2 = rect.height
        x = 1500 + x2
        y = 800
        pygame.display.update()

        elem = 0
        stroka = 1

        top = 0
        k = 0
        while True:
                    elem += 1
                    if ((x-x2<0)) and ((y-y2)<0):
                        pygame.image.save(sc, 'static/'+str(name)+'.jpg')
                        return 0
                    elif (x-x2)<0:
                        elem = 1
                        stroka += 1
                        x = 1500 + x2
                        y = y - y2
                    if stroka%4 == 1 or stroka%4 == 2:
                        if stroka%2==1 and elem%2==1:
                            x = x - x2
                            surf = pygame.transform.flip(save_surf,1,0)
                            rect = surf.get_rect(bottomright=(x,y))
                            sc.blit(surf, rect)
                            coordinate = rect.center
                            
                            surf = pygame.transform.rotate(save_surf,120)
                            rect = surf.get_rect(center = coordinate)
                            sc.blit(surf, rect)
                        elif stroka%2==1 and elem%2==0:
                            x = x - x2
                            surf = save_surf
                            rect = surf.get_rect(bottomright=(x,y))
                            sc.blit(surf, rect)

                            coordinate = rect.center
                            
                            surf = pygame.transform.flip(save_surf,1,0)
                            surf = pygame.transform.rotate(surf,-120)
                            rect = surf.get_rect(center = coordinate)
                            sc.blit(surf, rect)
                            
                        elif stroka%2==0 and elem%2==0:
                            x = x - x2
                            surf = pygame.transform.rotate(save_surf,240)
                            rect = surf.get_rect(bottomright=(x+0.7*x2, y))
                            sc.blit(surf, rect)

                            
                            surf = pygame.transform.flip(save_surf,0,1)
                            surf = pygame.transform.rotate(surf,-60)
                            rect = surf.get_rect(bottomright=(x+0.7*x2, y))
                            sc.blit(surf, rect)
                        else:
                            x = x - x2
                    else:
                        if stroka%2==1 and elem%2==0:
                            x = x - x2
                            surf = pygame.transform.flip(save_surf,1,0)
                            rect = surf.get_rect(bottomright=(x,y))
                            sc.blit(surf, rect)
                            coordinate = rect.center
                            
                            surf = pygame.transform.rotate(save_surf,120)
                            rect = surf.get_rect(center = coordinate)
                            sc.blit(surf, rect)
                        elif stroka%2==1 and elem%2==1:
                            x = x - x2
                            surf = save_surf
                            rect = surf.get_rect(bottomright=(x,y))
                            sc.blit(surf, rect)

                            coordinate = rect.center
                            
                            surf = pygame.transform.flip(save_surf,1,0)
                            surf = pygame.transform.rotate(surf,-120)
                            rect = surf.get_rect(center = coordinate)
                            sc.blit(surf, rect)
                            
                        elif stroka%2==0 and elem%2==1:
                            x = x - x2
                            surf = pygame.transform.rotate(save_surf,240)
                            rect = surf.get_rect(bottomright=(x+0.7*x2, y))
                            sc.blit(surf, rect)

                            
                            surf = pygame.transform.flip(save_surf,0,1)
                            surf = pygame.transform.rotate(surf,-60)
                            rect = surf.get_rect(bottomright=(x+0.7*x2, y))
                            sc.blit(surf, rect)
                        else:
                            x = x - x2
                    pygame.display.update()
    elif number == '15':
        import pygame
        import sys
        pygame.init()
        sc = pygame.display.set_mode((1500, 800))
        sc.fill((0, 0, 0))
        surf = pygame.image.load(s).convert() 
        surf.set_colorkey((255, 255, 255))
        rect = surf.get_rect(bottomright=(1500, 800))
        save_surf = surf

        x2 = rect.width
        y2 = rect.height
        x = 1500 + x2
        y = 800

        pygame.display.update()

        stroka = 1
        elem = 0

        while True:
                    elem += 1
                    if ((x-x2<0)) and ((y-y2)<0):
                        pygame.image.save(sc, 'static/'+str(name)+'.jpg')
                        return 0
                    elif (x-x2)<0:
                        stroka += 1
                        if stroka%2 == 1:
                            elem = 0
                            x = 1500 + x2
                            y = y - y2
                        else:
                            elem = 0
                            x = 1500 + 1.5*x2
                            y = y - y2
                    else:
                        x = x - x2
                        surf = save_surf
                        rect = surf.get_rect(bottomright=(x, y))
                        sc.blit(surf, rect)

                        centerr = rect.center

                        surf = pygame.transform.flip(surf, 0, 1)
                        rect = surf.get_rect(center = centerr)
                        sc.blit(surf, rect)

                        surf = pygame.transform.rotate(save_surf,120)
                        rect = surf.get_rect(center = centerr)
                        sc.blit(surf, rect)

                        surf = pygame.transform.flip(surf, 0, 1)
                        rect = surf.get_rect(center = centerr)
                        sc.blit(surf, rect)

                        surf = pygame.transform.rotate(save_surf,240)
                        rect = surf.get_rect(center = centerr)
                        sc.blit(surf, rect)
                        
                        surf = pygame.transform.flip(surf, 0, 1)
                        rect = surf.get_rect(center = centerr)
                        sc.blit(surf, rect)
                        
                        pygame.display.update()
    elif number == '16':
        import pygame
        import sys
        pygame.init()
        sc = pygame.display.set_mode((1500, 800))
        sc.fill((0, 0, 0))
        surf = pygame.image.load(s).convert()
        surf.set_colorkey((255, 255, 255))
        rect = surf.get_rect(bottomright=(1500, 800))
        save_surf = surf
        centerr = rect.center

        x2 = rect.width
        y2 = rect.height
        x = 1500 + x2
        y = 800
        pygame.display.update()

        stroka = 1
        while True:
                    if ((x-x2<0)) and ((y-y2)<0):
                        pygame.image.save(sc, 'static/'+str(name)+'.jpg')
                        return 0
                    elif (x-x2)<0:
                        stroka+=1
                        if stroka%2==0:
                            x = 1500 + 1.5*x2
                            y = y - y2
                        else:
                            x = 1500 + x2
                            y = y - y2
                    x = x - x2
                    surf = save_surf
                    rect = surf.get_rect(bottomright = (x, y))
                    sc.blit(surf, rect)

                    centerr = rect.center

                    surf = save_surf
                    rect = surf.get_rect(center = centerr)
                    sc.blit(surf, rect)
                                        
                    surf = pygame.transform.rotate(save_surf,60)
                    rect = surf.get_rect(center = centerr)
                    sc.blit(surf, rect)

                    surf = pygame.transform.rotate(save_surf,120)
                    rect = surf.get_rect(center = centerr)
                    sc.blit(surf, rect)

                    surf = pygame.transform.rotate(save_surf,180)
                    rect = surf.get_rect(center = centerr)
                    sc.blit(surf, rect)

                    surf = pygame.transform.rotate(save_surf,240)
                    rect = surf.get_rect(center = centerr)
                    sc.blit(surf, rect)

                    surf = pygame.transform.rotate(save_surf,300)
                    rect = surf.get_rect(center = centerr)
                    sc.blit(surf, rect)
                    pygame.display.update()
    elif number == '17':
        import pygame
        import sys
        pygame.init()
        sc = pygame.display.set_mode((1500, 800))
        sc.fill((0, 0, 0))
        surf = pygame.image.load(s).convert()
        surf.set_colorkey((255, 255, 255))
        rect = surf.get_rect(bottomright=(1500, 800))
        save_surf = surf
        centerr = rect.center

        x2 = rect.width
        y2 = rect.height
        x = 1500 + x2
        y = 800
        pygame.display.update()

        stroka = 1
        elem = 0
        while True:
                    elem+=1
                    if ((x-x2<0)) and ((y-y2)<0):
                        pygame.image.save(sc, 'static/'+str(name)+'.jpg')
                        return 0
                    elif (x-x2)<0:
                        stroka+=1
                        if stroka%2==1:
                            x = 1500 + x2
                            y = y - y2
                        else:
                            x=1500+1.5*x2
                            y=y-y2
                    x = x - x2
                    surf = save_surf
                    rect = surf.get_rect(bottomright=(x,y))
                    sc.blit(surf, rect)

                    centerr = rect.center
                    
                    surf = pygame.transform.rotate(save_surf,60)
                    rect = surf.get_rect(center = centerr)
                    sc.blit(surf, rect)

                    surf = pygame.transform.flip(save_surf,0,1)
                    rect = surf.get_rect(center = centerr)
                    sc.blit(surf, rect)

                    surf = pygame.transform.flip(save_surf,0,1)
                    surf = pygame.transform.rotate(surf,60)
                    rect = surf.get_rect(center = centerr)
                    sc.blit(surf, rect)

                    surf = pygame.transform.rotate(save_surf,120)
                    rect =  surf.get_rect(center = centerr)
                    sc.blit(surf, rect)

                    surf = pygame.transform.flip(save_surf,0,1)
                    surf = pygame.transform.rotate(surf,120)
                    rect = surf.get_rect(center = centerr)
                    sc.blit(surf, rect)

                    surf = pygame.transform.rotate(save_surf,180)
                    rect = surf.get_rect(center = centerr)
                    sc.blit(surf, rect)

                    surf = pygame.transform.flip(save_surf,0,1)
                    surf = pygame.transform.rotate(surf,180)
                    rect = surf.get_rect(center = centerr)
                    sc.blit(surf, rect)


                    surf = pygame.transform.rotate(save_surf,240)
                    rect = surf.get_rect(center = centerr)
                    sc.blit(surf, rect)

                    surf = pygame.transform.flip(save_surf,0,1)
                    surf = pygame.transform.rotate(surf,240)
                    rect = surf.get_rect(center = centerr)
                    sc.blit(surf, rect)

                    surf = pygame.transform.rotate(save_surf,300)
                    rect = surf.get_rect(center = centerr)
                    sc.blit(surf, rect)

                    surf = pygame.transform.flip(save_surf,0,1)
                    surf = pygame.transform.rotate(surf,300)
                    rect = surf.get_rect(center = centerr)
                    sc.blit(surf, rect)
                    
                    pygame.display.update()
