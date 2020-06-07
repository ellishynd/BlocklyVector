import os
import sys
sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            '..'
        )
    )
)
import unittest
from vector import Vector

class TestVector(unittest.TestCase):

    def setUp(self):
        self.robot = Vector()
    
    def tearDown(self):
        self.robot.disconnect()

    
    def test_methods(self):
        
        #Wheels
        self.robot.wheels_drive(20, 10)
        self.robot.wheels_drive(-20, 10)
        self.robot.wheels_turn(90)
        self.robot.wheels_turn(-90)

        #Head
        self.robot.head_angle(0)
        self.robot.head_angle(100)
        self.robot.head_angle(33)

        #Arm
        self.robot.lift_height(100)
        self.robot.lift_height(0)
        self.robot.lift_height(50)

        #Sound
        self.robot.speak_text('Hello World')
        self.robot.play_animation('FistBumpSuccess')
        

        #Environment
        #self.robot.look_around()
        #self.robot.drive_to_cube()
        #self.robot.dock_with_cube()
        self.robot.pickup_cube()
        self.robot.put_down_cube()


if __name__ == "__main__":
    unittest.main()