import os

# all dir and file name should be English
obj_dir = hou.ui.selectFile(title = "Select Obj Directory",file_type = hou.fileType.Directory)

obj_dir_expanded = hou.expandString(obj_dir)
obj_files = os.listdir(obj_dir_expanded)

file_nodes = []
loader = hou.node('/obj').createNode('geo', "Obj_Loader")

for obj in obj_files:
   obj_file_node = loader.createNode('file',obj)
   obj_file_node.parm('file').set(obj_dir + '/' + obj)
   obj_file_node.parm('missingframe').set(1)

   file_nodes.append(obj_file_node)

merge_objs = loader.createNode('merge','PHOTO_Merger')

i=0
for node in file_nodes:
   file_Transform = loader.createNode('xform','Transform')
   file_Transform.setInput(0,node)
   file_Transform.parm('ty').set(i)
   merge_objs.setNextInput(file_Transform)
   i+=1

loader.layoutChildren()

merge_objs.setDisplayFlag(True)
merge_objs.setRenderFlag(True)