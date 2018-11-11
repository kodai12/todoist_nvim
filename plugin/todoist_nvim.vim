" --------------------------------
" Add plugins
" --------------------------------
python import sys
python import vim
python sys.path.append(vim.eval('expand("<sfile>:p:h")'))
python import todoist_nvim

" --------------------------------
"  Define functions
" --------------------------------
function! todoist_nvim#get_user()
  python todoist_nvim.get_user()
endfunction

function! todoist_nvim#get_project(project_name)
  python todoist_nvim.get_project(vim.eval('a:project_name'))
endfunction

function! todoist_nvim#get_all_projects()
  python todoist_nvim.get_all_projects()
endfunction

function! todoist_nvim#get_all_tasks(project_name)
  python todoist_nvim.get_all_tasks(vim.eval('a:project_name'))
endfunction

function! todoist_nvim#get_all_notes()
  python todoist_nvim.get_all_notes()
endfunction

" --------------------------------
"  Expose commands
" --------------------------------
command! TodoistUser call todoist_nvim#get_user()
command! -nargs=1 TodoistProject call todoist_nvim#get_project(<q-args>)
command! TodoistProjects call todoist_nvim#get_all_projects()
command! -nargs=1 TodoistTasks call todoist_nvim#get_all_tasks(<q-args>)
command! TodoistNotes call todoist_nvim#get_all_notes()
