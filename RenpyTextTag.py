import sublime, sublime_plugin

# Extends TextCommand so that run() receives a View to modify.
class RenpyTextTagCommand(sublime_plugin.TextCommand):

    def run(self, edit, **args):

        tag = args['tag']
        view = self.view
        positions = []
        selections = view.sel()

        for selection in selections:

            view.insert(edit, selection.end(), "{/"+tag+"}")
            view.insert(edit, selection.begin(), "{"+tag+"}")

            lenSel = selection.size()
            (row, col) = self.view.rowcol(selection.begin())
            col += 3
            r1 = sublime.Region(view.text_point(row, col))
            if lenSel == 0:
                positions.append(r1)
            else:
                r2 = sublime.Region(view.text_point(row, col+lenSel))
                positions.append(r2.cover(r1))

        selections.clear()

        for position in positions:
            self.view.sel().add(position)
            self.view.show(position)