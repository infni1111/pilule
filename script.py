import bpy

# 1. Nettoyer la scène
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# 2. Ajouter un cube comme domaine
bpy.ops.mesh.primitive_cube_add(size=6, location=(0, 0, 3))
domain = bpy.context.object
domain.name = "Domain"

# Ajouter modifier Fluid - domaine
fluid_mod = domain.modifiers.new(name="Fluid", type='FLUID')
fluid_mod.fluid_type = 'DOMAIN'

# Configurer le domaine comme gaz (feu/fumée)
domain_settings = fluid_mod.domain_settings
domain_settings.domain_type = 'GAS'
domain_settings.cache_type = 'MODULAR'
domain_settings.cache_directory = "//cache"

# 3. Ajouter un cube comme source de feu
bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0, 1))
flow = bpy.context.object
flow.name = "Flow"

# Ajouter modifier Fluid - flow
fluid_flow = flow.modifiers.new(name="Fluid", type='FLUID')
fluid_flow.fluid_type = 'FLOW'

# Configurer comme émetteur de feu (fire source)
flow_settings = fluid_flow.flow_settings
flow_settings.flow_type = 'FIRE'
flow_settings.flow_behavior = 'INFLOW'

# 4. Ajouter une caméra
bpy.ops.object.camera_add(location=(10, -10, 10), rotation=(1.1, 0, 0.8))
camera = bpy.context.object
bpy.context.scene.camera = camera

# 5. Ajouter lumière
bpy.ops.object.light_add(type='SUN', location=(5, -5, 15))

# 6. Paramètres animation
bpy.context.scene.frame_start = 1
bpy.context.scene.frame_end = 250

# 7. Paramètres rendu vidéo
bpy.context.scene.render.filepath = "/tmp/fire_simulation_"
bpy.context.scene.render.image_settings.file_format = 'FFMPEG'
bpy.context.scene.render.ffmpeg.format = 'MPEG4'
bpy.context.scene.render.ffmpeg.codec = 'H264'
bpy.context.scene.render.ffmpeg.constant_rate_factor = 'HIGH'
bpy.context.scene.render.ffmpeg.ffmpeg_preset = 'GOOD'

# 8. Lancer rendu animation
bpy.ops.render.render(animation=True)

print("Simulation feu terminée, vidéo exportée dans /tmp/")
