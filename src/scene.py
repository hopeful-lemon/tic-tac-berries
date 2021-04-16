
class Scene_manager:
    def __init__(self):
        self.scenes = []
        self.current_scene = 1

    def switch(self, scene_num):
        self.current_scene = scene_num

    def add_scene(self, scene):
        self.scenes.append(scene)

    def draw(self):
        self.scenes[self.current_scene].draw()

    def handle_event(self, event):
        self.scenes[self.current_scene].handle_event(event)

class Scene:
    def __init__(self, draw_callback, handle_event_callback):
        self.draw_callback = draw_callback
        self.handle_event_callback = handle_event_callback
        
    def draw(self):
        self.draw_callback()

    def handle_event(self, event):
        self.handle_event_callback(event)
