<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php
    $link = mysqli_connect('127.0.0.1', 'root', 'root', 'gbphp');
    $result = mysqli_query($link, "SELECT * FROM images");

    function getPath ($path) {
        return scandir($path);
    }

    $path = "images";
    $images =  getPath($path);
    $pictures = array();

        for($i = 2; $i <= count($images) - 1; $i++) {
            $pictures[$i] ="{$path}/{$images[$i]}";
            $command = mysqli_query($link, "UPDATE `images` SET `link` = '$pictures[$i]' WHERE `id` = $j");
            $j++;
    }



    // $m = 0;
    // while($m < 3) {
    //     $command;
    // $m++;
    // }


    ?>
</body>
</html>