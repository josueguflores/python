<?php



$uploaddir = 'Imgs/';
$uploadfile = $uploaddir . basename($_FILES['userfile']['name']);
 
echo "<p>"; 
if (move_uploaded_file($_FILES['userfile']['tmp_name'], $uploadfile)) {
echo "File is valid, and was successfully uploaded.\n";
echo $_FILES['userfile']['name'];
header("Location: UploadExitoso.html?ImgName=".$_FILES['userfile']['name']."");
} else {
echo "Upload failed";
}
 
echo "</p>";
echo '<pre>';
echo 'Here is some more debugging info:';
print_r($_FILES);
print "</pre>";

?>