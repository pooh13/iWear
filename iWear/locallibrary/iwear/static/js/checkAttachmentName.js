<script type="text/javascript" language="javascript">
function checkfile(sender) {

  // 可接受的附檔名
  var validExts = new Array(".gif", ".jpeg", ".png");

  var fileExt = sender.value;
  fileExt = fileExt.substring(fileExt.lastIndexOf('.'));
  if (validExts.indexOf(fileExt) < 0) {
    alert("檔案類型錯誤，可接受的副檔名有：" + validExts.toString());
    sender.value = null;
    return false;
  }
  else return true;
}
</script>