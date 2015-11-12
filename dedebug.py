import sublime
import sublime_plugin


class DedebugCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        self.debugger_commands = ['import pdb; pdb.set_trace()', 'import pdb',
                                  'pdb.set_trace()', 'browser()']

        all_content = sublime.Region(0, self.view.size())
        line_regions = self.view.split_by_newlines(all_content)
        line_regions.sort(reverse=True)

        modified_lines = []

        for line_region in line_regions:
            line_text = self.view.substr(line_region)

            if self.contains_debuggers(line_text):
                stripped_line = self.strip_debuggers(line_text)
                self.view.replace(edit, line_region, stripped_line)

                (line_row, line_col) = self.view.rowcol(line_region.a)
                modified_lines.append(str(line_row))

        self.send_status_message(modified_lines)

    def contains_debuggers(self, line):
        for debugger_command in self.debugger_commands:
            if debugger_command in line:
                return True
        return False

    def strip_debuggers(self, line):
        for debugger_command in self.debugger_commands:
            line = line.replace(debugger_command, '')
        line = self.clear_if_all_whitespace(line)
        return line

    @staticmethod
    def clear_if_all_whitespace(line):
        if line.isspace():
            return ''
        return line

    @staticmethod
    def send_status_message(modified_lines):
        modified_lines.sort()
        if len(modified_lines) == 0:
            msg = 'No debugger commands found!'
        if len(modified_lines) == 1:
            msg = 'Removed debugger on line: ' + modified_lines[0]
        if len(modified_lines) >= 2:
            msg = 'Removed debuggers on lines: ' + ', '.join(modified_lines)

        sublime.status_message(msg)
