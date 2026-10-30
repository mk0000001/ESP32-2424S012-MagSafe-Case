from pathlib import Path
import json,trimesh
root=Path(__file__).resolve().parents[1]
p=root/'print/V18'
names=['BODY','BOARD_SUPPORT_FRAME','SCREW_RETAINING_RING_3POINT','MAGSAFE_OUTER_LID','BATTERY_TRAY_INNER','RING_TOOL_3POINT']
report={}
for n in names:
 m=trimesh.load_mesh(str(p/(n+'_V18_PRINT.stl')),process=True)
 row={'watertight':bool(m.is_watertight),'winding_consistent':bool(m.is_winding_consistent),'positive_volume':bool(m.volume>0),'components':len(m.split()),'bounds_mm':m.bounds.tolist(),'facets':len(m.faces)}
 assert row['watertight'] and row['winding_consistent'] and row['positive_volume'] and row['components']==1,n
 assert abs(m.bounds[0,2])<1e-4,n
 report[n]=row
(root/'validation/V18/verification_STL.json').write_text(json.dumps(report,indent=2))
print(json.dumps(report,indent=2))
