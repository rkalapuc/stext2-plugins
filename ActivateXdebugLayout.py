import sublime, sublime_plugin
class ActivateXdebugLayout(sublime_plugin.WindowCommand):
  def run(self):
    window = sublime.active_window()

    window.set_layout({
      "cols": [0.0, 0.5, 1.0],
      "rows": [0.0, 0.7, 1.0],
      "cells":
      [
          [0, 0, 2, 1],
          [0, 1, 1, 2],
          [1, 1, 2, 2]
      ]
    })

    window.run_command('move_to_group_by_name', {"vname": "Xdebug Context", "gindex": 1, "vindex": 0})
    window.run_command('move_to_group_by_name', {"vname": "Xdebug Watch", "gindex": 1, "vindex": 1})
    window.run_command('move_to_group_by_name', {"vname": "Xdebug Stack", "gindex": 2, "vindex": 0})
    window.run_command('move_to_group_by_name', {"vname": "Xdebug Breakpoint", "gindex": 2, "vindex": 1})