# SublimeDedebug
Remove Python and R debugger calls from an open text file in Sublime Text 3.

Tired of being shamed by friends, family and coworkers for forgetting to remove 
a `pdb` call in a commit? Despair no longer!

Removes any instance of `import pdb`, `pdb.set_trace()`, 
`import pdb; pdb.set_trace()` or `browser()` from a source file.

# Shortcut
ctrl+alt+e.

# Roadmap
* Support for projects
* Only activate if operating in Python, R or R-Extended syntax.
