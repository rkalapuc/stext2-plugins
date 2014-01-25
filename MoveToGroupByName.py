import sublime, sublime_plugin
class MoveToGroupByName(sublime_plugin.WindowCommand):
  def run(self, vname, gindex, vindex):
    window = sublime.active_window()
    views = window.views()

    targetView = None
    for view in views:
      if view.name() == vname:
        targetView = view
        break

    if targetView is  None:
      print 'View [' + vname+ '] not found!'
      return

    gcount = window.num_groups()

    if gindex < 0 or gindex >= gcount:
      print 'Invalid group index [',gindex,'] specified!'
      return

    window.set_view_index(targetView, gindex, vindex)