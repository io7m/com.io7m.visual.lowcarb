import bpy
  
for p in bpy.data.objects:
    if p and p.asset_data:
        p.asset_data.copyright = '© 2023 Mark Raynsford'
        p.asset_data.license = 'Public Domain'

for p in bpy.data.collections:
    if p and p.asset_data:
        p.asset_data.copyright = '© 2023 Mark Raynsford'
        p.asset_data.license = 'Public Domain'

