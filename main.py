from pyray import *
from upgrades import Upgrades

# Cookie Clicker!! (With circles)
class MyGame:
    def __init__(self):
        self.WINWIDTH = 900
        self.WINHEIGHT = 600
        init_window(self.WINWIDTH, self.WINHEIGHT, "Hi :D")

        self.upgrade_buttons = Upgrades()

        self.circleRad = 100
        self.circlePos = Vector2(self.WINWIDTH // 6, self.WINHEIGHT // 2)

        self.count = 0
        self.clicks = 1

        self.buttonsX = 3*(self.WINWIDTH // 4)
        self.moreClickBtn = False
        self.mCBdemand = 1


    def Update(self):
        self.count = max(0, self.count)

        if is_mouse_button_pressed(MouseButton.MOUSE_BUTTON_LEFT) and check_collision_point_circle(get_mouse_position(), self.circlePos, self.circleRad):
            self.count += self.clicks
        
        # Get more clicks per click upgrade
        self.count, self.clicks, self.mCBdemand = self.upgrade_buttons.MoreClicksPerClick(self.moreClickBtn, self.count, self.clicks, self.mCBdemand)

        # Passive Clicks Upgrade
        self.count = self.upgrade_buttons.PassiveClicks(True, self.count, get_frame_time())


    def Draw(self):
        begin_drawing()
        clear_background(BLACK)

        clickText = "Clicks: " + str(self.clicks)
        draw_circle_v(self.circlePos, self.circleRad, WHITE)
        draw_text(str(self.count), self.WINWIDTH // 2, 15, 75, WHITE)
        draw_text(clickText, int(self.circlePos.x) - len(clickText), int(self.circlePos.y + (self.circleRad + 15)), 15, WHITE)

        self.moreClickBtn = bool(gui_button(Rectangle(self.buttonsX, self.WINHEIGHT // 2, 207, 63), f"More Clicks (costs {self.mCBdemand} click) "))

        end_drawing()

    def Run(self):
        while not window_should_close():
            self.Update()
            self.Draw()
        close_window()

if __name__ == "__main__":
    app = MyGame()
    app.Run()
