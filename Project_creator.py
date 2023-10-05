bl_info = {
    "name": "Project Creator",
    "author": "Saul Malagon Martinez",
    "version": (1, 0),
    "blender": (3, 6, 2),
    "location": "File -> New Project",
    "description": "Create a folder structure from template",
    "category": "Import-Export",
}

import bpy
import bpy_extras
import pathlib
import json

new_project = {
    "content": []
}

class Project_creator_preferences(bpy.types.AddonPreferences):
    """Addon Settings"""
    bl_idname = __name__
    
    template: bpy.props.StringProperty(name="Template", subtype="FILE_PATH")
    
    def draw(self, context):
        layout = self.layout
        layout.label(text="Create Project Configs")
        layout.prop(self, "template")
    
    

class Project_creator(bpy.types.Operator, bpy_extras.io_utils.ImportHelper):
    """Create a project folder structure"""
    bl_idname = "project_creator.new_project"
    bl_label = "New Project"
    
    def execute(self, context):
        file_path = context.preferences.addons[__name__].preferences.template
        
        if file_path != "":
            try:
                template = self.get_template(file_path)
            except json.decoder.JSONDecodeError:
                return {'ERROR IN TEMPLATE FILE'}
            self.create_project(template, self.filepath)
        else:
            self.create_project(new_project, self.filepath)
            
        return {'FINISHED'}
    
    def create_project(self, project, project_name):
        if "content" in project:
            for e in project["content"]:
                self.create_project(e, project_name + "/" + e["name"])
        else:
            path = pathlib.Path(project_name)
            path.mkdir(parents=True, exist_ok=True)
            
    def get_template(self, file_path):
        template = None
        with open(file_path, 'r') as file:
            template = json.loads(file.read())
        return template
            

# Registration
def menu_func(self, context):
    self.layout.operator(Project_creator.bl_idname, text="New Project")
    
def register():
    bpy.utils.register_class(Project_creator)
    bpy.utils.register_class(Project_creator_preferences)
    bpy.types.TOPBAR_MT_file.append(menu_func)
    
def unregister():
    bpy.utils.unregister_class(Project_creator)
    bpy.utils.unregister_class(Project_creator_preferences)
    bpy.types.TOPBAR_MT_file.remove(menu_func)
    

if __name__ == "__main__":
    register()