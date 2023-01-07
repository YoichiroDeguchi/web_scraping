<?php
$command="python3 scraping.py ";
exec($command,$pythonData);

var_dump($pythonData);

?>