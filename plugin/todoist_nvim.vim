" --------------------------------
" Add our plugin to the path
" --------------------------------
python import sys
python sys.path.append(vim.eval('expand("<sfile>:h")'))
python import todoist_nvim

" --------------------------------
"  Function(s)
" --------------------------------
function! GetTasks()
python todoist_nvim.get_tasks()
endfunction

function! GetCompletedTasks()
python todoist_nvim.get_completed_tasks()
endfunction

function! GetProjects()
python todoist_nvim.get_projects()
endfunction

" --------------------------------
"  Expose our commands to the user
" --------------------------------
command! ToDo call GetTasks()
command! ToDoProjects call GetProjects()
command! ToDoCompleted call GetCompletedTasks()

