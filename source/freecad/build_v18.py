import FreeCAD as A, Part, MeshPart, math, json, os
from pathlib import Path
V=A.Vector
root=Path(__file__).resolve().parents[2]
src=str(root/'cad/V17/brep')
out=str(root/'build/V18')
os.makedirs(out,exist_ok=True)
def read(n):
 s=Part.Shape();s.read(src+'/'+n+'.brep');return s
names=['BODY','BOARD_SUPPORT_FRAME','SCREW_RETAINING_RING_3POINT','MAGSAFE_OUTER_LID','BATTERY_TRAY_INNER','RING_TOOL_3POINT']
parts={n:read(n) for n in names}
oldbody=parts['BODY'].copy();oldtray=parts['BATTERY_TRAY_INNER'].copy()
body=oldbody.copy();parts['BODY']=body
ux=2.8;seat=.5199259519577026*9;uz=seat-4.9;floor=-18.3
def port(w,h,r,y,zc,depth):
 ss=[Part.makeBox(w-2*r,depth,h,V(ux-w/2+r,y,zc-h/2)),Part.makeBox(w,depth,h-2*r,V(ux-w/2,y,zc-h/2+r))]
 for x in [ux-w/2+r,ux+w/2-r]:
  for z in [zc-h/2+r,zc+h/2-r]:ss.append(Part.makeCylinder(r,depth,V(x,y,z),V(0,1,0)))
 s=ss[0]
 for q in ss[1:]:s=s.fuse(q)
 return s.removeSplitter()
def rounded(s,r=.45):
 es=[e for e in s.Edges if e.BoundBox.ZLength>.1 and e.BoundBox.XLength<1e-6 and e.BoundBox.YLength<1e-6]
 return s.makeFillet(r,es)

shroud=port(20.2,13.9,1.4,20.2,uz-.5,14)
shroud=shroud.common(Part.makeCylinder(32.65177536010742,40,V(0,0,body.BoundBox.ZMin)))
shroud=shroud.common(Part.makeBox(80,80,body.BoundBox.ZMax-body.BoundBox.ZMin,V(-40,-40,body.BoundBox.ZMin)))
shroud=shroud.cut(port(17,10.7,.6,21.4,uz-.5,20))
shroud=shroud.cut(port(10.6,5.2,1.0,19.9,uz,20)).removeSplitter()
shroud=shroud.common(Part.makeBox(80,80,30,V(-40,-40,-4.8))).removeSplitter()
body=body.fuse(shroud).removeSplitter();parts['BODY']=body

# The rigid lid pads are 0.5 mm taller; the nominal cell remains uncompressed.
tray=oldtray.cut(Part.makeBox(54,35,8,V(-27,-17.5,floor))).removeSplitter()
for x in [-17,17]:
 for y in [-8,8]:tray=tray.fuse(Part.makeCylinder(3.5,1.1,V(x,y,floor-.1)))
tray=tray.fuse(Part.makeBox(12,10,1.1,V(-6,-5,floor-.1)))
for x in [25.3,-26.6]:tray=tray.fuse(rounded(Part.makeBox(1.3,8,3.2,V(x,-4,floor-.1))))
for y in [15.3,-16.6]:tray=tray.fuse(rounded(Part.makeBox(8,1.3,3.2,V(-4,y,floor-.1))))
tray=tray.removeSplitter();parts['BATTERY_TRAY_INNER']=tray
battery=Part.makeBox(50,30,5,V(-25,-15,-17.3))
magnet=read('MagnetReference');wire=read('WireReference')
frame=parts['BOARD_SUPPORT_FRAME'];ring=parts['SCREW_RETAINING_RING_3POINT'];tool=parts['RING_TOOL_3POINT'];outer=parts['MAGSAFE_OUTER_LID']
report={'version':18,'base_version':17,'changes':{
 'battery_pad_height_increase_mm':.5,'battery_guide_inner_mm':[50.6,30.6],
 'battery_guide_total_height_mm':3.2,'battery_vertical_free_travel_mm':.3,
 'usb_shield_back_y_mm':20.2,'usb_shield_front_y_mm':21.4,'usb_shield_thickness_mm':1.2,
 'usb_shield_window_mm':[10.6,5.2],'usb_shield_side_wall_nominal_mm':1.6,
 'usb_shield_bottom_z_mm':-4.8,'usb_outer_cable_recess_mm':[17,10.7],
 'usb_small_clearance_to_ring_mm':.4,'usb_socket_face_assumed_y_mm':22.,
 'usb_socket_clearance_each_side_mm':.6},
 'battery_measured_mm':[50,30,5],'battery_reference_back_z_mm':-17.3,
 'battery_is_not_compressed':True,'physical_validation':'CAD only; user reports V17 loose battery and exposed PCB at USB. V18 has not been printed.',
 'reprint_changed_parts':['BODY','BATTERY_TRAY_INNER'],
 'unchanged_from_v17':['BOARD_SUPPORT_FRAME','SCREW_RETAINING_RING_3POINT','MAGSAFE_OUTER_LID','RING_TOOL_3POINT']}
for n,s in parts.items():
 assert s.isValid() and len(s.Solids)==1,(n,s.isValid(),len(s.Solids))
case_names=names[:-1]
overlaps={}
for i,n in enumerate(case_names):
 for other in case_names[i+1:]:
  v=parts[n].common(parts[other]).Volume;overlaps[n+'__'+other]=v;assert v<1e-4,(n,other,v)
report['assembly_overlaps_mm3']=overlaps
references={}
for refname,s in [('battery',battery),('magnet',magnet),('wire',wire)]:
 for n in case_names:
  v=parts[n].common(s).Volume;references[refname+'__'+n]=v;assert v<1e-4,(refname,n,v)
report['reference_overlaps_mm3']=references
# All 27 V15/V17 full plug insertion poses must still clear the added shield.
cables=[]
for front in [21.8,22.3,23.]:
 for dx in [-.6,0,.6]:
  for dz in [-.8,0,.8]:
   head=Part.makeBox(15,14,8,V(ux+dx-7.5,front,uz+dz-4))
   metal=port(8.25,2.4,1.19,front-6.11,uz+dz,6.11);metal.translate(V(dx,0,0))
   row={'front_y':front,'dx':dx,'dz':dz,'overlap_mm3':{}}
   for n in case_names:
    v=parts[n].common(head).Volume+parts[n].common(metal).Volume
    row['overlap_mm3'][n]=v;assert v<1e-4,row
   cables.append(row)
report['full_plug_insertion_poses']=cables
# Nominal module PCB envelope, its front stem, and USB shell remain clear.
pcb=Part.makeCylinder(18.1,1.2,V(0,0,seat-3.7))
pcb=pcb.fuse(Part.makeBox(14.23,3.74,1.2,V(-7.115,16.26,seat-3.7)))
socket=Part.makeBox(9.4,9,4,V(ux-4.7,13,uz-2))
for label,s in [('pcb',pcb),('usb_shell',socket)]:
 v=body.common(s).Volume;report[label+'_body_overlap_mm3']=v;assert v<1e-4,(label,v)
# Direct sight through the old broad aperture at PCB height is intercepted
# except for the close-clearance USB shell opening. Count simple projection rays.
blocked=0;tested=0
for j in range(32):
 x=ux-8+.5*j
 if ux-5.3-.001<=x<=ux+5.3+.001:continue
 for z in [seat-3.7+.2,seat-3.7+.8]:
  ray=Part.makeBox(.05,1.2,.05,V(x,20.2,z))
  tested+=1
  if body.common(ray).Volume>1e-5:blocked+=1
assert blocked==tested,(blocked,tested)
report['pcb_direct_sight_test']={'rays_outside_socket_window':tested,'blocked_by_shield':blocked}
motions=[]
for a in [-720,-540,-360,-270,-180,-90,-45,0,11.25]:
 row={'angle':a}
 for n in ['SCREW_RETAINING_RING_3POINT','RING_TOOL_3POINT']:
  s=parts[n].copy();s.rotate(V(),V(0,0,1),a);s.translate(V(0,0,3.2*a/360))
  v=body.common(s).Volume+frame.common(s).Volume;row[n]=v;assert v<1e-4,row
 motions.append(row)
report['ring_and_tool_motion']=motions
for dz in [-20,-12,-5,-1,0]:
 s=frame.copy();s.translate(V(0,0,dz));assert body.common(s).Volume<1e-4,('frame_insert',dz)
inner=[]
for a in [10,8,6,4,2,0]:
 s=tray.copy();s.rotate(V(),V(0,0,1),a)
 v=outer.common(s).Volume;inner.append({'angle':a,'overlap_mm3':v});assert v<1e-4,inner[-1]
for dz in [14,8,4,2,0]:
 s=tray.copy();s.rotate(V(),V(0,0,1),10);s.translate(V(0,0,dz));assert outer.common(s).Volume<1e-4,('tray_insert',dz)
report['inner_tray_lock_motion']=inner
cap=[]
for a in [-20,-17.5,-15,-12.5,-10,-7.5,-5,-2.5,0]:
 row={'angle':a}
 for n,s0 in [('outer',outer),('tray',tray),('battery',battery),('magnet',magnet)]:
  s=s0.copy();s.rotate(V(),V(0,0,1),a);v=body.common(s).Volume
  row[n]=v;assert v<1e-4,row
 cap.append(row)
report['cap_rotation_motion']=cap
for dz in [-25,-12,-6,-2,0]:
 for n in ['MAGSAFE_OUTER_LID','BATTERY_TRAY_INNER']:
  s=parts[n].copy();s.rotate(V(),V(0,0,1),-20);s.translate(V(0,0,dz));assert body.common(s).Volume<1e-4,('cap_insert',n,dz)
free=battery.copy();free.translate(V(0,0,.3));assert body.common(free).Volume<1e-4
caught=battery.copy();caught.translate(V(0,0,.4));v=body.common(caught).Volume;assert v>1;report['battery_overtravel_0_4mm_collision_mm3']=v
assert wire.common(free).Volume<1e-4
# Four pads plus the centre support prevent rocking; measure both lateral limits.
lateral=[]
for axis in ['x','y']:
 for sign in [-1,1]:
  shift=V(.3*sign if axis=='x' else 0,.3*sign if axis=='y' else 0,0)
  s=battery.copy();s.translate(shift);assert tray.common(s).Volume<1e-4,('lateral_clear',axis,sign)
  shift=V(.45*sign if axis=='x' else 0,.45*sign if axis=='y' else 0,0)
  s=battery.copy();s.translate(shift);v=tray.common(s).Volume;assert v>.1
  lateral.append({'axis':axis,'sign':sign,'overtravel_0_45mm_capture_mm3':v})
report['battery_lateral_capture']=lateral
for label,roi in [('screen',Part.makeCylinder(18.8,4,V(0,0,2.5))),('rear_bayonet',Part.makeCylinder(40,7,V(0,0,body.BoundBox.ZMin)))]:
 a=oldbody.common(roi);b=body.common(roi);diff=a.cut(b).Volume+b.cut(a).Volume;assert diff<1e-4
 report[label+'_preserved_diff_mm3']=diff
print('V18 battery, sight shield, 27 plugs and assembly motion verified',flush=True)

doc=A.newDocument('ESP32_2424S012_FIT_V18')
for n,s in parts.items():
 s.exportBrep(out+'/'+n+'.brep')
 obj=doc.addObject('PartDesign::Feature',n);obj.Shape=s
 if n=='RING_TOOL_3POINT':obj.Visibility=False
 mesh=MeshPart.meshFromShape(Shape=s,LinearDeflection=.005,AngularDeflection=.12,Relative=False)
 assert mesh.isSolid() and len(mesh.getSelfIntersections())==0,n
 mesh.write(out+'/'+n+'_ASSEMBLY.stl')
 if n in ['BODY','BOARD_SUPPORT_FRAME']:
  matrix=A.Matrix();matrix.rotateX(math.pi);mesh.transform(matrix)
 matrix=A.Matrix();matrix.move(V(0,0,-mesh.BoundBox.ZMin));mesh.transform(matrix)
 mesh.write(out+'/'+n+'_V18_PRINT.stl');print('PRINT',n,mesh.CountFacets,flush=True)
for n,s in [('BatteryReference',battery),('MagnetReference',magnet),('WireReference',wire)]:
 obj=doc.addObject('PartDesign::Feature',n);obj.Shape=s;obj.Visibility=False;s.exportBrep(out+'/'+n+'.brep')
doc.Label='V18 — 배터리 흔들림 감소 / USB-C 기판 가림벽'
doc.recompute();doc.saveAs(out+'/ESP32_2424S012_FIT_V18.FCStd')
with open(out+'/verification_native.json','w',encoding='utf-8') as f:json.dump(report,f,ensure_ascii=False,indent=2)
print('COMPLETE V18',out,flush=True)
