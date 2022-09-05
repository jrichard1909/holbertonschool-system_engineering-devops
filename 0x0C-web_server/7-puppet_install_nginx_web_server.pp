# install nginx
exec {'/usr/bin/env sudo apt-get -y update': }
exec {'/usr/bin/env sudo apt-get -y install nginx': }
exec {'/usr/bin/env echo "Hello World" | sudo tee /var/www/html/index.nginx-debian.html': }
exec {'/usr/bin/env sudo sed -i '0,/location \/ {/s//location \/redirect_me {\n\t\treturn 301 https:\/\/www.youtube.com\/watch?v=QH2-TGUlwu4;/' /etc/nginx/sites-available/default': }
exec {'/usr/bin/env echo "Ceci n'est pas une page" | sudo tee /var/www/html/xyzfoo.html': }
exec {'/usr/bin/env sudo sed -i "0,/server_name _;/s//server_name _;\n\n\terror_page 404 \/xyzfoo.html;\n\tlocation \/xyzfoo.html {\n\t\troot \/var\/www\/html;\n\t\tinternal;\n\t}/" /etc/nginx/sites-available/default': }
exec {'/usr/bin/env service nginx start': }
