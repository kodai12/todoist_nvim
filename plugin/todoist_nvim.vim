" --------------------------------
" Add plugins
" --------------------------------
python import sys
python import vim
python sys.path.append(vim.eval('expand("<sfile>:p:h")'))
python import rplugin.python3.interface.todoist_nvim as todoist_nvim

" --------------------------------
"  Define functions
" --------------------------------
function! todoist_nvim#get_user()
  python todoist_nvim.get_user()
endfunction

function! todoist_nvim#get_project(args)
  python todoist_nvim.get_project(vim.eval('a:args'))
endfunction

function! todoist_nvim#get_all_projects()
  python todoist_nvim.get_all_projects()
endfunction

function! todoist_nvim#get_all_tasks(args)
  python todoist_nvim.get_all_tasks(vim.eval('a:args'))
endfunction

function! todoist_nvim#add_task(args)
  python todoist_nvim.add_task(vim.eval('a:args'))
endfunction

function! todoist_nvim#complete_task(args)
  python todoist_nvim.complete_task(vim.eval('a:args'))
endfunction

function! todoist_nvim#delete_task(args)
  python todoist_nvim.delete_task(vim.eval('a:args'))
endfunction

function! todoist_nvim#get_all_reminders(args)
  python todoist_nvim.get_all_reminders(vim.eval('a:args'))
endfunction

function! todoist_nvim#get_all_notes()
  python todoist_nvim.get_all_notes()
endfunction

" --------------------------------
"  Expose commands
" --------------------------------
command! TodoistUser call todoist_nvim#get_user()
command! -nargs=? TodoistProject call todoist_nvim#get_project(<q-args>)
command! TodoistProjects call todoist_nvim#get_all_projects()
command! -nargs=? TodoistTasks call todoist_nvim#get_all_tasks(<q-args>)
command! -nargs=1 TodoistAddTask call todoist_nvim#add_task(<q-args>)
command! -nargs=1 TodoistCompleteTask call todoist_nvim#complete_task(<q-args>)
command! -nargs=1 TodoistDeleteTask call todoist_nvim#delete_task(<q-args>)
command! TodoistNotes call todoist_nvim#get_all_notes()
command! -nargs=1 TodoistReminders call todoist_nvim#get_all_reminders(<q-args>)
