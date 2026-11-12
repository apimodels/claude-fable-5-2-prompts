# scene.py: build a small animated scene entirely in code and render it.
# usage:
#   blender -b -P scene.py -- --preview      # 3 key frames at 25% size, as PNG
#   blender -b -P scene.py -- --final        # every frame at full size, as MP4
import sys, math, os
import bpy

args = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
PREVIEW = "--preview" in args
OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), "out"))

bpy.ops.wm.read_factory_settings(use_empty=True)  # start from an empty scene
scene = bpy.context.scene
scene.frame_start, scene.frame_end = 1, 72          # 3 seconds at 24 fps
scene.render.fps = 24

def material(name, rgb, rough=0.5, metal=0.0):
    m = bpy.data.materials.new(name)
    p = m.node_tree.nodes["Principled BSDF"]
    p.inputs["Base Color"].default_value = (*rgb, 1)
    p.inputs["Roughness"].default_value = rough
    p.inputs["Metallic"].default_value = metal
    return m

# ground and a bouncing ball, all generated in code
bpy.ops.mesh.primitive_plane_add(size=20)
bpy.context.object.data.materials.append(material("Ground", (0.08, 0.09, 0.12), rough=0.9))
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.6, segments=64, ring_count=32)
ball = bpy.context.object
bpy.ops.object.shade_smooth()
ball.data.materials.append(material("Ball", (0.95, 0.45, 0.15), rough=0.25))

# keyframes: three bounces, squashed on contact
for f in range(scene.frame_start, scene.frame_end + 1):
    t = (f - 1) / 24
    phase = (t % 1.0)
    height = 4 * phase * (1 - phase) * 2.0          # parabola per bounce
    ball.location = (t * 1.2 - 1.8, 0, 0.6 + height)
    squash = 1 - 0.25 * max(0.0, 1 - height / 0.4)
    ball.scale = (1 / math.sqrt(squash), 1 / math.sqrt(squash), squash)
    ball.keyframe_insert("location", frame=f)
    ball.keyframe_insert("scale", frame=f)

# light, camera, world
bpy.ops.object.light_add(type="SUN", location=(4, -4, 8))
bpy.context.object.data.energy = 3.0
bpy.context.object.rotation_euler = (math.radians(50), 0, math.radians(35))
bpy.ops.object.camera_add(location=(0, -10, 2.4), rotation=(math.radians(84), 0, 0))
scene.camera = bpy.context.object
scene.world = bpy.data.worlds.new("World")
scene.world.node_tree.nodes["Background"].inputs["Color"].default_value = (0.02, 0.025, 0.035, 1)

# render settings
scene.render.engine = "BLENDER_EEVEE"
scene.render.resolution_x, scene.render.resolution_y = 1280, 720
scene.render.resolution_percentage = 25 if PREVIEW else 100

if PREVIEW:
    scene.render.image_settings.file_format = "PNG"
    for f in (1, 18, 36):
        scene.frame_set(f)
        scene.render.filepath = os.path.join(OUT, f"preview_{f:03d}.png")
        bpy.ops.render.render(write_still=True)
else:
    scene.render.image_settings.media_type = "VIDEO"
    scene.render.image_settings.file_format = "FFMPEG"
    scene.render.ffmpeg.format = "MPEG4"
    scene.render.ffmpeg.codec = "H264"
    scene.render.filepath = os.path.join(OUT, "ball_")
    bpy.ops.render.render(animation=True)
