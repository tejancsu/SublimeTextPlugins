import sublime, sublime_plugin

class CopyFileNameCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		f_name = self.view.file_name()
		sublime.set_clipboard(f_name)