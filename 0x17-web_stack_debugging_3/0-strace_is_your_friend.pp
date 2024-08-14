# Fixes extension problem in php file

exec {'Fix extension error phpp in wordpress-settings php file':
    command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
    path    => '/usr/local/bin/:/bin/',
    }