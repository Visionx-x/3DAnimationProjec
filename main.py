# main.py

from panda3d.core import Point3, Vec3
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from math import sin, cos, radians

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Set up the environment
        self.set_background_color(0.5, 0.5, 0.5)  # Light gray background

        # Create a ground plane
        self.ground = self.loader.loadModel("models/plane")  # Use a built-in plane model
        self.ground.reparentTo(self.render)
        self.ground.setScale(10, 10, 1)
        self.ground.setPos(0, 0, -1)

        # Create a cube to represent the boy
        self.boy = self.loader.loadModel("models/box")  # Use a built-in box model
        self.boy.reparentTo(self.render)
        self.boy.setScale(0.5, 0.5, 1)
        self.boy.setPos(0, 0, 0)

        # Add a task to animate the boy typing
        self.taskMgr.add(self.animate_typing, "animate_typing")

    def animate_typing(self, task):
        # Simple animation logic (moving the boy up and down)
        self.boy.setZ(0.5 * sin(task.time * 2))  # Move up and down
        return Task.cont

if __name__ == "__main__":
    app = MyApp()
    app.run()
