" --------------------------------
" Add our plugin to the path
" --------------------------------
python import sys
python import vim
python sys.path.append(vim.eval('expand("<sfile>:p:h")'))
python import todoist_nvim

" --------------------------------
"  Function(s)
" --------------------------------
function! todoist_nvim#get_project(project_name)
  python todoist_nvim.get_project(vim.eval('a:project_name'))
endfunction

function! todoist_nvim#get_projects()
  python todoist_nvim.get_all_projects()
endfunction

" --------------------------------
"  Expose our commands to the user
" --------------------------------
command! TodoistProjects call todoist#get_projects()
command! -nargs=1 TodoProject call todoist#get_project(<f-args>)
