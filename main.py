"""
Constructing a cardioid by pencil segment method
"""

import dataclasses
import math
from abc import ABC, abstractmethod

import pygame as pg


class Drawable(ABC):
    """
    Abstract base class for objects that can be drawn on a screen
    """

    @abstractmethod
    def draw(self):
        """
        Draws the object on the screen
        """


@dataclasses.dataclass
class Cardioid(Drawable):
    """
    Drawable object representing a cardioid
    """

    app: "App"
    radius: int = 400
    num_lines: int = 200
    counter: float = 0.0
    inc: float = 0.01

    @property
    def translate(self) -> tuple:
        """
        Returns the translation tuple to center the cardioid on the screen
        """
        return self.app.screen.get_width() // 2, self.app.screen.get_height() // 2

    def get_color(self) -> pg.Color:
        """
        Returns a color interpolated based on the counter value
        """
        self.counter += self.inc
        self.counter, self.inc = (
            (self.counter, self.inc)
            if 0 < self.counter < 1
            else (max(min(self.counter, 1), 0), -self.inc)
        )

        return pg.Color("red").lerp(pg.Color("green"), self.counter)

    def draw(self):
        """
        The draw function draws the cardioid on the screen
        """
        time = pg.time.get_ticks()
        self.radius = 350 + 50 * abs(math.sin(time * 0.004) - 0.5)
        factor = 1 + 0.0001 * time

        for i in range(self.num_lines):
            theta = (2 * math.pi / self.num_lines) * i
            x1 = int(self.radius * math.cos(theta)) + self.translate[0]
            y1 = int(self.radius * math.sin(theta)) + self.translate[1]

            x2 = int(self.radius * math.cos(factor * theta)) + self.translate[0]
            y2 = int(self.radius * math.sin(factor * theta)) + self.translate[1]

            pg.draw.aaline(self.app.screen, self.get_color(), (x1, y1), (x2, y2))


class App:
    """
    Application class encapsulating the main game loop and drawing logic
    """

    def __init__(self):
        """
        Initialize the application with a screen, a clock, and a Cardioid instance
        """
        self.screen = pg.display.set_mode([1600, 900])
        self.clock = pg.time.Clock()
        self.cardioid = Cardioid(self)

    def draw(self):
        """
        Draw the game objects on the screen
        """
        self.screen.fill(pg.Color("black"))
        self.cardioid.draw()
        pg.display.flip()

    def run(self):
        """
        Run the game loop until the user quits the game
        """
        while True:
            self.draw()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()
            self.clock.tick(60)


if __name__ == "__main__":
    app = App()
    app.run()
