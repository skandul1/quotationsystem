function unhide() {
    var hid = document.getElementsByClassName("exp");
    // Emulates jQuery $(element).is(':hidden');
    if(hid[0].offsetWidth > 0 && hid[0].offsetHeight > 0) {
        hid[0].style.visibility = "visible";
    }
}
function test() {
        var Excel = new ActiveXObject("Excel.Application");
        Excel.Visible = true;
        Excel.Workbooks.Open("Quotatio");
      }

// <script type="text/javascript">
    function EnableDisableTextBox(ddlModels) {
        var selectedValue = ddlModels.options[ddlModels.selectedIndex].value;
        var txtOther = document.getElementById("txtOther");
        txtOther.disabled = selectedValue == 5 ? false : true;
        if (!txtOther.disabled) {
            txtOther.focus();
        }
    }
// </script>

var subjectObject = {
  "Bombardier": {
    "737": ["Aluminium", "Steel", "IRON", "Titanium"],
    "727": ["Aluminium", "Steel"],
    "680": ["IRON", "Titanium"]
  },
  "AIRBUS": {
    "700": ["Aluminium"],
    "600": ["IRON"]
  },
  "Boeing": {
    "637": ["Aluminium", "Steel"],
    "787": ["Titanium"]
},
"COMAC": {
    "300": ["IRON", "Titanium"],
    "900": ["Aluminium", "Steel", "IRON", "Titanium"]
  },
"Other": {
    "300": ["IRON", "Titanium"],
    "900": ["Aluminium", "Steel", "IRON", "Titanium"]
  }
}
window.onload = function() {
  var subjectSel = document.getElementById("Manufacturer");
  var topicSel = document.getElementById("Model");
  var chapterSel = document.getElementById("Material");
  var FormSel = document.getElementById("Form")
  for (var x in subjectObject) {
    subjectSel.options[subjectSel.options.length] = new Option(x, x);
  }
  subjectSel.onchange = function() {
    //empty Chapters- and Topics- dropdowns
    chapterSel.length = 1;
    topicSel.length = 1;
    //display correct values
    for (var y in subjectObject[this.value]) {
      topicSel.options[topicSel.options.length] = new Option(y, y);
    }
  }
  topicSel.onchange = function() {
    //empty Chapters dropdown
    chapterSel.length = 1;
    //display correct values
    var z = subjectObject[subjectSel.value][this.value];
    for (var i = 0; i < z.length; i++) {
      chapterSel.options[chapterSel.options.length] = new Option(z[i], z[i]);
    }
  }
}


function goToURL() {
  window.open('https://drive.google.com/file/d/1EdIZRqZQuM-3LZBO_nmoNh-LTkBfmzhz/view?usp=sharing');
}

// var checkList = document.getElementById('list1');
// checkList.getElementsByClassName('anchor')[0].onclick = function(evt) {
//   if (checkList.classList.contains('visible'))
//     checkList.classList.remove('visible');
//   else
//     checkList.classList.add('visible');
// }

// $(document).ready(function() {
//         $('#ingredients').multiselect();
//     });

// $(document).ready(function () {
//   $("#test").CreateMultiCheckBox({ width: '230px',
//              defaultText : 'Select Below', height:'250px' });
// });
