from anki_vector import Robot
from anki_vector.util import parse_command_args, speed_mmps, distance_mm, degrees


class Vector:
    """
    An interface to abstract the anki_vector sdk to 
    further simplify implementation.
    """

    args = parse_command_args()
    robot = Robot(args.serial)

    def __init__(self):
        self.connect()
        #self.robot.world.connect_cube()
        self.robot.behavior.drive_off_charger()
    
    
    def connect(self):
        self.robot.connect()
    
    def disconnect(self):
        self.robot.disconnect()

    def connect_cube(self) -> bool:
        if not self.robot.world.connected_light_cube:
            self.robot.world.connect_cube()
        return self.robot.world.connected_light_cube

    
    @staticmethod
    def percentage_value(percentage: int, min_value: int, max_value: int) -> int:
        
        range_value = max_value - min_value
        percentage = 0 if percentage < 0 else 100 if percentage > 100 else percentage
        
        return min_value + percentage * range_value // 100
    

    def wheels_drive(self, distance: float, speed_percentage: int):
        #Parameter Speed range = 0-100

        min_speed = 1
        max_speed = 220

        self.robot.behavior.drive_straight(
            distance_mm(distance),
            speed_mmps(
                self.percentage_value(
                    percentage=speed_percentage,
                    min_value=min_speed,
                    max_value=max_speed
                )
            )
        )

    def wheels_turn(self, angle: float):
        self.robot.behavior.turn_in_place(
            degrees(angle)
        )
    
    def head_angle(self, angle_percentage: int):
        #Parameter angle range 0-100
        
        min_angle = -22
        max_angle = 45
        
        self.robot.behavior.set_head_angle(
            degrees(
                self.percentage_value(
                    percentage=angle_percentage,
                    min_value=min_angle,
                    max_value=max_angle
                )
            )
        )
    
    def lift_height(self, height_percentage: int):
        #Parameter height_percentage range 0-100
        height = height_percentage / 100
        self.robot.behavior.set_lift_height(height)
    
    def speak_text(self, text: str):
        self.robot.behavior.say_text(text)

    def play_animation(self, animation: str):
        self.robot.anim.play_animation_trigger(animation)
    
    def look_around(self):
        self.robot.behavior.look_around_in_place()
    
    def drive_to_cube(self):
        if self.robot.world.connected_light_cube and self.robot.world.light_cube.is_visible:
            self.robot.behavior.go_to_object(
                target_object=self.robot.world.connected_light_cube,
                distance_from_object=distance_mm(70)
            )
    
    def dock_with_cube(self):
        if self.robot.world.connected_light_cube and self.robot.world.light_cube.is_visible:
            r = self.robot.behavior.dock_with_cube(
                target_object=self.robot.world.connected_light_cube,
                num_retries=3
            )
            print(r)
    
    def pickup_cube(self):
        self.connect_cube()
        self.observe_cube()
        self.pickup_object()
    
    def pickup_object(self):            
        if self.robot.world.connected_light_cube and self.robot.world.light_cube.is_visible:
        
            self.robot.behavior.pickup_object(
                target_object=self.robot.world.connected_light_cube,
                num_retries=3
            )
    
    def put_down_cube(self):
        if self.robot.status.is_carrying_block:
            self.robot.behavior.place_object_on_ground_here()

    def observe_cube(self) -> bool:
        
        count = 7
        while not self.robot.world.light_cube.is_visible and count:
            print('cube seen: {}, attemps left: {}'.format(self.robot.world.light_cube.is_visible, count))
            self.play_animation('FindCubeTurns')
            count -= 1
        
        if self.robot.world.light_cube.is_visible:
            self.play_animation('FindCubeReactToCube')
        else:
            self.play_animation('FetchCubeFailure')
        
        return self.robot.world.light_cube.is_visible

if __name__ == "__main__":
    pass