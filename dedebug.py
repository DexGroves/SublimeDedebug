import sublime
import sublime_plugin


debugger_commands = ['import pdb; pdb.set_trace()', 'import pdb',
                     'pdb.set_trace()', 'browser()']


def strip_debuggers(line):
    for to_purge in debugger_commands:
        line = line.replace(to_purge, '')
    line = clear_if_all_whitespace(line)
    return line


def clear_if_all_whitespace(line):
    if line.isspace():
        return ''
    return line


class DedebugCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        all_content = sublime.Region(0, self.view.size())
        line_regions = self.view.split_by_newlines(all_content)
        line_regions.sort(reverse=True)

        for line_region in line_regions:
            stripped_line = strip_debuggers(self.view.substr(line_region))
            self.view.replace(edit, line_region, stripped_line)
