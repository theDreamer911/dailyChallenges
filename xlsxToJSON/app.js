var selectedFile;
document
  .getElementById("uploadFile")
  .addEventListener("change", function (event) {
    selectedFile = event.target.files[0];
  });
document.getElementById("uploadExcl").addEventListener("click", function () {
  if (selectedFile) {
    console.log("Your JSON Data");
    var fileReader = new FileReader();
    fileReader.onload = function (event) {
      var data = event.target.result;

      var workbook = XLSX.read(data, {
        type: "binary",
      });
      workbook.SheetNames.forEach((sheet) => {
        let rowObject = XLSX.utils.sheet_to_row_object_array(
          workbook.Sheets[sheet]
        );
        let jsonObject = JSON.stringify(rowObject);
        document.getElementById("answer").innerHTML = `\n${jsonObject}`;
        console.log(jsonObject);
      });
    };
    fileReader.readAsBinaryString(selectedFile);
  }
});
