

def render_center_of_screen(app: classmethod, width: int, height: int) -> tuple[int, int, int, int]:
    """ Calculate X and Y coordinates to center window 
    ---
    ``x = (screen_width - width) // 2`` \n
    ``y = (screen_height - height) // 2`` \n
    """
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()

    # Calculate X and Y coordinates to center window
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    return width, height, x, y