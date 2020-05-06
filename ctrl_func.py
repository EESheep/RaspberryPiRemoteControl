def check_play_button(button, play_button, mouse_x, mouse_y):
    if mouse_x < play_button.rect.right and mouse_x >= play_button.rect.left:
        if mouse_y > play_button.rect.top and mouse_y <= play_button.rect.bottom:
            button.stats = True