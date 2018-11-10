" --------------------------------
" Add our plugin to the path
" --------------------------------
python import sys
python sys.path.append(vim.eval('expand("<sfile>:p:h")'))
python import todoist_nvim

" --------------------------------
"  Function(s)
" --------------------------------
function! GetProjects()
python todoist_nvim.get_projects()
endfunction

" --------------------------------
"  Expose our commands to the user
" --------------------------------
command! TodoistProjects call GetProjects()

