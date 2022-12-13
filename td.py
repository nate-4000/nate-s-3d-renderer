import screen
screen.sx = 64
screen.sy = 64
class InsideCameraError(Exception):
    def __init__(self, point, message="Point is inside or unrenderable by camera: "):
        self.point = point
        self.message = message + str(point)
        super().__init__(self.message)
        
class camera:
    def ct2d(point:list=[0,0,0]):
        x = point[0]
        y = point[1]
        z = point[2]
        if z == 0:
            raise InsideCameraError(point)
        u = x/z
        v = y/z
        return [u, v]
    def floor(x):
        return int(x - (x % 1))
    def render(obj: list, offs:list=[0, 0 ,0]):
        for i in obj:
            oi = [i[0]+offs[0], i[1]+offs[1], i[2]+offs[2]]
            d = camera.ct2d(oi)
            screen.pushp(camera.floor(d[0]) + 32,camera.floor(d[1]) + 32, "#", False)
        screen.updscn()
