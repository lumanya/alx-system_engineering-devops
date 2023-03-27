# puppet manifest to kill process

exec {'kill-killmenow':

  command => '/usr/bin/pkill killmenow',

}
