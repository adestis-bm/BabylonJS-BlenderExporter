import bpy

if "bpy" in locals():
    import imp
    if 'nodes' in locals():
        imp.reload(nodes)  # directory
    if 'env_textures' in locals():
        imp.reload(env_textures)  # directory
    if 'baking_recipe' in locals():
        imp.reload(baking_recipe)
    if 'material' in locals():
        imp.reload(material)
    if 'texture' in locals():
        imp.reload(texture)