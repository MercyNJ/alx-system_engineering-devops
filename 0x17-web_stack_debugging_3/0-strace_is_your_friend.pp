# A puppet manuscript to replace a line causing an error in a file on a server

$file_with_error = '/var/www/html/wp-settings.php'

#Replaced "class-wp-locale.phpp" with "class-wp-locale.php"

exec { 'replace_line':
  command => "sed -i 's/class-wp-locale.phpp/class-wp-locale.php/g' ${file_with_error}",
  path    => ['/bin','/usr/bin']
}
