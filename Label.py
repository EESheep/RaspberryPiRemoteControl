import pygame
class Label(object):
    def __init__(self, left, top, text, font_info):
        self.status = 0                      # <0 :- 不显示。
        self.left = left
        self.top = top
        self.text = text
        self.display_x = left
        self.display_y = top

        if font_info is None:
            self.font = pygame.font.Font('font/msjh.ttc', 20)
            self.tc = (255, 255, 255)
            self.bc = (0, 0, 0)
            self.align = 0
            self.valign = 0
        else:
            self.font = font_info["font"]    # 字型及字体大小
            self.tc = font_info["tc"]
            self.bc = font_info["bc"]
            self.align = font_info.get("align", 0)
            self.valign = font_info.get("valign", 0)

        if text == "":
            self.text_surface = None
        else:
            self.set_text(text)

    def render(self, surface):
        if self.text != "" and self.status >= 0:
            surface.blit(self.text_surface, (self.display_x, self.display_y))

    def set_align(self, align):
        w, h = self.__get_size()
        if align == 2:
            self.display_x = self.left - w
        elif align == 1:
            self.display_x = self.left - int(w / 2)
            
    def set_valign(self, valign):
        w, h = self.get_size()
        if valign == 2:
            self.display_y = self.pos_y - h
        elif valign == 1:
            self.display_y = self.pos_y - int(h / 2)
        else:
            self.display_y = self.pos_y

    def __get_size(self):
        if self.text_surface is None:
            return (0, 0)
        else:
            return self.text_surface.get_size()    # return (w, h)

    def set_text(self, text, tc=None, bc=None):
        self.text = text

        if tc is not None:
            self.tc = tc

        if bc is not None:
            self.bc = bc

        self.text_surface = self.font.render(self.text, True, self.tc, self.bc)
        self.set_align(self.align)
        self.set_valign(self.valign)

    def set_hide(self, flag):
        if flag:
            self.status = -1
        else:
            self.status = 0
