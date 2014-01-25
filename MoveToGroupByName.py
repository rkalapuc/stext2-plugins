import sublime, sublime_plugin
class MoveToGroupByName(sublime_plugin.WindowCommand):
 def run(self, direction, test):
   pkg_name = "move_to_group_by_name"
   window = sublime.active_window()
   view = window.active_view()
   ret = window.get_view_index(view)
   print 'test=', test
   if ret == -1:
     return
   (group, index) = ret
   if group < 0 or index < 0:
     return
   views = window.views_in_group(window.active_group())
   num_views = len(views)
   oldIndex = index
   if direction == "left":
     if index > 0:
       index -= 1
   elif direction == "right":
     if index < num_views - 1:
       index += 1
   else:
     print 'Unrecognized direction1:',direction+'. Use left or right.'
   if oldIndex != index:
     window.set_view_index(view, group, index)